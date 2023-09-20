from PIL import Image

image = Image.new('RGB', (3, 2))

image.putpixel((0, 0), (5, 20, 64))
image.putpixel((0, 1), (5, 20, 64))
image.putpixel((1, 0), (255, 255, 255))
image.putpixel((1, 1), (255, 255, 255))
image.putpixel((2, 0), (236, 25, 32))
image.putpixel((2, 1), (236, 25, 32))

image.save("image.png")
