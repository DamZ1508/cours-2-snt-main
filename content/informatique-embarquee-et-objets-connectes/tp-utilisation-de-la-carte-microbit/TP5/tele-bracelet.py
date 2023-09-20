from microbit import *
import radio

# Activation et configuration de la radio.
radio.on()
# Choisissez un canal (un nombre) commun pour votre binôme.
radio.config(channel=XXX)

while True:
    display.show(Image.ASLEEP)  # Afficher un smiley endormi (tout va bien)

    if XXX:  # Si le bracelet est secoué
        display.show(XXX)  # Afficher une image triste
        radio.send(XXX)  # Envoyer le message "alerte"
        XXX  # Attendre une seconde
