from app.models.user_model import User
from app.utils.db import SessionLocal
from app.utils.security import hash_password, verify_password


def register_user(name, email, password):
    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if user:
        return {"error": "User already exists"}

    new_user = User(
        name=name,
        email=email,
        password=hash_password(password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully", "user_id": new_user.id}


def login_user(email, password):
    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if not user:
        return {"error": "User not found"}

    if not verify_password(password, user.password):
        return {"error": "Invalid password"}

    return {
        "message": "Login successful",
        "user_id": user.id,
        "name": user.name
    }