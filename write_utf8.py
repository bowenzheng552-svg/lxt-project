import os

base = r'C:\Users\JOYY\Documents\Codex\2026-07-14\new-chat-2\orbis-nft\src'

files = {}

# index.css
files[os.path.join(base, 'index.css')] = '''@import "tailwindcss";

@theme {
  --color-bg-dark: #010828;
  --color-cream: #eff4ff;
  --color-neon: #6fff00;
  --font-grotesk: "Anton", sans-serif;
  --font-condiment: "Condiment", cursive;
  --font-yahei: "Microsoft YaHei", "\\u5fae\\u8f6f\\u96c5\\u9ed1", sans-serif;
}

.liquid-glass {
  background: rgba(255, 255, 255, 0.01);
  background-blend-mode: luminosity;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  border: none;
  box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.1);
  position: relative;
  overflow: hidden;
}
.liquid-glass::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1.4px;
  background: linear-gradient(
    180deg,
    rgba(255, 255, 255, 0.45) 0%,
    rgba(255, 255, 255, 0.15) 20%,
    rgba(255, 255, 255, 0) 40%,
    rgba(255, 255, 255, 0) 60%,
    rgba(255, 255, 255, 0.15) 80%,
    rgba(255, 255, 255, 0.45) 100%
  );
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

.texture-overlay {
  position: fixed;
  inset: 0;
  z-index: 50;
  pointer-events: none;
  background-image: url("/texture.png");
  background-size: cover;
  background-position: center;
  mix-blend-mode: lighten;
  opacity: 0.08;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  padding: 0;
  background-color: #010828;
  color: #eff4ff;
  font-family: monospace, ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Microsoft YaHei", "\\u5fae\\u8f6f\\u96c5\\u9ed1", monospace;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}
'''

# About.tsx
about_content = '''import { useEffect, useRef } from "react";

export default function About() {
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

  const introText =
    "\u9675\u6821\u901a\u5927\u5b66\u751f\u591a\u5143\u670d\u52a1\u7a7a\u95f4\uff082026.6\uff09\u662f\u7531\u4ee5\u90d1\u535a\u6587\u7275\u5934\u7684\u9ad8\u6821\u4e3b\u521b\u56e2\u961f\u8bbe\u7acb\u7684\u9762\u5411\u5357\u4eac\u9ad8\u6821\u5927\u5b66\u751f\u7fa4\u4f53\u7684\u591a\u5143\u670d\u52a1\u5e73\u53f0";

  const teamText1 =
    "\u73b0\u5728LXT\u5de5\u4f5c\u5ba4\u4e00\u5171\u7531\u6559\u7814\u7ec4\uff0c\u8fd0\u8425\u7ec4\uff0c\u7814\u53d1\u7ec4\u7b497\u4e2a\u5c0f\u7ec4\u5171\u5341\u4e09\u4f4d\u5c0f\u4f19\u4f34\u7ec4\u6210\uff0c\u4e3b\u8981\u4e3a\u9675\u6821\u901a\u5357\u4eac\u7ebf\u4e0a\u666e\u901a\u8bdd\u6559\u57f9\uff0c\u7ebf\u4e0a\u7ebf\u4e0b\u914d\u97f3\u517c\u804c\uff0c\u5927\u5b66\u751f\u6821\u5185\u7535\u53f0\u4e09\u5927\u6a21\u5757\u63d0\u4f9b\u9879\u76ee\u8fd0\u8425\u548c\u5f00\u53d1\u7ba1\u7406\u3002";

  const teamText2 =
    "LXT\u5de5\u4f5c\u5c0f\u661f\u7403\u5df2\u7ecf\u5b8c\u6210\u5185\u90e8\u5de5\u4f5c\u6d41\u548c\u77e5\u8bc6\u5e93\u7684\u642d\u5efa\u5de5\u7a0b\uff0c\u7b7e\u7ea6\u5357\u4eac\u4fdd\u7814\u8003\u7814\u5408\u4f5c\u673a\u6784\u4e00\u6240\uff0c\u7b7e\u7ea6\u5927\u578b\u914d\u97f3\u516c\u53f8\u8fdb\u884c\u4e2d\uff0c\u5b8c\u6210\u516c\u4f17\u53f7\u670d\u52a1\u53f7\u7b49\u8fd0\u8425\u5411\u7ebf\u6761\u7684\u81ea\u52a8\u5316\uff0c\u534a\u81ea\u52a8\u5316agent skill\u6d41\u7a0b\u642d\u5efa\uff0c\u5bf9\u6807\u4e8c\u7ebf\u58f0\u97f3\u5de5\u4f5c\u5ba4\u548c\u5b66\u751f\u793e\u7fa4\u670d\u52a1\u4ea7\u54c1\u4ee5B\u7aef\u9879\u76ee\u670d\u52a1\u4e3a\u4e3b\u6253\u9020\u4e3b\u529b\u4ea7\u54c1";

  return (
    <section className="relative w-full min-h-screen overflow-hidden">
      <video
        ref={videoRef}
        className="absolute inset-0 w-full h-full object-cover"
        src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260331_151551_992053d1-3d3e-4b8c-abac-45f22158f411.mp4"
        autoPlay
        loop
        muted
        playsInline
      />
      <div className="absolute inset-0 bg-black/30" />
      <div className="relative z-10 flex flex-col justify-center min-h-screen max-w-[1831px] mx-auto w-full px-4 sm:px-6 md:px-10 lg:px-12 py-16 sm:py-20 md:py-24">
        <div className="flex flex-col lg:flex-row lg:items-start lg:justify-between gap-8 lg:gap-16">
          <div className="relative lg:ml-32 flex-shrink-0">
            <h2 className="font-grotesk uppercase text-[32px] sm:text-[40px] md:text-[50px] lg:text-[60px] text-cream leading-none m-0">
              about us:
            </h2>
          </div>
          <div className="lg:mr-12 max-w-[400px]">
            <p className="font-yahei text-[14px] sm:text-[15px] leading-relaxed text-cream m-0">
              {introText}
            </p>
          </div>
        </div>
        <div className="flex flex-row justify-between mt-16 sm:mt-20 lg:mt-24">
          <div className="flex flex-col gap-8 max-w-[450px]">
            <p className="font-yahei text-[13px] sm:text-[14px] leading-relaxed text-cream m-0">
              {teamText1}
            </p>
            <p className="font-yahei text-[13px] sm:text-[14px] leading-relaxed text-cream m-0">
              {teamText2}
            </p>
          </div>
          <div className="hidden lg:block w-[400px]" />
        </div>
      </div>
    </section>
  );
}
'''
files[os.path.join(base, 'components', 'About.tsx')] = about_content

# NftCollection.tsx
nft_content = '''import NftCard from "./NftCard";

const nfts = [
  {
    videoUrl:
      "https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260331_053923_22c0a6a5-313c-474c-85ff-3b50d25e944a.mp4",
    title: "lxt\\u666e\\u901a\\u8bdd\\u6559\\u57f9\\u5de5\\u4f5c\\u5ba4",
    subtitle: "26/6",
  },
  {
    videoUrl:
      "https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260331_054411_511c1b7a-fb2f-42ef-bf6c-32c0b1a06e79.mp4",
    title: "\\u201c\\u63a2\\u6e90\\u5c0f\\u52a9\\u624b\\u201dhhu\\u5fae\\u9898\\u5e93\\uff0c\\u201c\\u4e91\\u9732\\u6668\\u9891\\u201d\\u6821\\u5185ai\\u7535\\u53f0 \\u5c0f\\u7a0b\\u5e8f",
    subtitle: "26/7",
  },
  {
    videoUrl:
      "https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260331_055427_ac7035b5-9f3b-4289-86fc-941b2432317d.mp4",
    title: "\\u8a00\\u5c7b\\u201c\\u914d\\u97f3\\u517c\\u804c\\u63a5\\u5355\\u5e73\\u53f0",
    subtitle: "26/7",
  },
];

export default function NftCollection() {
  return (
    <section className="relative w-full bg-bg-dark py-16 sm:py-20 md:py-24">
      <div className="max-w-[1831px] mx-auto w-full px-4 sm:px-6 md:px-10 lg:px-12">
        <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-8 mb-12 lg:mb-16">
          <div className="lg:ml-32">
            <h2 className="font-grotesk uppercase text-[32px] sm:text-[40px] md:text-[50px] lg:text-[60px] text-cream leading-none m-0">
              see what we did!
            </h2>
          </div>
          <div className="lg:mr-12 flex-shrink-0">
            <div className="inline-block">
              <div className="flex items-start gap-1">
                <span className="font-grotesk uppercase text-[32px] sm:text-[40px] md:text-[50px] lg:text-[60px] text-cream leading-none">
                  SEE
                </span>
                <div className="flex flex-col">
                  <span className="font-grotesk uppercase text-[20px] sm:text-[24px] md:text-[30px] lg:text-[36px] text-cream leading-none">
                    ALL
                  </span>
                  <span className="font-grotesk uppercase text-[20px] sm:text-[24px] md:text-[30px] lg:text-[36px] text-cream leading-none">
                    PROJECTS
                  </span>
                </div>
              </div>
              <div className="bg-neon h-[6px] sm:h-[8px] lg:h-[10px] w-full mt-1" />
            </div>
          </div>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {nfts.map((nft, i) => (
            <NftCard key={i} videoUrl={nft.videoUrl} title={nft.title} subtitle={nft.subtitle} />
          ))}
        </div>
      </div>
    </section>
  );
}
'''
files[os.path.join(base, 'components', 'NftCollection.tsx')] = nft_content

# CtaSection.tsx
cta_content = '''import { useEffect, useRef } from "react";
import { Mail, X } from "lucide-react";

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

  const ctaText = "\\u60f3\\u83b7\\u5f97\\u66f4\\u591a\\u9879\\u76ee\\u7ecf\\u5386\\uff1f\\u60f3\\u6210\\u4e3a\\u56e2\\u961f\\u9879\\u76ee\\u7275\\u5934\\u4eba\\uff1f\\u627e\\u4e0d\\u5230\\u5730\\u65b9\\u65bd\\u5c55\\u4f60\\u7684\\u65e0\\u5c3d\\u624d\\u534e\\uff1fLXT\\u6b22\\u8fce\\u60a8\\u7684\\u52a0\\u5165\\uff01";

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
          <span className="font-condiment text-neon text-[17px] sm:text-[24px] md:text-[40px] lg:text-[68px] absolute -top-8 sm:-top-12 lg:-top-16 right-4 lg:right-[20%] rotate-1 mix-blend-exclusion whitespace-nowrap">
            Go beyond
          </span>
          <div className="text-right">
            <p className="font-grotesk uppercase text-[16px] sm:text-[24px] md:text-[40px] lg:text-[60px] text-cream leading-tight m-0 mb-4 lg:mb-8">
              JOIN US.
            </p>
            <p className="font-yahei text-[12px] sm:text-[15px] md:text-[20px] lg:text-[26px] text-cream leading-relaxed m-0 mb-4 lg:mb-6 max-w-[700px] ml-auto">
              {ctaText}
            </p>
            <p className="font-grotesk uppercase text-[16px] sm:text-[24px] md:text-[40px] lg:text-[60px] text-cream leading-tight m-0">
              DEFINE WHAT\\'S NEXT.
            </p>
            <p className="font-grotesk uppercase text-[16px] sm:text-[24px] md:text-[40px] lg:text-[60px] text-cream leading-tight m-0">
              FOLLOW THE SIGNAL.
            </p>
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
'''
files[os.path.join(base, 'components', 'CtaSection.tsx')] = cta_content

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Written: {os.path.basename(path)}')
print('Done')
