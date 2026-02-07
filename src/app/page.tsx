"use client";

import Link from "next/link";
import { ArrowRight, Box, Terminal, Database, TreeDeciduous, ShieldCheck, Scale, BarChart3, ChevronRight } from "lucide-react";
import { motion } from "framer-motion";

const projects = [
  {
    title: "Policy Shock Simulator",
    statement: "Modelling first-order impacts of policy shifts on long-term capital outcomes.",
    icon: Terminal,
    id: "policy-shock-simulator"
  },
  {
    title: "Member Outcome Engine",
    statement: "Translating raw fund data into member-centric retirement metrics.",
    icon: Database,
    id: "member-outcomes-lite"
  },
  {
    title: "Strategic Metric Translator",
    statement: "Converting technical complexity into board-level strategic narratives.",
    icon: BarChart3,
    id: "board-metrics-translator"
  },
  {
    title: "Decision Scenario Tree",
    statement: "A minimal engine for weighted decision tree and scenario planning.",
    icon: TreeDeciduous,
    id: "scenario-tree"
  },
  {
    title: "Systemic Data Refinery",
    statement: "Standardising public financial datasets for systemic risk analysis.",
    icon: Box,
    id: "super-data-cleaner"
  },
  {
    title: "Long Horizon Indicators",
    statement: "Defining metrics that maintain signal over 10 to 30 year horizons.",
    icon: ShieldCheck,
    id: "long-horizon-kpis"
  },
  {
    title: "AI Governance Framework",
    statement: "An framework for algorithmic governance and fiduciary deployment.",
    icon: Scale,
    id: "ethical-ai-checklist"
  }
];

export default function HomePage() {
  return (
    <div className="max-w-6xl mx-auto px-6 py-24 md:py-48 space-y-48">
      {/* Hero Section */}
      <section className="space-y-12 max-w-4xl">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="space-y-10"
        >
          <div className="h-1.5 w-16 bg-aero-blue" />
          <h1 className="text-7xl md:text-9xl font-black tracking-tighter leading-[0.8] text-midnight">
            Open tools for <br />
            <span className="text-aero-blue">long-term</span> capital.
          </h1>
          <p className="text-2xl md:text-3xl text-slate-custom font-medium leading-relaxed tracking-tight max-w-2xl">
            Long Horizon Labs develops minimalist, high-signal artifacts for risk, governance, and decision-making in capital markets.
          </p>
        </motion.div>
      </section>

      {/* Philosophy Section */}
      <section className="editorial-grid">
        <div className="col-span-full md:col-span-4 self-center">
          <h2 className="text-sm font-black uppercase tracking-[0.3em] text-aero-blue border-l-4 border-aero-blue pl-4">Philosophy</h2>
        </div>
        <div className="col-span-full md:col-span-8 space-y-10">
          <p className="text-3xl md:text-4xl text-midnight font-bold leading-[1.15] tracking-tight text-balance">
            Systemic risk is often buried in technical complexity. Clarity over cleverness is the primary focus, stripping away noise to expose the variables that drive 30-year outcomes. Explainability, technical restraint, and governance by design remain the core priorities.
          </p>
          <Link href="/principles" className="inline-flex items-center gap-4 text-midnight font-black text-xs uppercase tracking-widest border-b-2 border-midnight pb-2 hover:border-aero-blue hover:text-aero-blue transition-all group">
            View Design Principles <ArrowRight className="w-4 h-4 group-hover:translate-x-2 transition-transform" />
          </Link>
        </div>
      </section>

      {/* Projects Listing */}
      <section className="space-y-20">
        <div className="flex justify-between items-end border-b border-slate-200 pb-10">
          <div className="space-y-2">
            <h2 className="text-sm font-black uppercase tracking-[0.3em] text-aero-blue">Core Artifacts</h2>
            <p className="text-slate-custom font-medium max-w-md">Open source tools for institutional decision support.</p>
          </div>
          <Link href="/projects" className="text-xs font-black text-midnight uppercase tracking-widest hover:text-aero-blue transition-colors flex items-center gap-2">
            Explore All Projects <ChevronRight className="w-4 h-4" />
          </Link>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8">
          {projects.map((project, i) => (
            <Link
              key={project.id}
              href={`/projects/${project.id}`}
              className="group flex flex-col justify-between p-10 bg-white border border-slate-100 rounded-[40px] hover:shadow-premium hover:border-aero-blue/20 transition-all duration-500 relative overflow-hidden"
            >
              <div className="absolute top-0 right-0 p-8 opacity-5 group-hover:opacity-10 transition-opacity">
                <project.icon className="w-32 h-32" />
              </div>

              <div className="space-y-6 relative z-10">
                <div className="w-12 h-12 rounded-2xl bg-cream flex items-center justify-center text-slate-custom group-hover:bg-aero-blue group-hover:text-white transition-all duration-500">
                  <project.icon className="w-6 h-6" />
                </div>
                <div className="space-y-2">
                  <h3 className="text-2xl font-black tracking-tight text-midnight leading-none">{project.title}</h3>
                  <p className="text-base text-slate-custom leading-relaxed font-medium max-w-xs">{project.statement}</p>
                </div>
              </div>

              <div className="mt-12 flex items-center gap-3 text-[10px] font-black text-aero-blue uppercase tracking-widest transform translate-y-4 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-500">
                Open Sandbox <ArrowRight className="w-3 h-3" />
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* Footer Sign-off */}
      <footer className="pt-32 pb-16 flex flex-col md:flex-row justify-between gap-12 items-start md:items-end">
        <div className="space-y-4">
          <div className="font-black text-midnight tracking-tighter text-4xl">Long Horizon Labs</div>
          <p className="text-slate-custom font-medium max-w-xs leading-relaxed text-sm">
            Providing the technical substrate for 30-year strategic judgment in capital markets.
          </p>
          <div className="text-[10px] text-slate-400 font-black uppercase tracking-[0.2em] pt-4">© 2026. All Rights Reserved.</div>
        </div>
        <nav className="flex flex-wrap gap-x-12 gap-y-4 text-xs font-black text-midnight uppercase tracking-widest">
          <Link href="/about" className="hover:text-aero-blue transition-colors">Profile</Link>
          <Link href="/governance" className="hover:text-aero-blue transition-colors">Governance</Link>
          <Link href="https://github.com/aamerfattah" className="hover:text-aero-blue transition-colors underline decoration-aero-blue decoration-2 underline-offset-4">GitHub</Link>
        </nav>
      </footer>
    </div>
  );
}
