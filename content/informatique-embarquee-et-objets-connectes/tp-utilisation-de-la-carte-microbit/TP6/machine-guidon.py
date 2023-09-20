from microbit import *

état = "éteint"

while True:
    if état == "éteint":
        # Si l'on est dans l'état "eteint"
        if button_a.was_pressed():
            # Si on appuie sur le bouton A :
            # on passe dans l'état "gauche", et on affiche une flèche à gauche
            état = "gauche"
            display.show(Image.ARROW_W)
        if button_b.was_pressed():
            # Si on appuie sur le bouton B :
            # on passe dans l'état "droite", et on affiche une flèche à droite
            état = "droite"
            display.show(Image.ARROW_E)
    if état == "gauche":
        # Si l'on est dans l'état "gauche"
        if button_a.was_pressed():
            état = "éteint"
            XXX  # Éteindre l'écran
        if button_b.was_pressed():
            état = XXX
            XXX  # Afficher une flèche à droite
    if état == "droite":
        # Si l'on est dans l'état "droite"
        XXX
