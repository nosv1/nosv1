# MotoGP calendar

Puts MotoGP qualifying, sprint and race times in Google Calendar. It builds an .ics file from the official
motogp.com API, so you import your own copy and don't subscribe to anyone else's calendar.

```sh
python motogp_ics.py 2026 2027   # writes motogp.ics in the current folder
```

Import it in Google Calendar: Settings → **Import & export** → **Import**, with "Add to calendar" set to
the **MotoGP** calendar, not the main one.

- **Qualifying** is one event from the start of Q1 to the end of Q2. The **sprint** is 45 min and the **race**
  1 h; the API gives no end time for races.
- A round with no published session times becomes an all-day "(times TBA)" weekend placeholder. Times usually
  appear a few weeks before the round, so re-run then.
- Rounds already finished are skipped.
- UIDs are stable (`<year>-<round>-<Q|SPR|RAC|WKND>@motogp-ics`). Not yet tested: whether re-importing in
  Google updates existing events or adds duplicates. A placeholder's UID differs from its timed events, so
  once times are out, delete the placeholders with [cleanup.gs](cleanup.gs) (it matches every `@motogp-ics`
  event; narrow the filter to `-WKND@motogp-ics` to delete only placeholders).

Data source: `https://api.motogp.pulselive.com/motogp/v1/events?seasonYear=<year>`, the undocumented API
behind motogp.com. It may change without notice.
