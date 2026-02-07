export default function AboutPage() {
    return (
        <div className="max-w-6xl mx-auto px-6 py-24 md:py-48 space-y-48">
            <header className="space-y-10 max-w-3xl">
                <div className="h-1.5 w-16 bg-aero-blue" />
                <h1 className="text-7xl md:text-8xl font-black tracking-tighter leading-none text-midnight">Profile</h1>
                <p className="text-2xl text-slate-custom font-medium leading-relaxed tracking-tight">
                    Scaling financial services organisations through growth, risk discipline, and digital advantage.
                </p>
            </header>

            <section className="editorial-grid">
                <div className="col-span-full md:col-span-4 self-start">
                    <h2 className="text-sm font-black uppercase tracking-[0.3em] text-aero-blue">Strategic Logic</h2>
                </div>
                <div className="col-span-full md:col-span-8 space-y-12">
                    <p className="text-3xl md:text-4xl text-midnight font-bold leading-tight tracking-tight text-balance">
                        Enterprise expertise across 20-plus years leading strategy, product, technology, and transformation within highly regulated financial services environments.
                    </p>
                    <div className="space-y-8 max-w-2xl">
                        <p className="text-xl text-slate-custom font-medium leading-relaxed">
                            Proven performance in scaling organisations, executing complex mergers, and commercialising digital platforms while strengthening risk and compliance at the board level. Specialist focus remains on bridging commercial strategy with technology execution, aligning innovation with operating models to deliver regulatory confidence and superior customer outcomes.
                        </p>
                        <p className="text-xl text-slate-custom font-medium leading-relaxed">
                            Qualifications include Graduate Member status with the Australian Institute of Company Directors (GAICD) and an Executive MBA from AGSM. Domain expertise covers the emerging risks and opportunities within the superannuation, insurance, and data sectors.
                        </p>
                    </div>
                </div>
            </section>

            <section className="editorial-grid">
                <div className="col-span-full md:col-span-4 self-start">
                    <h2 className="text-sm font-black uppercase tracking-[0.3em] text-aero-blue">Core Capabilities</h2>
                </div>
                <div className="col-span-full md:col-span-8 grid grid-cols-1 md:grid-cols-2 gap-20">
                    <div className="space-y-8">
                        <h3 className="text-2xl font-black text-midnight tracking-tight">Strategic Domain</h3>
                        <ul className="space-y-4 text-xs text-midnight font-black uppercase tracking-[0.2em] pt-4">
                            <li className="flex items-center gap-4"><span className="w-2 h-2 bg-aero-blue rounded-full"></span> Enterprise Strategy & Value Creation</li>
                            <li className="flex items-center gap-4"><span className="w-2 h-2 bg-aero-blue rounded-full"></span> P&L Ownership & Capital Allocation</li>
                            <li className="flex items-center gap-4"><span className="w-2 h-2 bg-aero-blue rounded-full"></span> Board & Regulator Engagement</li>
                            <li className="flex items-center gap-4"><span className="w-2 h-2 bg-aero-blue rounded-full"></span> M&A Integration & Operating Models</li>
                            <li className="flex items-center gap-4"><span className="w-2 h-2 bg-aero-blue rounded-full"></span> Executive Leadership & Culture</li>
                        </ul>
                    </div>
                    <div className="space-y-8">
                        <h3 className="text-2xl font-black text-midnight tracking-tight">Technical Governance</h3>
                        <ul className="space-y-4 text-xs text-midnight font-black uppercase tracking-[0.2em] pt-4">
                            <li className="flex items-center gap-4"><span className="w-2 h-2 bg-midnight rounded-full"></span> Product & Platform Strategy</li>
                            <li className="flex items-center gap-4"><span className="w-2 h-2 bg-midnight rounded-full"></span> Data, AI & Digital Governance</li>
                            <li className="flex items-center gap-4"><span className="w-2 h-2 bg-midnight rounded-full"></span> Risk, Compliance & Assurance</li>
                            <li className="flex items-center gap-4"><span className="w-2 h-2 bg-midnight rounded-full"></span> Digital Advantage & Transformation</li>
                            <li className="flex items-center gap-4"><span className="w-2 h-2 bg-midnight rounded-full"></span> Ecosystem & Partnership Strategy</li>
                        </ul>
                    </div>
                </div>
            </section>

            <footer className="pt-32 pb-16 border-t border-slate-100 flex flex-col md:flex-row justify-between items-start md:items-center gap-8">
                <div className="text-[10px] font-black uppercase tracking-[0.4em] text-slate-400">
                    GAICD • Executive MBA (AGSM) • CFA Candidate
                </div>
                <div className="text-[10px] font-black uppercase tracking-[0.4em] text-aero-blue">
                    Long Horizon Labs
                </div>
            </footer>
        </div>
    );
}
