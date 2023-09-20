from microbit import *
import radio

radio.on()
radio.config(channel=42)

display.show(Image.ALL_CLOCKS, wait=False, loop=True)

while True:
    message = radio.receive()
    if message == "température":
        radio.send(str(temperature()))
    if message == "luminosité":
        radio.send(str(display.read_light_level()))
