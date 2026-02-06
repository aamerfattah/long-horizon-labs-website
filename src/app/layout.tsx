import type { Metadata } from "next";
import { Outfit } from "next/font/google";
import "./globals.css";
import { Navbar } from "@/components/Navbar";
import { LayoutWrapper } from "@/components/LayoutWrapper";

const outfit = Outfit({
  variable: "--font-sans",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Long Horizon Labs | Open Tools for Capital & Risk",
  description: "Minimalist, high-signal artifacts at the intersection of capital markets, retirement systems, and systemic risk.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${outfit.variable} antialiased selection:bg-slate-900/10 bg-white text-slate-900`}
      >
        <LayoutWrapper>
          {children}
        </LayoutWrapper>
      </body>
    </html>
  );
}
