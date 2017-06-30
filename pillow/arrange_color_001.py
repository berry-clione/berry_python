from PIL import Image

# img = Image.open("rikugien_001.jpg")
img = Image.open("rikugien_002.jpg")
r, g, b = img.split()
# img = Image.merge("RGB", (b,r,g)) # (r,g,b)
img = Image.merge("RGB", (g,r,b)) # (r,g,b)
# img.save("iwadatami_pillow.png","png")
img.save("rikugien_002.png","png")
