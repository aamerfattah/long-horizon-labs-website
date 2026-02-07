export default function PrinciplesPage() {
    const principles = [
        {
            title: "Long-term strategic focus",
            description: "Priority is given to outcomes over 10, 20, and 30-year horizons. Short-term noise is filtered to maintain strategic signal."
        },
        {
            title: "Outcome-focused metrics",
            description: "Benchmarks are secondary; member and capital outcomes are primary. Measurements focus on real-world sufficiency at the point of need."
        },
        {
            title: "Responsible technical design",
            description: "Technology serves governance rather than bypassing it. Tools are designed for explainability and rigorous human oversight."
        },
        {
            title: "Decision-grade analytics",
            description: "Information provided consists of decision-grade insights rather than raw data. Metrics must clarify strategic choices."
        },
        {
            title: "Governance by design",
            description: "Traceability, auditability, and ethical constraints are inherent to the architectures from the outset."
        }
    ];

    return (
        <div className="max-w-6xl mx-auto px-6 py-24 md:py-48 space-y-48">
            <header className="space-y-10 max-w-3xl">
                <div className="h-1.5 w-16 bg-aero-blue" />
                <h1 className="text-7xl md:text-8xl font-black tracking-tighter leading-none text-midnight">Principles</h1>
                <p className="text-2xl text-slate-custom font-medium leading-relaxed tracking-tight">
                    Baseline belief systems that guide technical design and strategic judgment within the Long Horizon Labs framework.
                </p>
            </header>

            <div className="space-y-24">
                {principles.map((principle, i) => (
                    <div key={i} className="editorial-grid group">
                        <div className="col-span-full md:col-span-4 border-l-4 border-slate-100 group-hover:border-aero-blue pl-8 transition-colors py-4">
                            <h2 className="text-3xl font-black tracking-tight text-midnight leading-tight">{principle.title}</h2>
                        </div>
                        <div className="col-span-full md:col-span-8 pt-4 md:pt-4">
                            <p className="text-xl text-slate-custom font-semibold leading-relaxed tracking-tight">
                                {principle.description}
                            </p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}
