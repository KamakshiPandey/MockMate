import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# =========================
# APP CONFIG
# =========================
APP_NAME = "AI Interview Platform"
DEBUG = os.getenv("DEBUG", "True") == "True"
ENV = os.getenv("ENV", "development")


# =========================
# DATABASE CONFIG
# =========================
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:password@localhost/ai_interview"
)


# =========================
# SECURITY CONFIG
# =========================
SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 1 day
REFRESH_TOKEN_EXPIRE_DAYS = 7


# =========================
# AI / LLM CONFIG
# =========================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

DEFAULT_LLM_MODEL = os.getenv("DEFAULT_LLM_MODEL", "gpt-4o-mini")

TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))

MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1000))


# =========================
# INTERVIEW SETTINGS
# =========================
DEFAULT_QUESTION_COUNT = 5
MAX_QUESTION_COUNT = 20
MIN_QUESTION_COUNT = 1

DEFAULT_DIFFICULTY = "medium"


# =========================
# FILE UPLOAD SETTINGS
# =========================
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads/")

ALLOWED_EXTENSIONS = {"pdf", "docx"}

MAX_FILE_SIZE_MB = 10


# =========================
# CORS SETTINGS (for FastAPI/React)
# =========================
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]


# =========================
# LOGGING CONFIG
# =========================
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")


# =========================
# ERROR MESSAGES
# =========================
ERRORS = {
    "DB_CONNECTION_FAILED": "Database connection failed",
    "INVALID_TOKEN": "Invalid or expired token",
    "USER_NOT_FOUND": "User not found",
    "UNAUTHORIZED": "Unauthorized access",
    "FILE_TOO_LARGE": "Uploaded file exceeds size limit"
}


# =========================
# SUCCESS MESSAGES
# =========================
SUCCESS = {
    "LOGIN_SUCCESS": "Login successful",
    "REGISTER_SUCCESS": "User registered successfully",
    "UPLOAD_SUCCESS": "File uploaded successfully",
    "INTERVIEW_COMPLETED": "Interview completed successfully"
}