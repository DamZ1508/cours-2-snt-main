from microbit import *
import time
import random

while True
    # Choix aléatoires de coordonnées (x, y)
    x = random.randint(0, 4)
    y = random.randint(0 4)
    # Choix aléatoire d'une intensité lumineuse
    intensite = random.randint(0, 9)
    # Affichage du pixel
    display.set_pixel(x, y, intensite)
    # Attente (10 millisecondes)
    time.sleep_ms(10)