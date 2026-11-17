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

## 2026-11-17 21:23 UTC (scheduled run)

- **Sent:** "Job list couldn't check postings: hosts blocked." No postings sent.
- **Budget used:** 8 of 12 searches, 6 of 15 fetches.
- **Network:** this run has the repo now (push worked). Blocked: www.garmin.com (proxy 403; careers.garmin.com
  redirects there), careers.rbglobal.com, jobs.gxo.com, builtin.com, coxautoinc.com (DNS/proxy refusal).
  garmin.wd1.myworkdayjobs.com connects but returns HTTP 500 to plain fetches, and the JSON job-search API call
  was refused by the session's permission classifier, so Garmin is still unverifiable. careers-model1.icims.com
  loads, but req 2122 (Inventory Operations Analyst) now shows only the site menu: likely closed.
- **Leads found, unverified (dropped by the live-only rule):**
  - IAA (RB Global), Analyst, Remarketing Enhancement & Make-Ready, req 11414, $56.2–70.3k, asks 3+ yrs analyst
    or ops; remote status unclear. https://careers.rbglobal.com/analyst-remarketing-enhancement-make-ready-rq5sna
  - Louis Dreyfus Company, Junior Logistics Analyst (KC MO, in office, entry level): rail logistics data, shipment
    tracking and metrics; Excel. Aggregator copies only (builtin.com/job/junior-logistics-analyst/9041951).
  - GXO, Logistics Analyst 1st Shift, req 392312, Botts Rd KC MO 64147, posted 2026-10-14 per search snippet.
    Check whether the site serves the NNSA campus next door (clearance = exclude).
  - Garmin (Olathe) leads from the first run, still unverifiable.
- **Dropped:** 4 (3 unverifiable hosts, 1 likely closed).
- **Fix:** allow www.garmin.com, careers.rbglobal.com, jobs.gxo.com in the routine's environment; allow the
  Workday JSON endpoint (POST /wday/cxs/...) for *.myworkdayjobs.com, since Workday pages need it to list jobs.
