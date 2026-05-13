import pdfplumber
import docx
import os
import re


# =========================
# PDF PARSER
# =========================
def extract_text_from_pdf(file_path: str) -> str:

    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

    return text.strip()


# =========================
# DOCX PARSER
# =========================
def extract_text_from_docx(file_path: str) -> str:

    try:
        doc = docx.Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs]).strip()
    except Exception as e:
        return f"Error reading DOCX: {str(e)}"


# =========================
# MAIN EXTRACTOR (IMPORTANT)
# =========================
def extract_text_from_file(file_path: str) -> str:
    """
    THIS is the function your service should import
    """

    if not os.path.exists(file_path):
        return "File not found"

    ext = file_path.split(".")[-1].lower()

    if ext == "pdf":
        return extract_text_from_pdf(file_path)

    elif ext == "docx":
        return extract_text_from_docx(file_path)

    else:
        return "Unsupported file format"


# =========================
# CLEAN TEXT
# =========================
def clean_resume_text(text: str) -> str:

    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9,.@()\-+/ ]", "", text)
    text = re.sub(r"\.{2,}", ".", text)

    return text.strip()


# =========================
# SKILL EXTRACTION
# =========================
def extract_basic_skills(text: str):

    skills = [
        "python", "java", "c++", "javascript", "react", "node",
        "machine learning", "ai", "data science", "sql",
        "html", "css", "flask", "django", "fastapi"
    ]

    text_lower = text.lower()

    return list(set([s for s in skills if s in text_lower]))


# =========================
# FULL PIPELINE
# =========================
def process_resume(file_path: str):

    raw_text = extract_text_from_file(file_path)
    cleaned_text = clean_resume_text(raw_text)
    skills = extract_basic_skills(cleaned_text)

    return {
        "raw_text": raw_text,
        "cleaned_text": cleaned_text,
        "skills": skills
    }