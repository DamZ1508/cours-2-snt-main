from microbit import *
import radio

radio.on()
radio.config(channel=42)

display.clear()

while True:
    if button_a.was_pressed():
        display.show(Image.ARROW_W, delay=1000, wait=False, clear=True)
        radio.send("GAUCHE")
    elif button_b.was_pressed():
        display.show(Image.ARROW_E, delay=1000, wait=False, clear=True)
        radio.send("DROITE")
