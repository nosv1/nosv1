# Job digest: what each weekly curated run sent (newest last)

## 2026-11-17 (first run, fired by hand; log rebuilt by the interactive session, the run's own push was refused)

- **Sent:** "No new verified fits this week." Not a real result: the run couldn't verify anything.
- **Why:** the routine's environment (Default) blocks careers.garmin.com and garmin.wd1.myworkdayjobs.com
  (proxy 403, confirmed from the interactive session too), and its push to nosv1/nosv1 was refused (repo not
  attached to the routine). Used 3 of 12 searches, 2 of 15 fetches.
- **Leads found but unverified (all from job-board copies, dropped by the live-only rule):** Garmin Global
  Transportation Analyst 1/2, Allocation and Lead Time Analyst, Operations Analyst 2, Planner 1 (Olathe);
  Penske Motor Group Material Control Analyst (KC); Harcros Chemicals Supply Chain Analyst.
- **Fix (his, at claude.ai/code/routines, from a computer):** add nosv1/nosv1 to the "Weekly job list" routine;
  allow job hosts on its environment: careers.garmin.com, *.myworkdayjobs.com, *.icims.com,
  job-boards.greenhouse.io, boards.greenhouse.io, jobs.lever.co. Wildcards are a Settings decision.
