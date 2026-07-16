import { useEffect, useRef } from "react";
import { Mail, X } from "lucide-react";
import Reveal from "./Reveal";
import DecryptedText from "./DecryptedText";

export default function CtaSection() {
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

  const ctaText = "\u60f3\u83b7\u5f97\u66f4\u591a\u9879\u76ee\u7ecf\u5386\uff1f\u60f3\u6210\u4e3a\u56e2\u961f\u9879\u76ee\u7275\u5934\u4eba\uff1f\u627e\u4e0d\u5230\u5730\u65b9\u65bd\u5c55\u4f60\u7684\u65e0\u5c3d\u624d\u534e\uff1fLXT\u6b22\u8fce\u60a8\u7684\u52a0\u5165\uff01";

  return (
    <section className="relative w-full overflow-hidden bg-bg-dark">
      <video
        ref={videoRef}
        className="w-full h-auto block"
        src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260331_055729_72d66327-b59e-4ae9-bb70-de6ccb5ecdb0.mp4"
        autoPlay
        loop
        muted
        playsInline
      />
      <div className="absolute inset-0 flex items-center justify-center">
        <div className="relative lg:pr-[20%] lg:pl-[15%] w-full max-w-[1831px] mx-auto px-4 sm:px-6 md:px-10">
          <Reveal animation="fade-in" delay={0.1}>
            <span className="font-condiment text-neon text-[17px] sm:text-[24px] md:text-[40px] lg:text-[68px] absolute -top-8 sm:-top-12 lg:-top-16 right-4 lg:right-[20%] rotate-1 mix-blend-exclusion whitespace-nowrap">
              Go beyond
            </span>
          </Reveal>
          <div className="text-right">
            <Reveal delay={0.2}>
              <p className="font-grotesk uppercase text-[16px] sm:text-[24px] md:text-[40px] lg:text-[60px] text-cream leading-tight m-0 mb-4 lg:mb-8">
                <DecryptedText text="JOIN US." animateOn="view" />
              </p>
            </Reveal>
            <Reveal delay={0.4}>
              <p className="font-yahei text-[12px] sm:text-[15px] md:text-[20px] lg:text-[26px] text-cream leading-relaxed m-0 mb-4 lg:mb-6 max-w-[700px] ml-auto">
                {ctaText}
              </p>
            </Reveal>
            <Reveal delay={0.6}>
              <p className="font-grotesk uppercase text-[16px] sm:text-[24px] md:text-[40px] lg:text-[60px] text-cream leading-tight m-0">
                <DecryptedText text="DEFINE WHAT'S NEXT." animateOn="view" />
              </p>
            </Reveal>
           <Reveal delay={0.8}>
             <p className="font-grotesk uppercase text-[16px] sm:text-[24px] md:text-[40px] lg:text-[60px] text-cream leading-tight m-0">
               <DecryptedText text="FOLLOW THE SIGNAL." animateOn="view" />
             </p>
           </Reveal>
            <Reveal delay={1.0}>
              <p className="font-yahei text-[12px] sm:text-[14px] md:text-[18px] lg:text-[22px] text-cream/80 leading-relaxed m-0 mt-6 max-w-[700px] ml-auto">
                发送简历邮件&作品集&加盟意向文件至：zbw202311111@qq.com
              </p>
            </Reveal>
          </div>
        </div>
      </div>
      <div className="absolute left-[8%] bottom-[12%] lg:bottom-[20%] z-10">
        <div className="liquid-glass rounded-[0.5rem] lg:rounded-[1.25rem] inline-flex flex-col">
          <a href="#" className="flex items-center justify-center no-underline text-cream transition-colors duration-200 hover:bg-white/10 w-[14vw] sm:w-[14.375rem] md:w-[10.78125rem] lg:w-[16.77rem] h-[14vw] sm:h-[14.375rem] md:h-[10.78125rem] lg:h-[16.77rem] border-b border-white/10" aria-label="Mail"><Mail size={20} /></a>
          <a href="#" className="flex items-center justify-center no-underline text-cream transition-colors duration-200 hover:bg-white/10 w-[14vw] sm:w-[14.375rem] md:w-[10.78125rem] lg:w-[16.77rem] h-[14vw] sm:h-[14.375rem] md:h-[10.78125rem] lg:h-[16.77rem] border-b border-white/10" aria-label="Twitter"><X size={20} /></a>
          <a href="#" className="flex items-center justify-center no-underline text-cream transition-colors duration-200 hover:bg-white/10 w-[14vw] sm:w-[14.375rem] md:w-[10.78125rem] lg:w-[16.77rem] h-[14vw] sm:h-[14.375rem] md:h-[10.78125rem] lg:h-[16.77rem]" aria-label="Github">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4" /></svg>
          </a>
        </div>
      </div>
    </section>
  );
}
