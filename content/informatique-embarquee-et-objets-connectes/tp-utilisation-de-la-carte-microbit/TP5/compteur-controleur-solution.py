from microbit import *
import radio

# Activation et configuration de la radio.
radio.on()
# Choisissez un canal (un nombre) commun pour votre binôme.
radio.config(channel=7)

while True:
    display.clear()

    if button_a.was_pressed():  # Le bouton A est pressé
        display.show("-")
        radio.send("moins")  # Envoyer le message "moins"
        sleep(100)  # Attendre 100 millisecondes (soit une demi-seconde)
    elif button_b.was_pressed():  # Le bouton B est pressé
        display.show("+")
        radio.send("plus")
        sleep(100)
    elif accelerometer.was_gesture("shake"):
        display.show(0)
        radio.send("reset")
        sleep(100)
