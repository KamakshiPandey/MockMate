import random


def generate_feedback(answer):

    answer = answer.strip()

    word_count = len(answer.split())

    # Default values
    score = 50
    strengths = []
    improvements = []

    # Length Analysis
    if word_count > 80:
        score += 20
        strengths.append(
            "Good detailed explanation."
        )
    elif word_count > 40:
        score += 10
        strengths.append(
            "Decent explanation length."
        )
    else:
        improvements.append(
            "Try explaining in more detail."
        )

    # Technical Keywords
    technical_keywords = [
        "api",
        "database",
        "react",
        "python",
        "fastapi",
        "authentication",
        "jwt",
        "algorithm",
        "optimization",
        "machine learning",
        "deployment",
        "cloud"
    ]

    detected_keywords = []

    lower_answer = answer.lower()

    for keyword in technical_keywords:

        if keyword in lower_answer:

            detected_keywords.append(keyword)

    # Technical Depth Score
    if len(detected_keywords) >= 5:
        score += 20

        strengths.append(
            "Strong technical depth detected."
        )

    elif len(detected_keywords) >= 2:
        score += 10

        strengths.append(
            "Good use of technical concepts."
        )

    else:
        improvements.append(
            "Add more technical explanation."
        )

    # Communication Check
    filler_words = [
        "umm",
        "uh",
        "like",
        "basically"
    ]

    filler_count = 0

    for word in filler_words:

        filler_count += lower_answer.count(word)

    if filler_count > 3:

        score -= 10

        improvements.append(
            "Reduce filler words while speaking."
        )

    else:

        strengths.append(
            "Clear communication style."
        )

    # Confidence Estimation
    confidence = random.randint(70, 95)

    # Final Score Limit
    if score > 100:
        score = 100

    if score < 0:
        score = 0

    # Suggested Answer
    suggested_answer = (
        "Structure your answer using: "
        "Introduction → Technical Approach → "
        "Challenges → Solution → Result."
    )

    return {
        "score": score,
        "confidence": confidence,
        "technical_keywords_used": detected_keywords,
        "strengths": strengths,
        "improvement_areas": improvements,
        "suggested_answer_tip": suggested_answer
    }