from microbit import *

display.show("?")

while True:

    if button_a.is_pressed():
        # Bouton A pressé : flèche vers la gauche.
        display.show(Image.ARROW_W)

    elif button_b.is_pressed():
        # Bouton B pressé : flèche vers la gauche.
        display.show(Image.ARROW_E)

    else:
        # Aucun bouton pressé.
        display.show("?")
