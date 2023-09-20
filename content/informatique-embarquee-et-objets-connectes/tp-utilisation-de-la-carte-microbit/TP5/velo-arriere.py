from microbit import *
import radio

# Activation et configuration de la radio.
radio.on()
# Choisissez un canal (un nombre) commun pour votre binôme.
radio.config(channel=XXX)

display.clear()

while True:
    display.clear()  # Effacer l'affichage
    XXX  # Lire un message reçu par radio

    if XXX:  # Si le message est "gauche"
        display.show(Image.ARROW_W)  # Afficher une flèche vers la gauche
        sleep(5000)  # Patienter 5 secondes (5000 millisecondes)

    # Si le message est "droite", afficher la flèche vers la droite,
    # et patienter 5 secondes
    XXX
