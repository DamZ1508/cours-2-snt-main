from microbit import *
import radio

radio.on()
radio.config(channel=42)

while True:
    display.show(Image.ASLEEP)
    message = radio.receive()
    if message == "alerte":
        display.show([Image.HEART, Image.HEART_SMALL], loop=True, wait=False)
        sleep(5000)
