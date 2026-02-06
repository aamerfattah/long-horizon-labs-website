export default function PrinciplesPage() {
    const principles = [
        {
            title: "Long term strategic thinking",
            description: "We focus on outcomes that matter over 10, 20, and 30 year horizons. Short term noise is deliberately filtered to maintain signal."
        },
        {
            title: "Outcome focused metrics",
            description: "Benchmarks are secondary; member and capital outcomes are primary. We measure what affects real world sufficiency at the point of need."
        },
        {
            title: "Responsible technical design",
            description: "Technology should serve governance, not bypass it. Every tool we build is designed for explainability and rigorous human oversight."
        },
        {
            title: "Decision grade analytics",
            description: "We do not provide just raw data; we provide decision grade insights. If it does not clarify a strategic choice, it is noise."
        },
        {
            title: "Governance by design",
            description: "Traceability, auditability, and ethical constraints are built into the architecture, not added as a reactive afterthought."
        }
    ];

    return (
        <div className="max-w-6xl mx-auto px-6 py-24 md:py-48 space-y-48">
            <header className="space-y-10 max-w-3xl">
                <div className="h-1.5 w-16 bg-aero-blue" />
                <h1 className="text-7xl md:text-8xl font-black tracking-tighter leading-none text-midnight">Principles</h1>
                <p className="text-2xl text-slate-custom font-medium leading-relaxed tracking-tight">
                    The foundational beliefs that guide our technical design and strategic judgment.
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
