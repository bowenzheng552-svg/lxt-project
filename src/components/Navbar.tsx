export default function Navbar() {
  const links = ["Homepage", "Gallery", "Buy NFT", "FAQ", "Contact"];

  return (
    <header className="relative z-10 flex items-center justify-between px-4 sm:px-6 md:px-10 lg:px-12 py-4 max-w-[1831px] mx-auto w-full">
      {/* Logo */}
      <a href="#" className="font-grotesk text-[16px] uppercase tracking-wider text-cream no-underline">
        Orbis.Nft
      </a>

      {/* Desktop Nav */}
      <nav className="hidden lg:block liquid-glass rounded-[28px] px-[52px] py-[24px]">
        <ul className="flex items-center gap-8 m-0 p-0 list-none">
          {links.map((link) => (
            <li key={link}>
              <a
                href="#"
                className="font-grotesk text-[13px] uppercase tracking-wide text-cream no-underline transition-colors duration-200 hover:text-neon"
              >
                {link}
              </a>
            </li>
          ))}
        </ul>
      </nav>

      {/* Spacer for desktop social icons alignment */}
      <div className="hidden lg:block w-[120px]" />
    </header>
  );
}
