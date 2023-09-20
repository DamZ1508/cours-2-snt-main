from microbit import *
import radio

# Activation et configuration de la radio.
radio.on()
# Choisissez un canal (un nombre) commun pour votre binôme.
radio.config(channel=7)

while True:
    message = radio.receive()
    if message == "gauche":
        XXX  # Afficher une flèche à gauche
    elif message == "droite":
        XXX  # Afficher une flèche à gauche
    elif XXX:
        XXX  # Éteindre l'écran
