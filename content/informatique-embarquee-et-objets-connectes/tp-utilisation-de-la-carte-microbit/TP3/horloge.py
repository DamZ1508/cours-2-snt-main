from microbit import *

# Liste des images d'aiguilles à afficher
AIGUILLES = [
    Image.CLOCK1,
    Image.CLOCK2,
    Image.CLOCK3,
    Image.CLOCK4,
    Image.CLOCK5,
    Image.CLOCK6,
    Image.CLOCK7,
    Image.CLOCK8,
    Image.CLOCK9,
    Image.CLOCK10,
    Image.CLOCK11,
    Image.CLOCK12,
]

# État initial : l'aiguille tourne
état = "tourne"

while True:
    # Si l'état est "tourne", alors affiche la bonne aiguille.
    # Cette partie-là est un peu compliquée ; ne cherchez pas à la comprendre.
    if état == "tourne":
        display.show(AIGUILLES[
            (running_time() // 50) % len(AIGUILLES)
        ])

    # Si on appuie sur le bouton A, alors l'état devient "tourne"
    if button_a.is_pressed():
        état = "tourne"

    # Sinon, si on appuie sur le bouton B, alors l'état devient "stop"
    elif button_b.is_pressed():
        état = "stop"
