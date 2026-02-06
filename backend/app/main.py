from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sentry_sdk

import os

# Initialize Sentry if DSN is provided
# sentry_sdk.init(dsn="YOUR_SENTRY_DSN", traces_sample_rate=1.0)

from .core.database import engine
from .models.base import Base
# Import all models to ensure they are registered with Base.metadata
from .models.models import TechnologyDomain, SubTheme, BriefAudit, AustraliaCase, AustraliaMetric, ResearchEntry, InterrogationHistory, EcosystemCompany

# Create tables if they don't exist
# In production/Vercel, we prefer managed migrations or explicit seeding,
# but we'll attempt auto-creation if a valid DATABASE_URL is present.
if os.getenv("DATABASE_URL") or os.getenv("POSTGRES_URL") or os.getenv("VERCEL") != "1":
    try:
        print("Attempting to initialize database tables...")
        Base.metadata.create_all(bind=engine)
        print("Database tables initialized successfully.")
    except Exception as e:
        print(f"Database table creation failed: {e}")
else:
    print("Skipping auto-table creation: No DATABASE_URL found in Vercel environment.")

app = FastAPI(
    title="DeepTechIQ API",
    description="Backend API for DeepTechIQ B2B SaaS Decision Support Platform",
    version="0.1.0"
)

# CORS configuration
origins = [
    "http://localhost:3000",
    "https://deeptechiq.com",
    "https://www.deeptechiq.com",
]

# Add Vercel preview deployments and environment variables
extra_origins = os.getenv("ALLOWED_ORIGINS")
if extra_origins:
    origins.extend(extra_origins.split(","))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if os.getenv("NODE_ENV") == "production" or os.getenv("VERCEL_ENV") == "production" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .api.endpoints import router as api_router

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():

    return {"message": "Welcome to DeepTechIQ API", "status": "active"}

@app.get("/api/v1/health")
async def api_v1_health():
    return {"status": "ok", "version": "v1"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
