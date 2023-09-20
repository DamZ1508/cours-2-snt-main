from microbit import *
import radio

# Activation et configuration de la radio.
radio.on()
# Choisissez un canal (un nombre) commun pour votre binôme.
radio.config(channel=XXX)

display.show("?")

while True:
    message = XXX  # Recevoir un message par la radio
    if message == "temperature" :  # Si le message est "température"
        radio.send(XXX)  # Envoyer la valeur de la température
    if XXX:  # Si le message est "luminosité"
        XXX  # Envoyer la valeur de la luminosité
