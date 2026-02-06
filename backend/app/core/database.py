from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Production-ready database configuration
# Support both 'DATABASE_URL' and Vercel's default 'POSTGRES_URL'
database_url = os.getenv("DATABASE_URL") or os.getenv("POSTGRES_URL")

if not database_url:
    if os.getenv("VERCEL") == "1" or os.getenv("NODE_ENV") == "production":
        # Crucial: Don't use local file on Vercel
        print("CRITICAL: No DATABASE_URL found in production environment.")
        # Fallback to a dummy that still matches the driver requirement but will fail fast on use
        database_url = "postgresql://unconfigured-db-host:5432/nothing"
    else:
        database_url = "sqlite:///./deeptechiq.db"

# Fix for SQLAlchemy 1.4+ which requires 'postgresql://' instead of 'postgres://'
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

print(f"Connecting to: {database_url.split('@')[-1] if '@' in database_url else database_url}")

engine = create_engine(
    database_url,
    # Increased pool size and timeouts for serverless environments
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    connect_args={"check_same_thread": False} if "sqlite" in str(database_url) else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
