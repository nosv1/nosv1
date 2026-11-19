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

**Updated 2026-11-08 21:29 CST** (last full pass 10-26 19:00 CDT) from the repos' own notes (Soma 10-18 to 21, Otto 10-23; PCB untouched since 10-11). Hub moved here from
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
  **Watching his team race (11-08):** he liked [Enduro Manager](https://enduromanager.com/); not yet tested while spectating.
  **Hub pointer verified both ways 10-10:** Windows Claude Code and a phone/cloud session both fetched
  PROFILE.md by raw URL.
- **E-ink temp/humidity PCB** with his brother Seth (10-11, [notes](ideas/eink-sensor-pcb.md)): first
  PCB, KiCad, PCBWay assembles. Schematic done (ERC 0/0), footprints part-way. Not in a repo yet.
- **SpellIt!** ([claude-spells](https://github.com/nosv1/claude-spells), started 11-02): a spelling app
  for the family's 2nd and 6th graders (and him), live at `nosv1.github.io/claude-spells`. **His call:
  "just build it"**, so Claude writes the code (a family tool, not a skill project), and since 11-05
  pushes straight to main. **It must stay free** (no paid services). Built 11-02 to 11-05:
  - **Quizzes:** typing with live green/red letters, or handwriting on an iPad pad.
  - **Word bank and audio:** 40–60 words a level with sentences and meanings; natural voices from
    Workers AI.
  - **Family features:** sync across devices with the family PIN, a star shop, and parent tools.
  - **Where to look:** the repo's CLAUDE.md (how to test and deploy) and BACKLOG.md (parked ideas:
    quiz alerts to parents' phones, drawing break).
- **YouTube quiz app** (idea, 11-06, "just build it" mode): pick videos via a Study playlist, a
  later "what did you learn?" conversation, reminders on missed topics only. Web app, free for him.
  [Notes](ideas/youtube-quiz.md). Repo [claudes-afterwatch](https://github.com/nosv1/claudes-afterwatch);
  cloud environment "afterwatch". Next: he adds a Gemini key (from a computer), then test 3 videos.
- **claude-trades** (11-15, "just build it"): from a video on food shortages and global trade; scope
  TBD. Local repo at `C:\Users\chris\cluade-trades` (typo folder name), no remote. [Notes](ideas/claude-trades.md).
- **Ride Finder** ([claudes-ride-finder](https://github.com/nosv1/claudes-ride-finder), since 10-31, "just build it"):
  motorcycle ride planner, live on GitHub Pages. Its README, FEATURES.md and BACKLOG.md hold the state. Local clone
  `C:\Users\chris\claudes-ride-finder`. 11-16: another session is bringing its code up to the coding standard.
- **Sufficiency / options thread (11-16, parked, he was tired):** wants to be "sufficient," not rich, and to be
  able to say no to a role change. Leads: retainer-style work ("paid to be available") selling the dealership
  Apps Script skill to others. Blocker he named: doesn't trust his code as production. Log: sessions/2026-11.md.
  11-17: he said solving others' problems daily "exhausts me"; his own (dealership) energize him. Overflow-lot
  Dijkstra's in Apps Script is the best evidence on file for the "production code" doubt. Don't push; pick up if he does.
- **Lot Walk, the dealership lot app** (11-17 kickoff, "just build it"): **live 11-18 at lot-walk.pages.dev**.
  Repo [claudes-lot](https://github.com/nosv1/claudes-lot) (private; clone `C:\Users\chris\claudes-lot`). Page on
  Cloudflare Pages, data in Google (Apps Script service reads Import view-only, writes only its own Lot App
  Data sheet). Dictation walk, all six lots plus Customer Lot, spot codes, paste, map, lists, flags. He owns
  the flow and steers design; the duplicate-swap solver and distance-to-door are **his** to design. The
  repo's CLAUDE.md and `docs/notes.md` hold state; open sessions there. He may redesign the UI layout
  around his checklists (survey in `docs/design.md`).
- **Reading** The Three-Body Problem (11-13) along with an archived r/bookclub read-along; links and progress in
  [reading/three-body-problem.md](reading/three-body-problem.md). He wants people, not AI, to share books with.
- Other ideas: [motorcycle telemetry](ideas/motorcycle-telemetry.md). Orbital path planning was active 10-07;
  not raised since. Bowling app parked — don't raise.
- **Off days are real.** He ran ~19 h/week for 22 days straight into October; enthusiasm dropped.
  Watch load, not just progress.

## Next session

0. **Lot Walk**: open sessions in claudes-lot and follow its `docs/notes.md`. 11-19 was a long on-the-lot day
   (~30 changes: battery log + import, Low Batteries, Customer Parking as a list, out-of-spot homes, zoom, list
   groups...). Code on a branch + preview; while he's on the lot, Claude reviews and merges itself (his call).
   Owed: a full code review of 068e2e7..HEAD, rule-5 checks in today's small handlers, remove batteryImport.
   **Inventory_Extra → Import migration in progress** (his ask 11-19): claudes-lot `docs/migration.md` is the handoff
   (37 formula columns staged; waiting on his Tiger_Sales table + Master_Used rename, then re-check). Claude has a paired read-only device (token in `~/.lot-walk`, never printed).
1. **Otto**: HW1 in the repo's `docs/roadmap.md`. Give the real assignment, no warm-ups (10-17).
   Open sessions in otto-the-robot. Retry the Fuel depot download first. Design stays his.
2. **iracing-soma**: flags, then the 60.9 s / 7.4 s outlier calls. Ask for his own approaches
   first. Follow the repo's `docs/notes.md`; open sessions in that repo, not here.
3. **E-ink PCB**: pick a display-only module (DFR0676 is a whole ESP32 board, so it's the
   firmware prototype instead), then footprints for J1–J3/SW1–2, then the PCB editor. Offer a repo
   for the KiCad project (scaffolding is mine to do).
4. **afterwatch**: open sessions in [claudes-afterwatch](https://github.com/nosv1/claudes-afterwatch) and
   follow its `docs/notes.md` handoff (Gemini key from a PC, then the 3-video test). "Just build it."
5. **Power of 10 recall (11-18):** open with a 60-second quiz, rules out of order. Carry over: he explains why the GC
   doesn't stop unbounded growth; round 2 in the 11-18 log. He thinks iracing-soma breaks rule 3; if he wants,
   have him find the uncapped collections himself.
6. **Still undecided from 10-10** (park unless he raises them): hours logging after the curriculum
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
  **Last asked: 2026-11-10** (in session). His framing: I'm a tool for his projects and career outlook, not a
  friend; keep it that way.
- **"Quiet check" routine** (his idea, 10-10: "you can be useful even if I don't open you"). It
  wakes on a fixed schedule (since 10-15, same rescheduling problem), and if there's been no activity across his repos for 7+ days, it
  pushes one line ("Quiet for N days. Break, or something stuck?"), at most once a week. Log:
  [ta-notes/pings.md](ta-notes/pings.md). **Both routines commit as `Claude (routine)`**, which
  the quiet check ignores. Interactive sessions keep committing as plain `Claude` so they count
  as him being active. Never tell him when either routine fires.
- **"Weekly Job Listings" scheduled task** (he asked, 11-17: "looking at them depresses me"): Sundays 6:05 pm CT,
  made by him in the app from career/job-list-prompt.md (id `trig_01Wt6vWBEonYyQsbCrwyZ1tH`; agents can't edit it,
  he can at claude.ai/code/routines). Finds at most 5 live, verified KC-or-remote operations/inventory/logistics
  analyst postings with "you have / missing", pushes to his phone, logs to career/job-digest.md. He knows it exists
  (unlike the check-ins). Claude's tool-made first copy was deleted 11-17. **Still to do (his):** allow job hosts
  on the Default environment (list in career/job-digest.md), confirm nosv1 is attached, then Run now. Its prompt
  still has the file's header paragraph pasted in; harmless, trim if editing.
  **11-17 test (he ran it):** repo push works; job hosts allowed (he added the ATS list, Claude added www.garmin.com,
  careers.rbglobal.com, jobs.gxo.com on his approval). Garmin Workday returns 500 to plain fetches and the run's
  classifier refused the JSON API, so Garmin may stay unverifiable. Each new employer domain may need allowing.
  **11-17 later:** Garmin verifies via careers.garmin.com/api/jobs (now in the prompt). Target rewritten after
  his reaction: hands-on ops seat with data and room to automate, not "own a number" (see search-terms Check-ins).
  **His to do:** paste the new TARGET and RULES lines into the app routine.
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
