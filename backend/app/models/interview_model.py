from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


# =========================
# 1. INTERVIEW SESSION
# =========================
class InterviewSession(Base):
    __tablename__ = "interview_sessions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    topic = Column(String(100), nullable=False)  # e.g., DSA, AI, Web Dev

    difficulty = Column(String(20), default="medium")

    status = Column(String(20), default="ongoing")  # ongoing | completed

    created_at = Column(DateTime, default=datetime.utcnow)

    # relationships
    questions = relationship("InterviewQuestion", back_populates="session", cascade="all, delete")


# =========================
# 2. INTERVIEW QUESTIONS
# =========================
class InterviewQuestion(Base):
    __tablename__ = "interview_questions"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(Integer, ForeignKey("interview_sessions.id"), nullable=False)

    question_text = Column(Text, nullable=False)

    expected_answer = Column(Text, nullable=True)

    question_order = Column(Integer, default=1)

    # relationships
    session = relationship("InterviewSession", back_populates="questions")
    answer = relationship("InterviewAnswer", back_populates="question", uselist=False)


# =========================
# 3. USER ANSWERS
# =========================
class InterviewAnswer(Base):
    __tablename__ = "interview_answers"

    id = Column(Integer, primary_key=True, index=True)

    question_id = Column(Integer, ForeignKey("interview_questions.id"), nullable=False)

    user_answer = Column(Text, nullable=False)

    score = Column(Float, default=0.0)  # AI evaluation score (0–10)

    feedback = Column(Text, nullable=True)

    strengths = Column(Text, nullable=True)

    improvements = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    # relationships
    question = relationship("InterviewQuestion", back_populates="answer")


# =========================
# 4. FINAL INTERVIEW RESULT
# =========================
class InterviewResult(Base):
    __tablename__ = "interview_results"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(Integer, ForeignKey("interview_sessions.id"), nullable=False)

    overall_score = Column(Float, default=0.0)

    summary = Column(Text, nullable=True)

    total_questions = Column(Integer, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)