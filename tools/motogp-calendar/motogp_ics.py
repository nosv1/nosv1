"""Build an .ics of MotoGP qualifying, sprint and race from the official motogp.com API.

Usage: python motogp_ics.py 2026 2027  ->  motogp.ics
Import (not subscribe) in Google Calendar: Settings > Import & export > Import.
Events have stable UIDs, so re-importing after times are published updates them in place.
"""
import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

API = "https://api.motogp.pulselive.com/motogp/v1/events?seasonYear={}"
DURATION = {"SPR": timedelta(minutes=45), "RAC": timedelta(hours=1)}


def parse(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%S%z").astimezone(timezone.utc)


def stamp(dt):
    return dt.strftime("%Y%m%dT%H%M%SZ")


def esc(s):
    return s.replace("\\", "\\\\").replace(",", "\\,").replace(";", "\\;")


def vevent(uid, summary, location, start=None, end=None, allday=None):
    lines = ["BEGIN:VEVENT", f"UID:{uid}@motogp-ics", f"DTSTAMP:{stamp(datetime.now(timezone.utc))}",
             f"SUMMARY:{esc(summary)}", f"LOCATION:{esc(location)}"]
    if allday:
        d0, d1 = allday
        lines += [f"DTSTART;VALUE=DATE:{d0:%Y%m%d}", f"DTEND;VALUE=DATE:{d1:%Y%m%d}"]
    else:
        lines += [f"DTSTART:{stamp(start)}", f"DTEND:{stamp(end)}"]
    return lines + ["END:VEVENT"]


def events_for(year):
    with urllib.request.urlopen(API.format(year)) as r:
        data = json.loads(r.read().decode("utf-8"))
    out = []
    for e in data:
        if e.get("kind") != "GP" or e.get("status") == "FINISHED":
            continue
        name = " ".join(e["name"].split()).title().replace("Of The", "of the").replace(" Of ", " of ")
        short = e.get("shortname") or name
        loc = (e.get("circuit") or {}).get("name", "")
        s = {b["shortname"]: b for b in e.get("broadcasts") or []
             if (b.get("category") or {}).get("acronym") == "MGP"}
        key = f"{year}-{short}"
        if "Q1" in s and "RAC" in s:
            out.append(vevent(f"{key}-Q", f"MotoGP Qualifying - {name}", loc,
                              parse(s["Q1"]["date_start"]), parse(s.get("Q2", s["Q1"])["date_end"])))
            for code, label in (("SPR", "Sprint"), ("RAC", "Race")):
                if code in s:
                    t = parse(s[code]["date_start"])
                    out.append(vevent(f"{key}-{code}", f"MotoGP {label} - {name}", loc, t, t + DURATION[code]))
        else:  # times not published yet: all-day weekend placeholder
            d0 = datetime.fromisoformat(e["date_start"]).date()
            d1 = datetime.fromisoformat(e["date_end"]).date() + timedelta(days=1)
            out.append(vevent(f"{key}-WKND", f"MotoGP - {name} (times TBA)", loc, allday=(d0, d1)))
    return out


def main(years):
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//motogp-ics//EN", "CALSCALE:GREGORIAN"]
    n = 0
    for y in years:
        for ev in events_for(y):
            lines += ev
            n += 1
    lines.append("END:VCALENDAR")
    with open("motogp.ics", "w", encoding="utf-8", newline="\r\n") as f:
        f.write("\n".join(lines) + "\n")
    print(f"wrote motogp.ics with {n} events")


if __name__ == "__main__":
    main(sys.argv[1:] or [str(datetime.now().year)])
