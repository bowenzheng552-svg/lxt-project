cssPath = r"C:\Users\JOYY\Documents\Codex\2026-07-14\new-chat-2\orbis-nft\src\index.css"
with open(cssPath, 'r', encoding='utf-8') as f:
    css = f.read()

animBlock = """

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

.opacity-hidden {
  opacity: 0;
  transform: translateY(20px);
  transition: none;
}
"""

# Remove existing anim block (between "Entrance Animations" comment markers)
start = css.find('/* ===== Entrance Animations ===== */')
end = css.find('.opacity-hidden')
if start >= 0:
    # Find the end of the .opacity-hidden block
    end_of_anim = css.find('}\n', end) + 1
    if end_of_anim > 0:
        css = css[:start] + '\n' + css[end_of_anim + 1:]
    else:
        css = css[:start]
    print("Removed existing animation block")
else:
    print("No existing animation block found")

# Append at the end
css = css.rstrip() + '\n' + animBlock

with open(cssPath, 'w', encoding='utf-8') as f:
    f.write(css)
print('CSS fixed')
