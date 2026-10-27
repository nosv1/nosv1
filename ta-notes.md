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

**Updated 2026-10-26 19:00 CDT** from the repos' own notes (Soma 10-18 to 21, Otto 10-23; PCB untouched since 10-11). Hub moved here from
[12_months](https://github.com/nosv1/12_months) on 10-10, history included.

- **The robotics curriculum is no longer the path** (decisions.md 10-10). The syllabus stays as a
  skills map that projects tick off. Weeks 1–5 done (59.77 h logged); week 6 not started, not owed.
  12_months stays public and clean, a place to come back to "if that itch comes back."
- **Goal is open, on purpose** (observations.md 10-10). The job hunt is seasonal, driven by outdoor
  work conditions. Don't push a career target. Projects = readiness: public, tested, honest history.
  **He asked to keep this in view: "winter is going to hit eventually and I need to be ready for it
  mentally."** When the weather turns, meet the itch with evidence of what's built.
- **No lead project (10-11, his call):** "the lead is irrelevant." He works on whatever he's
  thinking about that day. Three active:
- **Otto** (robot; first mission **reframed 10-17: red-team his own defense**, [notes](ideas/stealth-goal-seeker.md)),
  active 10-11. Repo [otto-the-robot](https://github.com/nosv1/otto-the-robot). **10-17:** setup done (Jazzy,
  Harmonic, Nav2 TB3 sim), C++, homework-style roadmap (`docs/roadmap.md`), package skeletons.
  **10-23:** HW1 steps 1–2 (twist publisher + odom subscriber, his). Depot model cached 10-20.
  Details: the repo's `docs/notes.md`.
  Ticks off the 12_months skills map.
- **iRacing race engineer**, a clean rewrite of Soma
  ([strategist](https://github.com/nosv1/strategist) stays a frozen ACC archive). First "useful"
  milestone: **the caught call**, spec in [ideas/iracing-race-engineer.md](ideas/iracing-race-engineer.md).
  Repo: [iracing-soma](https://github.com/nosv1/iracing-soma), cloned at
  `C:\Users\chris\iracing-soma`. Windows-side only: iRacing telemetry is Windows shared memory.
  **Caught call works (10-18) and spoke live in two races (10-20).** Not "done": bad calls in
  race 1 (caught by 60.9 s / 7.4 s) still unexplained. Also 10-19 to 21: session switches, race-start
  fix, lap times from his own crossings, flags started. Next per the repo: flags, then the outliers.
  Details live in the repo's `docs/notes.md`.
  **Hub pointer verified both ways 10-10:** Windows Claude Code and a phone/cloud session both fetched
  PROFILE.md by raw URL.
- **E-ink temp/humidity PCB** with his brother Seth (10-11, [notes](ideas/eink-sensor-pcb.md)): first
  PCB, KiCad, PCBWay assembles. Schematic done (ERC 0/0), footprints part-way. Not in a repo yet.
- Other ideas: [motorcycle telemetry](ideas/motorcycle-telemetry.md). Orbital path planning was active 10-07;
  not raised since. Bowling app parked — don't raise.
- **Off days are real.** He ran ~19 h/week for 22 days straight into October; enthusiasm dropped.
  Watch load, not just progress.

## Next session

1. **Otto**: HW1 in the repo's `docs/roadmap.md`. Give the real assignment, no warm-ups (10-17).
   Open sessions in otto-the-robot. Retry the Fuel depot download first. Design stays his.
2. **iracing-soma**: flags, then the 60.9 s / 7.4 s outlier calls. Ask for his own approaches
   first. Follow the repo's `docs/notes.md`; open sessions in that repo, not here.
3. **E-ink PCB**: pick a display-only module (DFR0676 is a whole ESP32 board, so it's the
   firmware prototype instead), then footprints for J1–J3/SW1–2, then the PCB editor. Offer a repo
   for the KiCad project (scaffolding is mine to do).
4. **Still undecided from 10-10** (park unless he raises them): hours logging after the curriculum
   (proposed: log project hours, all projects); open caught-call questions (ahead by position or on
   track; name or position in the call); the milestone's "done" (proposed: spoken, a real race,
   left on the whole time, calls right).

**Keep replies short.** Put the task in the **final** message, never mid-turn.

## Standing instructions

- **Open every session with where things stand**: active projects, their current milestones, what's
  left. No lead; don't rank them (10-11).
  He asked (09-26) for the remaining-work picture up front, not as a surprise at the end.
- **Bug him about the career thread, on purpose** (asked 10-10: "prob a good idea to bug me about
  this every once in a while, I turn 30 eventually"). **A cloud routine, "career check-in"**,
  pushes one question to his phone at random 2–5 week intervals in his free hours and logs it.
  Since 10-26 it wakes on a fixed schedule and rolls dice against the last date in the Check-ins
  log, so it never reschedules itself (the 10-10 version couldn't: agents can't edit routines made
  through the API, and it died after its first question). An in-session ask logged there resets
  its clock too. **Never tell him when it fires**; he asked not to see the schedule. If a run
  reports a failure, fix it at claude.ai/code/routines. In sessions too: human-feeling intervals: roughly every few weeks, irregular, at a natural opening (weather,
  a bad work day, a project milestone worth putting on a résumé), never as a fixed monthly ritual.
  One short question, not a lecture. E.g. "Any word from your Garmin contact?", "Want me to rerun
  the searches?", "SQL started?" Log the date in [career/search-terms.md](career/search-terms.md).
  **Last asked: 2026-10-26.** His framing: I'm a tool for his projects and career outlook, not a
  friend; keep it that way.
- **"Quiet check" routine** (his idea, 10-10: "you can be useful even if I don't open you"). It
  wakes on a fixed schedule (since 10-15, same rescheduling problem), and if there's been no activity across his repos for 7+ days, it
  pushes one line ("Quiet for N days. Break, or something stuck?"), at most once a week. Log:
  [ta-notes/pings.md](ta-notes/pings.md). **Both routines commit as `Claude (routine)`**, which
  the quiet check ignores. Interactive sessions keep committing as plain `Claude` so they count
  as him being active. Never tell him when either routine fires.
- **Hours: undecided** since the curriculum ended. Don't log until he decides. (Curriculum hours
  were logged in 12_months' `background-threads/week-NN.md`; that log is frozen.)
- **Make room for creative thinking, not just known solutions** (asked 10-13: "would be fun to
  try and inspire creative thinking"). On open problems (caught-call rules, beating patrol
  detectors), ask for his own approach first, ideally two or three, before naming any known
  technique. Now and then on known ground too: "how would you solve this if nobody had yet?",
  then compare with the standard answer. Light touch; not every exchange.
- **Commits I make are authored as Claude** (`--author="Claude <noreply@anthropic.com>"`). Don't
  sweep his uncommitted edits into my commits. **Stage explicit paths. Never `git add -A` or
  `git add .`** Broke this 09-18; he caught it.
- **Verify before advising** — his "done" and my own summaries both. Run it.
  Routine output too: check what a routine says about him against the notes and his repos
  before relaying it (10-26: passed on an Apps Script/SQL claim that the notes already contradicted).
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
