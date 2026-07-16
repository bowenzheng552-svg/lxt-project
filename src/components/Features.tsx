import Reveal from "./Reveal";
import DecryptedText from "./DecryptedText";

export default function Features() {
  const features = [
    {
      title: "多元服务平台校内市场蓝海",
      desc: "校内多元服务平台在各高校缺乏整合平台，现阶段核心产品普通话教培在各校存在需求市场。高校市场准入壁垒使校园工作室能极大降低校外竞争品竞争压力",
    },
    {
      title: "agent 智能工作流辅助",
      desc: "我们利用AI工具辅佐我们完成从项目课程科学性设置，运营图文方案设计与执行，风控和收益模型拟定，销售和社群搭建全流程各板块建造，团队部分核心板块工作流借鉴OPC模式",
    },
    {
      title: "定价与成员优势",
      desc: "我们的核心产品，普通话教培产品，讲师均为一乙及以上师资，但均为大学生群体，保证高效沟通的同时价格具有极大优势。核心项目组成员均具备国赛经验，项目管理与写作经验丰富",
    },
  ];

  return (
    <section className="relative w-full bg-bg-dark py-16 sm:py-20 md:py-24">
      <div className="max-w-[1831px] mx-auto w-full px-4 sm:px-6 md:px-10 lg:px-12">
        <Reveal className="lg:ml-32 mb-12 lg:mb-16" as="div" delay={0.1}>
          <h2 className="font-yahei font-bold text-[28px] sm:text-[34px] md:text-[42px] lg:text-[52px] text-cream leading-none m-0">
            <DecryptedText text="项目组核心竞争力" animateOn="view" />
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
