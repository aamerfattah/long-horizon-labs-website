"use client";

import { projectRegistry } from '@/lib/projectRegistry';
import Link from "next/link";
import { ArrowRight, Github, ExternalLink } from "lucide-react";
import { motion } from "framer-motion";

export default function ProjectsPage() {
    const projects = Object.entries(projectRegistry).map(([id, data]) => ({
        id,
        ...data
    }));

    return (
        <div className="max-w-6xl mx-auto px-6 py-24 md:py-48 space-y-48">
            <header className="space-y-10 max-w-3xl">
                <div className="h-1.5 w-16 bg-aero-blue" />
                <h1 className="text-7xl md:text-8xl font-black tracking-tighter leading-none text-midnight">Projects</h1>
                <p className="text-2xl text-slate-custom font-medium leading-relaxed tracking-tight">
                    The project suite focuses on minimalist, high-signal artifacts. Technical restraint is prioritised over complexity to ensure decision-grade signal.
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
                            <div className="flex flex-col gap-4 pt-4">
                                <Link
                                    href={`/projects/${project.id}`}
                                    className="inline-flex items-center justify-center gap-3 text-xs font-black uppercase tracking-widest text-white bg-midnight px-8 py-4 rounded-full hover:bg-aero-blue transition-all shadow-premium group"
                                >
                                    Open Sandbox <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                                </Link>
                                <Link
                                    href={`https://github.com/aamerfattah/${project.id}`}
                                    target="_blank"
                                    className="inline-flex items-center justify-center gap-3 text-xs font-black uppercase tracking-widest text-midnight bg-cream px-8 py-4 rounded-full border border-slate-200 hover:border-midnight transition-all group"
                                >
                                    <Github className="w-4 h-4" /> Source Code <ExternalLink className="w-4 h-4 opacity-0 group-hover:opacity-100 transition-opacity" />
                                </Link>
                            </div>
                        </div>
                        <div className="col-span-full md:col-span-8 space-y-20 pt-4 md:pt-0">
                            <div className="space-y-6">
                                <h3 className="text-xs font-black uppercase tracking-[0.3em] text-slate-400">Problem Statement</h3>
                                <p className="text-2xl text-midnight font-bold leading-relaxed tracking-tight">{project.problem}</p>
                            </div>
                            <div className="space-y-6">
                                <h3 className="text-xs font-black uppercase tracking-[0.3em] text-slate-400">Technical Methodology</h3>
                                <p className="text-xl text-slate-custom font-medium leading-relaxed tracking-tight">{project.methodology}</p>
                            </div>
                            <div className="space-y-6 bg-cream p-10 rounded-[40px] border border-slate-100 shadow-subtle">
                                <h3 className="text-xs font-black uppercase tracking-[0.3em] text-aero-blue">Strategic Outcome</h3>
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
