from microbit import *
import radio

# Activation et configuration de la radio.
radio.on()
# Choisissez un canal (un nombre) commun pour votre binôme.
radio.config(channel=7)

compteur = 0

while True:
    display.show(compteur)

    message = radio.receive()
    if message == "plus":
        compteur = compteur + 1
    elif message == "moins":
        compteur = compteur - 1
