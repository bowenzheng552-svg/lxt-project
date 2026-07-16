import NftCard from "./NftCard";
import Reveal from "./Reveal";
import DecryptedText from "./DecryptedText";

const nfts = [
  {
    videoUrl:
      "https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260331_053923_22c0a6a5-313c-474c-85ff-3b50d25e944a.mp4",
    title: "lxt\u666e\u901a\u8bdd\u6559\u57f9\u5de5\u4f5c\u5ba4",
    subtitle: "26/6",
    articleText: "2026\u5e746\u81f37\u6708\u4ee5\u6cb3\u6d77\u5927\u5b66\u6c5f\u5b81\u6821\u533a\u4e3a\u9996\u4e2a\u8bd5\u70b9\uff0c\u6838\u5fc3\u4e1a\u52a1\u9762\u5411\u5728\u6821\u5927\u5b66\u751f\u5f00\u8bbe\u666e\u901a\u8bdd\u4e8c\u7532\u51b2\u523a\u5c0f\u73ed\u3001\u4e00\u5bf9\u4e00\u7ea0\u97f3\u8f85\u5bfc\uff0c\u5c0f\u73ed\u9488\u5bf9\u6027\u8f85\u5bfc\u548c\u966a\u7ec3\uff0c\u586b\u8865\u6821\u5185\u666e\u901a\u8bdd\u57f9\u8bad\u5e02\u573a\u7a7a\u767d\u3002\u65d7\u4e0b\u8a00\u5c7b\u5de5\u4f5c\u5ba4\u4e3b\u8981\u627f\u63a5\u914d\u97f3\u4e1a\u52a1\u3002\u56e2\u961f\u4e2d\u6709\u6559\u7814\u4eba\u5458\uff0c\u8fd0\u8425\u4eba\u5458\uff0c\u914d\u97f3\u4e13\u5458",
  },
  {
    videoUrl:
      "https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260331_054411_511c1b7a-fb2f-42ef-bf6c-32c0b1a06e79.mp4",
    title: "\u201c\u63a2\u6e90\u5c0f\u52a9\u624b\u201dhhu\u5fae\u9898\u5e93\uff0c\u201c\u4e91\u9732\u6668\u9891\u201d\u6821\u5185ai\u7535\u53f0 \u5c0f\u7a0b\u5e8f",
    subtitle: "26/7",
    articleText: "\u63a2\u6e90\u5c0f\u7a0b\u5e8f\u5b9a\u4f4d\u662f\u4e00\u6b3e\u9488\u5bf9\u6cb3\u6d77\u6821\u5185\u7684\u9898\u5e93\u7a0b\u5e8f\uff0c\u6c47\u603b\u5404\u5b66\u79d1\u9898\u5e93\u4e0e\u8d44\u6599\uff0c\u5e2e\u52a9LXT\u9879\u76ee\u6253\u5f00\u5e02\u573a\u4e0e\u5efa\u7acb\u6821\u5185\u793e\u7fa4\uff0c\u5bfb\u627e\u9700\u6c42\u7528\u6237\u3002",
  },
  {
    videoUrl:
      "https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260331_055427_ac7035b5-9f3b-4289-86fc-941b2432317d.mp4",
    title: "\u8a00\u5c7b\u201c\u914d\u97f3\u517c\u804c\u63a5\u5355\u5e73\u53f0",
    subtitle: "26/7",
    articleText: "\u8a00\u5c7b\u662f\u9762\u5411LXT\u5185\u90e8\u6559\u5458\u8bbe\u7f6e\u7684\u5357\u4eac\u5927\u5b66\u751f\u914d\u97f3\u517c\u804c\u5e73\u53f0\uff0c\u4e3a\u6821\u5185\u6559\u5458\u63d0\u4f9b\u989d\u5916\u7684\u8d44\u91d1\u652f\u6301\uff0c\u5e76\u5411\u5404\u9700\u6c42\u4f01\u4e1a\u63d0\u4f9b\u9ad8\u8d28\u91cf\u4e14\u5b9e\u60e0\u7684\u914d\u97f3\u4fee\u97f3\u670d\u52a1",
  },
];

export default function NftCollection() {
  return (
    <section className="relative w-full bg-bg-dark py-16 sm:py-20 md:py-24">
      <div className="max-w-[1831px] mx-auto w-full px-4 sm:px-6 md:px-10 lg:px-12">
        <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-8 mb-12 lg:mb-16">
          <Reveal className="lg:ml-32" as="div" delay={0.1}>
            <h2 className="font-grotesk uppercase text-[32px] sm:text-[40px] md:text-[50px] lg:text-[60px] text-cream leading-none m-0">
              <DecryptedText text="see what we did!" animateOn="view" />
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
