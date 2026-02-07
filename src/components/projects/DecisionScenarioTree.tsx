"use client";

import React, { useState } from 'react';
import { TreeDeciduous, ArrowRight, Target, ShieldAlert, MousePointer2 } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

export default function DecisionScenarioTree() {
    const [activePath, setActivePath] = useState<number[]>([]);

    const tree = {
        label: "Strategic Regime Shift",
        options: [
            {
                id: 1,
                label: "Aggressive Growth",
                prob: 0.6,
                outcome: "High Yield / High Vol",
                risk: "Severe",
                desc: "I pivot the mandate towards emerging tech and private equity to capture the next super-cycle."
            },
            {
                id: 2,
                label: "Defensive Protection",
                prob: 0.4,
                outcome: "Low Yield / Stability",
                risk: "Minimal",
                desc: "I prioritise purchasing power protection by increasing bond duration and cash buffers."
            }
        ]
    };

    const selectedOption = activePath.length > 0 ? tree.options.find(o => o.id === activePath[0]) : null;

    return (
        <div className="space-y-12 bg-white rounded-[40px] p-8 md:p-12 border border-slate-100 shadow-premium">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
                {/* Tree Visualization */}
                <div className="space-y-8 bg-cream rounded-[40px] p-10 border border-slate-100 flex flex-col justify-center min-h-[400px]">
                    <div className="flex flex-col items-center gap-6">
                        <div className="p-6 bg-midnight text-white rounded-3xl shadow-premium relative">
                            <div className="text-[10px] font-black uppercase tracking-[0.2em] text-aero-blue mb-1">Root Decision</div>
                            <div className="text-xl font-black tracking-tight">{tree.label}</div>
                            <div className="absolute top-1/2 -right-4 w-4 h-0.5 bg-midnight" />
                        </div>

                        <div className="flex gap-12 pt-8 relative">
                            <div className="absolute top-0 left-1/2 -ml-[1px] w-[2px] h-8 bg-slate-200" />
                            {tree.options.map((opt) => (
                                <button
                                    key={opt.id}
                                    onClick={() => setActivePath([opt.id])}
                                    className={`group relative p-8 rounded-[32px] border-2 transition-all duration-500 flex flex-col items-center gap-4 text-center w-48 ${activePath.includes(opt.id) ? 'bg-white border-aero-blue shadow-premium scale-105' : 'bg-white/50 border-transparent hover:border-slate-200'}`}
                                >
                                    <div className={`p-4 rounded-2xl transition-colors ${activePath.includes(opt.id) ? 'bg-aero-blue text-white' : 'bg-slate-100 text-slate-400 group-hover:bg-slate-200'}`}>
                                        {opt.id === 1 ? <TrendingUp className="w-5 h-5" /> : <ShieldAlert className="w-5 h-5" />}
                                    </div>
                                    <div className="space-y-1">
                                        <div className="text-sm font-black text-midnight">{opt.label}</div>
                                        <div className="text-[10px] font-bold text-slate-400 uppercase tracking-widest">{opt.prob * 100}% Prob</div>
                                    </div>
                                    {activePath.includes(opt.id) && (
                                        <motion.div layoutId="pointer" className="absolute -top-12 text-aero-blue">
                                            <MousePointer2 className="w-6 h-6 animate-bounce" />
                                        </motion.div>
                                    )}
                                </button>
                            ))}
                        </div>
                    </div>
                </div>

                {/* Path Analysis */}
                <div className="flex flex-col justify-center">
                    <AnimatePresence mode="wait">
                        {selectedOption ? (
                            <motion.div
                                key={selectedOption.id}
                                initial={{ opacity: 0, x: 20 }}
                                animate={{ opacity: 1, x: 0 }}
                                exit={{ opacity: 0, x: -20 }}
                                className="space-y-8"
                            >
                                <div className="flex items-center gap-4 text-xs font-black uppercase tracking-[0.4em] text-aero-blue">
                                    <Target className="w-4 h-4" /> Path Analysis
                                </div>
                                <div className="space-y-6">
                                    <h2 className="text-5xl font-black text-midnight tracking-tighter leading-none">{selectedOption.label}</h2>
                                    <p className="text-xl text-slate-custom font-medium leading-relaxed tracking-tight max-w-md">
                                        {selectedOption.desc}
                                    </p>
                                </div>

                                <div className="grid grid-cols-2 gap-4">
                                    <div className="p-6 bg-cream rounded-3xl border border-slate-100">
                                        <div className="text-[10px] font-black uppercase tracking-widest text-slate-400 mb-2">Expected Outcome</div>
                                        <div className="text-lg font-black text-midnight">{selectedOption.outcome}</div>
                                    </div>
                                    <div className="p-6 bg-cream rounded-3xl border border-slate-100">
                                        <div className="text-[10px] font-black uppercase tracking-widest text-slate-400 mb-2">Tail Risk</div>
                                        <div className="text-lg font-black text-aero-blue">{selectedOption.risk}</div>
                                    </div>
                                </div>
                            </motion.div>
                        ) : (
                            <div className="space-y-6 text-center lg:text-left py-12">
                                <TreeDeciduous className="w-16 h-16 text-slate-200 mx-auto lg:mx-0 mb-6" />
                                <h2 className="text-3xl font-black text-slate-300 tracking-tighter">Select a decision path <br /> to model outcomes.</h2>
                            </div>
                        )}
                    </AnimatePresence>
                </div>
            </div>

            <div className="pt-12 border-t border-slate-100 grid grid-cols-1 md:grid-cols-2 gap-12">
                <div className="space-y-4">
                    <h3 className="text-xs font-black uppercase tracking-[0.3em] text-midnight">Logic Architecture</h3>
                    <p className="text-base text-slate-custom font-medium leading-relaxed">
                        I built this tree engine to prevent 'analysis paralysis'. By defining weighted paths, I force a quantification of subjective strategy. It is not about predicting the future; it is about ensuring that whatever path I choose, I have calculated the cost of being wrong.
                    </p>
                </div>
                <div className="bg-cream p-10 rounded-[48px] border border-slate-100 flex flex-col justify-center gap-2">
                    <div className="text-[10px] font-black uppercase tracking-[0.4em] text-aero-blue">Strategic Mantra</div>
                    <p className="text-2xl font-black text-midnight tracking-tight leading-tight">
                        'I value valid process over certain outcomes.'
                    </p>
                </div>
            </div>
        </div>
    );
}

function TrendingUp(props: React.SVGProps<SVGSVGElement>) {
    return (
        <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="lucide lucide-trending-up"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17" /><polyline points="16 7 22 7 22 13" /></svg>
    )
}
