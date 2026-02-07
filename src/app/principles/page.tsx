export default function PrinciplesPage() {
    const principles = [
        {
            title: "Long term strategic thinking",
            description: "I focus on outcomes that matter over 10, 20, and 30 year horizons. I deliberately filter short term noise to maintain strategic signal."
        },
        {
            title: "Outcome focused metrics",
            description: "Benchmarks are secondary; member and capital outcomes are primary. I measure what affects real world sufficiency at the point of need."
        },
        {
            title: "Responsible technical design",
            description: "I believe technology should serve governance, not bypass it. Every tool I build is designed for explainability and rigorous human oversight."
        },
        {
            title: "Decision grade analytics",
            description: "I do not provide just raw data; I provide decision grade insights. If a metric does not clarify a strategic choice, I consider it noise."
        },
        {
            title: "Governance by design",
            description: "Traceability, auditability, and ethical constraints are built into my architectures, not added as a reactive afterthought."
        }
    ];

    return (
        <div className="max-w-6xl mx-auto px-6 py-24 md:py-48 space-y-48">
            <header className="space-y-10 max-w-3xl">
                <div className="h-1.5 w-16 bg-aero-blue" />
                <h1 className="text-7xl md:text-8xl font-black tracking-tighter leading-none text-midnight">Principles</h1>
                <p className="text-2xl text-slate-custom font-medium leading-relaxed tracking-tight">
                    The foundational beliefs that guide my technical design and strategic judgment.
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
