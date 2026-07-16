import os

base = r'C:\Users\JOYY\Documents\Codex\2026-07-14\new-chat-2\orbis-nft\src'
comp = os.path.join(base, 'components')
files = {}

# ============ index.css ============
css_path = os.path.join(base, 'index.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

anim_css = '''
/* ===== Entrance Animations ===== */
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(36px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}
@keyframes scale-in {
  from { opacity: 0; transform: scale(0.88); }
  to { opacity: 1; transform: scale(1); }
}

.animate-fade-in-up {
  animation: fade-in-up 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
.animate-fade-in {
  animation: fade-in 0.6s ease-out forwards;
}
.animate-scale-in {
  animation: scale-in 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
.animate-delay-1  { animation-delay: 0.1s; }
.animate-delay-2  { animation-delay: 0.2s; }
.animate-delay-3  { animation-delay: 0.3s; }
.animate-delay-4  { animation-delay: 0.4s; }
.animate-delay-5  { animation-delay: 0.5s; }
.animate-delay-6  { animation-delay: 0.6s; }
.animate-delay-7  { animation-delay: 0.7s; }
.animate-delay-8  { animation-delay: 0.8s; }
.animate-delay-10 { animation-delay: 1.0s; }

/* Opacity hidden for scroll-reveal */
.opacity-hidden {
  opacity: 0;
  transform: translateY(20px);
  transition: none;
}
'''

if '@keyframes fade-in-up' not in css:
    idx = css.rfind('}')
    if idx >= 0:
        css = css[:idx] + anim_css + '\n' + css[idx:]
files[css_path] = css

# ============ Reveal.tsx ============
reveal_tsx = '''import { useEffect, useRef, useState } from "react";

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

  return (
    <Tag
      ref={ref}
      className={${className}}
      style={visible ? { animationDelay: delay + "s" } : undefined}
    >
      {children}
    </Tag>
  );
}
'''
files[os.path.join(comp, 'Reveal.tsx')] = reveal_tsx

# ============ Hero.tsx ============
hero_tsx = '''import { useEffect, useRef } from "react";
import Navbar from "./Navbar";
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
        <div className="flex-1 flex items-center max-w-[1831px] mx-auto w-full px-4 sm:px-6 md:px-10 lg:px-12">
          <div className="lg:ml-32 max-w-[800px]">
            <h1 className="font-grotesk uppercase leading-tight text-[40px] sm:text-[50px] md:text-[60px] lg:text-[72px] text-cream m-0 animate-fade-in-up animate-delay-1">
              Greetings from the
              <br />
              LXT Project Team.
            </h1>
            <p className="font-grotesk uppercase leading-tight text-[30px] sm:text-[36px] md:text-[44px] lg:text-[52px] text-cream mt-6 m-0 animate-fade-in-up animate-delay-3">
              Let\\'s begin our exploration!
            </p>
          </div>
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
'''
files[os.path.join(comp, 'Hero.tsx')] = hero_tsx

# ============ About.tsx ============
about_tsx = '''import { useEffect, useRef } from "react";
import Reveal from "./Reveal";

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
          <Reveal className="relative lg:ml-32 flex-shrink-0" as="div" delay={0.1}>
            <h2 className="font-grotesk uppercase text-[32px] sm:text-[40px] md:text-[50px] lg:text-[60px] text-cream leading-none m-0">
              about us:
            </h2>
          </Reveal>
          <Reveal className="lg:mr-12 max-w-[400px]" as="div" delay={0.3}>
            <p className="font-yahei text-[14px] sm:text-[15px] leading-relaxed text-cream m-0">
              {introText}
            </p>
          </Reveal>
        </div>
        <div className="flex flex-row justify-between mt-20 sm:mt-24 lg:mt-32">
          <div className="flex flex-col gap-10 max-w-[500px]">
            <Reveal delay={0.2}>
              <p className="font-yahei text-[15px] sm:text-[16px] leading-relaxed text-cream m-0">{teamText1}</p>
            </Reveal>
            <Reveal delay={0.4}>
              <p className="font-yahei text-[15px] sm:text-[16px] leading-relaxed text-cream m-0">{teamText2}</p>
            </Reveal>
          </div>
          <div className="hidden lg:block w-[400px]" />
        </div>

        <Reveal animation="fade-in" delay={0.3}>
          <div className="relative mt-20 sm:mt-28 lg:mt-36 text-center select-none">
            <div className="text-[100px] sm:text-[160px] md:text-[220px] lg:text-[300px] font-bold leading-none tracking-[0.3em] lxt-gradient">
              LXT
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
'''
files[os.path.join(comp, 'About.tsx')] = about_tsx

# ============ NftCollection.tsx ============
nftcol_tsx = '''import NftCard from "./NftCard";
import Reveal from "./Reveal";

const nfts = [
  {
    videoUrl:
      "https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260331_053923_22c0a6a5-313c-474c-85ff-3b50d25e944a.mp4",
    title: "lxt\\u666e\\u901a\\u8bdd\\u6559\\u57f9\\u5de5\\u4f5c\\u5ba4",
    subtitle: "26/6",
    articleText: "2026\\u5e746\\u81f37\\u6708\\u4ee5\\u6cb3\\u6d77\\u5927\\u5b66\\u6c5f\\u5b81\\u6821\\u533a\\u4e3a\\u9996\\u4e2a\\u8bd5\\u70b9\\uff0c\\u6838\\u5fc3\\u4e1a\\u52a1\\u9762\\u5411\\u5728\\u6821\\u5927\\u5b66\\u751f\\u5f00\\u8bbe\\u666e\\u901a\\u8bdd\\u4e8c\\u7532\\u51b2\\u523a\\u5c0f\\u73ed\\u3001\\u4e00\\u5bf9\\u4e00\\u7ea0\\u97f3\\u8f85\\u5bfc\\uff0c\\u5c0f\\u73ed\\u9488\\u5bf9\\u6027\\u8f85\\u5bfc\\u548c\\u966a\\u7ec3\\uff0c\\u586b\\u8865\\u6821\\u5185\\u666e\\u901a\\u8bdd\\u57f9\\u8bad\\u5e02\\u573a\\u7a7a\\u767d\\u3002\\u65d7\\u4e0b\\u8a00\\u5c7b\\u5de5\\u4f5c\\u5ba4\\u4e3b\\u8981\\u627f\\u63a5\\u914d\\u97f3\\u4e1a\\u52a1\\u3002\\u56e2\\u961f\\u4e2d\\u6709\\u6559\\u7814\\u4eba\\u5458\\uff0c\\u8fd0\\u8425\\u4eba\\u5458\\uff0c\\u914d\\u97f3\\u4e13\\u5458",
  },
  {
    videoUrl:
      "https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260331_054411_511c1b7a-fb2f-42ef-bf6c-32c0b1a06e79.mp4",
    title: "\\u201c\\u63a2\\u6e90\\u5c0f\\u52a9\\u624b\\u201dhhu\\u5fae\\u9898\\u5e93\\uff0c\\u201c\\u4e91\\u9732\\u6668\\u9891\\u201d\\u6821\\u5185ai\\u7535\\u53f0 \\u5c0f\\u7a0b\\u5e8f",
    subtitle: "26/7",
    articleText: "\\u63a2\\u6e90\\u5c0f\\u7a0b\\u5e8f\\u5b9a\\u4f4d\\u662f\\u4e00\\u6b3e\\u9488\\u5bf9\\u6cb3\\u6d77\\u6821\\u5185\\u7684\\u9898\\u5e93\\u7a0b\\u5e8f\\uff0c\\u6c47\\u603b\\u5404\\u5b66\\u79d1\\u9898\\u5e93\\u4e0e\\u8d44\\u6599\\uff0c\\u5e2e\\u52a9LXT\\u9879\\u76ee\\u6253\\u5f00\\u5e02\\u573a\\u4e0e\\u5efa\\u7acb\\u6821\\u5185\\u793e\\u7fa4\\uff0c\\u5bfb\\u627e\\u9700\\u6c42\\u7528\\u6237\\u3002",
  },
  {
    videoUrl:
      "https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260331_055427_ac7035b5-9f3b-4289-86fc-941b2432317d.mp4",
    title: "\\u8a00\\u5c7b\\u201c\\u914d\\u97f3\\u517c\\u804c\\u63a5\\u5355\\u5e73\\u53f0",
    subtitle: "26/7",
    articleText: "\\u8a00\\u5c7b\\u662f\\u9762\\u5411LXT\\u5185\\u90e8\\u6559\\u5458\\u8bbe\\u7f6e\\u7684\\u5357\\u4eac\\u5927\\u5b66\\u751f\\u914d\\u97f3\\u517c\\u804c\\u5e73\\u53f0\\uff0c\\u4e3a\\u6821\\u5185\\u6559\\u5458\\u63d0\\u4f9b\\u989d\\u5916\\u7684\\u8d44\\u91d1\\u652f\\u6301\\uff0c\\u5e76\\u5411\\u5404\\u9700\\u6c42\\u4f01\\u4e1a\\u63d0\\u4f9b\\u9ad8\\u8d28\\u91cf\\u4e14\\u5b9e\\u60e0\\u7684\\u914d\\u97f3\\u4fee\\u97f3\\u670d\\u52a1",
  },
];

export default function NftCollection() {
  return (
    <section className="relative w-full bg-bg-dark py-16 sm:py-20 md:py-24">
      <div className="max-w-[1831px] mx-auto w-full px-4 sm:px-6 md:px-10 lg:px-12">
        <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-8 mb-12 lg:mb-16">
          <Reveal className="lg:ml-32" as="div" delay={0.1}>
            <h2 className="font-grotesk uppercase text-[32px] sm:text-[40px] md:text-[50px] lg:text-[60px] text-cream leading-none m-0">
              see what we did!
            </h2>
          </Reveal>
          <Reveal className="lg:mr-12 flex-shrink-0" as="div" delay={0.3} animation="fade-in">
            <div className="inline-block">
              <div className="flex items-start gap-1">
                <span className="font-grotesk uppercase text-[32px] sm:text-[40px] md:text-[50px] lg:text-[60px] text-cream leading-none">SEE</span>
                <div className="flex flex-col">
                  <span className="font-grotesk uppercase text-[20px] sm:text-[24px] md:text-[30px] lg:text-[36px] text-cream leading-none">ALL</span>
                  <span className="font-grotesk uppercase text-[20px] sm:text-[24px] md:text-[30px] lg:text-[36px] text-cream leading-none">PROJECTS</span>
                </div>
              </div>
              <div className="bg-neon h-[6px] sm:h-[8px] lg:h-[10px] w-full mt-1" />
            </div>
          </Reveal>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {nfts.map((nft, i) => (
            <Reveal key={i} animation="scale-in" delay={0.1 + i * 0.15}>
              <NftCard videoUrl={nft.videoUrl} title={nft.title} subtitle={nft.subtitle} articleText={nft.articleText} />
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
'''
files[os.path.join(comp, 'NftCollection.tsx')] = nftcol_tsx

# ============ Features.tsx ============
features_tsx = '''import Reveal from "./Reveal";

export default function Features() {
  const features = [
    {
      title: "\u591a\u5143\u670d\u52a1\u5e73\u53f0\u6821\u5185\u5e02\u573a\u84dd\u6d77",
      desc: "\u6821\u5185\u591a\u5143\u670d\u52a1\u5e73\u53f0\u5728\u5404\u9ad8\u6821\u7f3a\u4e4f\u6574\u5408\u5e73\u53f0\uff0c\u73b0\u9636\u6bb5\u6838\u5fc3\u4ea7\u54c1\u666e\u901a\u8bdd\u6559\u57f9\u5728\u5404\u6821\u5b58\u5728\u9700\u6c42\u5e02\u573a\u3002\u9ad8\u6821\u5e02\u573a\u51c6\u5165\u58c1\u5792\u4f7f\u6821\u56ed\u5de5\u4f5c\u5ba4\u80fd\u6781\u5927\u964d\u4f4e\u6821\u5916\u7ade\u4e89\u54c1\u7ade\u4e89\u538b\u529b",
    },
    {
      title: "agent \u667a\u80fd\u5de5\u4f5c\u6d41\u8f85\u52a9",
      desc: "\u6211\u4eec\u5229\u7528AI\u5de5\u5177\u8f85\u4f50\u6211\u4eec\u5b8c\u6210\u4ece\u9879\u76ee\u8bfe\u7a0b\u79d1\u5b66\u6027\u8bbe\u7f6e\uff0c\u8fd0\u8425\u56fe\u6587\u65b9\u6848\u8bbe\u8ba1\u4e0e\u6267\u884c\uff0c\u98ce\u63a7\u548c\u6536\u76ca\u6a21\u578b\u62df\u5b9a\uff0c\u9500\u552e\u548c\u793e\u7fa4\u642d\u5efa\u5168\u6d41\u7a0b\u5404\u677f\u5757\u5efa\u9020\uff0c\u56e2\u961f\u90e8\u5206\u6838\u5fc3\u677f\u5757\u5de5\u4f5c\u6d41\u501f\u9274OPC\u6a21\u5f0f",
    },
    {
      title: "\u5b9a\u4ef7\u4e0e\u6210\u5458\u4f18\u52bf",
      desc: "\u6211\u4eec\u7684\u6838\u5fc3\u4ea7\u54c1\uff0c\u666e\u901a\u8bdd\u6559\u57f9\u4ea7\u54c1\uff0c\u8bb2\u5e08\u5747\u4e3a\u4e00\u4e59\u53ca\u4ee5\u4e0a\u5e08\u8d44\uff0c\u4f46\u5747\u4e3a\u5927\u5b66\u751f\u7fa4\u4f53\uff0c\u4fdd\u8bc1\u9ad8\u6548\u6c9f\u901a\u7684\u540c\u65f6\u4ef7\u683c\u5177\u6709\u6781\u5927\u4f18\u52bf\u3002\u6838\u5fc3\u9879\u76ee\u7ec4\u6210\u5458\u5747\u5177\u5907\u56fd\u8d5b\u7ecf\u9a8c\uff0c\u9879\u76ee\u7ba1\u7406\u4e0e\u5199\u4f5c\u7ecf\u9a8c\u4e30\u5bcc",
    },
  ];

  return (
    <section className="relative w-full bg-bg-dark py-16 sm:py-20 md:py-24">
      <div className="max-w-[1831px] mx-auto w-full px-4 sm:px-6 md:px-10 lg:px-12">
        <Reveal className="lg:ml-32 mb-12 lg:mb-16" as="div" delay={0.1}>
          <h2 className="font-yahei font-bold text-[28px] sm:text-[34px] md:text-[42px] lg:text-[52px] text-cream leading-none m-0">
            \u9879\u76ee\u7ec4\u6838\u5fc3\u7ade\u4e89\u529b
          </h2>
        </Reveal>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {features.map((f, i) => (
            <Reveal key={i} animation="scale-in" delay={0.1 + i * 0.15}>
              <div className="liquid-glass rounded-[32px] p-8 sm:p-10 transition-colors duration-200 hover:bg-white/10">
                <h3 className="font-yahei font-bold text-[22px] sm:text-[26px] text-cream leading-tight m-0">{f.title}</h3>
                <div className="bg-neon h-[6px] sm:h-[8px] w-16 mt-4 mb-6" />
                <p className="font-yahei text-[13px] sm:text-[14px] text-cream/80 leading-relaxed m-0">{f.desc}</p>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
'''
files[os.path.join(comp, 'Features.tsx')] = features_tsx

# ============ Roadmap.tsx ============
roadmap_tsx = '''import Reveal from "./Reveal";

export default function Roadmap() {
  const milestones = [
    { phase: "GENESIS", title: "Phase One", date: "Q3 2026", desc: "\u7ec4\u5efa\u9879\u76ee\u56e2\u961f\uff0c\u4e3b\u9879\u76ee\u65b9\u5411\u9009\u5b9a\u4e0e\u5e02\u573a\u9700\u6c42\u8c03\u7814" },
    { phase: "EXPANSION", title: "Phase Two", date: "Q4 2026", desc: "\u660e\u786e\u5404\u7ebf\u6761\u8d1f\u8d23\u65b9\u5411\uff0c\u591a\u7ebf\u6761\u591a\u9879\u76ee\u5f00\u5de5\uff0c\u548c\u5408\u4f5c\u65b9\u53d6\u5f97\u8fde\u63a5\uff0c\u8054\u7cfb\u5546\u4f1a\u521b\u4e1a\u9879\u76ee\u52a9\u5b66\u5bfc\u5e08" },
    { phase: "CONVERGENCE", title: "Phase Three", date: "Q1 2027", desc: "\u642d\u5efa\u5185\u90e8\u5de5\u4f5c\u6d41\u4e0e\u77e5\u8bc6\u5e93\uff0c\u591a\u5e73\u53f0\u5ba3\u4f20\u516c\u4f17\u53f7\u642d\u5efa\uff0c\u542f\u52a8\u5c0f\u52a9\u624b\uff0c\u54a8\u8be2\u5b8c\u5584\u793e\u7fa4\u5f15\u5bfc\u6d41\u7a0b\uff0c\u5229\u7528coding\u4e0ecodex\u5f00\u6e90\u9644\u5c5e\u4ea7\u54c1\uff0c\u5ba3\u4f20\u7ebf\u6761\u5f62\u6210\u7a33\u5b9a\u81ea\u52a8\u5316\u5de5\u4f5c\u6d41" },
    { phase: "ASCENSION", title: "Phase Four", date: "Q2 2027", desc: "\u6211\u4eec\u5728\u52aa\u529b\u4e2d\u7684\uff1a\u66f4\u591a\u7684\u52a0\u76df\u5408\u4f5c\u65b9\u5411\u4e0e\u9879\u76ee\u6210\u5458\uff0c\u5728\u591a\u5e73\u53f0\u521b\u7acb\u591aIP\u5f15\u6d41\uff0c\u9644\u5c5e\u4ea7\u54c1\u5e26\u52a8\u4e3b\u529b\u4ea7\u54c1\u7684\u63a8\u5e7f\u4e0e\u54c1\u724c\u5ba3\u4f20\u88c2\u53d8" },
  ];

  return (
    <section className="relative w-full bg-bg-dark py-16 sm:py-20 md:py-24 overflow-hidden">
      <div className="max-w-[1831px] mx-auto w-full px-4 sm:px-6 md:px-10 lg:px-12">
        <Reveal className="relative mb-16 lg:mb-20" as="div" delay={0.1}>
          <div className="lg:ml-32">
            <h2 className="font-grotesk uppercase text-[32px] sm:text-[40px] md:text-[50px] lg:text-[60px] text-cream leading-none m-0">The Path</h2>
            <span className="font-condiment text-neon text-[36px] sm:text-[44px] md:text-[56px] lg:text-[68px] absolute right-4 lg:right-[15%] top-0 -rotate-1 mix-blend-exclusion whitespace-nowrap">Forward</span>
          </div>
        </Reveal>
        <div className="relative lg:ml-32">
          <Reveal animation="fade-in" delay={0.2}>
            <div className="absolute left-3 md:left-4 top-0 bottom-0 w-[2px] bg-neon/30" />
          </Reveal>
          {milestones.map((m, i) => (
            <Reveal key={i} delay={0.2 + i * 0.15}>
              <div className="relative pl-10 md:pl-14 pb-14 md:pb-16 last:pb-0">
                <div className="absolute left-[7px] md:left-[11px] top-1 w-[10px] h-[10px] md:w-[14px] md:h-[14px] rounded-full bg-neon shadow-[0_0_12px_rgba(111,255,0,0.5)]" />
                <div className="liquid-glass rounded-[24px] p-6 sm:p-8 max-w-[650px] transition-colors duration-200 hover:bg-white/10">
                  <div className="flex items-center gap-3 mb-3">
                    <span className="font-grotesk text-[11px] uppercase text-neon tracking-widest">{m.phase}</span>
                    <span className="text-cream/40 text-[11px] font-mono">{m.date}</span>
                  </div>
                  <h3 className="font-grotesk uppercase text-[20px] sm:text-[24px] text-cream leading-none m-0 mb-3">{m.title}</h3>
                  <p className="font-yahei text-[13px] sm:text-[14px] text-cream/80 leading-relaxed m-0">{m.desc}</p>
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
'''
files[os.path.join(comp, 'Roadmap.tsx')] = roadmap_tsx

# ============ CtaSection.tsx ============
cta_tsx = '''import { useEffect, useRef } from "react";
import { Mail, X } from "lucide-react";
import Reveal from "./Reveal";

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
          <Reveal animation="fade-in" delay={0.1}>
            <span className="font-condiment text-neon text-[17px] sm:text-[24px] md:text-[40px] lg:text-[68px] absolute -top-8 sm:-top-12 lg:-top-16 right-4 lg:right-[20%] rotate-1 mix-blend-exclusion whitespace-nowrap">
              Go beyond
            </span>
          </Reveal>
          <div className="text-right">
            <Reveal delay={0.2}>
              <p className="font-grotesk uppercase text-[16px] sm:text-[24px] md:text-[40px] lg:text-[60px] text-cream leading-tight m-0 mb-4 lg:mb-8">
                JOIN US.
              </p>
            </Reveal>
            <Reveal delay={0.4}>
              <p className="font-yahei text-[12px] sm:text-[15px] md:text-[20px] lg:text-[26px] text-cream leading-relaxed m-0 mb-4 lg:mb-6 max-w-[700px] ml-auto">
                {ctaText}
              </p>
            </Reveal>
            <Reveal delay={0.6}>
              <p className="font-grotesk uppercase text-[16px] sm:text-[24px] md:text-[40px] lg:text-[60px] text-cream leading-tight m-0">
                DEFINE WHAT\\'S NEXT.
              </p>
            </Reveal>
            <Reveal delay={0.8}>
              <p className="font-grotesk uppercase text-[16px] sm:text-[24px] md:text-[40px] lg:text-[60px] text-cream leading-tight m-0">
                FOLLOW THE SIGNAL.
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
'''
files[os.path.join(comp, 'CtaSection.tsx')] = cta_tsx

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Written: {os.path.basename(path)}')
print('Done')
