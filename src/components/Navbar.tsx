"use client";

import Link from "next/link";
import { Menu, X } from "lucide-react";
import { useState } from "react";
import { cn } from "@/lib/utils";

export function Navbar({ onMenuClick, isSidebarVisible }: { onMenuClick: () => void; isSidebarVisible: boolean }) {
    return (
        <header className={cn(
            "fixed top-0 right-0 left-0 h-24 bg-white/70 backdrop-blur-xl z-40 px-6 md:px-12 flex items-center justify-between transition-all duration-500",
            isSidebarVisible ? "lg:left-64" : ""
        )}>
            <div className="flex items-center gap-12">
                <Link href="/" className="font-black text-2xl tracking-tighter text-midnight hover:text-aero-blue transition-colors">
                    Long Horizon Labs
                </Link>

                <nav className="hidden md:flex items-center gap-10">
                    <Link href="/projects" className="text-[11px] font-black text-slate-custom hover:text-midnight uppercase tracking-[0.25em] transition-all">
                        Projects
                    </Link>
                    <Link href="/principles" className="text-[11px] font-black text-slate-custom hover:text-midnight uppercase tracking-[0.25em] transition-all">
                        Principles
                    </Link>
                    <Link href="/about" className="text-[11px] font-black text-slate-custom hover:text-midnight uppercase tracking-[0.25em] transition-all">
                        About
                    </Link>
                </nav>
            </div>

            <div className="flex items-center gap-8">
                <Link
                    href="https://github.com/aamerfattah"
                    target="_blank"
                    className="hidden md:block text-[11px] font-black text-midnight uppercase tracking-[0.25em] border-b-2 border-midnight pb-1 hover:border-aero-blue hover:text-aero-blue transition-all"
                >
                    GitHub
                </Link>
                <button
                    onClick={onMenuClick}
                    className="p-3 text-midnight lg:hidden hover:bg-slate-100 rounded-full transition-colors"
                >
                    <Menu className="w-6 h-6" />
                </button>
            </div>
        </header>
    );
}
