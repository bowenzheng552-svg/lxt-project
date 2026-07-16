import { useEffect, useRef, useState } from "react";

interface RevealProps {
  children: React.ReactNode;
  className?: string;
  animation?: "fade-in-up" | "fade-in" | "scale-in";
  delay?: number;
  as?: "div" | "section" | "span" | "h2" | "h3" | "p";
}

export default function Reveal({
  children,
  className = "",
  animation = "fade-in-up",
  delay = 0,
  as: Tag = "div",
}: RevealProps) {
  const ref = useRef<HTMLDivElement>(null);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setVisible(true);
          observer.unobserve(el);
        }
      },
      { threshold: 0.1, rootMargin: "0px 0px -40px 0px" }
    );
    observer.observe(el);
    return () => observer.disconnect();
  }, []);

  const animClass = visible ? " animate-" + animation : " opacity-hidden";

  return (
    <Tag
      ref={ref}
      className={className + animClass}
      style={visible ? { animationDelay: delay + "s" } : undefined}
    >
      {children}
    </Tag>
  );
}
