path = r"C:\Users\JOYY\Documents\Codex\2026-07-14\new-chat-2\orbis-nft\src\components\Hero.tsx"

content = """import { useEffect, useRef } from "react";
import Navbar from "./Navbar";
import ASCIIText from "./ASCIIText";
import { SocialIconsVertical, SocialIconsHorizontal } from "./SocialIcons";

export default function Hero() {
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    const video = videoRef.current;
    if (!video) return;
    video.play().catch(() => {
      const handleInteraction = () => {
        video.play();
        document.removeEventListener("click", handleInteraction);
        document.removeEventListener("touchstart", handleInteraction);
      };
      document.addEventListener("click", handleInteraction);
      document.addEventListener("touchstart", handleInteraction);
    });
  }, []);

  return (
    <section className="relative w-full h-screen overflow-hidden rounded-b-[32px]">
      <video
        ref={videoRef}
        className="absolute inset-0 w-full h-full object-cover"
        src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260331_045634_e1c98c76-1265-4f5c-882a-4276f2080894.mp4"
        autoPlay
        loop
        muted
        playsInline
      />
      <div className="absolute inset-0 bg-black/30" />
      <div className="relative z-10 flex flex-col h-full">
        <Navbar />
        <div className="flex-1 flex flex-col justify-center max-w-[1831px] mx-auto w-full px-4 sm:px-6 md:px-10 lg:px-12">
          <div className="lg:ml-32 w-full h-[180px] sm:h-[220px] md:h-[260px] relative">
            <ASCIIText
              text="Greetings from the LXT Project Team"
              enableWaves={true}
              asciiFontSize={8}
              textFontSize={160}
              textColor="#EFF4FF"
              planeBaseHeight={5}
            />
          </div>
          <p className="font-grotesk uppercase leading-tight text-[20px] sm:text-[26px] md:text-[32px] lg:text-[38px] text-cream mt-1 lg:ml-32 m-0 animate-fade-in-up animate-delay-5">
            Let\\'s begin our exploration!
          </p>
        </div>
        <div className="animate-fade-in animate-delay-5">
          <SocialIconsVertical />
        </div>
        <div className="pb-12 animate-fade-in animate-delay-6">
          <SocialIconsHorizontal />
        </div>
      </div>
    </section>
  );
}
"""

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Hero.tsx written')
