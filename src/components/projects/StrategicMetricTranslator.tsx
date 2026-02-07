"use client";

import React, { useState } from 'react';
import { BarChart3, Quote, FileText, CheckCircle, AlertCircle, XCircle } from 'lucide-react';

const metrics = [
    {
        id: 'liquidity',
        name: 'Liquidity Coverage',
        desc: 'Availability of cash for 30-day obligations.',
        templates: {
            green: "Liquidity remains robust, exceeding the internal corridor of 120%. I am confident that current buffers are sufficient to weather unforeseen redemption volatility without asset liquidation.",
            amber: "Liquidity is currently within the lower bounds of our tolerance (105%). I have initiated a tactical watch and am prepared to rebalance the cash sleeve if redemption rates trend higher in Q2.",
            red: "Liquidity has breached the 100% threshold. I am executing a mandatory deleveraging protocol to restore baseline stability and am reporting this as a Tier 1 governance incident."
        }
    },
    {
        id: 'capital',
        name: 'Retirement Sufficiency',
        desc: 'Projected member income vs target replacement.',
        templates: {
            green: "Outcome projections show 85% of members on track for target sufficiency. My current strategic allocation is delivering predictable real returns in line with 30-year objectives.",
            amber: "Sufficiency has dipped to 72% due to persistent CPI headwinds. I am reviewing the growth-to-defensive ratio to ensure we are not sacrificing long-term purchasing power for short-term stability.",
            red: "Outcome sufficiency has dropped below the 60% floor. I consider this a systemic failure of the current mandate and am recommending an immediate board review of the strategic asset allocation (SAA)."
        }
    },
    {
        id: 'esg',
        name: 'Climate Transition Risk',
        desc: 'Portfolio exposure to high-carbon transition assets.',
        templates: {
            green: "Transition risk is well mitigated with 90% alignment to our Net Zero 2040 roadmap. I have successfully rotated out of stranded asset risks without compromising yield.",
            amber: "We are seeing marginal delay in transition benchmarks within the private equity sleeve. I am engaging with fund managers to accelerate decarbonisation targets by year-end.",
            red: "Transition risk exposure has spiked due to valuation shifts in the energy sector. I am mandating an immediate divestment strategy to protect the long-term integrity of the fund."
        }
    }
];

export default function StrategicMetricTranslator() {
    const [selectedMetric, setSelectedMetric] = useState(metrics[0]);
    const [status, setStatus] = useState<'green' | 'amber' | 'red'>('green');

    return (
        <div className="space-y-12 bg-white rounded-[40px] p-8 md:p-12 border border-slate-100 shadow-premium">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
                {/* Metric Selection */}
                <div className="space-y-10">
                    <div className="space-y-6">
                        <h3 className="text-[10px] font-black uppercase tracking-[0.3em] text-slate-400">Step 1: Select Metric</h3>
                        <div className="space-y-4">
                            {metrics.map((m) => (
                                <button
                                    key={m.id}
                                    onClick={() => setSelectedMetric(m)}
                                    className={`w-full p-6 rounded-3xl border text-left transition-all duration-300 ${selectedMetric.id === m.id ? 'bg-midnight text-white border-midnight shadow-premium' : 'bg-cream border-transparent text-midnight hover:border-slate-200'}`}
                                >
                                    <div className="font-black tracking-tight text-lg">{m.name}</div>
                                    <div className={`text-xs mt-1 ${selectedMetric.id === m.id ? 'text-slate-400' : 'text-slate-500'}`}>{m.desc}</div>
                                </button>
                            ))}
                        </div>
                    </div>

                    <div className="space-y-6">
                        <h3 className="text-[10px] font-black uppercase tracking-[0.3em] text-slate-400">Step 2: Technical Status</h3>
                        <div className="flex gap-4">
                            {(['green', 'amber', 'red'] as const).map((s) => (
                                <button
                                    key={s}
                                    onClick={() => setStatus(s)}
                                    className={`flex-1 p-4 rounded-2xl border-2 flex flex-col items-center gap-2 transition-all ${status === s
                                            ? (s === 'green' ? 'bg-emerald-50 border-emerald-500 text-emerald-700' : s === 'amber' ? 'bg-orange-50 border-orange-500 text-orange-700' : 'bg-red-50 border-red-500 text-red-700')
                                            : 'border-slate-100 bg-white text-slate-400 hover:border-slate-200'
                                        }`}
                                >
                                    {s === 'green' ? <CheckCircle className="w-5 h-5" /> : s === 'amber' ? <AlertCircle className="w-5 h-5" /> : <XCircle className="w-5 h-5" />}
                                    <span className="text-[10px] font-black uppercase tracking-widest">{s}</span>
                                </button>
                            ))}
                        </div>
                    </div>
                </div>

                {/* Narrative Output */}
                <div className="space-y-8">
                    <div className="h-full bg-cream rounded-[40px] p-10 border border-slate-100 flex flex-col justify-between relative overflow-hidden">
                        <div className="absolute top-0 right-0 p-10 opacity-[0.03]">
                            <BarChart3 className="w-48 h-48" />
                        </div>

                        <div className="space-y-8 relative z-10">
                            <div className="flex items-center gap-4 text-xs font-black uppercase tracking-[0.4em] text-aero-blue">
                                <FileText className="w-4 h-4" /> Board Pack Preview
                            </div>

                            <div className="space-y-6">
                                <h2 className="text-3xl font-black text-midnight tracking-tighter leading-tight">
                                    CEO Strategic Narrative: <br />
                                    <span className="text-aero-blue">{selectedMetric.name}</span>
                                </h2>
                                <div className="p-8 bg-white/60 backdrop-blur-sm rounded-[32px] border border-white relative mt-8">
                                    <Quote className="w-8 h-8 text-aero-blue mb-4 opacity-50" />
                                    <p className="text-xl md:text-2xl text-midnight font-bold leading-[1.3] tracking-tight text-balance italic">
                                        {selectedMetric.templates[status]}
                                    </p>
                                </div>
                            </div>
                        </div>

                        <div className="mt-12 pt-8 border-t border-slate-200/50 flex justify-between items-center text-[10px] font-black uppercase tracking-widest text-slate-400">
                            <span>Ref: LABS-SR-2026</span>
                            <span className="text-midnight">Generated Artifact</span>
                        </div>
                    </div>
                </div>
            </div>

            <div className="pt-12 border-t border-slate-100 grid grid-cols-1 md:grid-cols-2 gap-12">
                <div className="space-y-4">
                    <h3 className="text-xs font-black uppercase tracking-[0.3em] text-midnight">Reporting Philosophy</h3>
                    <p className="text-base text-slate-custom font-medium leading-relaxed">
                        I believe that too many executive reports fail because they provide data without perspective. My 'Strategic Metric Translator' is designed to force technical teams to commit to a narrative. It translates quantitative breach levels into qualitative strategic choices that Boards can actually act upon.
                    </p>
                </div>
                <div className="bg-midnight p-8 rounded-[32px] text-white flex items-center justify-center text-center">
                    <p className="text-lg font-bold text-aero-blue leading-tight tracking-tight px-4">
                        'I don't report numbers; I report the risks those numbers represent.'
                    </p>
                </div>
            </div>
        </div>
    );
}
