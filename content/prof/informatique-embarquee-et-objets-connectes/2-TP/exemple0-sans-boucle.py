from microbit import *

if button_a.is_pressed():
    display.show(Image.ARROW_W)
elif button_b.is_pressed():
    display.show(Image.ARROW_E)
else:
    display.show("?")