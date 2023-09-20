from microbit import *
import radio

radio.on()
radio.config(channel=42)

display.clear()

EMPTY = Image("00000:00000:00000:00000:00000")

etat = "stop"

while True:
    if button_a.was_pressed():
        if etat == "gauche":
            etat = "stop"
            radio.send("STOP")
            display.clear()
        else:
            etat = "gauche"
            radio.send("GAUCHE")
            display.show(
                [Image.ARROW_W, EMPTY],
                delay=250,
                wait=False,
                loop=True,
            )
    elif button_b.was_pressed():
        if etat == "droite":
            etat = "stop"
            radio.send("STOP")
            display.clear()
        else:
            etat = "droite"
            radio.send("DROITE")
            display.show(
                [Image.ARROW_E, EMPTY],
                delay=250,
                wait=False,
                loop=True,
            )

