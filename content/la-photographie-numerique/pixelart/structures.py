from PIL import Image
import random

image = Image.new("RGB", (256, 256))

x = round(255 / 2)
y = round(255 / 2)
rouge = round(255 / 2)
vert = round(255 / 2)
bleu = round(255 / 2)

for i in range(1000):
    direction = random.choice(["gauche", "droite", "haut", "bas"])
    if direction == "gauche":
        x = (x - 1) % 256
    elif direction == "droite":
        x = (x + 1) % 256
    elif direction == "haut":
        y = (y - 1) % 256
    else:
        y = (y + 1) % 256

    rouge = (rouge + 2) % 256
    vert = (vert - 1) % 256
    if random.randint(0, 1) == 0:
        bleu = (bleu + 3) % 256
    else:
        bleu = (bleu - 3) % 256
    image.putpixel((x, y), (rouge, vert, bleu))

image.save("image.png")
