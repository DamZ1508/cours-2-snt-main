# Idée : https://www.101computing.net/bbc-microbit-hogwarts-sorting-hat/

from microbit import *
import random

MAISONS = [
    "Gryffondor",
    "Poufsouffle",
    "Serdaigle",
    "Serpentard",
    ]

while True:
    display.show("?")
    if accelerometer.was_gesture("shake"):
        display.show(Image.ALL_CLOCKS, delay=100)
        display.scroll(random.choice(MAISONS))
