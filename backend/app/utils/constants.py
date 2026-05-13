
# =========================
# USER ROLES
# =========================
ROLES = {
    "STUDENT": "student",
    "ADMIN": "admin",
    "RECRUITER": "recruiter"
}


# =========================
# INTERVIEW DIFFICULTY LEVELS
# =========================
DIFFICULTY_LEVELS = {
    "EASY": "easy",
    "MEDIUM": "medium",
    "HARD": "hard"
}


# =========================
# INTERVIEW STATUS
# =========================
INTERVIEW_STATUS = {
    "ONGOING": "ongoing",
    "COMPLETED": "completed"
}


# =========================
# DEFAULT SETTINGS
# =========================
DEFAULT_QUESTION_COUNT = 5
MAX_QUESTION_COUNT = 20
MIN_QUESTION_COUNT = 1


# =========================
# SCORE LIMITS
# =========================
MAX_SCORE = 10
MIN_SCORE = 0


# =========================
# RESUME FILE TYPES
# =========================
ALLOWED_RESUME_TYPES = ["pdf", "docx"]


# =========================
# AI MODEL SETTINGS
# =========================
DEFAULT_AI_MODEL = "gpt-4o-mini"

TEMPERATURE = 0.7

MAX_TOKENS = 1000


# =========================
# ERROR MESSAGES
# =========================
ERROR_MESSAGES = {
    "USER_NOT_FOUND": "User does not exist",
    "INVALID_CREDENTIALS": "Invalid email or password",
    "UNAUTHORIZED": "You are not authorized to access this resource",
    "INVALID_REQUEST": "Invalid request data",
    "SERVER_ERROR": "Something went wrong on the server"
}


# =========================
# SUCCESS MESSAGES
# =========================
SUCCESS_MESSAGES = {
    "USER_CREATED": "User created successfully",
    "LOGIN_SUCCESS": "Login successful",
    "INTERVIEW_STARTED": "Interview started successfully",
    "ANSWER_SAVED": "Answer saved successfully",
    "FEEDBACK_GENERATED": "Feedback generated successfully"
}


# =========================
# ROUTES (optional but useful)
# =========================
API_ROUTES = {
    "AUTH": "/auth",
    "USER": "/user",
    "INTERVIEW": "/interview",
    "RESUME": "/resume"
}