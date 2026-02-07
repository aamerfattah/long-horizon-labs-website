"use client";

import Link from "next/link";
import { ArrowLeft, Compass } from "lucide-react";
import { motion } from "framer-motion";

export default function NotFound() {
    return (
        <div className="min-h-screen bg-cream flex items-center justify-center p-6">
            <div className="max-w-2xl w-full text-center space-y-12">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="space-y-6"
                >
                    <div className="w-20 h-20 bg-midnight rounded-3xl flex items-center justify-center mx-auto shadow-premium text-aero-blue">
                        <Compass className="w-10 h-10" />
                    </div>
                    <div className="space-y-2">
                        <h1 className="text-6xl md:text-8xl font-black tracking-tighter text-midnight leading-none">404</h1>
                        <h2 className="text-2xl font-black uppercase tracking-[0.4em] text-aero-blue">Route Not Found</h2>
                    </div>
                    <p className="text-xl text-slate-custom font-medium leading-relaxed max-w-md mx-auto">
                        The technical entry or deep-dive artifact requested does not exist on this server.
                    </p>
                </motion.div>

                <Link
                    href="/"
                    className="inline-flex items-center gap-3 text-xs font-black uppercase tracking-widest text-white bg-midnight px-10 py-5 rounded-full hover:bg-aero-blue transition-all shadow-premium group"
                >
                    <ArrowLeft className="w-4 h-4 group-hover:-translate-x-1 transition-transform" /> Return to Base
                </Link>
            </div>
        </div>
    );
}
