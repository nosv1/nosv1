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

## Open (his)

- The day list: each time he opens a sheet, what is he finding out or recording? Plus what breaks
  or annoys him (crashes, stale pastes, dead batteries, double entry).
- Constraints: must it stay inside the dealership's Google Workspace? Who else uses it?
