"use client";

import { motion } from "framer-motion";
import { cn } from "@/lib/utils";

export function Logo({ className, iconOnly = false }: { className?: string, iconOnly?: boolean }) {
    return (
        <div className={cn("flex items-center gap-3 group select-none", className)}>
            <div className="relative">
                {/* Animated Background Glow */}
                <motion.div
                    animate={{
                        scale: [1, 1.2, 1],
                        opacity: [0.5, 0.8, 0.5],
                    }}
                    transition={{
                        duration: 4,
                        repeat: Infinity,
                        ease: "easeInOut"
                    }}
                    className="absolute inset-0 bg-quantum-blue/20 blur-xl rounded-full"
                />

                {/* Logo Icon */}
                <div className="relative w-10 h-10 rounded-xl bg-slate-900 flex items-center justify-center overflow-hidden shadow-2xl shadow-quantum-blue/20 border border-slate-800">
                    {/* Geometric shapes inside */}
                    <div className="absolute inset-0 bg-gradient-to-br from-quantum-blue via-transparent to-quantum-purple opacity-20" />

                    <svg
                        viewBox="0 0 24 24"
                        fill="none"
                        className="w-6 h-6 text-white relative z-10"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <motion.path
                            initial={{ pathLength: 0 }}
                            animate={{ pathLength: 1 }}
                            transition={{ duration: 1.5, ease: "easeInOut" }}
                            d="M12 3L4 7.5V16.5L12 21L20 16.5V7.5L12 3Z"
                            stroke="currentColor"
                            strokeWidth="2"
                            strokeLinecap="round"
                            strokeLinejoin="round"
                        />
                        <motion.path
                            initial={{ opacity: 0, scale: 0.5 }}
                            animate={{ opacity: 1, scale: 1 }}
                            transition={{ delay: 0.5, duration: 0.5 }}
                            d="M12 8V16M8 12H16"
                            stroke="currentColor"
                            strokeWidth="2"
                            strokeLinecap="round"
                        />
                    </svg>

                    {/* Shimmer effect */}
                    <motion.div
                        animate={{
                            x: ["-100%", "200%"]
                        }}
                        transition={{
                            duration: 3,
                            repeat: Infinity,
                            ease: "linear",
                            delay: 1
                        }}
                        className="absolute top-0 bottom-0 w-1/2 bg-gradient-to-r from-transparent via-white/10 to-transparent skew-x-12"
                    />
                </div>
            </div>

            {!iconOnly && (
                <div className="flex flex-col -space-y-1">
                    <span className="text-xl font-black tracking-tighter text-slate-900 group-hover:text-quantum-blue transition-colors">
                        DeepTech<span className="text-quantum-blue text-sm ml-0.5">IQ</span>
                    </span>
                    <span className="text-[8px] font-bold text-slate-400 uppercase tracking-[0.3em] pl-0.5">
                        Institutional intelligence
                    </span>
                </div>
            )}
        </div>
    );
}
