from microbit import *

display.show(Image.HAPPY)
while True:
    if accelerometer.current_gesture() == "shake":
        display.show(Image.SAD)
        sleep(100)
        display.show(Image.HAPPY)