"use client";

import { useParams, notFound } from 'next/navigation';
import { projectRegistry } from '@/lib/projectRegistry';
import Link from 'next/link';
import { ArrowLeft, Github, ExternalLink } from 'lucide-react';
import { motion } from 'framer-motion';

export default function ProjectDetailPage() {
    const params = useParams();
    const id = params.id as string;
    const project = projectRegistry[id as keyof typeof projectRegistry];

    if (!project) {
        notFound();
    }

    const InteractiveComponent = project.component;

    return (
        <div className="max-w-6xl mx-auto px-6 py-24 md:py-48 space-y-32">
            {/* Breadcrumb / Back */}
            <motion.div
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                className="flex items-center gap-4"
            >
                <Link href="/projects" className="group flex items-center gap-2 text-xs font-black uppercase tracking-widest text-slate-400 hover:text-midnight transition-colors">
                    <ArrowLeft className="w-4 h-4 group-hover:-translate-x-1 transition-transform" /> Back to projects
                </Link>
            </motion.div>

            {/* Header */}
            <header className="editorial-grid">
                <div className="col-span-full md:col-span-4 space-y-8">
                    <div className="w-20 h-20 rounded-3xl bg-midnight text-white flex items-center justify-center shadow-premium">
                        <project.icon className="w-10 h-10" />
                    </div>
                    <div className="space-y-4">
                        <div className="h-1 w-12 bg-aero-blue" />
                        <h1 className="text-6xl md:text-7xl font-black tracking-tighter text-midnight leading-none">
                            {project.title}
                        </h1>
                        <p className="text-xs font-black uppercase tracking-[0.4em] text-aero-blue">{project.tagline}</p>
                    </div>
                </div>
                <div className="col-span-full md:col-span-8 self-end pt-12 md:pt-0">
                    <p className="text-3xl md:text-4xl text-midnight font-bold leading-tight tracking-tight text-balance">
                        {project.problem}
                    </p>
                </div>
            </header>

            {/* Interactive Sandbox */}
            <section className="space-y-12">
                <div className="flex justify-between items-end">
                    <div className="space-y-2">
                        <h2 className="text-xs font-black uppercase tracking-[0.3em] text-slate-400">Interactive Sandbox</h2>
                        <p className="text-slate-custom font-medium">This interface allows for the modelling of specific dynamics using custom variables.</p>
                    </div>
                </div>

                {InteractiveComponent ? (
                    <InteractiveComponent />
                ) : (
                    <div className="bg-cream rounded-[48px] p-24 border border-dashed border-slate-200 text-center space-y-6">
                        <div className="w-16 h-16 bg-white rounded-full flex items-center justify-center mx-auto shadow-subtle text-slate-300">
                            <project.icon className="w-8 h-8" />
                        </div>
                        <div className="space-y-2">
                            <h3 className="text-2xl font-black text-midnight tracking-tight">Interactive Preview pending.</h3>
                            <p className="text-slate-custom font-medium max-w-sm mx-auto">The technical engine for {project.title} is being prepared for this web interface.</p>
                        </div>
                        <Link href={`https://github.com/aamerfattah/${id}`} target="_blank" className="inline-flex items-center gap-3 text-xs font-black uppercase tracking-widest text-white bg-midnight px-8 py-4 rounded-full hover:bg-aero-blue transition-all">
                            Browse Source <ExternalLink className="w-4 h-4" />
                        </Link>
                    </div>
                )}
            </section>

            {/* Methodology */}
            <section className="editorial-grid py-24 border-t border-slate-100">
                <div className="col-span-full md:col-span-4">
                    <h2 className="text-sm font-black uppercase tracking-[0.3em] text-aero-blue">Methodology</h2>
                </div>
                <div className="col-span-full md:col-span-8 space-y-12">
                    <div className="bg-midnight p-12 rounded-[48px] text-white space-y-8">
                        <p className="text-3xl font-bold leading-tight tracking-tight">
                            {project.methodology}
                        </p>
                        <div className="flex gap-8">
                            <Link href={`https://github.com/aamerfattah/${id}`} target="_blank" className="group flex items-center gap-3 text-xs font-black uppercase tracking-widest text-aero-blue hover:text-white transition-colors">
                                <Github className="w-5 h-5" /> View on GitHub <ArrowLeft className="rotate-180 w-4 h-4 group-hover:translate-x-1 transition-transform" />
                            </Link>
                        </div>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-12 pt-8">
                        <div className="space-y-4">
                            <h3 className="text-xs font-black uppercase tracking-[0.3em] text-slate-400">Strategic Alignment</h3>
                            <p className="text-xl text-midnight font-bold leading-relaxed tracking-tight">
                                {project.why}
                            </p>
                        </div>
                        <div className="space-y-4">
                            <h3 className="text-xs font-black uppercase tracking-[0.3em] text-slate-400">Technical Fiduciary</h3>
                            <p className="text-base text-slate-custom font-medium leading-relaxed">
                                Open source standards are a prerequisite for financial trust. Every line of logic within these tools is public, auditable, and designed for rigorous peer review.
                            </p>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    );
}
