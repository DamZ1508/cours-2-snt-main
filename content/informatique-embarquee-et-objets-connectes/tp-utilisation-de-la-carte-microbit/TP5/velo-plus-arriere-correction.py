from microbit import *
import radio

radio.on()
radio.config(channel=42)

display.clear()

EMPTY = Image("00000:00000:00000:00000:00000")

while True:
    message = radio.receive()
    if message == "GAUCHE":
        display.show([Image.ARROW_W, EMPTY], delay=250, loop=True, wait=False)
    if message == "DROITE":
        display.show([Image.ARROW_E, EMPTY], delay=250, loop=True, wait=False)
    if message == "STOP":
        display.clear()
