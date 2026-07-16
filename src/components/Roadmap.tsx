import Reveal from "./Reveal";
import DecryptedText from "./DecryptedText";

export default function Roadmap() {
  const milestones = [
    { phase: "GENESIS", title: "Phase One", date: "Q3 2026", desc: "组建项目团队，主项目方向选定与市场需求调研" },
    { phase: "EXPANSION", title: "Phase Two", date: "Q4 2026", desc: "明确各线条负责方向，多线条多项目开工，和合作方取得连接，联系商会创业项目助学导师" },
    { phase: "CONVERGENCE", title: "Phase Three", date: "Q1 2027", desc: "搭建内部工作流与知识库，多平台宣传公众号搭建，启动小助手，咨询完善社群引导流程，利用coding与codex开源附属产品，宣传线条形成稳定自动化工作流" },
    { phase: "ASCENSION", title: "Phase Four", date: "Q2 2027", desc: "我们在努力中的：更多的加盟合作方向与项目成员，在多平台创立多IP引流，附属产品带动主力产品的推广与品牌宣传裂变" },
  ];

  return (
    <section className="relative w-full bg-bg-dark py-16 sm:py-20 md:py-24 overflow-hidden">
      <div className="max-w-[1831px] mx-auto w-full px-4 sm:px-6 md:px-10 lg:px-12">
        <Reveal className="relative mb-16 lg:mb-20" as="div" delay={0.1}>
          <div className="lg:ml-32">
            <h2 className="font-grotesk uppercase text-[32px] sm:text-[40px] md:text-[50px] lg:text-[60px] text-cream leading-none m-0">
              <DecryptedText text="The Path" animateOn="view" />
            </h2>
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
