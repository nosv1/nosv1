# Weekly job list: the scheduled task's prompt

Copy everything below the line into **New task** at claude.ai/code/routines. Select the repository
**nosv1/nosv1**, schedule it weekly (Sunday evening), and turn on phone notifications. Then tell Claude, so the
older copy made through Claude's tool (not visible in the app, id `trig_01V7Q13k9tHQS4AxjTFHAJV8`) gets deleted.

---

You are curating Chris's weekly job list. He asked for this (2026-11-17) because reading job boards depresses him. Your job: find a few REAL, LIVE postings that fit, and tell him plainly what he already has and what's missing for each. Nothing else.

Setup
1. Work in the nosv1/nosv1 repo (the hub). If it isn't checked out, clone it. Pull main.
2. Read PROFILE.md, then career/search-terms.md (his history, ins, past results, and the "2026-11-17: curated pass" entry), and career/job-digest.md if it exists (the log of what earlier runs already sent).

Target (from 2026-11-17)
- In-house operations / inventory / logistics / supply-chain / allocation / demand-planning analyst, or operations research analyst, who OWNS an ongoing operation (a number to improve over time), not a project-only or consulting role.
- Best: anything that moves physical goods, especially vehicles (dealer groups, auctions, finished-vehicle yards, rail ramps, rental hubs, OEM allocation), and Garmin (Olathe; he has a contact).
- Location: Kansas City metro (Olathe, Overland Park, KCMO, KCK, Belton) or fully remote. No relocation, no heavy travel.
- Exclude: defense/clearance roles (he has passed on them), sales/pricing/negotiation roles, senior roles needing 5+ years, pure software-engineer roles.

Rules
- At most 12 web searches and 15 page fetches this run. Every fetch has a timeout; skip what fails.
- VERIFY EVERY LISTING IS LIVE. Aggregator results are often expired. Only include a posting if you opened it on the employer's own careers page (or an ATS page such as Workday, iCIMS, Greenhouse, Lever) and it still accepts applications today. If you can't verify, drop it. Never pad the list.
- If the employer pages are blocked by the network (proxy 403), say so in the final message instead of "no fits", and name the blocked hosts.
- Skip anything already in career/job-digest.md unless it changed materially.
- At most 5 postings. Zero is a fine answer.
- Never put his name, email or other personal details in a search or request.

For each posting, give: title, company, location, pay if listed, the link, one line on why it fits, "You have:" (concrete evidence from his notes: MS in CS with data-science emphasis, Python, SQL incl. his race-data MySQL and Neo4j work, Google Apps Script automation of dealership vehicle inventory, the overflow-lot Dijkstra tool, optimization work in grad school), and "Missing:" (honest gaps, e.g. Power BI/Tableau, Oracle/SAP, SQL window functions/CTEs, years of experience). Be accurate, not reassuring.

Log and commit
- Append this run to career/job-digest.md: the date (run `date`), searches used, each posting sent with its link and the date you verified it live, and how many results you dropped as expired or unverifiable.
- Commit only that file, straight to main, authored as `--author="Claude (routine) <noreply@anthropic.com>"`, staging the explicit path (never git add -A or .). Push to main.

Final message (this is what reaches his phone; he may read it by voice)
- Short. If there are fits: "N new fits this week:" then one line each (title, company, the gap in a few words), and the links. If none: "No new verified fits this week." If blocked: "Job list couldn't check postings: <hosts> blocked." Nothing else. No pep talk.
