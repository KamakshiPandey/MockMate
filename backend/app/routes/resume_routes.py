from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil
from uuid import uuid4

from app.services.resume_services import analyze_resume_from_file
from app.services.pdf_service import generate_analysis_pdf

router = APIRouter(tags=["Resume"])

UPLOAD_DIR = "uploads/resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# =========================
# UPLOAD + AUTO ANALYZE + PDF
# =========================
@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    # -------------------------
    # VALIDATION
    # -------------------------
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    allowed_extensions = ["pdf", "docx", "txt"]
    file_extension = file.filename.split(".")[-1].lower()

    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file format. Upload PDF, DOCX or TXT only."
        )

    try:
        # -------------------------
        # SAVE FILE
        # -------------------------
        safe_filename = f"{uuid4()}.{file_extension}"
        file_path = os.path.join(UPLOAD_DIR, safe_filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # -------------------------
        # AI ANALYSIS
        # -------------------------
        analysis = analyze_resume_from_file(file_path)

        # -------------------------
        # GENERATE PDF
        # -------------------------
        pdf_filename = f"{uuid4()}.pdf"
        pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)

        generate_analysis_pdf(analysis.get("analysis"), pdf_path)

        # -------------------------
        # RESPONSE
        # -------------------------
        return {
            "message": "Resume uploaded and analyzed successfully",
            "original_filename": file.filename,
            "stored_filename": safe_filename,
            "file_path": file_path,
            "file_url": analysis.get("file_url"),
            "analysis": analysis.get("analysis"),
            "pdf_url": pdf_path   # ✅ NOW FIXED
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Upload failed: {str(e)}"
        )


# =========================
# DOWNLOAD ANALYSIS (SEPARATE ENDPOINT)
# =========================
@router.post("/download-analysis")
async def download_analysis(file: UploadFile = File(...)):

    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    try:
        # -------------------------
        # SAVE FILE FIRST (IMPORTANT FIX)
        # -------------------------
        file_extension = file.filename.split(".")[-1].lower()
        safe_filename = f"{uuid4()}.{file_extension}"
        file_path = os.path.join(UPLOAD_DIR, safe_filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # -------------------------
        # ANALYZE
        # -------------------------
        analysis = analyze_resume_from_file(file_path)

        # -------------------------
        # GENERATE PDF
        # -------------------------
        pdf_filename = f"{uuid4()}.pdf"
        pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)

        generate_analysis_pdf(analysis.get("analysis"), pdf_path)

        return {
            "message": "PDF generated successfully",
            "pdf_url": pdf_path
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))