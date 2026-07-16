import { useEffect, useRef, useState } from "react";
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
