import dynamic from 'next/dynamic';
import { Terminal, Database, BarChart3, TreeDeciduous, Box, ShieldCheck, Scale } from 'lucide-react';

const PolicyShockSimulator = dynamic(() => import('@/components/projects/PolicyShockSimulator'), { ssr: false });
const MemberOutcomeEngine = dynamic(() => import('@/components/projects/MemberOutcomeEngine'), { ssr: false });
const StrategicMetricTranslator = dynamic(() => import('@/components/projects/StrategicMetricTranslator'), { ssr: false });
const DecisionScenarioTree = dynamic(() => import('@/components/projects/DecisionScenarioTree'), { ssr: false });

export const projectRegistry = {
    "policy-shock-simulator": {
        title: "Policy Shock Simulator",
        tagline: "First-order macro impact modelling.",
        icon: Terminal,
        component: PolicyShockSimulator,
        problem: "Policy shifts—such as inflation, tax, or contribution rate changes—often have non-linear impacts on long-term capital outcomes that are poorly understood by decision makers.",
        methodology: "A deterministic scenario engine designed to bypass the noise of stochastic volatility. It focuses on the primary sensitivities of a 30-year accumulation plan to sustained external shocks.",
        why: "Enables CIOs to answer 'what if' questions during regime shifts with immediate, explainable data."
    },
    "member-outcomes-lite": {
        title: "Member Outcome Engine",
        tagline: "Outcome-centric fund analytics.",
        icon: Database,
        component: MemberOutcomeEngine,
        problem: "Institutional reporting often focuses on relative performance against arbitrary benchmarks while overlooking the absolute reality of member retirement sufficiency.",
        methodology: "This engine translates raw asset data into human metrics. 'Funded Years' and 'Replacement Ratios' serve as the primary signals of fund health.",
        why: "Positions retirement fund leadership around the primary metric of member quality of life."
    },
    "board-metrics-translator": {
        title: "Strategic Metric Translator",
        tagline: "Bridging the technical governance gap.",
        icon: BarChart3,
        component: StrategicMetricTranslator,
        problem: "Technical teams provide data while Boards require strategic judgment. The translation layer is often where critical risks are obscured by jargon.",
        methodology: "A rule-based mapping engine that requires a commitment to narrative. Technical breaches are translated into boardroom-ready strategic choices.",
        why: "Ensures technical risk is communicated with executive clarity to enable informed capital allocation."
    },
    "scenario-tree": {
        title: "Decision Scenario Tree",
        tagline: "Simplified decision architecture.",
        icon: TreeDeciduous,
        component: DecisionScenarioTree,
        problem: "Decision-making in capital markets often suffers from either over-simplification or 'black-box' complexity that lacks accountability.",
        methodology: "A logic tree engine designed for probability weighting and expected value calculations across multiple strategic regimes.",
        why: "Provides clarity in assumptions and ensures a valid process even when outcomes are uncertain."
    },
    "super-data-cleaner": {
        title: "Systemic Data Refinery",
        tagline: "Standardising public financial datasets.",
        icon: Box,
        component: null,
        problem: "Systemic risk analysis is hampered by the fragmented, non-standard nature of public financial disclosures across jurisdictions.",
        methodology: "A rule-based refinery that standardises disparate CSV and JSON blobs into a unified schema for multi-asset stress testing.",
        why: "Reduces data processing overhead, allowing for a focus on signal rather than syntax."
    },
    "long-horizon-kpis": {
        title: "Long Horizon Indicators",
        tagline: "Metrics that maintain signal over decades.",
        icon: ShieldCheck,
        component: null,
        problem: "Most financial KPIs are optimized for quarterly or annual reporting, which can create traps that degrade long-term capital value.",
        methodology: "A library of indicators that explicitly weight long-duration variables over transient market volatility.",
        why: "Ensures alignment with 10-to-30 year stewardship obligations."
    },
    "ethical-ai-checklist": {
        title: "AI Governance Framework",
        tagline: "Opinionated algorithmic governance.",
        icon: Scale,
        component: null,
        problem: "The rapid deployment of AI in investment processes often occurs without a rigorous ethical or fiduciary audit trail.",
        methodology: "A multi-step audit framework designed to generate a 'Fiduciary Alignment Score' for any automated trading or risk model.",
        why: "Ensures that autonomous systems remain within the boundaries of institutional accountability."
    }
};
