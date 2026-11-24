# Coding standard

One standard for every repo, Chris's code and Claude's alike: NASA/JPL's *Power of 10* (Holzmann, 2006),
carried from C into JavaScript and Python at the strictest settings the tools have (his call, 2026-11-16 and
11-23: "as strict as possible"). This file is the only copy. Each repo's CLAUDE.md links here and adds only
its own commands and any extra rules (trades' "claims are code too", for example). The ten rules in
[PROFILE.md](PROFILE.md) are the short form.

Tool settings live beside this file in [standard/](standard/). Repos keep copies of them; change the hub's
first, then copy them out.

## Every code change

Claude does these without being reminded, in every repo:

1. **Read this file** before writing code in a session.
2. **Before every commit, run the repo's check command** (CLAUDE.md, "Check"): lint with zero warnings,
   strict types, the baselines, and the tests that cover the change. Don't push and let CI find it.
3. **In the reply, say which rules the change touched and that the checks passed**, or show what failed.
4. **New and changed code meets every rule in full.** The baselines hold old findings only (see below).

In Chris's own repos (iracing-soma, otto-the-robot) he writes the code; Claude reviews it against this file,
tags each finding **fix now / noted / taste**, and sets up the tools and CI.

## The rules

"Lint" means ESLint or Ruff; "types" means `tsc` or mypy, both strict. "Review" means nothing can check it
mechanically, so it's checked by reading.

| # | Power of 10 | JavaScript | Python | Checked by |
| --- | --- | --- | --- | --- |
| 1 | Simple control flow | No recursion, labels, `with` or `arguments.callee`. No exceptions as flow control. | No recursion. No exceptions as flow control. | lint (labels, with), review (recursion) |
| 2 | Every loop has a fixed bound | No `while (true)` / `for (;;)`; retries, polling and pagination have a max count; every `fetch` has a timeout (`AbortSignal.timeout`). | Same; every network call and subprocess has a `timeout=`. | lint (constant loops), review |
| 3 | No unbounded growth | Caches, maps, queues and anything filled from outside input have a cap or are cleared. Fetched bodies have a size cap. | Same. | review |
| 4 | A function fits on a page | 60 lines (blank lines and comments don't count), complexity 10, nesting 4, 4 parameters (pass an object beyond that), callbacks 3 deep. | Complexity 10, 50 statements, 12 branches, 6 returns, nesting 4, 4 arguments. | lint |
| 5 | Assert the contract | Check data where it crosses a boundary (network, storage, another module, the DOM) and the invariants a change relies on: aim for two checks a function. A failed check does something explicit: throw, or log and return a safe value where throwing would hurt the user (the repo says which). | `if not ok: raise ValueError(...)`, never `assert` outside tests (it vanishes under `-O`). | lint (Python `assert`, S101), review |
| 6 | Smallest scope | `const` by default, no `var`, no shadowing, no reassigned parameters, no implicit globals. Module state only when several functions share it, with a comment saying what it holds. | No mutable module globals; constants in UPPER_CASE. | lint |
| 7 | Check every result | Every promise is awaited, returned, given a `.catch`, or marked `void` with a comment saying who handles the failure. Every `fetch` checks `r.ok`. No empty `catch`, nothing unused, only `Error`s thrown. | No bare or broad `except` unless any failure means the same thing (say what in a comment). Every subprocess checks its exit code. | lint, types |
| 8 | No metaprogramming | No `eval`, `new Function`, code from strings, `__proto__` or changes to built-ins. | No `eval`/`exec`, monkeypatching or runtime code generation; decorators stay plain. | lint |
| 9 | Limit indirection | Short call chains (`a.b.c` at most), no dispatch on strings, no functions passed through more than one layer without a name saying what they're for. | Same. | review |
| 10 | Zero warnings, strictest settings | ESLint with every rule an error and `--max-warnings 0`; `tsc` strict plus the extra flags below, over the JavaScript (`checkJs`, JSDoc where a type isn't clear). | Ruff with the families below; mypy `strict` plus the extra error codes. Annotations on everything. | lint, types, CI on every push |

## The settings

| File | What |
| --- | --- |
| [standard/eslint-standard.mjs](standard/eslint-standard.mjs) | The ESLint rules, grouped by rule number: `standardRules` for every file, `typeAwareRules` (rule 7's promise checks, needs typescript-eslint), `testRuleOverrides` (rule 4's size limits off for tests and build tools), `linterOptions` (a disable comment that disables nothing is an error). |
| [standard/tsconfig.strict.json](standard/tsconfig.strict.json) | `strict` plus `noImplicitReturns`, `noFallthroughCasesInSwitch`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `noImplicitOverride`, `noUnusedLocals`, no unreachable code or unused labels. |
| [standard/ruff.toml](standard/ruff.toml) | Every Ruff family that maps to a rule (bugs, broad except, complexity, security, annotations, unused arguments, returns, pylint, commented-out code, naming, imports). Style-only families (docstrings, quotes, commas) are taste and stay off. |
| [standard/mypy.ini](standard/mypy.ini) | `strict`, `warn_unreachable`, `extra_checks`, and the error codes for possibly-undefined names, redundant expressions, always-true conditions, unused awaitables and bare `# type: ignore`. |
| [standard/check_baseline.py](standard/check_baseline.py) | The baseline ratchet for `tsc`, Ruff and mypy (below). Standard library only; tests beside it. |

Pinned versions (raise them in the hub first): ESLint 10.14.0, @eslint/js 10.0.1, typescript-eslint 8.72.1,
TypeScript 6.0.3, globals 17.13.0, Ruff 0.17.3, mypy 2.4.1.

## Baselines: old code

The standard came in on 2026-11-16 and tightened on 2026-11-23, after most of the code was written. Old
findings are recorded in a baseline so the checks pass today, and **the baseline only ever shrinks**.

- **ESLint:** its own suppressions file, `eslint-suppressions.json` (`eslint --suppress-all` once, then
  `eslint --prune-suppressions` after fixing).
- **tsc, Ruff, mypy:** `checks-baseline.json`, kept by `tools/check_baseline.py`. It counts findings per file
  and code. More than the baseline, or a new file or code, fails. Fewer passes and says to run it again
  with `--update`, which refuses to raise any count. Two runs of one checker (two tsconfigs) keep apart
  with `--section`.
- **CI fails on any finding not in a baseline.** Nobody adds to a baseline by hand or to get a commit
  through. The one exception: the standard itself tightens (a new rule or a stricter limit). Then the
  baseline is regenerated with `--init` / `--suppress-all` in its own commit, which says what changed.
- **When you touch a file, clean what's in it where that's reasonable in the same change** (split the
  long function, type the parameter), then prune or `--update`. No big rewrite just for the standard: a
  risky rewrite of working code is worse than the finding.

## Exceptions

A rule that's wrong for one line is disabled on that line only, with the rule named and the reason:
`// eslint-disable-next-line no-await-in-loop -- one request at a time, the server rate-limits`,
`# noqa: S603 (the command is ours)`, `# type: ignore[import-untyped]  # no stubs published`. No file-wide
or blanket disables, no bare `# type: ignore` (mypy rejects it). An unused disable comment fails lint.

## Where it stands (2026-11-23)

Every repo has these settings, its baselines and CI (Soma's on branch `claude/festive-mayer-oc3q1q` for his
review). Old findings at the start, lint / types / Python:

| Repo | Lint | Types | Python (Ruff + mypy) |
| --- | --- | --- | --- |
| claudes-lot | 104 | 168 | 44 + 63 |
| claude-trades | 41 | 765 | 190 + 179 |
| claudes-ride-finder | 226 | 2,045 | 435 + 550 |
| claude-spells | 95 | 788 | none |
| claudes-afterwatch | none yet | none yet | 7 + 9 |
| iracing-soma (his) | — | — | 114 + 3 |

## A repo's CLAUDE.md

Every repo's CLAUDE.md has this, after "Read first" (the template in
[templates/project-CLAUDE.md](templates/project-CLAUDE.md) has the wording):

- A link to this file and the four "Every code change" steps.
- **Check:** the one command that runs everything (lint, types, baselines, tests), and how CI runs it.
- Any rule the repo adds, and how its rule 5 failures behave (throw, or log and return a safe value).
