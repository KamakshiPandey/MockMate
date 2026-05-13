print("🔥 LOADED: resume_service.py")

import os
from dotenv import load_dotenv

load_dotenv()

import pdfplumber
from docx import Document
import requests
import json
import re
import cloudinary
import cloudinary.uploader

# =========================
# CONFIG
# =========================
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

print("🔑 OPENROUTER KEY LOADED:", bool(OPENROUTER_API_KEY))
print("☁️ CLOUD NAME:", os.getenv("CLOUDINARY_CLOUD_NAME"))

API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

# =========================
# CLOUDINARY CONFIG
# =========================
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

# =========================
# UPLOAD TO CLOUDINARY
# =========================
def upload_to_cloudinary(file_path: str):
    try:
        print("☁️ Uploading to Cloudinary...")

        result = cloudinary.uploader.upload(
            file_path,
            resource_type="auto",  # for pdf/docx
            access_mode="public"
        )

        file_url = result.get("secure_url")

        print("🌐 Uploaded URL:", file_url)

        return file_url

    except Exception as e:
        print("❌ Cloudinary upload failed:", str(e))
        return None


# =========================
# EXTRACT TEXT
# =========================
def extract_text(file_path: str):
    print("📂 Extracting file:", file_path)

    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)

    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])

    else:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    print("📄 Extracted length:", len(text))
    return text


# =========================
# JSON CLEANER
# =========================
def extract_json(text: str):
    print("🧹 Cleaning JSON output...")

    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())

        print("⚠️ No JSON found in response")
        return {"raw_output": text}

    except Exception as e:
        print("❌ JSON parse error:", str(e))
        return {"raw_output": text}


# =========================
# AI ANALYSIS
# =========================
def analyze_resume_from_file(file_path: str):

    print("\n==============================")
    print("🚀 RESUME ANALYSIS STARTED")
    print("==============================")

    # ✅ 1. Upload to Cloudinary
    file_url = upload_to_cloudinary(file_path)

    # ✅ 2. Extract text
    text = extract_text(file_path)

    print("\n📝 Resume Preview (first 500 chars):\n")
    print(text[:500])

    prompt = f"""
You are an expert resume analyzer.

Return ONLY raw JSON.
Do NOT add explanation.
Do NOT use backticks.
Do NOT write anything outside JSON.

IMPORTANT:
- Always fill ALL fields.
- suggested_interview_questions MUST contain at least 5 questions.
- weaknesses MUST contain at least 2 points (if none, infer realistic ones).
- ats_score must be between 0 and 100.

Resume:
{text}

Format:
{{
  "skills_found": [],
  "experience_level": "",
  "ats_score": 0,
  "summary": "",
  "strengths": [],
  "weaknesses": [],
  "suggested_interview_questions": []
}}
"""

    print("\n🤖 Sending request to OpenRouter...")

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={
                "model": "meta-llama/llama-3-8b-instruct",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3,
                "max_tokens": 500
            },
            timeout=60
        )

        # =========================
        # RESPONSE DEBUGGING
        # =========================
        print("\n📡 STATUS CODE:", response.status_code)
        print("\n📡 RESPONSE HEADERS:", dict(response.headers))
        print("\n📡 RAW RESPONSE TEXT:\n", response.text[:1000])

        if response.status_code != 200:
            print("❌ API FAILED")
            return {
                "error": "API error",
                "status": response.status_code,
                "details": response.text
            }

        # =========================
        # PARSE JSON RESPONSE
        # =========================
        try:
            result = response.json()
        except Exception as e:
            print("❌ JSON decode failed:", str(e))
            return {
                "error": "Invalid JSON response",
                "raw": response.text
            }

        print("\n📦 RAW RESULT:", result)

        # =========================
        # EXTRACT MODEL OUTPUT
        # =========================
        try:
            output_text = result["choices"][0]["message"]["content"]
        except Exception as e:
            print("❌ Unexpected response format:", str(e))
            return {
                "error": "Invalid response format",
                "raw": result
            }

        print("\n🧠 MODEL OUTPUT:\n", output_text)

        # =========================
        # CLEAN FINAL JSON
        # =========================
        final_output = extract_json(output_text)

        print("\n✅ FINAL PARSED RESULT:\n", final_output)

        # ✅ 3. Return URL + Analysis
        return {
            "file_url": file_url,
            "analysis": final_output
        }

    except requests.exceptions.Timeout:
        print("❌ REQUEST TIMEOUT")
        return {"error": "Request timed out"}

    except Exception as e:
        print("❌ EXCEPTION:", str(e))
        return {"error": str(e)}