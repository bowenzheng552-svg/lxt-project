import Hero from "./components/Hero";
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
