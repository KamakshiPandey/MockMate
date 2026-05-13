from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import logging

from app.routes.resume_routes import router as resume_router
from app.routes.interview_routes import router as interview_router
from app.routes.auth_routes import router as auth_router
from app.utils.db import Base, engine

# =========================
# APP
# =========================
app = FastAPI(
    title="AI Interview Platform",
    description="Resume-based AI Interview System",
    version="1.0.0"
)

# =========================
# LOGGING
# =========================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =========================
# CORS (DEV FIX)
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # ⚠️ In production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# STATIC FILES (VERY IMPORTANT ✅)
# =========================
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# =========================
# ROUTES
# =========================
app.include_router(auth_router, prefix="/auth")
app.include_router(resume_router, prefix="/resume", tags=["Resume"])
app.include_router(interview_router, prefix="/interview")

# =========================
# STARTUP
# =========================
@app.on_event("startup")
def startup():
    logger.info("Starting backend...")

    Base.metadata.create_all(bind=engine)

    logger.info("Database ready")

# =========================
# ROOT
# =========================
@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}