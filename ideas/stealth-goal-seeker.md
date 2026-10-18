# Stealth goal seeker (idea, 2026-10-10)

> **Reframed 10-17: red-teaming his own defense.** See [the 10-17 section](#10-17-reframed-red-teaming-his-own-defense).
> The history below is kept as it was.

From his grad robotics class, about three years ago. Never finished because the class ended.

## The problem

- **Blue robot**: reach a goal.
- **Two or three red robots**: move along **predetermined paths**, each with a detection cone.
- Map of the space built with SLAM beforehand.

## What the class already had working

- Route planning to the goal, without detectors.
- Proportional navigation to avoid the detector robots.

## The open problem, in his words

"How do you avoid the red robot and also stay optimal to getting to the goal."

## Status

**Active, 10-11.** Its own repo (created 10-11), like every project; not a curriculum week. The
10-10 "in the curriculum" plan was overtaken the same evening when the curriculum stopped being the
path. It ticks skills off the [12_months](https://github.com/nosv1/12_months) map instead (SLAM,
planning, ROS 2 + Gazebo, controllers). The 2022 repos below stay as the archive; the new repo
starts fresh, same as strategist → iracing-soma. Design is his. Flight-instructor terms apply.

## The original code (found 10-10)

Course: **ME5501 Robotics, Fall 2022**, ROS 2 (`rclpy`) + Gazebo + TurtleBot3.

- [seagraves_unmanned_systems_pkg](https://github.com/nosv1/seagraves_unmanned_systems_pkg):
  ROS 2 package. `TagYoureIt/pursuer.py` and `evader.py` (pursuit-evasion between two TurtleBots),
  `support_module/PN.py` (proportional navigation), `PID.py`, `DetectedObject.py` (lidar object
  detection), `PathFollower/`, `multi_bots.py`, `post_processing/LogPlotter.py`.
- [seagraves_unmanned_systems](https://github.com/nosv1/seagraves_unmanned_systems): homeworks.
  `SearchAlgorithms/` has Dijkstra, A*, RRT, Dubins testing, and a GA for TSP, with JSON scenarios.
  `Exam2/` has TagYoureIt videos, A* TSP, and a Gazebo world. `HW6/` is the PN write-up.
- **The detector-cone scenario itself isn't in either repo.** The class ended before it was built.

## His first approaches (10-11, morning, in bed)

1. **Observe first**: watch red's movements to see if it repeats, then find the optimal path.
2. **Scout**: blue has a scout.
3. **Cone as obstacle**: add red's *known* detection cone to blue's obstacle list and replan as
   needed.

## Scoring and sensors (10-11, his)

- Blue's sensors vs red's: if blue's aren't better, blue must be faster. A blue that's slower and
  doesn't know where red is "is going to lose every time."
- **Time is scored.** Reach the goal as fast as possible, undetected.
- Detected is "not ideal"; detected **and caught** is the real problem. Maybe being slightly detected
  is acceptable if blue still reaches the goal.
- **Rescue variant:** reach the goal and get back, undetected.

## Name: Otto (10-11, his pick)

**OTTO**: *Observe, Think, Then Operate.* Named for the robot, not the mission, so it still fits
if the robot's capabilities grow into something else (his reason). Stealth is Otto's first mission.
Repo: [otto-the-robot](https://github.com/nosv1/otto-the-robot) ("to at least be a little
descriptive"; lowercase to match his other repos), created 10-11.

## 10-17: reframed, red-teaming his own defense

Evening session in the repo (WSL). Setup is done: ROS 2 Jazzy, Gazebo Harmonic, Nav2 TB3 sim all
checked. Then he went through the story four times:

1. **Stealth** (the original). Dropped: "the idea behind sneaking means no cooperation, and i
   don't like that mindset."
2. **Considerate store robot** (QuikTrip's floor cleaner is too slow for people moving at walking
   speed). Dropped: "these aren't 'fun' problems, these are just chores." His point: "things are
   high risk because there is no cooperation."
3. **A game** (tag, capture the flag). "*but why* are we playing tag."
4. **Red-teaming his own defense** (kept; he enjoyed red-teaming at work). He builds both sides:
   the patrol is his defense, Otto is the attacker built to find its holes, and each attack that
   works hardens the defense. Has both the stakes and the cooperation.

**Decided 10-17 (all his calls unless marked):**

- **Colors follow security convention:** blue = the patrol (his defense), red = Otto (the attacker).
  This flips the original. "blue is me... BUT NO that's not nice of me, UNLESS the actual objective
  is for me to design an attacker on my own defense."
- **Scope: 1v1 or 2v1.** One Otto, always. The scout approach is parked.
- **Sensing: 6 m for both sides** (sim lidar is 20 m, real LDS-01 about 3.5 m).
- **Map:** more complex than the Nav2 sandbox (depot or warehouse), for fun. He's fine editing robot
  models for speed and sensing. Blocked 10-17 by a Gazebo Fuel 502 outage.
- **C++** for the nodes: "keeps me from lazy understanding old code." The 2022 Python is a
  reference to port.
- **Packages** (names are Claude's, at his request): `otto` (nodes: `blue/`, `red/`, `debrief/`) and
  `otto_sim` (assets). MIT license ("no liabilities, ships as is").
- **Roadmap as homework** with Mission: Impossible briefs and a scoreboard (attack × defense)
  standing in for classmates. It lives in the repo: `docs/roadmap.md`.

Not settled: what makes the cone a cone when both sides sense the same (HW2), and what "caught"
means (HW3).