from pydantic import BaseModel, Field
from typing import List, Optional


# =========================
# 1. Resume Upload Schema
# =========================
class ResumeUploadResponse(BaseModel):
    message: str
    extracted_text: str
    skills: Optional[List[str]] = []


# =========================
# 2. Interview Question Request
# =========================
class InterviewRequest(BaseModel):
    topic: str = Field(..., description="Role like 'Software Engineer'")
    difficulty: Optional[str] = Field(
        default="medium",
        description="easy | medium | hard"
    )
    num_questions: Optional[int] = Field(default=5, ge=1, le=20)


# =========================
# 3. Interview Question Response
# =========================
class InterviewQuestion(BaseModel):
    question_id: int
    question: str
    expected_concepts: Optional[List[str]] = []


class InterviewResponse(BaseModel):
    topic: str
    questions: List[InterviewQuestion]


# =========================
# 4. LIVE INTERVIEW (IMPORTANT 🔥)
# =========================
class AnswerRequest(BaseModel):
    previous_question: str
    answer: str
    question_count: int = Field(..., ge=1)
    interview_type: str = Field(..., description="technical | hr")


# =========================
# 5. Answer Submission (Batch)
# =========================
class AnswerSubmission(BaseModel):
    question_id: int
    question: str
    answer: str


class InterviewSubmissionRequest(BaseModel):
    session_id: str
    answers: List[AnswerSubmission]


# =========================
# 6. Feedback Schema (AI Evaluation)
# =========================
class AnswerFeedback(BaseModel):
    question_id: int
    score: float = Field(..., ge=0, le=10)
    feedback: str
    strengths: List[str] = []
    improvements: List[str] = []


class InterviewFeedbackResponse(BaseModel):
    overall_score: float
    summary: str
    feedback: List[AnswerFeedback]


# =========================
# 7. FINAL REPORT (NEW 🔥)
# =========================
class FinalReportRequest(BaseModel):
    interview_type: str
    answers: List[str]


class FinalReportResponse(BaseModel):
    overall_score: float
    technical_skills: str
    communication_skills: str
    strengths: List[str]
    weaknesses: List[str]
    decision: str  # Hire / No Hire


# =========================
# 8. Interview Session Schema
# =========================
class InterviewSession(BaseModel):
    session_id: str
    user_id: Optional[str] = None
    topic: str
    created_at: Optional[str] = None
    status: str = "ongoing"  # ongoing | completed