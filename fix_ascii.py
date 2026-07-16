path = r"C:\Users\JOYY\Documents\Codex\2026-07-14\new-chat-2\orbis-nft\src\components\ASCIIText.tsx"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the charset line - the double quote inside the string breaks the JS string
old = '''this.charset = charset ?? " .'`^",:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$";'''
new = """this.charset = charset ?? ' .\\'`^",:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$';"""

if old in content:
    content = content.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed')
else:
    print('Line not found')
    # Debug: show what's on line 96
    lines = content.split('\n')
    for i, line in enumerate(lines[93:98], start=94):
        print(f'Line {i}: {repr(line)}')
