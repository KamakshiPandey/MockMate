from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# =========================
# DATABASE URL
# =========================
# MySQL (recommended for your project)
DATABASE_URL = "mysql+pymysql://root:kkupshbabSH*@localhost/ai_interview"

# If using SQLite (for testing only):
# DATABASE_URL = "sqlite:///./ai_interview.db"


# =========================
# ENGINE
# =========================
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # checks connection before using
    pool_recycle=3600     # avoids connection timeout issues
)


# =========================
# SESSION
# =========================
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# =========================
# BASE MODEL
# =========================
Base = declarative_base()


# =========================
# DB DEPENDENCY (FASTAPI)
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()