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
  the value and moves the text into a cell note.
- **Main (Inventory) sheet:** dead batteries, inventory type counts, sales rundowns, lists of cars
  that could be moved to avoid duplicates, "a lot of that kind of stuff."
- **Map tab (fig 2):** the same data laid out in the lot's shape around the buildings (service,
  store, delivery bay, service garage), plus a "might be somewhere over here" box for unplaced cars.
  Used cars show #N/A there.
- **Scale:** about 1,500 spots in total; he logs about 300 in front and about 100 in back. Tabs exist for
  lots he doesn't walk (recon, service).

## Open questions (his, answer when he can)

He was still answering when Claude asked these; he ran out of time 11-17.

1. Are the spot numbers physically painted on the lot (G30, G29…)? If so, is "G29" the spot's ID and
   the walk order just a route through those IDs?
2. Who uses the map, and for what (finding a car for someone, spotting gaps, showing a manager)? Want it
   in the app on day one?
3. Other lots (recon, service…): in the app from the start, or only the ~400 he walks, the rest later?
4. The #N/A cells on the map are nearly all used cars (VIN-6 entries): a known bug, or is the lookup
   only built for stock #s? Related: why stock # for new and last 6 of the VIN for used (what's printed
   on the car, or the systems)? Which one does the app treat as the car's ID?
5. What do the emoji in the model labels mean? Which come from data, which are added by hand?
6. Can a car have more than one flag at a time (e.g. dead battery and missing paperwork)? A cell only
   holds one color; the app could hold several.
7. What codes does the edit script recognize besides "xy"?
8. On a walk, does he retype every spot or only the changes? How often does he walk, on what device
   (phone, tablet), and is the signal good everywhere on the lot (offline needed)?
9. When a car sells but is still in its cell, what happens today?
10. Do any spots change (restriped lines, cones for events)?

Next rounds: the import side (which systems, how often, any automatic exports), and what goes back out
to the dealership spreadsheets.

## Open (his, from the start)

- The day list: each time he opens a sheet, what is he finding out or recording? Plus what breaks
  or annoys him (crashes, stale pastes, dead batteries, double entry).
- Constraints: must it stay inside the dealership's Google Workspace? Who else uses it?
