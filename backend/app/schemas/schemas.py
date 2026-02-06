from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import datetime

class CitationBase(BaseModel):
    source: str
    url: str
    label: str

class CitationRead(CitationBase):
    id: int
    class Config:
        from_attributes = True

class SubThemeBase(BaseModel):
    title: str
    description: str
    explainer: Optional[str] = None
    technologies: Optional[List[str]] = None

class SubThemeRead(SubThemeBase):
    id: int
    class Config:
        from_attributes = True

class InvestmentLensBase(BaseModel):
    title: str
    details: str

class InvestmentLensRead(InvestmentLensBase):
    id: int
    class Config:
        from_attributes = True

class ScientificPrincipleRead(InvestmentLensRead):
    pass

class DomainBase(BaseModel):
    topic_id: str
    number: int
    name: str
    icon: str
    why_it_matters: str
    insight: Optional[str] = None
    category: str
    type: str
    reliability_score: float
    evidence_level: str
    trl: int
    years_to_scale: int
    critical_questions: Optional[List[Dict[str, str]]] = None
    scientific_rationale: Optional[str] = None
    investor_rationale: Optional[str] = None

class DomainRead(DomainBase):
    id: int
    sub_themes: List[SubThemeRead] = []
    investment_lenses: List[InvestmentLensRead] = []
    scientific_principles: List[ScientificPrincipleRead] = []
    citations: List[CitationRead] = []

    class Config:
        from_attributes = True

class PortfolioProfileBase(BaseModel):
    asset_allocation: Dict[str, float]
    public_private_split: Dict[str, float]
    infra_exposure: float
    risk_tolerance: str

class PortfolioProfileRead(PortfolioProfileBase):
    id: int
    user_id: str
    class Config:
        from_attributes = True

class ScenarioRunResult(BaseModel):
    scenario_id: int
    impact_bands: List[float]
    risk_deltas: Dict[str, float]
    confidence_intervals: List[float]
    assumptions_explicit: Dict[str, Any]
    augmented_assumptions: Optional[List[str]] = None

class ScenarioRequest(BaseModel):
    topic_id: str
    scenario_type: str
    portfolio_data: PortfolioProfileBase

class InterrogationRequest(BaseModel):
    user_id: str
    topic_id: str
    query: str

class InterrogationResponse(BaseModel):
    answer: str
    evidence: str
    avoid_rationale: Optional[str] = None
    confidence_score: float
    sources: List[CitationBase] = []

class BriefAuditBase(BaseModel):
    topic_id: str
    format: str
    selections: Dict[str, bool]

class BriefAuditCreate(BriefAuditBase):
    user_id: str

class BriefAuditRead(BriefAuditBase):
    id: int
    audit_id: str
    user_id: str
    timestamp: datetime.datetime

    class Config:
        from_attributes = True

class AustraliaCaseBase(BaseModel):
    name: str
    sector: str
    model_type: str
    revenue_status: str
    investor_mix: str
    horizon: str
    risk_profile: str
    city: str
    efficiency_metric: str

class AustraliaCaseRead(AustraliaCaseBase):
    id: int
    class Config:
        from_attributes = True

class AustraliaMetricBase(BaseModel):
    category: str
    label: str
    value: float
    color_hex: str

class AustraliaMetricRead(AustraliaMetricBase):
    id: int
    class Config:
        from_attributes = True

class AustraliaRegionalResponse(BaseModel):
    cases: List[AustraliaCaseRead]
    metrics: List[AustraliaMetricRead]

class ResearchEntryBase(BaseModel):
    topic_id: str
    title: str
    summary: str
    content: str
    author: str
    category: str
    status: str = "published"
    sources: Optional[List[Dict[str, str]]] = None
    quant_data: Optional[List[Dict[str, Any]]] = None
    modelling: Optional[str] = None

class ResearchEntryCreate(ResearchEntryBase):
    pass

class ResearchEntryRead(ResearchEntryBase):
    id: int
    timestamp: datetime.datetime

    class Config:
        from_attributes = True

class InterrogationHistoryRead(BaseModel):
    id: int
    user_id: str
    topic_id: str
    query: str
    answer: str
    evidence: str
    confidence_score: float
    timestamp: datetime.datetime

    class Config:
        from_attributes = True

class EcosystemCompanyBase(BaseModel):
    name: str
    category: str
    sub_category: str
    description: str
    website: str
    location: str
    funding_stage: str
    strategic_relevance: int
    trl: int = 1
    is_australian: int = 0
    latest_news: Optional[List[Dict[str, Any]]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    headquarters: Optional[str] = None

class EcosystemCompanyRead(EcosystemCompanyBase):
    id: int
    timestamp: datetime.datetime

    class Config:
        from_attributes = True
