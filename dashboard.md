# X Algo Observer — Web Dashboard Blueprint

## Purpose
This dashboard is designed to help observe and understand how X’s recommendation algorithm appears to behave over time using only observable data.

It focuses on pattern detection, early signals, and identifying when algorithm behavior changes (“regime shifts”), not on prediction or reverse engineering.

---

## Target User
- Individual creators
- Researchers
- Analysts experimenting with content performance on X

The user is assumed to manually log or import post performance data.

---

## Primary Screens

### 1. Overview (Home)
**Goal:** Quick situational awareness

Displays:
- Current algorithm climate:
  - Stable
  - Volatile
  - Chaotic
- Summary of the last 24 hours:
  - Number of posts tested
  - Average early velocity
- Alerts:
  - “Possible regime shift detected”
- Key indicators:
  - Early impressions trend
  - Engagement ratio trend

---

### 2. Post Experiments
**Goal:** Inspect individual posts

For each post:
- Timestamp
- Post format (text / image / video / link)
- Topic or tag
- Early impressions:
  - 5 minutes
  - 15 minutes
  - 30 minutes
- Engagement metrics:
  - Likes
  - Replies
  - Reposts
- Distribution state:
  - Green (expanded reach)
  - Yellow (local reach)
  - Red (suppressed)

---

### 3. Trends
**Goal:** Detect patterns over time

Visualizations:
- Performance by time of day
- Performance by format
- Topic heat map (what appears favored recently)
- Engagement vs impressions over time

---

### 4. Regime Changes
**Goal:** Identify algorithm shifts

Shows:
- Timeline of detected regime changes
- Before vs after comparisons
- Notes on:
  - What stopped working
  - What started working
- Reference control posts used for detection

---

### 5. Notes & Hypotheses
**Goal:** Human interpretation layer

Features:
- Manual notes
- Hypotheses about algorithm behavior
- Links to specific posts or time ranges
- Free-form research observations

---

## Non-Goals
- No automation of posting
- No scraping
- No claims of “cracking” the algorithm
- No guaranteed performance improvements

---

## Status
This document defines the planned web interface only.
Implementation details will be added in future iterations.