from microbit import *

# Initialiation du compteur à 0
compteur = 0

while True:
    display.show(compteur)

    # Si le bouton B est appuyé
    if button_b.was_pressed():
        # Alors augmenter la valeur du compteur de 1
        compteur = compteur + 1

