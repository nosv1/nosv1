# Dealership lot app

**Started 2026-11-17. Mode: "just build it"** (his call: "I have the flow, and the need, not the
time"). Claude writes the code; Chris owns the flow and the requirements.

## What it replaces

His current Google Sheets system: three spreadsheets, split only because Sheets got slow and
crashed (calculation time, cell count), especially on a phone.

- **Import:** VINCue, IKON battery reports, IGNITE schedules, recon, etc. are pasted into a CDK Data
  Import sheet; Inventory Helpers compile one unique list of VINs (Inventory). An Audit tab reads
  Inventory Extra back from the Inventory spreadsheet (a back-reference, not circular).
- **Inventory:** the heavy lifting. Takes Inventory plus logged locations from Inputs and assigns
  attributes to each vehicle in an Inventory Extra table.
- **Inputs:** what he uses on the lot to log which cars are where, plus notes.

His diagram (11-17) is a little stale; redraw for the app.

## What carries over

- One data store. The three-spreadsheet split is a Sheets workaround; the copies go away.
- Three jobs: ingest, compute attributes, log on the lot.
- **Core requirement:** lot logging is fast on a phone. That's what Sheets couldn't do.
- The overflow-lot retrieval cost (25×7 grid, Dijkstra's; see sessions/2026-11.md, 11-17) is one
  attribute this system feeds.

## Answers so far (11-17)

- **Platform:** stay inside Google. Shape: dealership spreadsheets <-> his bridge spreadsheet <-> app.
  So an Apps Script web app.
- **Users:** him first; an assistant is being hired soon, who shouldn't need to learn his sheets.
- **Workflow today:** download the inventories as Excel, upload them to a Google Drive folder, a script
  copies them into Import, Import parses the columns he cares about. Covers new, used, deleted,
  appraisals, leads, reconditioning, wholesale. Then he walks the lot and updates locations in Inputs.
- **Inputs sheet (fig 1):** one column pair per walk line (model label + stock # or last 6 of VIN),
  cells in physical order. Headers are spot ranges, e.g. "1 G 30 - 8" = line 1, row G, spots 30 to 8;
  "11 K 11-1 / E 12-1" crosses two rows. Walk order roughly counterclockwise, north to south.
- **Cell colors:** green = repark (alignment); pink = empty spot (a number left in the cell is
  probably being shown, not missing); orange = issue (damage, restock, etc.); red = dead battery;
  blue = move to another spot; yellow = missing in-car paperwork.
- **Edit script:** e.g. typing "11213 window sticker addendum xy" turns the cell yellow, keeps 11213 as
  the value and moves the text into a cell note. (Full codes: round 2, Q7.)
- **Main (Inventory) sheet:** dead batteries, inventory type counts, sales rundowns, lists of cars
  that could be moved to avoid duplicates, "a lot of that kind of stuff."
- **Map tab (fig 2):** the same data laid out in the lot's shape around the buildings (service,
  store, delivery bay, service garage), plus a "might be somewhere over here" box for unplaced cars.
  Used cars show #N/A there.
- **Scale:** about 1,500 spots in total; he logs about 300 in front and about 100 in back. Tabs exist for
  lots he doesn't walk (recon, service).

## Answers, round 2 (11-18)

1. **Spots:** painted, every car in a real spot; curbs when full (e.g. a "north curb" input area, where
   only "in this lot or not" matters). **The location ID depends on the lot:** the retail lot uses
   "RETAIL [section]" (the row is known but matters less); every other lot is just the lot name. The
   overflow lot is one location for now; a per-spot grid only for the Dijkstra's work.
2. **Map:** mainly a quick lookup ("do I have a location for this stock # / VIN?") via find-on-page;
   otherwise for show. So a search box covers the real use on day one; the drawn map can wait.
3. **Scope:** 350–450 spots for retail-ready cars (new, plus used cars through detail). ~500 more for
   recon, service, employees.
4. **IDs:** used cars are logged by VIN (last 6), new by stock #; both get pulled to the map so either
   can be searched. #N/A = blank cell or an ID not in inventory (a REGEXEXTRACT on "" errors).
   App: the VIN is the key; accept either a stock # or the last 6 of the VIN as input.
5. **Emoji:** ~35 flags, nearly all computed from Inventory Extra columns in one ArrayFormula
   (new: photo count < 20, dead / started after dead, not reporting, issue, unique, duplicate, move to
   retail, oldest, inactive, sold < 10 days ago, retired loaner, dealer trade, multiple locations, stop
   sale, sticker event, needs MSRP, needs addendum, recall; used: UVeye scan, needs physical, needs
   miles, transferred out, age buckets 21/45 days). Plus class, color and certification emoji.
6. **Multiple flags:** no way to show them today. The app holds a set of flags per car.
7. **Edit script** (`onEdit`, Inputs):
   - `x` clears the cell. In the overflow lot it resets the key location to "TBD" instead.
   - `<number><note>x<color>` keeps the number, appends the note to the cell note and sets the color:
     b, g, p, r, w, y, o.
   - `<number>ps` = parked out of spot: logs it to a ParkedOutOfSpot list, clears the cell, turns it pink.
8. **Walks:** edits changes only, never retypes. The used lot (~90 cars) every morning; the new lot is
   spot-checked, triggered by bad parking or **dark cars touching dark cars (or light touching light)**.
   iPhone 16 Pro; signal present but spotty (near an airport); battery forces Low Power Mode late in
   the day, which slows Sheets further.
9. **Sold, not delivered:** stays in its cell with a "probably sold" emoji.
10. **Spots changing:** shouldn't; the lot was just repaved.

His other scripts: Inventory (Code, ReconPaths, AStar, Dijkstra, StatusDialog, services, vAutoHeaders,
LocationLog) and Import (Code, ImportExcelAttachments). **His call (11-18): the scripts are his, not
the dealership's, and fine in public.** Exception found 11-18: Inventory's `vAutoHeaders.js` holds a
vAuto session cookie (a login credential), so it's git-ignored in claudes-lot. Pulled with clasp into
claudes-lot `reference/scripts/` (inputs, inventory, import). App repo: private [claudes-lot](https://github.com/nosv1/claudes-lot),
cloned at `C:\Users\chris\claudes-lot`; screenshots live in its `reference/`.

**Spots and order (11-18):**

- Every spot gets an ID for the app. People see a plain-language label (e.g. "Used Lot, curb side,
  spot 20"), never the code.
- Order within a row is required, because neighbors matter. When duplicates in front get swapped for
  unique cars from the back, neighboring cars can't be dark next to dark or light next to light. A
  unique car with no swap that satisfies that is no use, unless moving n other cars makes room. That's
  an optimization problem, offered to him as his piece (like the overflow Dijkstra's).
- **Neighbors** = cars in spots directly next to each other. Where a sidewalk separates two spots,
  a clash is a soft rule there: avoided if possible, not a problem if not. So the app stores, per
  spot, its neighbor and whether a sidewalk lies between.
- **The solver is not for now.** It's been on his to-do list a long time; he's open to thinking it
  through later. Getting scripts: clasp (11-18).

Next rounds: the import side (which systems, how often, any automatic exports), and what goes back out
to the dealership spreadsheets.

## Open (his, from the start)

- The day list: each time he opens a sheet, what is he finding out or recording? Plus what breaks
  or annoys him (crashes, stale pastes, dead batteries, double entry).
- Constraints: must it stay inside the dealership's Google Workspace? Who else uses it?
