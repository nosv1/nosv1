# Job search terms (2026-10-10)

Made at his request, for when the seasonal itch hits (see
[observations.md](../ta-notes/observations.md), 10-10: "winter is going to hit eventually").

**His filter:** someone out there wants the job he *can* do, so he doesn't need to take it, unless
he actually wants it and believes he can be decent at it. "Want" is his call. "Can be decent" —
let the posting's requirements answer that, not his gut; he has underrated himself before.

## His ins (10-10)

- **Honeywell, Belton MO area:** his brother works there. Likely the Kansas City National Security
  Campus (Botts Rd, south KC, next to Belton), which Honeywell runs for NNSA. Clearance work;
  he passed on defense offers before. Not confirmed which site.
- **Garmin, Olathe KS:** at least one connection.

**On aeronautics (his words: "would be cool, but I don't have that aeronautics background, I just
code things"):** Garmin aviation hires software engineers and data people, not only aero
engineers; domain is learned on the job. His adjacent evidence: proportional navigation, Dubins
paths, pursuit-evasion, and path planning (2022 grad course); thrust vector control (12_months
textbook 27); orbital path planning side project.

"Companies I may not dream about but could probably get in the door at least." A referral usually
does more than a perfect search term; when the itch comes, ask the contact *before* applying.

**His framing of the tradeoff:** "I don't dream of being a software engineer, but money and inside
has its pros, just like clocking out, low stress, and daily fresh air do." Both sides have real
pros. Don't treat the current job as something to escape.

## 1. Strong pull: strategy, racing, optimization

- `race strategy engineer`, `race strategist`
- `motorsport data analyst`, `performance engineer motorsport`, `data engineer motorsport`
- `vehicle dynamics simulation engineer` (lap-time sim; a stretch, same problem as his stint/fuel
  calculators)
- Sim-racing companies + "careers": iRacing, Coach Dave Academy, Garage 61, Track Titan, VRS,
  SimHub, Crew Chief. Small teams; a working race engineer (Soma) is a direct portfolio piece.
- `sports analytics`, `esports analytics`

## 2. Same brain, different domain

- `operations research analyst`
- `optimization engineer`, `decision scientist`
- `simulation analyst`, `Monte Carlo`
- `scheduling optimization` (F1 schedule optimizer, GA-TSP)

## 3. Bridge from current job (inside, fastest)

- `inventory optimization analyst`, `supply chain analyst`, `demand forecasting analyst`
- `automotive pricing analyst`, `dealer operations analyst` (dealer groups, Cox Automotive, CDK,
  vAuto)
- `business automation developer`, `Google Apps Script developer`

His vehicle-inventory automation is direct experience here.

## 4. Revisit

- Garmin (Olathe): `data analyst`, `test engineer`, `software engineer`. Applied before, no
  interviews; local; telemetry overlap with Soma.

**Modifiers:** `remote`, his metro, `junior` / `associate` / `entry level`.

## Log

When he searches, note date, terms, and what came back worth a second look. Months of real
postings make the winter decision easier than a blank page.

### 2026-10-10 — first look (Claude, web search; boards like motorsportjobs.com block fetching)

- **Pro race strategy:** mostly F1, UK-based, 3+ years in motorsport (strategy engineer roles).
  Graduate tier exists (Cadillac F1 graduate strategy analyst, Silverstone; closed July 2026).
  US: Ford Racing strategy engineer (sim modelling, live timing, telemetry) — location/experience
  not verified. Williams: Senior AI and Modelling Engineer – Strategy. Bridge for him: motorsport
  data work he can show (Soma).
- **iRacing jobs:** gameplay/game systems programmers (C++ console game), XAML UI, customer
  service. Not a fit today.
- **Garmin Olathe, Data Scientist 2** (recurring posting): ML frameworks (scikit-learn, PyTorch),
  statistics, time series, MLOps/CI a plus. **Closest fit to his MS**, local. Also Senior Data
  Engineer, Aeronautical Data Analyst.
- **Inventory analyst, remote:** Amerit Fleet automotive inventory analyst $70–80k (SQL + Tableau/
  Power BI/DOMO); Carrier strategic inventory analyst $79–158k; Apex Wheels demand analyst $80–100k.
- **KC operations analyst:** ~$51–75k (Payscale avg ~$61k, KC MO).
- **Sim-racing startups** (Track Titan raised $5M; Coach Dave pays sim engineers): no data roles
  found. Watch.
- **Recurring ask across analyst postings: SQL and a BI tool.** SQL is not a gap (see below); a
  BI tool is.

### SQL: what he already has (reviewed 10-26 from his public repos)

He has written MySQL against his own self-hosted server since 2021, in Discord bots and race data
tools. Not in Apps Script or any current project.

- **[MoBot](https://github.com/nosv1/MoBot)** (2021–22), **[Phyner](https://github.com/nosv1/Phyner)**
  (2022–23), **[GTALens](https://github.com/nosv1/GTALens)** (2021–22): Discord bots backed by
  MySQL (`mysql.connector`). Bot state, guilds, events, custom commands, and racing-league data.
- **[sra_data](https://github.com/nosv1/sra_data)** (2025): parses ACC race results into MySQL tables
  he designed, with composite primary keys (session, server, car, driver) and per-driver lap
  percentiles and pace vs. field.
- **Neo4j / Cypher, committed (2025-03 to 04, and on):** sra_data has 15 `.cypher` scripts
  (`neo4j_scripts/cyphers/`) plus Python loaders. The graph is sessions, laps, cars, drivers, and
  team-series seasons, rounds, and weekends. Example: `races/set_car_avg_middle_half_lap.cypher`
  takes each car's valid race laps, keeps the interquartile middle half, averages it, and drops
  cars that ran under 75% of the winner's laps. That's real pace analysis, not CRUD. The
  [sra-insights](https://github.com/nosv1/sra-insights) server queries the graph (28 `MATCH`es
  behind 17 endpoints, through 2026-05). Uses `MATCH`/`MERGE`, `ON CREATE SET`, chained `WITH`
  pipelines, `COLLECT`, `UNWIND`, list comprehensions, `REDUCE`. **He said it was fun to learn
  (10-26)**: same pattern as Rust in GTALens, a tool learned because a project he cared about
  needed it.
- **Used:** schema design, `INSERT ... ON DUPLICATE KEY UPDATE` upserts, `INNER` and `LEFT JOIN`
  (including a left-join anti-join delete), derived-table and `NOT IN` subqueries, `GROUP BY`,
  `DISTINCT`, `ORDER BY ... LIMIT`, commits.
- **Not found:** window functions (`OVER (...)`), CTEs (`WITH`), parameterized queries. Every
  query is an f-string with hand-rolled quote escaping. Analyst interviews lean hard on window
  functions and CTEs, and any dev interview would flag the injection risk. Those three are the
  real SQL gap, and they're small.
- **Power BI / Tableau:** no evidence. That's the actual gap.

Sources:
[Fluid Jobs — race team](https://fluidjobs.com/jobs/race-team) ·
[F1 Strategy Engineer (2026)](https://www.motorsportjobs.com/en/job/f1-strategy-engineer-2026-3) ·
[Graduate Race Strategy Engineer, Silverstone](https://www.motorsportjobs.com/en/job/graduate-race-strategy-engineer-1) ·
[Strategy Engineer jobs](https://www.motorsportjobs.com/en/jobs/strategy-engineer) ·
[Autosport — top five roles](https://www.autosport.com/general/news/top-five-roles-on-motorsport-jobs-this-week-10832740/10832740/) ·
[iRacing jobs](https://www.iracing.com/jobs) ·
[Sportscar Data Analyst, Concord](https://www.motorsportjobs.com/us/job/motorsports-sportscar-data-analyst) ·
[Fluid Jobs — data analyst](https://fluidjobs.com/jobs/data-analyst) ·
[Garmin Data Scientist 2 (SpaceTalent)](https://jobs.spacetalent.org/companies/garmin-2/jobs/56870350-data-scientist-2) ·
[Garmin Data Scientist 2 (WeAreDevelopers)](https://www.wearedevelopers.com/jobs/ext/7169825/data-scientist-2) ·
[Garmin Aviation Data Analyst (Tallo)](https://tallo.com/talent/job/transportation/pilot/ks/olathe/aviation-pilot-data-analyst-8a2b6bc9) ·
[Automotive Inventory Analyst](https://www.virtualvocations.com/job/automotive-inventory-analyst-3113489-i.html) ·
[Demand Analyst, Remote](https://builtin.com/job/demand-analyst-remote-usa/7360822) ·
[Carrier Strategic Inventory Analyst](https://remotive.com/remote/jobs/supply-chain/strategic-inventory-analyst-5117521) ·
[Operations Analyst salary, KC MO](https://www.payscale.com/research/US/Job=Operations_Analyst/Salary/a81b2a1d/Kansas-City-MO) ·
[Track Titan raises $5M](https://itbrief.news/story/track-titan-raises-usd-5m-to-power-ai-racing-coaching) ·
[Coach Dave Academy](https://coachdaveacademy.com/?p=98209)

## Check-ins

- 2026-10-26 (CT): Career check-in: Most analyst postings I pulled want SQL plus a BI tool. Have you started either, or is your Apps Script work already covering some of it?
  - **His answer (10-26):** neither is part of Apps Script or any current project; his SQL is from
    the Discord bot days. Reviewed and written up above.
