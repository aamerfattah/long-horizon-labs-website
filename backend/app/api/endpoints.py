from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import uuid
import os
import sys
from ..core.database import get_db, engine
from ..models.models import TechnologyDomain, SubTheme, BriefAudit, AustraliaCase, AustraliaMetric, ResearchEntry, InterrogationHistory, EcosystemCompany
from ..schemas.schemas import DomainRead, SubThemeRead, ScenarioRunResult, PortfolioProfileBase, InterrogationRequest, InterrogationResponse, BriefAuditCreate, BriefAuditRead, AustraliaRegionalResponse, AustraliaCaseBase, ResearchEntryCreate, ResearchEntryRead, ScenarioRequest, InterrogationHistoryRead, EcosystemCompanyRead
from .interrogate import synthesize_expert_response
from ..core.ai_service import augment_scenario_assumptions, generate_research_news
from ..core.simulation import engine as mc_engine
from ..seed import seed_data

router = APIRouter()

@router.post("/seed")
async def trigger_seed(drop: bool = False, db: Session = Depends(get_db)):
    """
    Triggers the database seeding process.
    """
    print(f"Seed triggered with drop={drop}")
    if os.getenv("VERCEL") == "1" and not (os.getenv("DATABASE_URL") or os.getenv("POSTGRES_URL")):
         raise HTTPException(status_code=400, detail="DATABASE_URL environment variable is not configured on Vercel.")

    try:
        seed_data(drop_tables=drop)
        return {
            "status": "success",
            "message": f"Database seeded successfully (drop_tables={drop})",
            "environment": "production" if os.getenv("VERCEL") == "1" else "development"
        }
    except Exception as e:
        print(f"Seeding error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Seeding failed: {str(e)}")

@router.get("/env-check")
async def env_check():
    return {
        "keys": list(os.environ.keys()),
        "cwd": os.getcwd(),
        "sys_path": sys.path,
        "vercel": os.getenv("VERCEL")
    }

@router.get("/db-check")
async def db_check(db: Session = Depends(get_db)):
    try:
        from sqlalchemy import text
        from ..core.database import engine
        db.execute(text("SELECT 1"))
        return {
            "status": "connected",
            "url_type": "postgres" if "postgres" in str(engine.url) else "sqlite",
            "has_postgres_env": os.getenv("POSTGRES_URL") is not None,
            "has_database_url": os.getenv("DATABASE_URL") is not None
        }
    except Exception as e:
        import traceback
        return {"status": "error", "detail": str(e), "traceback": traceback.format_exc()}

@router.get("/domains", response_model=List[DomainRead])
async def get_domains(db: Session = Depends(get_db)):
    domains = db.query(TechnologyDomain).all()
    return domains

@router.get("/domains/{topic_id}", response_model=DomainRead)
async def get_domain(topic_id: str, db: Session = Depends(get_db)):
    domain = db.query(TechnologyDomain).filter(TechnologyDomain.topic_id == topic_id).first()
    if not domain:
        raise HTTPException(status_code=404, detail="Domain not found")
    return domain

@router.get("/segments", response_model=List[SubThemeRead])
async def get_segments(domain_id: int, db: Session = Depends(get_db)):
    segments = db.query(SubTheme).filter(SubTheme.domain_id == domain_id).all()
    return segments

@router.post("/briefs", response_model=BriefAuditRead)
async def create_brief_audit(brief: BriefAuditCreate, db: Session = Depends(get_db)):
    db_brief = BriefAudit(
        user_id=brief.user_id,
        topic_id=brief.topic_id,
        format=brief.format,
        selections=brief.selections
    )
    db.add(db_brief)
    db.commit()
    db.refresh(db_brief)
    return db_brief

@router.get("/briefs", response_model=List[BriefAuditRead])
async def get_brief_audits(user_id: str, db: Session = Depends(get_db)):
    return db.query(BriefAudit).filter(BriefAudit.user_id == user_id).order_by(BriefAudit.timestamp.desc()).all()

@router.get("/regional/australia", response_model=AustraliaRegionalResponse)
async def get_australia_lens(db: Session = Depends(get_db)):
    cases = db.query(AustraliaCase).all()
    metrics = db.query(AustraliaMetric).all()
    return {"cases": cases, "metrics": metrics}

@router.post("/regional/australia/cases")
async def add_australia_case(case: AustraliaCaseBase, db: Session = Depends(get_db)):
    db_case = AustraliaCase(**case.dict())
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case

@router.post("/interrogate", response_model=InterrogationResponse)
async def interrogate_topic(request: InterrogationRequest, db: Session = Depends(get_db)):
    response = await synthesize_expert_response(db, request.topic_id, request.query)

    # Persist the interaction
    db_history = InterrogationHistory(
        user_id=request.user_id,
        topic_id=request.topic_id,
        query=request.query,
        answer=response.answer,
        evidence=response.evidence,
        confidence_score=response.confidence_score
    )
    db.add(db_history)
    db.commit()
    db.refresh(db_history)

    return response

@router.get("/interrogate/history", response_model=List[InterrogationHistoryRead])
async def get_interrogation_history(user_id: str, topic_id: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(InterrogationHistory).filter(InterrogationHistory.user_id == user_id)
    if topic_id:
        query = query.filter(InterrogationHistory.topic_id == topic_id)
    return query.order_by(InterrogationHistory.timestamp.desc()).all()

@router.post("/scenario/run", response_model=ScenarioRunResult)
async def run_scenario(request: ScenarioRequest, db: Session = Depends(get_db)):
    # 1. Fetch domain for context
    domain = db.query(TechnologyDomain).filter(TechnologyDomain.topic_id == request.topic_id).first()

    # 2. Get AI Augmented Assumptions (Quantitative Bounds)
    augmentation = await augment_scenario_assumptions(domain.name if domain else request.topic_id, request.scenario_type)

    # 3. Calculate Portfolio Exposure
    # Simple logic: sum weighted exposure to domains matching this topic
    exposure = request.portfolio_data.asset_allocation.get("DeepTech", 0.1) # Fallback to 10%

    # 4. Execute functional Monte Carlo logic (10,000 paths)
    mu = augmentation.get("mu", 0.05)
    sigma = augmentation.get("sigma", 0.2)

    sim_results = mc_engine.run_simulation(
        base_value=1.0,
        mu=mu,
        sigma=sigma,
        portfolio_exposure=exposure
    )

    return {
        "scenario_id": augmentation.get("horizons", 5),
        "impact_bands": sim_results["impact_bands"],
        "risk_deltas": sim_results["risk_deltas"],
        "confidence_intervals": sim_results["confidence_intervals"],
        "assumptions_explicit": {
            "mu": mu,
            "sigma": sigma,
            "exposure": exposure
        },
        "augmented_assumptions": augmentation.get("assumptions", [])
    }

# CMS / Research Endpoints
@router.get("/research", response_model=List[ResearchEntryRead])
async def get_all_research(category: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(ResearchEntry)
    if category:
        query = query.filter(ResearchEntry.category == category)
    return query.order_by(ResearchEntry.timestamp.desc()).all()

@router.get("/research/{topic_id}", response_model=List[ResearchEntryRead])
async def get_research_by_topic(topic_id: str, db: Session = Depends(get_db)):
    return db.query(ResearchEntry).filter(ResearchEntry.topic_id == topic_id).order_by(ResearchEntry.timestamp.desc()).all()

@router.post("/research", response_model=ResearchEntryRead)
async def create_research_entry(entry: ResearchEntryCreate, db: Session = Depends(get_db)):
    db_entry = ResearchEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.post("/research/generate/{topic_id}", response_model=ResearchEntryRead)
async def generate_topic_research(topic_id: str, db: Session = Depends(get_db)):
    domain = db.query(TechnologyDomain).filter(TechnologyDomain.topic_id == topic_id).first()
    if not domain:
        raise HTTPException(status_code=404, detail="Topic not found")

    print(f"Generating research for {topic_id} ({domain.name})")
    try:
        news_data = await generate_research_news(domain.name)
        db_entry = ResearchEntry(
            topic_id=topic_id,
            title=news_data.get("title", f"Update: {domain.name}"),
            summary=news_data.get("summary", "Technical synthesis in progress."),
            content=news_data.get("content", "Detailed analysis being finalized."),
            category=news_data.get("category", "technical-insight"),
            author=news_data.get("author", "DeepTechIQ Research"),
            status="published"
        )
        db.add(db_entry)
        db.commit()
        db.refresh(db_entry)
        print(f"Successfully generated entry: {db_entry.id}")
        return db_entry
    except Exception as e:
        print(f"Error during research generation: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/research/seed-all")
async def seed_all_research(db: Session = Depends(get_db)):
    """
    Seeds all technology domains with a research entry using parallel AI generation.
    """
    import asyncio
    domains = db.query(TechnologyDomain).all()

    async def generate_and_save(domain):
        try:
            print(f"Parallel Seeding: {domain.name}")
            news_data = await generate_research_news(domain.name)
            db_entry = ResearchEntry(
                topic_id=domain.topic_id,
                title=news_data.get("title", f"Strategic Update: {domain.name}"),
                summary=news_data.get("summary", "Technical synthesis in progress."),
                content=news_data.get("content", "Analysis being finalized."),
                category=news_data.get("category", "news"),
                author=news_data.get("author", "DeepTechIQ Research"),
                status="published"
            )
            return db_entry
        except Exception as e:
            print(f"Failed to generate for {domain.name}: {e}")
            return None

    # Run everything in parallel
    tasks = [generate_and_save(d) for d in domains]
    results = await asyncio.gather(*tasks)

    new_entries = [r for r in results if r is not None]

    if new_entries:
        db.add_all(new_entries)
        db.commit()
        return {"status": "success", "count": len(new_entries)}

    return {"status": "no_updates", "count": 0}

@router.get("/ecosystem", response_model=List[EcosystemCompanyRead])
async def get_ecosystem(db: Session = Depends(get_db)):
    """
    Retrieves all companies in the quantum ecosystem.
    """
    return db.query(EcosystemCompany).all()
