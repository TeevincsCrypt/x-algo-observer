# X Algo Observer — Data Model

This document defines the core data structures used by the dashboard.
All fields are observational and manually logged or imported.

---

## Entity: Post

Represents a single post published on X.

Fields:
- post_id (string)
- timestamp (date + time)
- format (text / image / video / link)
- topic (string or tag)
- tone (neutral / opinion / question / provocative)
- hashtags_used (integer)
- control_post (boolean)

---

## Entity: EarlyMetrics

Captured shortly after posting.

Fields:
- impressions_5min
- impressions_15min
- impressions_30min
- likes
- replies
- reposts
- bookmarks
- profile_clicks

Derived:
- early_velocity
- engagement_ratio

---

## Entity: DistributionState

Classification assigned to a post.

Values:
- GREEN (expanded distribution)
- YELLOW (local distribution)
- RED (suppressed or deprioritized)

---

## Entity: DailySummary

Aggregated daily signals.

Fields:
- date
- posts_tested
- avg_early_velocity
- avg_engagement_ratio
- dominant_formats
- dominant_topics
- detected_algo_climate (stable / volatile / chaotic)

---

## Entity: RegimeShift

Represents a detected algorithm behavior change.

Fields:
- detected_at (date)
- confidence_level (low / medium / high)
- control_post_reference
- notes