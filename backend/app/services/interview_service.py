from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def evaluate_answer(question, answer):
    prompt = f"""
    You are a professional interviewer.

    Question: {question}
    Candidate Answer: {answer}

    Evaluate the answer based on:
    - Accuracy
    - Clarity
    - Depth

    Return response in JSON format:
    {{
        "score": number (out of 10),
        "strengths": "...",
        "weaknesses": "...",
        "improved_answer": "..."
    }}
    """

    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    print("USING MODEL: mixtral-8x7b-32768")
    return response.choices[0].message.content