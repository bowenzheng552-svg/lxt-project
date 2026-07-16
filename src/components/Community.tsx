import DecryptedText from "./DecryptedText";
export default function Community() {
  const stats = [
    { value: "1,024", label: "Objects Minted" },
    { value: "847", label: "Collectors" },
    { value: "12", label: "Events Hosted" },
  ];

  return (
    <section className="relative w-full bg-bg-dark py-16 sm:py-20 md:py-24">
      <div className="max-w-[1831px] mx-auto w-full px-4 sm:px-6 md:px-10 lg:px-12">
        {/* Stats Row */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 mb-16 lg:mb-20">
          {stats.map((s, i) => (
            <div
              key={i}
              className="liquid-glass rounded-[24px] p-6 sm:p-8 text-center transition-colors duration-200 hover:bg-white/10"
            >
              <p className="font-grotesk text-[36px] sm:text-[44px] md:text-[52px] text-neon leading-none m-0 mb-2">
                {s.value}
              </p>
              <p className="font-mono text-[13px] sm:text-[14px] text-cream/70 uppercase m-0">
                {s.label}
              </p>
            </div>
          ))}
        </div>

        {/* CTA Content */}
        <div className="lg:ml-32 max-w-[700px]">
         <h2 className="font-grotesk uppercase text-[32px] sm:text-[40px] md:text-[50px] lg:text-[60px] text-cream leading-[1.05] m-0">
            <DecryptedText text="Become a" animateOn="view" />
            <br />
            <DecryptedText text="signal seeker" animateOn="view" />
          </h2>

          <div className="relative inline-block mt-4 mb-8">
            <span className="font-condiment text-neon text-[36px] sm:text-[44px] md:text-[56px] lg:text-[68px] absolute -top-2 -right-6 rotate-2 mix-blend-exclusion whitespace-nowrap">
              Join now
            </span>
            <div className="bg-neon h-[6px] sm:h-[8px] lg:h-[10px] w-32 mt-2" />
          </div>

          <p className="font-mono text-[13px] sm:text-[14px] text-cream/70 uppercase leading-relaxed m-0 max-w-[480px]">
            Early access to new drops, spatial experiences, and exclusive community signals.
          </p>

          {/* Email input */}
          <div className="flex flex-col sm:flex-row gap-3 mt-8 max-w-[500px]">
            <input
              type="email"
              placeholder="ENTER YOUR SIGNAL"
              className="flex-1 bg-white/5 border border-white/10 rounded-[12px] px-5 py-3 font-mono text-[13px] text-cream uppercase placeholder:text-cream/20 outline-none focus:border-neon/50 transition-colors"
            />
            <button className="font-grotesk text-[13px] uppercase text-bg-dark bg-neon rounded-[12px] px-6 py-3 cursor-pointer border-none transition-all duration-200 hover:bg-neon/80 hover:shadow-[0_0_20px_rgba(111,255,0,0.3)] whitespace-nowrap">
              Subscribe
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}

