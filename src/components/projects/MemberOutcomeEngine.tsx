"use client";

import React, { useState, useMemo } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts';
import { Database, TrendingUp, AlertTriangle, CheckCircle2 } from 'lucide-react';

export default function MemberOutcomeEngine() {
    const [age, setAge] = useState(35);
    const [retireAge, setRetireAge] = useState(65);
    const [balance, setBalance] = useState(150000);
    const [contribution, setContribution] = useState(15000);
    const [returns, setReturns] = useState(7);
    const [income, setIncome] = useState(80000);

    const results = useMemo(() => {
        let currentBalance = balance;
        const yearsToRetire = retireAge - age;
        const timeline = [];

        // Accumulation
        for (let i = 0; i <= yearsToRetire; i++) {
            timeline.push({
                age: age + i,
                balance: Math.round(currentBalance),
                type: 'accumulation'
            });
            currentBalance = currentBalance * (1 + returns / 100) + contribution;
        }

        // Decumulation
        let fundedYears = 0;
        for (let i = 1; i <= 40; i++) {
            if (currentBalance <= 0) break;
            fundedYears++;
            currentBalance = (currentBalance - income) * (1 + (returns - 2) / 100); // Lower returns in retirement
            timeline.push({
                age: retireAge + i,
                balance: Math.max(0, Math.round(currentBalance)),
                type: 'decumulation'
            });
        }

        return { timeline, fundedYears };
    }, [age, retireAge, balance, contribution, returns, income]);

    const isSecure = results.fundedYears >= 25;

    return (
        <div className="space-y-12 bg-white rounded-[40px] p-8 md:p-12 border border-slate-100 shadow-premium">
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
                {/* Inputs */}
                <div className="space-y-8">
                    <div className="grid grid-cols-2 gap-4">
                        <div className="space-y-2">
                            <label className="text-[10px] font-black uppercase tracking-[0.2em] text-slate-400">Current Age</label>
                            <input type="number" value={age} onChange={(e) => setAge(Number(e.target.value))} className="w-full bg-cream border-none rounded-xl p-3 font-bold text-midnight" />
                        </div>
                        <div className="space-y-2">
                            <label className="text-[10px] font-black uppercase tracking-[0.2em] text-slate-400">Retire Age</label>
                            <input type="number" value={retireAge} onChange={(e) => setRetireAge(Number(e.target.value))} className="w-full bg-cream border-none rounded-xl p-3 font-bold text-midnight" />
                        </div>
                    </div>

                    <div className="space-y-4">
                        <label className="text-[10px] font-black uppercase tracking-[0.2em] text-slate-400">Current Balance ($)</label>
                        <input type="number" value={balance} onChange={(e) => setBalance(Number(e.target.value))} className="w-full bg-cream border-none rounded-xl p-3 font-bold text-midnight" />
                    </div>

                    <div className="space-y-4">
                        <label className="text-[10px] font-black uppercase tracking-[0.2em] text-slate-400">Annual Contribution ($)</label>
                        <input type="number" value={contribution} onChange={(e) => setContribution(Number(e.target.value))} className="w-full bg-cream border-none rounded-xl p-3 font-bold text-midnight" />
                    </div>

                    <div className="space-y-4">
                        <label className="text-[10px] font-black uppercase tracking-[0.2em] text-slate-400">Desired Annual Income ($)</label>
                        <input type="number" value={income} onChange={(e) => setIncome(Number(e.target.value))} className="w-full bg-cream border-none rounded-xl p-3 font-bold text-midnight" />
                    </div>
                </div>

                {/* Status Cards */}
                <div className="lg:col-span-2 space-y-8">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div className="p-8 bg-midnight rounded-[32px] text-white space-y-2">
                            <div className="text-[10px] font-black uppercase tracking-[0.3em] text-aero-blue">Longevity Signal</div>
                            <div className="text-5xl font-black tracking-tighter">{results.fundedYears} <span className="text-lg">Years</span></div>
                            <p className="text-xs text-slate-400 font-medium pt-4">Estimated duration of retirement capital before exhaustion.</p>
                        </div>
                        <div className={`p-8 rounded-[32px] border flex flex-col justify-between ${isSecure ? 'bg-emerald-50 border-emerald-100' : 'bg-orange-50 border-orange-100'}`}>
                            <div className="flex justify-between items-start">
                                <div className={`text-[10px] font-black uppercase tracking-[0.3em] ${isSecure ? 'text-emerald-600' : 'text-orange-600'}`}>Security Rating</div>
                                {isSecure ? <CheckCircle2 className="text-emerald-500" /> : <AlertTriangle className="text-orange-500" />}
                            </div>
                            <div className={`text-3xl font-black tracking-tighter ${isSecure ? 'text-emerald-900' : 'text-orange-900'}`}>
                                {isSecure ? 'Horizon Stable' : 'Action Required'}
                            </div>
                        </div>
                    </div>

                    {/* Chart */}
                    <div className="h-[300px] w-full pt-4">
                        <ResponsiveContainer width="100%" height="100%">
                            <BarChart data={results.timeline}>
                                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f1f5f9" />
                                <XAxis dataKey="age" axisLine={false} tickLine={false} tick={{ fontSize: 10, fill: '#94a3b8' }} hide={true} />
                                <Tooltip cursor={{ fill: 'transparent' }} contentStyle={{ borderRadius: '16px', border: 'none', boxShadow: '0 10px 40px -10px rgba(0,0,0,0.1)' }} />
                                <Bar dataKey="balance" radius={[4, 4, 0, 0]}>
                                    {results.timeline.map((entry, index) => (
                                        <Cell key={`cell-${index}`} fill={entry.type === 'accumulation' ? '#000B18' : '#00A3FF'} />
                                    ))}
                                </Bar>
                            </BarChart>
                        </ResponsiveContainer>
                        <div className="flex justify-center gap-8 pt-4">
                            <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-midnight">
                                <div className="w-2 h-2 rounded-full bg-midnight" /> Accumulation
                            </div>
                            <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-aero-blue">
                                <div className="w-2 h-2 rounded-full bg-aero-blue" /> Retirement
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {/* Insight */}
            <div className="pt-12 border-t border-slate-100 grid grid-cols-1 md:grid-cols-2 gap-12">
                <div className="space-y-4">
                    <h3 className="text-xs font-black uppercase tracking-[0.3em] text-midnight">Pedagogy</h3>
                    <p className="text-base text-slate-custom font-medium leading-relaxed">
                        Retirement security remains a decumulation risk management exercise. The sequence of returns during the Retirement Risk Zone (the first 5 years of decumulation) is more critical than the prior accumulation phase.
                    </p>
                </div>
                <div className="bg-cream p-8 rounded-[32px] border border-slate-100 space-y-4">
                    <h2 className="text-[10px] font-black uppercase tracking-[0.3em] text-aero-blue">Core Metric</h2>
                    <p className="text-lg font-bold text-midnight tracking-tight">
                        Fund success is measured by the years of security provided, rather than the asset base managed.
                    </p>
                </div>
            </div>
        </div>
    );
}
