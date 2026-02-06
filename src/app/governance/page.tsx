export default function GovernancePage() {
    return (
        <div className="max-w-6xl mx-auto px-6 py-24 md:py-48 space-y-48">
            <header className="space-y-10 max-w-3xl">
                <div className="h-1.5 w-16 bg-aero-blue" />
                <h1 className="text-7xl md:text-8xl font-black tracking-tighter leading-none text-midnight">Governance</h1>
                <p className="text-2xl text-slate-custom font-medium leading-relaxed tracking-tight">
                    Open source and ethical standards for long horizon decision tools.
                </p>
            </header>

            <section className="editorial-grid">
                <div className="col-span-full md:col-span-4 self-start">
                    <h2 className="text-sm font-black uppercase tracking-[0.3em] text-aero-blue">Licensing</h2>
                </div>
                <div className="col-span-full md:col-span-8 space-y-10">
                    <p className="text-2xl text-midnight font-bold leading-relaxed tracking-tight">
                        All code developed under Long Horizon Labs is released under the MIT License. We believe that the tools required for systemic risk assessment and long term capital management should be transparent, auditable, and accessible to the global financial community.
                    </p>
                </div>
            </section>

            <section className="editorial-grid">
                <div className="col-span-full md:col-span-4 self-start">
                    <h2 className="text-sm font-black uppercase tracking-[0.3em] text-aero-blue">Ethical Use</h2>
                </div>
                <div className="col-span-full md:col-span-8 space-y-12">
                    <p className="text-xl text-slate-custom font-medium leading-relaxed">
                        Our tools are designed to model long term outcomes and systemic risks. They are not intended for short term speculation, market manipulation, or the automation of decisions without human in the loop oversight.
                    </p>
                    <div className="p-16 bg-cream rounded-[48px] border border-slate-100 shadow-premium space-y-8">
                        <h3 className="text-xs font-black uppercase tracking-[0.4em] text-midnight">Accountability Standard</h3>
                        <p className="text-2xl text-midnight font-bold leading-tight tracking-tight text-balance">
                            Users of Long Horizon Labs tools bear full responsibility for the results of their models. Our software is provided as is, and we emphasize the importance of rigorous stress testing and external verification of any strategic judgment derived from these tools.
                        </p>
                    </div>
                </div>
            </section>

            <section className="editorial-grid">
                <div className="col-span-full md:col-span-4 self-start">
                    <h2 className="text-sm font-black uppercase tracking-[0.3em] text-aero-blue">Contribution</h2>
                </div>
                <div className="col-span-full md:col-span-8 space-y-10">
                    <p className="text-2xl text-midnight font-bold leading-relaxed tracking-tight">
                        We welcome contributions that align with our core principles of clarity, restraint, and high signal output. We prioritize pull requests that improve documentation, add robust testing, or simplify existing code over those that introduce new complexity.
                    </p>
                </div>
            </section>
        </div>
    );
}
