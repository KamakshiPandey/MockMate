import re
import string


# =========================
# 1. BASIC TEXT CLEANING
# =========================
def clean_text(text: str) -> str:
    """
    General purpose text cleaner
    """

    if not text:
        return ""

    # convert to lowercase
    text = text.lower()

    # remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # remove email addresses
    text = re.sub(r"\S+@\S+", "", text)

    # remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    return text.strip()


# =========================
# 2. RESUME CLEANING (LIGHT)
# =========================
def clean_resume_text(text: str) -> str:
    """
    Keeps structure but removes noise from resume
    """

    if not text:
        return ""

    # remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # remove weird symbols but keep important ones like + . @ -
    text = re.sub(r"[^a-zA-Z0-9,.@+\-() /]", "", text)

    # remove repeated dots
    text = re.sub(r"\.{2,}", ".", text)

    return text.strip()


# =========================
# 3. AI INPUT CLEANING (IMPORTANT FOR LLM)
# =========================
def clean_for_llm(text: str) -> str:
    """
    Prepares text for LLM input (removes noise but keeps meaning)
    """

    if not text:
        return ""

    # normalize spaces
    text = re.sub(r"\s+", " ", text)

    # remove special junk characters
    text = re.sub(r"[^\w\s,.?()-]", "", text)

    # trim
    return text.strip()


# =========================
# 4. REMOVE STOP WORDS (OPTIONAL BASIC VERSION)
# =========================
STOP_WORDS = set([
    "is", "am", "are", "the", "a", "an", "and", "or", "to", "in",
    "of", "for", "on", "with", "this", "that", "it"
])


def remove_stop_words(text: str) -> str:
    """
    Removes common stop words (basic NLP helper)
    """

    words = text.split()
    filtered_words = [w for w in words if w.lower() not in STOP_WORDS]

    return " ".join(filtered_words)


# =========================
# 5. NORMALIZE SPACING
# =========================
def normalize_spacing(text: str) -> str:
    """
    Fixes inconsistent spacing
    """

    return re.sub(r"\s+", " ", text).strip()


# =========================
# 6. PIPELINE FUNCTION
# =========================
def preprocess_text(text: str, mode: str = "general") -> str:
    """
    Full preprocessing pipeline
    modes:
    - general
    - resume
    - llm
    """

    if mode == "resume":
        text = clean_resume_text(text)

    elif mode == "llm":
        text = clean_for_llm(text)

    else:
        text = clean_text(text)

    text = normalize_spacing(text)

    return text