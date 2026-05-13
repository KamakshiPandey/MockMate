import os
from typing import List, Dict

# You can switch provider later easily
# Example: OpenAI / OpenRouter / Ollama

try:
    from openai import OpenAI
except:
    OpenAI = None


# =========================
# CONFIG
# =========================
API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key")

client = OpenAI(api_key=API_KEY) if OpenAI else None

MODEL = "gpt-4o-mini"


# =========================
# 1. GENERATE INTERVIEW QUESTIONS
# =========================
def generate_interview_questions(topic: str, difficulty: str = "medium", count: int = 5):
    """
    Generate interview questions based on topic and difficulty
    """

    prompt = f"""
    You are an expert interviewer.

    Generate {count} {difficulty} level interview questions for the topic: {topic}

    Return in JSON format like:
    [
      {{
        "question": "...",
        "expected_concepts": ["..."]
      }}
    ]
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content


# =========================
# 2. EVALUATE ANSWER
# =========================
def evaluate_answer(question: str, answer: str):
    """
    Evaluate user answer and give score + feedback
    """

    prompt = f"""
    You are an AI interview evaluator.

    Question: {question}
    Answer: {answer}

    Evaluate the answer and return JSON:
    {{
        "score": (0 to 10),
        "feedback": "...",
        "strengths": ["..."],
        "improvements": ["..."]
    }}
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content


# =========================
# 3. RESUME ANALYSIS
# =========================
def extract_skills_from_resume(resume_text: str):
    """
    Extract skills from resume
    """

    prompt = f"""
    Extract technical skills from this resume text:

    {resume_text}

    Return only a JSON list of skills.
    Example:
    ["Python", "React", "Machine Learning"]
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content


# =========================
# 4. INTERVIEW SUMMARY GENERATION
# =========================
def generate_interview_summary(scores: List[float], feedback_list: List[str]):
    """
    Generate final interview summary
    """

    prompt = f"""
    You are an AI HR assistant.

    Scores: {scores}
    Feedback: {feedback_list}

    Generate:
    - overall performance summary
    - final recommendation (hire / not hire / need improvement)
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content