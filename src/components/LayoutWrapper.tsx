"use client";

import { useState, useEffect } from "react";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";
import { Navbar } from "./Navbar";
import Link from "next/link";

export function LayoutWrapper({ children }: { children: React.ReactNode }) {
    const pathname = usePathname();
    const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

    // Close mobile menu on route change
    useEffect(() => {
        setIsMobileMenuOpen(false);
    }, [pathname]);

    return (
        <div className="flex min-h-screen bg-cream selection:bg-aero-blue/10">
            <div className="flex-1 min-h-screen flex flex-col">
                <Navbar onMenuClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)} isSidebarVisible={false} />
                <main className="flex-1 mt-24">
                    {children}
                </main>
            </div>

            {/* Mobile Menu Overlay */}
            {isMobileMenuOpen && (
                <div
                    className="fixed inset-0 bg-white z-50 flex flex-col items-center justify-center space-y-12 p-12 transition-all animate-in fade-in zoom-in-95 duration-300"
                >
                    <button
                        onClick={() => setIsMobileMenuOpen(false)}
                        className="absolute top-12 right-12 p-4 text-midnight hover:bg-slate-50 rounded-full transition-colors"
                    >
                        <svg className="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" /></svg>
                    </button>
                    <Link href="/" onClick={() => setIsMobileMenuOpen(false)} className="text-5xl font-black text-midnight tracking-tighter hover:text-aero-blue transition-colors">Home</Link>
                    <Link href="/projects" onClick={() => setIsMobileMenuOpen(false)} className="text-5xl font-black text-midnight tracking-tighter hover:text-aero-blue transition-colors">Projects</Link>
                    <Link href="/principles" onClick={() => setIsMobileMenuOpen(false)} className="text-5xl font-black text-midnight tracking-tighter hover:text-aero-blue transition-colors">Principles</Link>
                    <Link href="/about" onClick={() => setIsMobileMenuOpen(false)} className="text-5xl font-black text-midnight tracking-tighter hover:text-aero-blue transition-colors">About</Link>

                    <div className="pt-12">
                        <Link href="https://github.com/aamerfattah" target="_blank" className="text-xs font-black uppercase tracking-[0.4em] text-aero-blue border-b-2 border-aero-blue pb-2">Institutional GitHub</Link>
                    </div>
                </div>
            )}
        </div>
    );
}
