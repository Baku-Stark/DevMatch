import type React from "react";

interface SectionContainerProps {
  children: React.ReactNode
}

export default function SectionContainer({ children }: SectionContainerProps) {
  return (
    <section className="grid grid-cols-1 gap-4 px-6 py-8">
      {children}
    </section>
  );
}