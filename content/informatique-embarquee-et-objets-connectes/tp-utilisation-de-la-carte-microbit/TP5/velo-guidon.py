from microbit import *
import radio

# Activation et configuration de la radio.
radio.on()
# Choisissez un canal (un nombre) commun pour votre binôme.
radio.config(channel=XXX)

while True:
    display.clear()  # Effacer l'écran

    if button_a.was_pressed():  # Si le bouton A est pressé
        display.show(Image.ARROW_W)  # Afficher une flèche vers la gauche
        radio.send(XXX)  # Envoyer le message "gauche"
        XXX  # Attendre 5000 millisecondes (soit 5 secondes)

    # Si le bouton B est pressé, afficher une flèche vers la droite,
    # puis envoyer le message "droite", puis attendre 5 secondes.
    # XXX
