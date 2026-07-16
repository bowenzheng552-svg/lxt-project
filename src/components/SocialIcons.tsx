import { Mail, X } from "lucide-react";

export function SocialIconsVertical() {
  return (
    <div className="hidden lg:flex flex-col absolute top-24 right-4 xl:right-8 gap-3 z-20">
      <a
        href="#"
        className="liquid-glass w-14 h-14 rounded-[1rem] flex items-center justify-center text-cream transition-colors duration-200 hover:bg-white/10 no-underline"
        aria-label="Mail"
      >
        <Mail size={20} />
      </a>
      <a
        href="#"
        className="liquid-glass w-14 h-14 rounded-[1rem] flex items-center justify-center text-cream transition-colors duration-200 hover:bg-white/10 no-underline"
        aria-label="Twitter"
      >
        <X size={20} />
      </a>
      <a
        href="#"
        className="liquid-glass w-14 h-14 rounded-[1rem] flex items-center justify-center text-cream transition-colors duration-200 hover:bg-white/10 no-underline"
        aria-label="Github"
      >
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4" />
        </svg>
      </a>
    </div>
  );
}

export function SocialIconsHorizontal() {
  return (
    <div className="flex lg:hidden justify-center gap-3 mt-6">
      <a
        href="#"
        className="liquid-glass w-14 h-14 rounded-[1rem] flex items-center justify-center text-cream transition-colors duration-200 hover:bg-white/10 no-underline"
        aria-label="Mail"
      >
        <Mail size={20} />
      </a>
      <a
        href="#"
        className="liquid-glass w-14 h-14 rounded-[1rem] flex items-center justify-center text-cream transition-colors duration-200 hover:bg-white/10 no-underline"
        aria-label="Twitter"
      >
        <X size={20} />
      </a>
      <a
        href="#"
        className="liquid-glass w-14 h-14 rounded-[1rem] flex items-center justify-center text-cream transition-colors duration-200 hover:bg-white/10 no-underline"
        aria-label="Github"
      >
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4" />
        </svg>
      </a>
    </div>
  );
}
