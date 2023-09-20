from microbit import *
import radio

# Activation et configuration de la radio.
radio.on()
# Choisissez un canal (un nombre) commun pour votre binôme.
radio.config(channel=XXX)

while True:
    XXX  # Afficher un smiley endormi (tout va bien)
    message = radio.receive()  # Recevoir un message sur la radio
    if message == "alerte":  # Si le message reçu est "alerte"
        XXX  # Afficher "alerte"
