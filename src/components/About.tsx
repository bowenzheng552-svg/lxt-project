import { useEffect, useRef } from "react";
import Reveal from "./Reveal";
import DecryptedText from "./DecryptedText";

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
    "陵校通大学生多元服务空间（2026.6）是由以郑博文牵头的高校主创团队设立的面向南京高校大学生群体的多元服务平台";

  const teamText1 =
    "现在LXT工作室一共由教研组，运营组，研发组等7个小组共十三位小伙伴组成，主要为陵校通南京线上普通话教培，线上线下配音兼职，大学生校内电台三大模块提供项目运营和开发管理。";

  const teamText2 =
    "LXT工作小星球已经完成内部工作流和知识库的搭建工程，签约南京保研考研合作机构一所，签约大型配音公司进行中，完成公众号服务号等运营向线条的自动化，半自动化agent skill流程搭建，对标二线声音工作室和学生社群服务产品以B端项目服务为主打造主力产品";

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
              <DecryptedText text="about us:" animateOn="view" />
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
