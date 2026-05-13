import jwt
import datetime
from passlib.context import CryptContext
import hashlib
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

# =========================
# PASSWORD HASHING SETUP
# =========================
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# =========================
# 1. HASH PASSWORD
# =========================
def hash_password(password: str) -> str:
    """
    Safe hashing (fixes bcrypt 72-byte limit)
    """
    if len(password.encode("utf-8")) > 72:
        password = hashlib.sha256(password.encode()).hexdigest()
    return pwd_context.hash(password)
# =========================
# 2. VERIFY PASSWORD
# =========================
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Safe verification
    """
    if len(plain_password.encode("utf-8")) > 72:
        plain_password = hashlib.sha256(plain_password.encode()).hexdigest()
    return pwd_context.verify(plain_password, hashed_password)
  
# =========================
# 3. CREATE JWT TOKEN
# =========================
def create_access_token(data: dict, expires_delta: int = None):
    """
    Generate JWT token for authentication
    """

    to_encode = data.copy()

    expire = datetime.datetime.utcnow() + datetime.timedelta(
        minutes=expires_delta or ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


# =========================
# 4. VERIFY JWT TOKEN
# =========================
def verify_token(token: str):
    """
    Decode and validate JWT token
    """

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload

    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}

    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}


# =========================
# 5. GET USER FROM TOKEN
# =========================
def get_user_from_token(token: str):
    """
    Extract user info from token (usually email or user_id)
    """

    payload = verify_token(token)

    if isinstance(payload, dict) and "error" in payload:
        return None

    return payload.get("sub")  # "sub" = subject (user identity)


# =========================
# 6. OPTIONAL: REFRESH TOKEN
# =========================
def create_refresh_token(data: dict):
    """
    Create long-lived refresh token (optional feature)
    """

    expire = datetime.datetime.utcnow() + datetime.timedelta(days=7)

    to_encode = data.copy()
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)