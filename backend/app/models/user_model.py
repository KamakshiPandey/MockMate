from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.utils.db import Base


# =========================
# USER TABLE
# =========================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(120), unique=True, index=True, nullable=False)

    password = Column(String(255), nullable=False)  # hashed password

    role = Column(String(50), default="student")  # student | admin | recruiter

    resume_text = Column(Text, nullable=True)

    skills = Column(Text, nullable=True)  # store JSON or comma-separated

    experience_level = Column(String(50), default="fresher")

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 🔥 RELATIONSHIP (IMPORTANT FIX)
    interviews = relationship("UserInterviewHistory", back_populates="user")


# =========================
# USER INTERVIEW HISTORY
# =========================
class UserInterviewHistory(Base):
    __tablename__ = "user_interview_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))  # FIXED

    session_id = Column(String(100), index=True)  # better than Integer

    topic = Column(String(100))

    score = Column(String(10))

    created_at = Column(DateTime, default=datetime.utcnow)

    # 🔥 RELATIONSHIP
    user = relationship("User", back_populates="interviews")