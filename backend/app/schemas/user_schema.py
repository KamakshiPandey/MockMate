from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

Base = declarative_base()


# =========================
# 1. DATABASE MODEL
# =========================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(120), unique=True, index=True, nullable=False)

    password = Column(String(255), nullable=False)  # hashed password

    role = Column(String(50), default="student")  # student | admin | recruiter

    resume_text = Column(Text, nullable=True)

    skills = Column(Text, nullable=True)  # store as comma-separated or JSON string

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# =========================
# 2. PYDANTIC SCHEMAS
# =========================

# ---- Create User ----
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


# ---- Login User ----
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ---- User Response (safe - no password) ----
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    resume_text: Optional[str] = None
    skills: Optional[str] = None

    class Config:
        from_attributes = True


# ---- Update User ----
class UserUpdate(BaseModel):
    name: Optional[str] = None
    password: Optional[str] = None
    resume_text: Optional[str] = None
    skills: Optional[str] = None