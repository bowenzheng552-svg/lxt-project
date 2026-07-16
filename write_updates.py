import os

base = r'C:\Users\JOYY\Documents\Codex\2026-07-14\new-chat-2\orbis-nft\src'
files = {}

# Features.tsx
features_text = '''export default function Features() {
  const features = [
    {
      title: "\u591a\u5143\u670d\u52a1\u5e73\u53f0\u6821\u5185\u5e02\u573a\u84dd\u6d77",
      subtitle: "",
      desc: "\u6821\u5185\u591a\u5143\u670d\u52a1\u5e73\u53f0\u5728\u5404\u9ad8\u6821\u7f3a\u4e4f\u6574\u5408\u5e73\u53f0\uff0c\u73b0\u9636\u6bb5\u6838\u5fc3\u4ea7\u54c1\u666e\u901a\u8bdd\u6559\u57f9\u5728\u5404\u6821\u5b58\u5728\u9700\u6c42\u5e02\u573a\u3002\u9ad8\u6821\u5e02\u573a\u51c6\u5165\u58c1\u5792\u4f7f\u6821\u56ed\u5de5\u4f5c\u5ba4\u80fd\u6781\u5927\u964d\u4f4e\u6821\u5916\u7ade\u4e89\u54c1\u7ade\u4e89\u538b\u529b",
    },
    {
      title: "agent \u667a\u80fd\u5de5\u4f5c\u6d41\u8f85\u52a9",
      subtitle: "",
      desc: "\u6211\u4eec\u5229\u7528AI\u5de5\u5177\u8f85\u4f50\u6211\u4eec\u5b8c\u6210\u4ece\u9879\u76ee\u8bfe\u7a0b\u79d1\u5b66\u6027\u8bbe\u7f6e\uff0c\u8fd0\u8425\u56fe\u6587\u65b9\u6848\u8bbe\u8ba1\u4e0e\u6267\u884c\uff0c\u98ce\u63a7\u548c\u6536\u76ca\u6a21\u578b\u62df\u5b9a\uff0c\u9500\u552e\u548c\u793e\u7fa4\u642d\u5efa\u5168\u6d41\u7a0b\u5404\u677f\u5757\u5efa\u9020\uff0c\u56e2\u961f\u90e8\u5206\u6838\u5fc3\u677f\u5757\u5de5\u4f5c\u6d41\u501f\u9274OPC\u6a21\u5f0f",
    },
    {
      title: "\u5b9a\u4ef7\u4e0e\u6210\u5458\u4f18\u52bf",
      subtitle: "",
      desc: "\u6211\u4eec\u7684\u6838\u5fc3\u4ea7\u54c1\uff0c\u666e\u901a\u8bdd\u6559\u57f9\u4ea7\u54c1\uff0c\u8bb2\u5e08\u5747\u4e3a\u4e00\u4e59\u53ca\u4ee5\u4e0a\u5e08\u8d44\uff0c\u4f46\u5747\u4e3a\u5927\u5b66\u751f\u7fa4\u4f53\uff0c\u4fdd\u8bc1\u9ad8\u6548\u6c9f\u901a\u7684\u540c\u65f6\u4ef7\u683c\u5177\u6709\u6781\u5927\u4f18\u52bf\u3002\u6838\u5fc3\u9879\u76ee\u7ec4\u6210\u5458\u5747\u5177\u5907\u56fd\u8d5b\u7ecf\u9a8c\uff0c\u9879\u76ee\u7ba1\u7406\u4e0e\u5199\u4f5c\u7ecf\u9a8c\u4e30\u5bcc",
    },
  ];

  return (
    <section className="relative w-full bg-bg-dark py-16 sm:py-20 md:py-24">
      <div className="max-w-[1831px] mx-auto w-full px-4 sm:px-6 md:px-10 lg:px-12">
        <div className="lg:ml-32 mb-12 lg:mb-16">
          <h2 className="font-yahei font-bold text-[28px] sm:text-[34px] md:text-[42px] lg:text-[52px] text-cream leading-none m-0">
            \u9879\u76ee\u7ec4\u6838\u5fc3\u7ade\u4e89\u529b
          </h2>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {features.map((f, i) => (
            <div key={i} className="liquid-glass rounded-[32px] p-8 sm:p-10 transition-colors duration-200 hover:bg-white/10">
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

# NftCard.tsx - add modal
nftcard_text = '''import { useEffect, useRef, useState } from "react";
import { ChevronRight, X } from "lucide-react";

interface NftCardProps {
  videoUrl: string;
  title: string;
  subtitle: string;
  articleText: string;
}

export default function NftCard({ videoUrl, title, subtitle, articleText }: NftCardProps) {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

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
    <>
      <div className="liquid-glass rounded-[32px] p-[18px] transition-colors duration-200 hover:bg-white/10">
        <div className="relative w-full pb-[100%] rounded-[24px] overflow-hidden">
          <video
            ref={videoRef}
            className="absolute inset-0 w-full h-full object-cover"
            src={videoUrl}
            autoPlay
            loop
            muted
            playsInline
          />
        </div>
        <div className="liquid-glass rounded-[20px] px-5 py-4 mt-3 flex items-center justify-between min-h-[72px]">
          <div className="flex-1 min-w-0">
            <p className="text-[12px] sm:text-[13px] text-cream font-mono uppercase m-0 leading-tight">{title}</p>
            <p className="text-[15px] sm:text-[16px] text-neon font-grotesk m-0 mt-1 leading-none">{subtitle}</p>
          </div>
          <button
            onClick={() => setIsModalOpen(true)}
            className="w-12 h-12 rounded-full bg-gradient-to-br from-[#b724ff] to-[#7c3aed] flex items-center justify-center shadow-lg shadow-purple-500/50 transition-transform duration-200 hover:scale-110 cursor-pointer border-none flex-shrink-0 ml-3"
          >
            <ChevronRight size={20} className="text-white" />
          </button>
        </div>
      </div>

      {/* Modal Overlay */}
      {isModalOpen && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center p-4"
          onClick={() => setIsModalOpen(false)}
        >
          <div className="absolute inset-0 bg-black/60" />
          <div
            className="relative liquid-glass rounded-[24px] p-6 sm:p-8 max-w-[560px] w-full max-h-[75vh] overflow-y-auto"
            onClick={(e) => e.stopPropagation()}
          >
            <button
              onClick={() => setIsModalOpen(false)}
              className="absolute top-4 right-4 w-8 h-8 flex items-center justify-center text-cream/50 hover:text-cream transition-colors cursor-pointer border-none bg-transparent"
            >
              <X size={18} />
            </button>
            <p className="font-yahei text-[14px] sm:text-[15px] text-cream/90 leading-relaxed m-0 pr-6">
              {articleText}
            </p>
          </div>
        </div>
      )}
    </>
  );
}
'''
files[os.path.join(base, 'components', 'NftCard.tsx')] = nftcard_text

# NftCollection.tsx - add articleText to each card
nftcol_text = '''import NftCard from "./NftCard";

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
          <div className="lg:ml-32">
            <h2 className="font-grotesk uppercase text-[32px] sm:text-[40px] md:text-[50px] lg:text-[60px] text-cream leading-none m-0">
              see what we did!
            </h2>
          </div>
          <div className="lg:mr-12 flex-shrink-0">
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
          </div>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {nfts.map((nft, i) => (
            <NftCard key={i} videoUrl={nft.videoUrl} title={nft.title} subtitle={nft.subtitle} articleText={nft.articleText} />
          ))}
        </div>
      </div>
    </section>
  );
}
'''
files[os.path.join(base, 'components', 'NftCollection.tsx')] = nftcol_text

# App.tsx - remove Community
app_text = '''import Hero from "./components/Hero";
import About from "./components/About";
import NftCollection from "./components/NftCollection";
import Features from "./components/Features";
import Roadmap from "./components/Roadmap";
import CtaSection from "./components/CtaSection";
import TextureOverlay from "./components/TextureOverlay";

export default function App() {
  return (
    <>
      <TextureOverlay />
      <main className="relative min-h-screen">
        <Hero />
        <About />
        <NftCollection />
        <Features />
        <Roadmap />
        <CtaSection />
      </main>
    </>
  );
}
'''
files[os.path.join(base, 'App.tsx')] = app_text

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Written: {os.path.basename(path)}')
print('Done')
