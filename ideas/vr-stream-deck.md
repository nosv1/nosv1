# Stream Deck buttons without the Stream Deck (idea, 2026-11-26)

**The problem:** in VR, the Stream Deck is out of reach. The buttons are useful (Close Rig and the rest),
but pressing one means taking the headset off or reaching blind. He wants the same buttons to work
without touching the box.

**The idea:** the same actions, triggered from inside VR or from something already in his hands.

## Directions to weigh

- **Wheel or button box:** map spare wheel buttons to the actions. The hands are already there, and nothing
  shows in VR.
- **In-VR panel:** an overlay he can see and point at or touch in the headset.
- **Voice:** "close the rig", through the speech pipeline iracing-soma already has.
- **Keyboard shortcuts:** hotkeys on the PC (AutoHotkey or similar). Simplest, but a keyboard is hard to find
  blind in VR too.

## Open questions

- Which buttons does he actually use mid-session versus before or after? Close Rig runs after the headset
  comes off, so it may not need to be reachable in VR at all.
- Does the Stream Deck software let other apps trigger its buttons, or do the actions need to live
  as standalone scripts (like `~/scripts/Close-Rig.cmd`) that any trigger can call?

Related: the rig close script (session log 2026-11-26), [iracing-race-engineer.md](iracing-race-engineer.md).
