import { Terminal, Database, TreeDeciduous, ShieldCheck, Scale, BarChart3, Box, ArrowRight, Github } from "lucide-react";
import Link from "next/link";

const projects = [
    {
        id: "policy-shock-simulator",
        title: "Policy Shock Simulator",
        tagline: "First order macro impact modelling.",
        problem: "Policy shifts, such as inflation, tax, or contribution rate changes, often have non-linear impacts on long term capital outcomes that are poorly understood by decision makers.",
        approach: "A deterministic scenario engine that models the sensitivity of retirement outcomes to specific policy shocks without the noise of stochastic volatility.",
        why: "Enables CIOs to answer 'what if' questions during regime shifts with immediate, explainable data.",
        icon: Terminal,
        repo: "https://github.com/aamerfattah/policy-shock-simulator"
    },
    {
        id: "member-outcomes-lite",
        title: "Member Outcome Engine",
        tagline: "Outcome centric fund analytics.",
        problem: "Institutional reporting focuses on relative performance, such as benchmarks, rather than the absolute reality of member retirement sufficiency.",
        approach: "Translates high level fund data into human metrics, specifically replacement ratios and funded years.",
        why: "Positions retirement fund leadership around the only metric that matters, which is the member's quality of life.",
        icon: Database,
        repo: "https://github.com/aamerfattah/member-outcomes-lite"
    },
    {
        id: "board-metrics-translator",
        title: "Strategic Metric Translator",
        tagline: "Bridging the technical governance gap.",
        problem: "Engineers and quants provide data while Boards require strategic judgment. The translation layer is often lost in translation.",
        approach: "A rule based mapping engine that generates markdown board packs from technical output.",
        why: "Ensures technical risk is communicated with executive clarity, not jargon.",
        icon: BarChart3,
        repo: "https://github.com/aamerfattah/board-metrics-translator"
    },
    {
        id: "scenario-tree",
        title: "Decision Scenario Tree",
        tagline: "Simplified decision architecture.",
        problem: "Traditional decision trees are either too simple, such as manual trees, or too complex, such as black box AI.",
        approach: "YAML defined logic trees that allow for probability weighting and expected value calculations.",
        why: "Forces clarity in assumptions during complex, multi stage decision processes.",
        icon: TreeDeciduous,
        repo: "https://github.com/aamerfattah/scenario-tree"
    }
];

export default function ProjectsPage() {
    return (
        <div className="max-w-6xl mx-auto px-6 py-24 md:py-48 space-y-48">
            <header className="space-y-10 max-w-3xl">
                <div className="h-1.5 w-16 bg-aero-blue" />
                <h1 className="text-7xl md:text-8xl font-black tracking-tighter leading-none text-midnight">Projects</h1>
                <p className="text-2xl text-slate-custom font-medium leading-relaxed tracking-tight">
                    Our projects are minimalist, opinionated, and built to be understood. We prioritize technical restraint over complexity to ensure decision grade signal.
                </p>
            </header>

            <section className="space-y-48">
                {projects.map((project) => (
                    <div key={project.id} id={project.id} className="editorial-grid scroll-mt-48 pb-24 border-b border-slate-100 last:border-0">
                        <div className="col-span-full md:col-span-4 space-y-10 sticky top-48">
                            <div className="w-16 h-16 rounded-3xl bg-midnight text-white flex items-center justify-center shadow-premium">
                                <project.icon className="w-8 h-8" />
                            </div>
                            <div className="space-y-4">
                                <h2 className="text-4xl font-black tracking-tighter text-midnight leading-none">{project.title}</h2>
                                <div className="text-xs font-black uppercase tracking-[0.3em] text-aero-blue">{project.tagline}</div>
                            </div>
                            <div className="flex gap-4 pt-4">
                                <Link
                                    href={project.repo}
                                    target="_blank"
                                    className="inline-flex items-center gap-3 text-xs font-black uppercase tracking-widest text-white bg-midnight px-8 py-4 rounded-full hover:bg-aero-blue transition-all shadow-premium group"
                                >
                                    <Github className="w-4 h-4" /> Open Repository <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                                </Link>
                            </div>
                        </div>
                        <div className="col-span-full md:col-span-8 space-y-20 pt-4 md:pt-0">
                            <div className="space-y-6">
                                <h3 className="text-xs font-black uppercase tracking-[0.3em] text-slate-400">The Problem</h3>
                                <p className="text-2xl text-midnight font-bold leading-relaxed tracking-tight">{project.problem}</p>
                            </div>
                            <div className="space-y-6">
                                <h3 className="text-xs font-black uppercase tracking-[0.3em] text-slate-400">Technical Approach</h3>
                                <p className="text-xl text-slate-custom font-medium leading-relaxed tracking-tight">{project.approach}</p>
                            </div>
                            <div className="space-y-6 bg-cream p-10 rounded-[40px] border border-slate-100 shadow-subtle">
                                <h3 className="text-xs font-black uppercase tracking-[0.3em] text-aero-blue">Strategic Value</h3>
                                <p className="text-2xl text-midnight font-bold leading-relaxed tracking-tight">
                                    {project.why}
                                </p>
                            </div>
                        </div>
                    </div>
                ))}
            </section>

            <footer className="pt-24 text-center border-t border-slate-200">
                <p className="text-xs text-slate-custom font-black uppercase tracking-[0.3em]">
                    All projects are licensed under the MIT Open Source standard.
                </p>
            </footer>
        </div>
    );
}
