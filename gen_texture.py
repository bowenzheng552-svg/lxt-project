import struct, zlib, random, os
random.seed(42)
width, height = 800, 600
pixels = bytearray()
for y in range(height):
    pixels.extend(b'\x00')
    for x in range(width):
        v = random.randint(180, 235)
        pixels.extend([v, v, v, 255])

def create_png(w, h, raw):
    def chunk(ctype, data):
        c = ctype + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xFFFFFFFF)
    sig = b'\x89PNG\r\n\x1a\n'
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0))
    idat = chunk(b'IDAT', zlib.compress(bytes(raw)))
    iend = chunk(b'IEND', b'')
    return sig + ihdr + idat + iend

png_data = create_png(width, height, pixels)
path = r'C:\Users\JOYY\Documents\Codex\2026-07-14\new-chat-2\orbis-nft\public\texture.png'
with open(path, 'wb') as f:
    f.write(png_data)
print('Texture generated')
