from sqlalchemy.orm import Session
from ..models.models import TechnologyDomain, ResearchEntry
from ..schemas.schemas import InterrogationResponse
from ..core.ai_service import generate_interrogation_response
import random

async def synthesize_expert_response(db: Session, topic_id: str, query: str) -> InterrogationResponse:
    # Attempt AI augmentation
    ai_result = await generate_interrogation_response(db, topic_id, query)

    if "error" not in ai_result:
        return InterrogationResponse(**ai_result)

    # Fallback to Heuristic logic if AI fails
    domain = db.query(TechnologyDomain).filter(TechnologyDomain.topic_id == topic_id).first()
    if not domain:
        return InterrogationResponse(
            answer="I'm sorry, I don't have enough research data on this specific domain yet.",
            evidence="Domain not found in database.",
            confidence_score=0.0,
            sources=[]
        )

    # Enhance answer with sub-themes if available
    themes = [st.title for st in domain.sub_themes[:2]]
    theme_str = f" Key active research areas include {', '.join(themes)}." if themes else ""

    # Check for recent research signals
    research = db.query(ResearchEntry).filter(ResearchEntry.topic_id == topic_id).order_by(ResearchEntry.timestamp.desc()).limit(2).all()
    research_str = ""
    if research:
        titles = [r.title for r in research]
        research_str = f" Recent strategic signals include: {'; '.join(titles)}."

    return InterrogationResponse(
        answer=f"Regarding {domain.name}: {domain.insight or domain.why_it_matters}.{theme_str}{research_str}",
        evidence=f"Synthesized from {domain.evidence_level} institutional research, {len(domain.sub_themes)} technical sub-themes, and {len(research)} recent field reports.",
        avoid_rationale="Ensure technical timelines are cross-verified with TRL-specific milestones.",
        confidence_score=0.7,
        sources=domain.citations[:1]
    )
