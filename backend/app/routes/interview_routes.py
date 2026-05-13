from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import ask_ai_question

router = APIRouter()

# =========================
# CONSTANT
# =========================
MAX_QUESTIONS = 10


# =========================
# REQUEST MODEL
# =========================
class AnswerRequest(BaseModel):
    answer: str
    previous_question: str
    question_count: int
    interview_type: str  # "technical" or "hr"


# =========================
# START INTERVIEW
# =========================
@router.get("/start")
def start_interview(interview_type: str = "technical"):

    if interview_type == "hr":
        prompt = "Start an HR interview. Ask the first behavioral question."
    else:
        prompt = "Start a technical interview. Ask the first question."

    first_question = ask_ai_question(prompt)

    return {
        "question": first_question,
        "question_count": 1
    }


# =========================
# NEXT QUESTION + EVALUATION
# =========================
@router.post("/next")
def next_question(data: AnswerRequest):

    # ✅ STOP at max questions
    if data.question_count >= MAX_QUESTIONS:
        return {
            "completed": True,
            "message": "Interview finished. Generating report..."
        }

    # ✅ Dynamic prompt based on type
    if data.interview_type == "hr":
        system_type = "You are an HR interviewer.The candidate is a B.Tech student preparing for placements. Do NOT assume any senior role like manager or experienced professional.Ask a simple and relevant HR interview question suitable for a fresher.Keep it short."
    else:
        system_type = "You are a technical interviewer. Focus on DSA, backend, system design ,projects from resume."

    prompt = f"""
    {system_type}

    Previous Question:
    {data.previous_question}

    Candidate Answer:
    {data.answer}

    1. Evaluate the answer:
       - Give score out of 10
       - Give strengths
       - Give weaknesses

    2. Ask next question.

    Return STRICT JSON:
    {{
        "score": number,
        "feedback": "...",
        "next_question": "..."
    }}
    """

    result = ask_ai_question(prompt)

    return {
        "completed": False,
        "data": result,
        "next_question_number": data.question_count + 1
    }