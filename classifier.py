# X Algo Observer — Distribution Classifier v0.1

def calculate_early_velocity(impressions_5, impressions_15, impressions_30):
    """
    Simple early velocity heuristic.
    """
    return impressions_30 - impressions_5


def calculate_engagement_ratio(likes, replies, reposts, impressions_30):
    """
    Engagement divided by impressions.
    """
    if impressions_30 == 0:
        return 0
    return (likes + replies + reposts) / impressions_30


def classify_distribution(impressions_5, impressions_15, impressions_30,
                          likes, replies, reposts):
    """
    Returns GREEN, YELLOW, or RED based on early signals.
    """

    velocity = calculate_early_velocity(
        impressions_5, impressions_15, impressions_30
    )
    engagement_ratio = calculate_engagement_ratio(
        likes, replies, reposts, impressions_30
    )

    # Heuristic thresholds (can be tuned later)
    if velocity > 500 and engagement_ratio > 0.02:
        state = "GREEN"
    elif velocity > 100:
        state = "YELLOW"
    else:
        state = "RED"

    return state, velocity, engagement_ratio


# Example usage
if __name__ == "__main__":
    state, velocity, ratio = classify_distribution(
        impressions_5=120,
        impressions_15=260,
        impressions_30=900,
        likes=20,
        replies=4,
        reposts=3
    )

    print("Distribution state:", state)
    print("Early velocity:", velocity)
    print("Engagement ratio:", round(ratio, 3))