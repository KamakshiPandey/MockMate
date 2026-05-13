from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.utils.db import get_db
from app.models.user_model import User
from app.utils.security import hash_password, verify_password, create_access_token
from app.schemas.auth_schema import SignupRequest, LoginRequest

router = APIRouter(tags=["Auth"])


# =========================
# SIGNUP
# =========================
@router.post("/signup")
def signup(data: SignupRequest, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == data.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_pw = hash_password(data.password)

    new_user = User(
        name=data.name,
        email=data.email,
        password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token({"sub": new_user.email})

    return {
        "message": "User created successfully",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        },
        "access_token": token
    }


# =========================
# LOGIN
# =========================
@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    token = create_access_token({"sub": user.email})

    return {
        "message": "Login successful",
        "access_token": token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }