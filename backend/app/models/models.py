from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, JSON, Enum, DateTime
from sqlalchemy.orm import relationship
from .base import Base
import enum
import datetime
import uuid

class CategoryEnum(str, enum.Enum):
    CORE = "CORE"
    ADJACENT = "ADJACENT"
    FRONTIER = "FRONTIER"
    THEME = "THEME"

class TypeEnum(str, enum.Enum):
    TOPIC = "TOPIC"
    THEME = "THEME"

class EvidenceLevelEnum(str, enum.Enum):
    HIGH = "HIGH"
    MODERATE = "MODERATE"
    SPECULATIVE = "SPECULATIVE"

class TechnologyDomain(Base):
    __tablename__ = "technology_domains"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(String, unique=True, index=True) # e.g. 'quantum'
    number = Column(Integer)
    name = Column(String, index=True)
    icon = Column(String) # Store icon name
    why_it_matters = Column(Text)
    insight = Column(Text, nullable=True)
    category = Column(String) # Handle as string for simplicity in SQLite or Enum if Postgres
    type = Column(String)
    reliability_score = Column(Float)
    evidence_level = Column(String)
    trl = Column(Integer)
    years_to_scale = Column(Integer)
    critical_questions = Column(JSON, nullable=True) # List of dicts: [{"question": "...", "answer": "..."}]
    scientific_rationale = Column(Text, nullable=True)
    investor_rationale = Column(Text, nullable=True)

    sub_themes = relationship("SubTheme", back_populates="domain", cascade="all, delete-orphan")
    investment_lenses = relationship("InvestmentLens", back_populates="domain", cascade="all, delete-orphan")
    scientific_principles = relationship("ScientificPrinciple", back_populates="domain", cascade="all, delete-orphan")
    citations = relationship("Citation", back_populates="domain", cascade="all, delete-orphan")
    brief_audits = relationship("BriefAudit", back_populates="domain")
    interrogations = relationship("InterrogationHistory", back_populates="domain")

class SubTheme(Base):
    __tablename__ = "sub_themes"

    id = Column(Integer, primary_key=True, index=True)
    domain_id = Column(Integer, ForeignKey("technology_domains.id"))
    title = Column(String)
    description = Column(Text)
    explainer = Column(Text, nullable=True)
    technologies = Column(JSON, nullable=True)

    domain = relationship("TechnologyDomain", back_populates="sub_themes")

class InvestmentLens(Base):
    __tablename__ = "investment_lenses"

    id = Column(Integer, primary_key=True, index=True)
    domain_id = Column(Integer, ForeignKey("technology_domains.id"))
    title = Column(String)
    details = Column(Text)

    domain = relationship("TechnologyDomain", back_populates="investment_lenses")

class ScientificPrinciple(Base):
    __tablename__ = "scientific_principles"

    id = Column(Integer, primary_key=True, index=True)
    domain_id = Column(Integer, ForeignKey("technology_domains.id"))
    title = Column(String)
    details = Column(Text)

    domain = relationship("TechnologyDomain", back_populates="scientific_principles")

class Citation(Base):
    __tablename__ = "citations"

    id = Column(Integer, primary_key=True, index=True)
    domain_id = Column(Integer, ForeignKey("technology_domains.id"))
    source = Column(String)
    url = Column(String)
    label = Column(String)

    domain = relationship("TechnologyDomain", back_populates="citations")

class PortfolioProfile(Base):
    __tablename__ = "portfolio_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    asset_allocation = Column(JSON)
    public_private_split = Column(JSON)
    infra_exposure = Column(Float)
    risk_tolerance = Column(String)

    cyber_risks = relationship("CyberRisk", back_populates="portfolio")

class CyberRisk(Base):
    __tablename__ = "cyber_risks"

    id = Column(Integer, primary_key=True, index=True)
    portfolio_id = Column(Integer, ForeignKey("portfolio_profiles.id"))
    risk_area = Column(String)
    severity = Column(String)
    readiness_score = Column(Integer)

    portfolio = relationship("PortfolioProfile", back_populates="cyber_risks")

class BriefAudit(Base):
    __tablename__ = "brief_audits"

    id = Column(Integer, primary_key=True, index=True)
    audit_id = Column(String, unique=True, index=True, default=lambda: str(uuid.uuid4())[:8].upper())
    user_id = Column(String, index=True)
    topic_id = Column(String, ForeignKey("technology_domains.topic_id"))
    format = Column(String) # '1-page' or '3-page'
    selections = Column(JSON) # e.g. {"portfolio": true, "scenarios": true, ...}
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    domain = relationship("TechnologyDomain", back_populates="brief_audits")

class AustraliaCase(Base):
    __tablename__ = "australia_cases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sector = Column(String)
    model_type = Column(String)
    revenue_status = Column(String)
    investor_mix = Column(String)
    horizon = Column(String)
    risk_profile = Column(String)
    city = Column(String)
    efficiency_metric = Column(String)

class AustraliaMetric(Base):
    __tablename__ = "australia_metrics"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String) # 'Efficiency' or 'Composition'
    label = Column(String)
    value = Column(Float)
    color_hex = Column(String)

class ResearchEntry(Base):
    __tablename__ = "research_entries"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(String, ForeignKey("technology_domains.topic_id"), index=True)
    title = Column(String, index=True)
    summary = Column(Text)
    content = Column(Text) # Markdown or HTML
    author = Column(String)
    category = Column(String) # 'news', 'landscape', 'case-study'
    status = Column(String, default="published") # 'draft', 'published'
    sources = Column(JSON, nullable=True) # List of dicts: [{"source": "...", "label": "...", "url": "..."}]
    quant_data = Column(JSON, nullable=True) # List of objects: [{"label": "...", "value": "...", "unit": "..."}]
    modelling = Column(Text, nullable=True) # Markdown text for modelling/projections
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    domain = relationship("TechnologyDomain")

class InterrogationHistory(Base):
    __tablename__ = "interrogation_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    topic_id = Column(String, ForeignKey("technology_domains.topic_id"))
    query = Column(Text)
    answer = Column(Text)
    evidence = Column(Text)
    confidence_score = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    domain = relationship("TechnologyDomain", back_populates="interrogations")

class EcosystemCompany(Base):
    __tablename__ = "ecosystem_companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String) # Hardware, Software, Sensing, Comms
    sub_category = Column(String) # e.g. Superconducting, Error Correction
    description = Column(Text)
    website = Column(String)
    location = Column(String)
    funding_stage = Column(String) # Seed, Series A, Public, etc.
    strategic_relevance = Column(Integer) # 1-10
    trl = Column(Integer, default=1)
    is_australian = Column(Integer, default=0) # 1 for True, 0 for False
    latest_news = Column(JSON, nullable=True) # List of {title, date, url}
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    headquarters = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
