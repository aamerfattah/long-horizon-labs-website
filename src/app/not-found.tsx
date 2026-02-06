import Link from 'next/link'

export default function NotFound() {
    return (
        <div className="min-h-[60vh] flex flex-col items-center justify-center space-y-6 text-center">
            <div className="space-y-2">
                <h2 className="text-4xl font-bold text-gradient">404 - Dashboard Not Found</h2>
                <p className="text-slate-400">The deep tech segment or dashboard you are looking for does not exist.</p>
            </div>
            <Link
                href="/"
                className="px-6 py-3 rounded-xl bg-quantum-blue text-white font-bold hover:shadow-quantum-lg transition-all"
            >
                Return to Overview
            </Link>
        </div>
    )
}
