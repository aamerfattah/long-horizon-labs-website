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
        problem: "Policy shifts—such as inflation, tax, or contribution rate changes—often have non-linear impacts on long term capital outcomes that are poorly understood by decision makers.",
        methodology: "I built this deterministic scenario engine to bypass the noise of stochastic volatility. It focuses on the primary sensitivities of a 30-year accumulation plan to sustained external shocks.",
        why: "Enables CIOs to answer 'what if' questions during regime shifts with immediate, explainable data."
    },
    "member-outcomes-lite": {
        title: "Member Outcome Engine",
        tagline: "Outcome-centric fund analytics.",
        icon: Database,
        component: MemberOutcomeEngine,
        problem: "Institutional reporting often obsessively tracks 'relative performance' against arbitrary benchmarks while ignoring the absolute reality of member retirement sufficiency.",
        methodology: "This engine translates raw asset data into human metrics. I focus on 'Funded Years' and 'Replacement Ratios' as the primary signals of fund health.",
        why: "I position retirement fund leadership around the only metric that matters: the member's quality of life."
    },
    "board-metrics-translator": {
        title: "Strategic Metric Translator",
        tagline: "Bridging the technical governance gap.",
        icon: BarChart3,
        component: StrategicMetricTranslator,
        problem: "Technical teams provide data; Boards require strategic judgment. The translation layer is where critical risks are often lost or obscured by jargon.",
        methodology: "I designed a rule-based mapping engine that forces a commitment to narrative. It translates technical breaches into boardroom-ready strategic choices.",
        why: "I ensure technical risk is communicated with executive clarity, enabling informed capital allocation."
    },
    "scenario-tree": {
        title: "Decision Scenario Tree",
        tagline: "Simplified decision architecture.",
        icon: TreeDeciduous,
        component: DecisionScenarioTree,
        problem: "Decision-making in capital markets often suffers from either over-simplification or 'black-box' complexity that lacks accountability.",
        methodology: "I developed this YAML-defined logic tree engine to allow for probability weighting and expected value calculations across multiple strategic regimes.",
        why: "Forces clarity in assumptions and ensures a valid process even when outcomes are uncertain."
    },
    "super-data-cleaner": {
        title: "Systemic Data Refinery",
        tagline: "Standardising public financial datasets.",
        icon: Box,
        component: null, // To be built or just a placeholder for now
        problem: "Systemic risk analysis is hampered by the fragmented, non-standard nature of public financial disclosures across different jurisdictions.",
        methodology: "I am building a rule-based refinery that standardises disparate CSV and JSON blobs into a unified schema for multi-asset stress testing.",
        why: "Reduces the 'data janitor' overhead, allowing quants to focus on signal rather than syntax."
    },
    "long-horizon-kpis": {
        title: "Long Horizon Indicators",
        tagline: "Metrics that maintain signal over decades.",
        icon: ShieldCheck,
        component: null,
        problem: "Most financial KPIs are optimized for quarterly or annual reporting, creating a 'short-termism' trap that degrades long-term capital value.",
        methodology: "I am defining a library of indicators that explicitly weight long-duration variables over transient market volatility.",
        why: "Ensures the organisation remains aligned with 10-to-30 year stewardship obligations."
    },
    "ethical-ai-checklist": {
        title: "AI Governance Framework",
        tagline: "Opinionated algorithmic governance.",
        icon: Scale,
        component: null,
        problem: "The rapid deployment of AI in investment processes often happens without a rigorous ethical or fiduciary audit trail.",
        methodology: "My framework is an opinionated multi-step audit that generates a 'Fiduciary Alignment Score' for any automated trading or risk model.",
        why: "Ensures that 'autonomous' systems remain within the boundaries of institutional accountability."
    }
};
