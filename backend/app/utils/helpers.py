import json
import re
import uuid
from datetime import datetime


# =========================
# 1. STRING HELPERS
# =========================
def generate_uuid():
    """Generate unique session or object ID"""
    return str(uuid.uuid4())


def clean_text(text: str) -> str:
    """Clean extra spaces and unwanted characters"""
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s,.?()-]", "", text)
    return text.strip()


def extract_keywords(text: str):
    """Simple keyword extraction (can upgrade with NLP later)"""
    words = re.findall(r"\b\w+\b", text.lower())
    stop_words = {"is", "the", "a", "an", "and", "or", "to", "in", "of", "for"}
    return list(set([w for w in words if w not in stop_words]))


# =========================
# 2. LIST / DATA HELPERS
# =========================
def list_to_string(data: list) -> str:
    """Convert list to comma-separated string"""
    return ",".join(map(str, data))


def string_to_list(data: str) -> list:
    """Convert comma-separated string to list"""
    if not data:
        return []
    return data.split(",")


def safe_json_load(data: str):
    """Safely parse JSON string"""
    try:
        return json.loads(data)
    except Exception:
        return {}


# =========================
# 3. RESPONSE HELPERS
# =========================
def success_response(message: str, data=None):
    return {
        "success": True,
        "message": message,
        "data": data
    }


def error_response(message: str, error=None):
    return {
        "success": False,
        "message": message,
        "error": str(error) if error else None
    }


# =========================
# 4. DATE/TIME HELPERS
# =========================
def current_timestamp():
    return datetime.utcnow().isoformat()


def format_datetime(dt: datetime):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


# =========================
# 5. SCORE HELPERS
# =========================
def normalize_score(score: float, min_score=0, max_score=10):
    """Ensure score stays within limits"""
    return max(min_score, min(max_score, score))


def calculate_average(scores: list):
    """Calculate average score safely"""
    if not scores:
        return 0
    return sum(scores) / len(scores)