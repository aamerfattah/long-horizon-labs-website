import asyncio
import os
import sys

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import SessionLocal
from app.models.models import TechnologyDomain, ResearchEntry
from app.core.ai_service import generate_research_news

async def seed_news():
    db = SessionLocal()
    domains = db.query(TechnologyDomain).all()

    print(f"Found {len(domains)} domains. Starting AI news generation...")

    for domain in domains:
        print(f"Generating news for: {domain.name}...")
        try:
            news_data = await generate_research_news(domain.name)

            # Check if an entry already exists for this topic recently (simple mock)
            # For now, just add a new one
            entry = ResearchEntry(
                topic_id=domain.topic_id,
                title=news_data.get("title", f"{domain.name} Update"),
                summary=news_data.get("summary", ""),
                content=news_data.get("content", ""),
                category=news_data.get("category", "landscape"),
                author=news_data.get("author", "DeepTechIQ Research"),
                status="published"
            )
            db.add(entry)
            print(f"  [SUCCESS] Added: {entry.title}")
        except Exception as e:
            print(f"  [ERROR] Failed for {domain.name}: {e}")

    db.commit()
    db.close()
    print("Seeding complete.")

if __name__ == "__main__":
    asyncio.run(seed_news())
