# <Project name>

<One line: what this is.>

## Read first

**Before anything else this session, fetch and read Chris's profile:**
https://raw.githubusercontent.com/nosv1/nosv1/main/PROFILE.md

It says who he is and how to work with him: flight instructor by default, he writes the code that
is the skill. It applies here unless this file says otherwise. If the fetch fails, say so; don't
proceed as a generic assistant.

**Before writing any code, fetch and read the coding standard:**
https://raw.githubusercontent.com/nosv1/nosv1/main/CODING.md

Then read this repo's [docs/notes.md](docs/notes.md) (session notes; update at sign-off, commit as
Claude).

## This project

- **Mode:** <flight instructor (the default) or "just build it" (his call, date)>.
- **Skill he's building here:** <e.g. real-time audio pipeline, LLM tool calling>. He writes that.
- **Fair game for me:** <tooling, setup, scaffolding specific to this repo>.
- **Run it:** `<command>`

## Coding standard

[CODING.md](https://github.com/nosv1/nosv1/blob/main/CODING.md) in the hub, at its strictest settings.
Every code change, without being reminded: read it first; run **Check** before every commit (don't push
and let CI find it); in the reply, say which rules the change touched and that Check passed; new and
changed code meets every rule in full. Baselines (`eslint-suppressions.json`, `checks-baseline.json`)
only shrink.

- **Check:** `<one command: lint, types, baselines, tests>`. CI runs the same on every push.
- **Rule 5 failures here:** <throw, or log and return a safe value>.
- <Any rule this repo adds.>

## Git

- Commits authored as Claude (`--author="Claude <noreply@anthropic.com>"`), explicit paths only, never
  `git add -A` or `git add .`.
- <Where code goes: a branch for his review, or straight to main (his call, date).>
