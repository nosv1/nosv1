// Google Apps Script: delete events imported from motogp.ics (UIDs ending @motogp-ics).
// Paste at script.google.com, run cleanup with DRY_RUN = true, check the log, then flip it.
// Change getDefaultCalendar() to getCalendarsByName('MotoGP')[0] to clean the MotoGP calendar instead.
function cleanup() {
  const DRY_RUN = true; // flip to false once the log looks right
  const cal = CalendarApp.getDefaultCalendar();
  const events = cal.getEvents(new Date('2026-11-01'), new Date('2028-01-01'));
  const mine = events.filter(e => e.getId().endsWith('@motogp-ics'));
  mine.forEach(e => {
    Logger.log(`${e.getStartTime()}  ${e.getTitle()}`);
    if (!DRY_RUN) e.deleteEvent();
  });
  Logger.log(`${mine.length} events ${DRY_RUN ? 'would be' : ''} deleted`);
}
