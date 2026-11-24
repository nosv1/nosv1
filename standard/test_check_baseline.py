"""Tests for check_baseline.py, standard library only: python3 -m unittest standard/test_check_baseline.py"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_baseline as cb

TSC_OUT = """web/a.js(3,5): error TS2345: Argument of type 'string' is not assignable.
  Type 'string' is not assignable to type 'number'.
web/a.js(9,1): error TS2345: Again.
web/b.js(1,1): error TS7006: Parameter 'x' implicitly has an 'any' type.
"""
MYPY_OUT = """src/x.py:3: error: Missing return type  [no-untyped-def]
src/x.py:4:7: error: Incompatible types  [assignment]
src/x.py:4: note: See docs
Found 2 errors in 1 file (checked 3 source files)
"""


def fake_checker(tmp: Path, stdout: str, code: int) -> list[str]:
    """A command that prints stdout and exits with code, so run_checker is tested end to end."""
    out_file = tmp / "out.txt"
    out_file.write_text(stdout, encoding="utf-8")
    script = f"import sys; sys.stdout.write(open({str(out_file)!r}).read()); sys.exit({code})"
    return [sys.executable, "-c", script]


class Parsing(unittest.TestCase):
    def test_tsc_counts_per_file_and_code(self) -> None:
        self.assertEqual(cb.parse_tsc(TSC_OUT), {"web/a.js": {"TS2345": 2}, "web/b.js": {"TS7006": 1}})

    def test_tsc_config_error_has_no_file(self) -> None:
        self.assertEqual(cb.parse_tsc("error TS18003: No inputs were found.\n"), {"<config>": {"TS18003": 1}})

    def test_mypy_skips_notes(self) -> None:
        self.assertEqual(cb.parse_mypy(MYPY_OUT), {"src/x.py": {"no-untyped-def": 1, "assignment": 1}})

    def test_mypy_without_summary_is_an_error(self) -> None:
        with self.assertRaises(cb.BaselineError):
            cb.parse_mypy("")

    def test_ruff_json(self) -> None:
        out = json.dumps([{"filename": "a.py", "code": "F401"}, {"filename": "a.py", "code": None}])
        self.assertEqual(cb.parse_ruff(out), {"a.py": {"F401": 1, "syntax-error": 1}})

    def test_ruff_text_is_an_error(self) -> None:
        with self.assertRaises(cb.BaselineError):
            cb.parse_ruff("a.py:1:1: F401 unused")


class Ratchet(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.old_cwd = Path.cwd()
        os.chdir(self.tmp)
        self.base = self.tmp / "checks-baseline.json"

    def tearDown(self) -> None:
        os.chdir(self.old_cwd)

    def run_main(self, stdout: str, code: int, *flags: str) -> int:
        return cb.main(["tsc", "--baseline", str(self.base), *flags, "--", *fake_checker(self.tmp, stdout, code)])

    def test_init_then_same_passes(self) -> None:
        self.assertEqual(self.run_main(TSC_OUT, 2, "--init"), 0)
        self.assertEqual(self.run_main(TSC_OUT, 2), 0)

    def test_growth_fails_and_update_refuses(self) -> None:
        self.run_main(TSC_OUT, 2, "--init")
        grown = TSC_OUT + "web/c.js(1,1): error TS2304: Cannot find name.\n"
        self.assertEqual(self.run_main(grown, 2), 1)
        self.assertEqual(self.run_main(grown, 2, "--update"), 1)
        self.assertNotIn("web/c.js", self.base.read_text(encoding="utf-8"))

    def test_shrink_passes_and_update_writes(self) -> None:
        self.run_main(TSC_OUT, 2, "--init")
        fewer = "web/b.js(1,1): error TS7006: Parameter 'x' implicitly has an 'any' type.\n"
        self.assertEqual(self.run_main(fewer, 2), 0)
        self.assertEqual(self.run_main(fewer, 2, "--update"), 0)
        self.assertEqual(json.loads(self.base.read_text(encoding="utf-8")), {"tsc": {"web/b.js": {"TS7006": 1}}})

    def test_clean_run_removes_the_section(self) -> None:
        self.run_main(TSC_OUT, 2, "--init")
        self.assertEqual(self.run_main("", 0, "--update"), 0)
        self.assertEqual(json.loads(self.base.read_text(encoding="utf-8")), {})

    def test_crashed_checker_is_not_clean(self) -> None:
        self.assertEqual(self.run_main("Segmentation fault\n", 139), cb.CHECKER_FAILED)

    def test_damaged_baseline_is_an_error(self) -> None:
        self.base.write_text('{"tsc": {"a.js": {"TS1": "two"}}}', encoding="utf-8")
        self.assertEqual(self.run_main(TSC_OUT, 2), cb.CHECKER_FAILED)


if __name__ == "__main__":
    unittest.main()
