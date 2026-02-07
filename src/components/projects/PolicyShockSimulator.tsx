"use client";

import React, { useState, useMemo } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';
import { Terminal, Info, RefreshCcw } from 'lucide-react';

export default function PolicyShockSimulator() {
    const [capital, setCapital] = useState(1000000);
    const [horizon, setHorizon] = useState(30);
    const [yieldRate, setYieldRate] = useState(5);
    const [inflationShock, setInflationShock] = useState(2);
    const [shockYear, setShockYear] = useState(5);

    const data = useMemo(() => {
        let baseCapital = capital;
        let shockCapital = capital;
        const chartData = [];

        for (let year = 0; year <= horizon; year++) {
            const currentYield = yieldRate / 100;
            const currentShock = year >= shockYear ? (inflationShock / 100) : 0;

            chartData.push({
                year,
                base: Math.round(baseCapital),
                shocked: Math.round(shockCapital),
                delta: Math.round(shockCapital - baseCapital)
            });

            baseCapital *= (1 + currentYield);
            // Shocked capital is eroded by the inflation shock
            shockCapital *= (1 + currentYield - currentShock);
        }
        return chartData;
    }, [capital, horizon, yieldRate, inflationShock, shockYear]);

    return (
        <div className="space-y-12 bg-white rounded-[40px] p-8 md:p-12 border border-slate-100 shadow-premium">
            <div className="flex flex-col md:flex-row gap-12">
                {/* Controls */}
                <div className="w-full md:w-1/3 space-y-10">
                    <div className="space-y-4">
                        <label className="text-[10px] font-black uppercase tracking-[0.2em] text-slate-400 flex items-center gap-2">
                            Initial Capital ($) <Info className="w-3 h-3" />
                        </label>
                        <input
                            type="number"
                            value={capital}
                            onChange={(e) => setCapital(Number(e.target.value))}
                            className="w-full bg-cream border-none rounded-2xl p-4 font-bold text-midnight focus:ring-2 focus:ring-aero-blue transition-all"
                        />
                    </div>

                    <div className="space-y-4">
                        <label className="text-[10px] font-black uppercase tracking-[0.2em] text-slate-400">
                            Horizon: {horizon} Years
                        </label>
                        <input
                            type="range" min="5" max="50" value={horizon}
                            onChange={(e) => setHorizon(Number(e.target.value))}
                            className="w-full h-1.5 bg-slate-100 rounded-lg appearance-none cursor-pointer accent-aero-blue"
                        />
                    </div>

                    <div className="space-y-4">
                        <label className="text-[10px] font-black uppercase tracking-[0.2em] text-slate-400">
                            Annual Yield: {yieldRate}%
                        </label>
                        <input
                            type="range" min="1" max="15" value={yieldRate}
                            onChange={(e) => setYieldRate(Number(e.target.value))}
                            className="w-full h-1.5 bg-slate-100 rounded-lg appearance-none cursor-pointer accent-midnight"
                        />
                    </div>

                    <div className="space-y-4 p-6 bg-cream rounded-3xl border border-aero-blue/10">
                        <label className="text-[10px] font-black uppercase tracking-[0.2em] text-aero-blue flex items-center gap-2">
                            Inflation Shock (%) <RefreshCcw className="w-3 h-3" />
                        </label>
                        <input
                            type="range" min="0" max="10" step="0.5" value={inflationShock}
                            onChange={(e) => setInflationShock(Number(e.target.value))}
                            className="w-full h-1.5 bg-aero-blue/20 rounded-lg appearance-none cursor-pointer accent-aero-blue"
                        />
                        <p className="text-[10px] text-slate-400 font-medium pt-2">
                            Simulated real-yield erosion starting at year {shockYear}.
                        </p>
                    </div>
                </div>

                {/* Visualization */}
                <div className="w-full md:w-2/3 h-[400px] bg-cream rounded-[40px] p-8 relative">
                    <div className="absolute top-8 left-8 z-10">
                        <div className="text-[10px] font-black uppercase tracking-[0.2em] text-midnight">Capital Projection</div>
                        <div className="text-3xl font-black text-midnight tracking-tighter">
                            {((data[data.length - 1].delta / data[data.length - 1].base) * 100).toFixed(1)}% <span className="text-sm font-bold text-slate-400 tracking-normal">Impact</span>
                        </div>
                    </div>

                    <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={data}>
                            <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#E2E8F0" />
                            <XAxis
                                dataKey="year"
                                axisLine={false}
                                tickLine={false}
                                tick={{ fontSize: 10, fontWeight: 700, fill: '#94A3B8' }}
                                dy={10}
                            />
                            <YAxis
                                hide={true}
                                domain={['auto', 'auto']}
                            />
                            <Tooltip
                                contentStyle={{ borderRadius: '20px', border: 'none', boxShadow: '0 10px 40px -10px rgba(0,0,0,0.1)', padding: '20px' }}
                                itemStyle={{ fontSize: '12px', fontWeight: 800, textTransform: 'uppercase', letterSpacing: '0.1em' }}
                            />
                            <Line
                                type="monotone"
                                dataKey="base"
                                stroke="#000B18"
                                strokeWidth={4}
                                dot={false}
                                name="Base Case"
                            />
                            <Line
                                type="monotone"
                                dataKey="shocked"
                                stroke="#00A3FF"
                                strokeWidth={4}
                                strokeDasharray="8 8"
                                dot={false}
                                name="Shock Case"
                            />
                        </LineChart>
                    </ResponsiveContainer>
                </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-12 pt-12 border-t border-slate-100">
                <div className="space-y-4">
                    <h3 className="text-xs font-black uppercase tracking-[0.3em] text-midnight">Walkthrough</h3>
                    <p className="text-base text-slate-custom font-medium leading-relaxed">
                        I designed this simulator to expose the non-linear relationship between persistent macro shifts and terminal capital. Even a modest 2% sustained inflation shock, often dismissed as 'cyclical noise', can erode over 30% of real purchasing power over a 30-year horizon.
                    </p>
                </div>
                <div className="bg-midnight p-8 rounded-[32px] text-white space-y-4">
                    <h3 className="text-[10px] font-black uppercase tracking-[0.3em] text-aero-blue">Strategic Insight</h3>
                    <p className="text-lg font-bold leading-tight tracking-tight">
                        'Compounding works both ways. My model shows that regressive shocks are not arithmetic; they are exponential.'
                    </p>
                </div>
            </div>
        </div>
    );
}
