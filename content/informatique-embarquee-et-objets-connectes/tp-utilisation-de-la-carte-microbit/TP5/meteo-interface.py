from microbit import *
import radio

# Activation et configuration de la radio.
radio.on()
# Choisissez un canal (un nombre) commun pour votre binôme.
radio.config(channel=XXX)

while True:
    display.show("?")
    if button_a.was_pressed():  # Si l'utilisatrice appuie sur le bouton A
        radio.send(XXX)  # Envoyer le message "température"
    if XXX:  # Si l'utilisatrice appuie sur le bouton B
        XXX  # Envoyer le message "luminosité"

    message = XXX  # Lire un message reçu par radio (la réponse du capteur)
    if message:  # Si on a lu quelque chose
        display.scroll(message)  # Afficher le message reçu

