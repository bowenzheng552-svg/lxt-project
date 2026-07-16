import os

base = r'C:\Users\JOYY\Documents\Codex\2026-07-14\new-chat-2\orbis-nft\src'
files = {}

# Hero.tsx - larger fonts
files[os.path.join(base, 'components', 'Hero.tsx')] = '''import { useEffect, useRef } from "react";
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
            <h1 className="font-grotesk uppercase leading-tight text-[40px] sm:text-[50px] md:text-[60px] lg:text-[72px] text-cream m-0">
              Greetings from the
              <br />
              LXT Project Team.
            </h1>
            <p className="font-grotesk uppercase leading-tight text-[30px] sm:text-[36px] md:text-[44px] lg:text-[52px] text-cream mt-6 m-0">
              Let\\'s begin our exploration!
            </p>
          </div>
        </div>
        <SocialIconsVertical />
        <div className="pb-12">
          <SocialIconsHorizontal />
        </div>
      </div>
    </section>
  );
}
'''

# About.tsx - fonts larger, bottom LXT art text
about_text = '''import { useEffect, useRef } from "react";

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
        <div className="flex flex-row justify-between mt-20 sm:mt-24 lg:mt-32">
          <div className="flex flex-col gap-10 max-w-[500px]">
            <p className="font-yahei text-[15px] sm:text-[16px] leading-relaxed text-cream m-0">
              {teamText1}
            </p>
            <p className="font-yahei text-[15px] sm:text-[16px] leading-relaxed text-cream m-0">
              {teamText2}
            </p>
          </div>
          <div className="hidden lg:block w-[400px]" />
        </div>

        {/* LXT gradient art text */}
        <div className="relative mt-20 sm:mt-28 lg:mt-36 text-center select-none">
          <div className="text-[100px] sm:text-[160px] md:text-[220px] lg:text-[300px] font-bold leading-none tracking-[0.3em] lxt-gradient">
            LXT
          </div>
        </div>
      </div>
    </section>
  );
}
'''
files[os.path.join(base, 'components', 'About.tsx')] = about_text

# Features.tsx - all Chinese content
features_text = '''export default function Features() {
  const features = [
    {
      title: "\u573a\u666f\u4fe1\u4efb\u7684\u533a\u57df\u4f18\u52bf",
      subtitle: "",
      desc: "\u5168\u7a0b\u6821\u5185\u6388\u8bfe\uff0c\u7075\u6d3b\u5339\u914d\u5b66\u751f\u665a\u81ea\u4e60\u3001\u5468\u672b\u65f6\u95f4\uff0c\u4f9d\u9760\u5b66\u751f\u5708\u5c42\u53e3\u7891\u88c2\u53d8\u83b7\u5ba2\uff0c\u6613\u83b7\u53d6\u5b66\u751f\u4fe1\u4efb",
    },
    {
      title: "agent \u667a\u80fd\u5de5\u4f5c\u6d41\u8f85\u52a9",
      subtitle: "",
      desc: "\u6211\u4eec\u5229\u7528AI\u5de5\u5177\u8f85\u4f50\u6211\u4eec\u5b8c\u6210\u4ece\u9879\u76ee\u8bfe\u7a0b\u79d1\u5b66\u6027\u8bbe\u7f6e\uff0c\u8fd0\u8425\u56fe\u6587\u65b9\u6848\u8bbe\u8ba1\u4e0e\u6267\u884c\uff0c\u98ce\u63a7\u548c\u6536\u76ca\u6a21\u578b\u62df\u5b9a\uff0c\u9500\u552e\u548c\u793e\u7fa4\u642d\u5efa\u5168\u6d41\u7a0b\u5404\u677f\u5757\u5efa\u9020\uff0c\u56e2\u961f\u90e8\u5206\u6838\u5fc3\u677f\u5757\u5de5\u4f5c\u6d41\u501f\u9274OPC\u6a21\u5f0f",
    },
    {
      title: "\u5b9a\u4ef7\u4f18\u52bf",
      subtitle: "",
      desc: "\u6211\u4eec\u7684\u6838\u5fc3\u4ea7\u54c1\uff0c\u666e\u901a\u8bdd\u6559\u57f9\u4ea7\u54c1\uff0c\u8bb2\u5e08\u5747\u4e3a\u4e00\u4e59\u53ca\u4ee5\u4e0a\u5e08\u8d44\uff0c\u4f46\u5747\u4e3a\u5927\u5b66\u751f\u7fa4\u4f53\uff0c\u4fdd\u8bc1\u9ad8\u6548\u6c9f\u901a\u7684\u540c\u65f6\u4ef7\u683c\u5177\u6709\u6781\u5927\u4f18\u52bf",
    },
  ];

  return (
    <section className="relative w-full bg-bg-dark py-16 sm:py-20 md:py-24">
      <div className="max-w-[1831px] mx-auto w-full px-4 sm:px-6 md:px-10 lg:px-12">
        {/* Heading */}
        <div className="lg:ml-32 mb-12 lg:mb-16">
          <h2 className="font-yahei font-bold text-[28px] sm:text-[34px] md:text-[42px] lg:text-[52px] text-cream leading-none m-0">
            \u9879\u76ee\u7ec4\u6838\u5fc3\u7ade\u4e89\u529b
          </h2>
        </div>

        {/* Feature Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {features.map((f, i) => (
            <div
              key={i}
              className="liquid-glass rounded-[32px] p-8 sm:p-10 transition-colors duration-200 hover:bg-white/10"
            >
              <h3 className="font-yahei font-bold text-[22px] sm:text-[26px] text-cream leading-tight m-0">
                {f.title}
              </h3>
              <div className="bg-neon h-[6px] sm:h-[8px] w-16 mt-4 mb-6" />
              <p className="font-yahei text-[13px] sm:text-[14px] text-cream/80 leading-relaxed m-0">
                {f.desc}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
'''
files[os.path.join(base, 'components', 'Features.tsx')] = features_text

# Roadmap.tsx - Chinese descriptions
roadmap_text = '''export default function Roadmap() {
  const milestones = [
    {
      phase: "GENESIS",
      title: "Phase One",
      date: "Q3 2026",
      desc: "\u7ec4\u5efa\u9879\u76ee\u56e2\u961f\uff0c\u4e3b\u9879\u76ee\u65b9\u5411\u9009\u5b9a\u4e0e\u5e02\u573a\u9700\u6c42\u8c03\u7814",
    },
    {
      phase: "EXPANSION",
      title: "Phase Two",
      date: "Q4 2026",
      desc: "\u660e\u786e\u5404\u7ebf\u6761\u8d1f\u8d23\u65b9\u5411\uff0c\u591a\u7ebf\u6761\u591a\u9879\u76ee\u5f00\u5de5\uff0c\u548c\u5408\u4f5c\u65b9\u53d6\u5f97\u8fde\u63a5\uff0c\u8054\u7cfb\u5546\u4f1a\u521b\u4e1a\u9879\u76ee\u52a9\u5b66\u5bfc\u5e08",
    },
    {
      phase: "CONVERGENCE",
      title: "Phase Three",
      date: "Q1 2027",
      desc: "\u642d\u5efa\u5185\u90e8\u5de5\u4f5c\u6d41\u4e0e\u77e5\u8bc6\u5e93\uff0c\u591a\u5e73\u53f0\u5ba3\u4f20\u516c\u4f17\u53f7\u642d\u5efa\uff0c\u542f\u52a8\u5c0f\u52a9\u624b\uff0c\u54a8\u8be2\u5b8c\u5584\u793e\u7fa4\u5f15\u5bfc\u6d41\u7a0b\uff0c\u5229\u7528coding\u4e0ecodex\u5f00\u6e90\u9644\u5c5e\u4ea7\u54c1\uff0c\u5ba3\u4f20\u7ebf\u6761\u5f62\u6210\u7a33\u5b9a\u81ea\u52a8\u5316\u5de5\u4f5c\u6d41",
    },
    {
      phase: "ASCENSION",
      title: "Phase Four",
      date: "Q2 2027",
      desc: "\u6211\u4eec\u5728\u52aa\u529b\u4e2d\u7684\uff1a\u66f4\u591a\u7684\u52a0\u76df\u5408\u4f5c\u65b9\u5411\u4e0e\u9879\u76ee\u6210\u5458\uff0c\u5728\u591a\u5e73\u53f0\u521b\u7acb\u591aIP\u5f15\u6d41\uff0c\u9644\u5c5e\u4ea7\u54c1\u5e26\u52a8\u4e3b\u529b\u4ea7\u54c1\u7684\u63a8\u5e7f\u4e0e\u54c1\u724c\u5ba3\u4f20\u88c2\u53d8",
    },
  ];

  return (
    <section className="relative w-full bg-bg-dark py-16 sm:py-20 md:py-24 overflow-hidden">
      <div className="max-w-[1831px] mx-auto w-full px-4 sm:px-6 md:px-10 lg:px-12">
        {/* Heading */}
        <div className="relative mb-16 lg:mb-20">
          <div className="lg:ml-32">
            <h2 className="font-grotesk uppercase text-[32px] sm:text-[40px] md:text-[50px] lg:text-[60px] text-cream leading-none m-0">
              The Path
            </h2>
            <span className="font-condiment text-neon text-[36px] sm:text-[44px] md:text-[56px] lg:text-[68px] absolute right-4 lg:right-[15%] top-0 -rotate-1 mix-blend-exclusion whitespace-nowrap">
              Forward
            </span>
          </div>
        </div>

        {/* Timeline */}
        <div className="relative lg:ml-32">
          {/* Vertical line */}
          <div className="absolute left-3 md:left-4 top-0 bottom-0 w-[2px] bg-neon/30" />

          {milestones.map((m, i) => (
            <div key={i} className="relative pl-10 md:pl-14 pb-14 md:pb-16 last:pb-0">
              {/* Dot on timeline */}
              <div className="absolute left-[7px] md:left-[11px] top-1 w-[10px] h-[10px] md:w-[14px] md:h-[14px] rounded-full bg-neon shadow-[0_0_12px_rgba(111,255,0,0.5)]" />

              {/* Card */}
              <div className="liquid-glass rounded-[24px] p-6 sm:p-8 max-w-[650px] transition-colors duration-200 hover:bg-white/10">
                <div className="flex items-center gap-3 mb-3">
                  <span className="font-grotesk text-[11px] uppercase text-neon tracking-widest">
                    {m.phase}
                  </span>
                  <span className="text-cream/40 text-[11px] font-mono">
                    {m.date}
                  </span>
                </div>
                <h3 className="font-grotesk uppercase text-[20px] sm:text-[24px] text-cream leading-none m-0 mb-3">
                  {m.title}
                </h3>
                <p className="font-yahei text-[13px] sm:text-[14px] text-cream/80 leading-relaxed m-0">
                  {m.desc}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
'''
files[os.path.join(base, 'components', 'Roadmap.tsx')] = roadmap_text

# Also update index.css with LXT gradient class
css_path = os.path.join(base, 'index.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

gradient_class = '''
.lxt-gradient {
  background: linear-gradient(to top, rgba(239, 244, 255, 0.9), rgba(239, 244, 255, 0));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 900;
  line-height: 1;
  letter-spacing: 0.3em;
  user-select: none;
}
'''

if '.lxt-gradient' not in css_content:
    # Insert before the last closing brace
    idx = css_content.rfind('}')
    if idx >= 0:
        css_content = css_content[:idx] + gradient_class + '\n' + css_content[idx:]

files[css_path] = css_content

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Written: {os.path.basename(path)}')
print('Done')
