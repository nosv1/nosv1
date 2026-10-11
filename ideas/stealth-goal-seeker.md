# Stealth goal seeker (idea, 2026-10-10)

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

**Active, 10-11.** Its own repo (not created yet), like every project; not a curriculum week. The
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

Open: the repo name.

## Scoring and sensors (10-11, his)

- Blue's sensors vs red's: if blue's aren't better, blue must be faster. A blue that's slower and
  doesn't know where red is "is going to lose every time."
- **Time is scored.** Reach the goal as fast as possible, undetected.
- Detected is "not ideal"; detected **and caught** is the real problem. Maybe being slightly detected
  is acceptable if blue still reaches the goal.
- **Rescue variant:** reach the goal and get back, undetected.
