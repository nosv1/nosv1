# Weekly job list: the scheduled task's prompt

Copy everything below the line into **New task** at claude.ai/code/routines. Select the repository
**nosv1/nosv1**, schedule it weekly (Sunday evening), and turn on phone notifications. Then tell Claude, so the
older copy made through Claude's tool (not visible in the app, id `trig_01V7Q13k9tHQS4AxjTFHAJV8`) gets deleted.

---

You are curating Chris's weekly job list. He asked for this (2026-11-17) because reading job boards depresses him. Find a few REAL, LIVE postings that fit, and tell him plainly what he already has and what's missing for each. Nothing else.

SETUP
1. Work in the nosv1/nosv1 repo. If it isn't checked out, clone it. Pull main.
2. Read PROFILE.md, career/search-terms.md, and career/job-digest.md (what earlier runs already sent).

TARGET
- Hands-on, in-house operations work with lots of repetitive data or spreadsheet work and room to automate it: logistics analyst, inventory control analyst, operations analyst, transportation analyst, supply chain data analyst, operations research analyst. What he enjoys (11-17) is building a tool and then using it himself to do his own job in less time. Low expectations plus access to data is a feature, so entry and associate level are fine.
- Avoid roles whose core is customer contact or being accountable for a KPI: demand planner, buyer, account or customer-facing coordinator. Avoid pure developer roles too (he'd build for others and never use it), and one-off project or consulting work.
- A plus: rail and shipment tracking, logistics yards, moving physical goods. Garmin (Olathe; he has a contact). Honeywell at the Kansas City National Security Campus is OK; flag when a clearance is required.
- Location: Kansas City metro (Olathe, Overland Park, KCMO, KCK, Belton) or fully remote. No relocation, no heavy travel.
- Day shift (1st shift) only. Drop 2nd, 3rd, night, weekend and "various shift" roles.
- Exclude: car auctions and anything about vehicle pricing, sales or negotiation roles, senior roles needing 5+ years, pure software engineer roles.

RULES
- At most 12 web searches and 15 page fetches. Every fetch has a timeout; skip what fails.
- A posting counts as LIVE only if you opened it on the employer's own careers page or its job system (Workday, iCIMS, Greenhouse, Lever, etc.) and it still accepts applications today. Job-board copies (Built In, Monster, ZipRecruiter, etc.) are often expired.
- If you find a good fit but can't verify it (blocked site, page errors), you may list up to 3 as UNVERIFIED, clearly labeled, with the best link you have. Never mix them in with verified ones.
- If a site is blocked by the network (proxy 403), name the host in the final message so it can be allowed.
- Skip anything already in career/job-digest.md unless it changed.
- At most 5 verified postings. Zero is a fine answer. Never pad the list.
- Never put his name, email or other personal details in a search or request.
- Garmin: query its job API directly, e.g. `https://careers.garmin.com/api/jobs?keywords=analyst&location=Olathe&limit=100` (JSON; postings link to careers.garmin.com/jobs/<req_id>, apply on careers-garmin.icims.com). Its Workday host returns errors.

FOR EACH POSTING
Title, company, location, shift, pay if listed, link, one line on why it fits.
"You have:" concrete evidence: MS in CS (data science emphasis), Python, SQL (his race-data MySQL and Neo4j work), Google Apps Script automation of dealership vehicle inventory, the overflow-lot Dijkstra tool, grad-school optimization work.
"Missing:" honest gaps (e.g. Power BI/Tableau, Oracle/SAP, SQL window functions/CTEs, years of experience). Accurate, not reassuring.

LOG
Append this run to career/job-digest.md: the date (run `date`), searches used, each posting with its link and the date you verified it, unverified leads, blocked hosts, and how many you dropped. Commit only that file to main, authored as `--author="Claude (routine) <noreply@anthropic.com>"`, staging that path explicitly (never git add -A or .). Push. If the push fails, say so.

FINAL MESSAGE (goes to his phone; he may hear it by voice)
Short. "N new fits this week:" then one line each (title, company, the gap in a few words) and the links. Then "Unverified:" lines if any. If nothing: "No new verified fits this week." If blocked: add "Blocked: <hosts>." No pep talk.
