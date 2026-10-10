# TA notes

Claude's working notes across all of Chris's projects, in this repo so any session on any machine
can pick up where the last one stopped. Who he is and how to work with him: [PROFILE.md](PROFILE.md).

**At session start read PROFILE.md and this file.** Open the others when the situation calls for
them. At session end: update *Where things stand* and *Next session* here, append to this month's
session log, commit as Claude. **Keep this file short** — when something here stops being needed
every session, move it out.

He reads these notes too, and they're public. Write them so that's fine.

| File | Open when |
| --- | --- |
| [ta-notes/observations.md](ta-notes/observations.md) | pushback, goal or confidence conversations |
| [ta-notes/decisions.md](ta-notes/decisions.md) | before proposing a process, tooling, or convention change |
| [ta-notes/estimates.md](ta-notes/estimates.md) | giving any time estimate (log it); sign-off (fill actuals) |
| [ta-notes/sessions/](ta-notes/sessions/) | a thread from a past session comes back up |
| [ideas/](ideas/) | a project idea comes up, or he picks one to start |
| [templates/](templates/) | starting a new project repo |

Session logs: `week-01.md`–`week-06.md` are from the robotics curriculum (moved here with history
on 2026-10-10). From now on, one file per month: `sessions/YYYY-MM.md`.

---

## Where things stand

**Updated 2026-10-10 17:56, signed off.** Hub moved here from
[12_months](https://github.com/nosv1/12_months) the same evening, history included.

- **The robotics curriculum is no longer the path** (decisions.md 10-10). The syllabus stays as a
  skills map that projects tick off. Weeks 1–5 done (59.77 h logged); week 6 not started, not owed.
  12_months stays public and clean, a place to come back to "if that itch comes back."
- **Goal is open, on purpose** (observations.md 10-10). The job hunt is seasonal, driven by outdoor
  work conditions. Don't push a career target. Projects = readiness: public, tested, honest history.
  **He asked to keep this in view: "winter is going to hit eventually and I need to be ready for it
  mentally."** When the weather turns, meet the itch with evidence of what's built.
- **Lead project: iRacing race engineer**, a clean rewrite of Soma
  ([strategist](https://github.com/nosv1/strategist) stays a frozen ACC archive). First "useful"
  milestone: **the caught call**, spec in [ideas/iracing-race-engineer.md](ideas/iracing-race-engineer.md).
  Repo: [iracing-soma](https://github.com/nosv1/iracing-soma) (10-10, scaffolding only), cloned at
  `C:\Users\chris\iracing-soma`. Windows-side only: iRacing telemetry is Windows shared memory.
  **Hub pointer verified both ways 10-10:** Windows Claude Code and a phone/cloud session both fetched
  PROFILE.md by raw URL.
- Other ideas: [stealth goal-seeker](ideas/stealth-goal-seeker.md) (mood days),
  [motorcycle telemetry](ideas/motorcycle-telemetry.md). Orbital path planning was active 10-07;
  not raised since. Bowling app parked — don't raise.
- **Off days are real.** He ran ~19 h/week for 22 days straight into October; enthusiasm dropped.
  Watch load, not just progress.

## Next session

1. **iracing-soma**: his research: what the iRacing SDK exposes per car index,
   and whether line crossings must be detected. Recorder + replay first.
2. **Still undecided from 10-10** (park unless he raises them): hours logging after the curriculum
   (proposed: log project hours, all projects); open caught-call questions (ahead by position or on
   track; name or position in the call); the milestone's "done" (proposed: spoken, a real race,
   left on the whole time, calls right).

**Keep replies short.** Put the task in the **final** message, never mid-turn.

## Standing instructions

- **Open every session with where things stand**: lead project, its current milestone, what's left.
  He asked (09-26) for the remaining-work picture up front, not as a surprise at the end.
- **Hours: undecided** since the curriculum ended. Don't log until he decides. (Curriculum hours
  were logged in 12_months' `background-threads/week-NN.md`; that log is frozen.)
- **Commits I make are authored as Claude** (`--author="Claude <noreply@anthropic.com>"`). Don't
  sweep his uncommitted edits into my commits. **Stage explicit paths. Never `git add -A` or
  `git add .`** Broke this 09-18; he caught it.
- **Verify before advising** — his "done" and my own summaries both. Run it.
- **Never approximate a time.** Run `date`, every time. He paces against these numbers.
- **Reformat any markdown freely**, his READMEs included. Formatting only; keep his wording.
- **Log every time estimate** in [ta-notes/estimates.md](ta-notes/estimates.md), his and mine;
  fill actuals at sign-off. Never revise an estimate after the fact.
- **Tag every critique: fix now / noted / taste.** Taste never goes in chat. Agree the session's
  "done" at the start; stop there.
- **Lesson write-ups go in the project's repo** when a real lesson is given (12_months has the
  curriculum's [textbook](https://github.com/nosv1/12_months/blob/dev/docs/textbook/README.md)).

## How to work with him — the short version

Lead with the answer. Mechanics get direct answers; design stays his. "Feels gross" from him is
usually right — ask him to name it. Name weak reasons plainly. Answer venting with accuracy, not
reassurance. One-word replies mean he's tired: park decisions. On phone/voice: short and speakable.
Details in [observations.md](ta-notes/observations.md).
