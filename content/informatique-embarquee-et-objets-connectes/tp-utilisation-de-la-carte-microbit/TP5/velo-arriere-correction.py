from microbit import *
import radio

radio.on()
radio.config(channel=42)

display.clear()

EMPTY = Image("00000:00000:00000:00000:00000")

while True:
    display.clear()
    message = radio.receive()
    if message == "GAUCHE":
        display.show([Image.ARROW_W, EMPTY], delay=250, loop=True, wait=False)
        sleep(5000)
    if message == "DROITE":
        display.show([Image.ARROW_E, EMPTY], delay=250, loop=True, wait=False)
        sleep(5000)
