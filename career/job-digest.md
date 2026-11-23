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

## 2026-11-17 21:38 UTC (scheduled run)

- **Sent:** 1 verified fit (Garmin Planner 2), 1 unverified lead.
- **Budget used:** 1 of 12 searches, 15 of 15 fetches.
- **Network:** www.garmin.com, jobs.gxo.com, careers.rbglobal.com all load now (200). garmin.wd1.myworkdayjobs.com
  still returns 500 / 422, but Garmin's real job system is careers.garmin.com (`/api/jobs` JSON, applications on
  careers-garmin.icims.com), which works. Next run: query that directly.
- **Verified (Garmin careers API, 2026-11-17):**
  - **Garmin, Planner 2 (demand planner), Olathe KS, req 20280**, posted 2026-11-11, full time, pay and shift not
    listed (HQ office role; ESD shoes required on the floor). Demand forecasting vs channel inventory and
    sell-through; "owns accountability for department KPIs". Asks bachelor's + 2 yrs relevant experience; desired
    manufacturing/distribution experience, CPIM, 5+ yrs (desired, not required).
    https://careers.garmin.com/jobs/20280 (apply: https://careers-garmin.icims.com/jobs/20280/login)
- **Unverified (fetch budget ran out):** Louis Dreyfus Company, Junior Logistics Analyst (KC MO, entry level, rail
  logistics and shipment tracking). Only aggregator copy: https://builtin.com/job/junior-logistics-analyst/9041951
- **Closed or gone since last run:** Garmin Global Transportation Analyst 1, Allocation and Lead Time Analyst,
  Operations Analyst 2, Planner 1 (none in Garmin's Olathe listings today); GXO Logistics Analyst 1st Shift req
  392312 (not in GXO's Kansas City analyst search).
- **Dropped:** 4. Garmin ERP Application Analyst – Supply Chain (Oracle EBS configuration, IT role, not owning an
  operation); GXO Implementation Analyst (2nd shift); GXO Trade Compliance Senior Analyst (senior); Garmin
  interns. IAA/RB Global remarketing analyst not rechecked (vehicle remarketing, borderline excluded).
- **Blocked hosts:** none.

## 2026-11-23 00:05 UTC (scheduled run)

- **Sent:** "No new verified fits this week." 3 unverified leads.
- **Budget used:** 10 of 12 searches, 13 of 15 fetches.
- **Searches:** KC logistics analyst (ATS hosts); LDC Junior Logistics Analyst careers; inventory control analyst KC/Lenexa/Olathe/OP;
  transportation/operations analyst entry level KC rail/freight/warehouse; LDC careers site; CPKC Local Operations &
  Inventory Management Coordinator (x2); LDC on Workday. Garmin via its careers API (keywords analyst, logistics, supply,
  inventory, transportation; Olathe).
- **Verified:** none fit.
- **Unverified (employer job system blocked or not found):**
  - **Louis Dreyfus Company, Junior Logistics Analyst** (KC MO, entry level, 0-3 yrs): rail logistics data, shipment
    tracking, billing, metrics; Excel. LDC's job system is SmartRecruiters (blocked). Aggregator copy dated 4/14/2026,
    "reposted recently" on Built In. https://builtin.com/job/junior-logistics-analyst/9041951
  - **CPKC, Local Operations & Inventory Management Coordinator** (KC MO or Winnipeg, entry level): local rail operations
    planning, inventory audits, waybilling. No employer page surfaced.
    https://tealhq.com/job/coordinator-local-operations-planning_18ede942-ab28-4ee9-83f2-5b33d1a5985f
  - **University of Kansas Health System, Inventory Analyst (M-F 7am-3:30pm)**, Kansas City KS (also a Shawnee
    distribution-center Inventory Analyst). Employer site blocked.
    https://jobs.kansashealthsystem.com/job/kansas-city/inventory-analyst-m-f-7am-3-30pm/38901/81061204912
- **Dropped:** 6. Garmin Business Analyst OM Support, req 19240 (posted 11-18; requirements-gathering and training role,
  15%+ travel, international-hours flex); Garmin IT Asset Analyst 2, req 20495 (5 yrs); Garmin Inventory Planning,
  Transportation Analyst, Supply Planner interns (internships); GXO Procurement Analyst 1st Shift (buyer role, 1 yr
  commodity buyer, 25% travel); GXO Implementation Analyst (2nd shift, carried over); Children's Mercy Inventory Control
  Analyst req 2025-35506 (HTTP 410, closed). Garmin Planner 2 (req 20280) still open, already sent.
- **Blocked hosts:** jobs.kansashealthsystem.com, careers.cargill.com, jobs.smartrecruiters.com, api.smartrecruiters.com
  (DNS/proxy 403). Cargill Rail Execution Specialist (KC KS, 2 yrs, $64-80k) unchecked as a result.
