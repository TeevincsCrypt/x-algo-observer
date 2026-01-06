# X Algo Observer

## What This Is
X Algo Observer is a black-box research protocol for observing how X’s recommendation algorithm behaves over time, even when it changes frequently.

This project does NOT attempt to reverse-engineer the algorithm.
It focuses on detecting patterns, gradients, and regime shifts using observable inputs and outputs.

---

## Core Assumptions
- The algorithm is a black box
- Only inputs and outputs are observable
- Early engagement velocity is a dominant signal
- The system changes frequently and non-transparently

---

## Protocol Overview
1. Control inputs (post time, format, topic, tone)
2. Measure early signals (5–30 minutes)
3. Classify distribution states (green / yellow / red)
4. Use control posts to detect regime shifts
5. Adapt a weighted model instead of fixed rules

---

## Pseudo-Code (High Level)

```text
SYSTEM X_Algo_Observer

INITIALIZE
  MetricsLog
  WeightModel
  ControlPostProfile

DAILY LOOP
  Assess algorithm climate
  Schedule micro-experiments
  Publish controlled posts
  Capture early metrics
  Classify distribution state
  Detect regime shifts
  Adapt weighting model


---

## Future Web Dashboard (Planned)

This project is intended to evolve into a web-based dashboard for observing and analyzing changes in X’s recommendation behavior over time.

The dashboard will visualize patterns, early signals, and detected regime shifts based on logged post metrics.