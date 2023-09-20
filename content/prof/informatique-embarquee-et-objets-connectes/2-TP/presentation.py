from microbit import *
import random

while True:
    if accelerometer.was_gesture("shake"):
        display.show(Image.SAD)
        sleep(2000)
    elif button_a.is_pressed() and button_b.is_pressed():
        display.set_pixel(random.randint(0, 4), random.randint(0, 4), random.randint(0, 9))
    elif button_a.is_pressed():
        display.scroll(str(temperature()))
    elif button_b.is_pressed():
        lecture = accelerometer.get_x()
        if lecture > 500:
            display.show(Image.ARROW_E)
        elif lecture > 250:
            display.show(Image.ARROW_SE)
        elif lecture > -250:
            display.show(Image.ARROW_S)
        elif lecture > -500:
            display.show(Image.ARROW_SW)
        else:
            display.show(Image.ARROW_W)
    else:
        display.show("?")
