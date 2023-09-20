from microbit import *
import radio

radio.on()
radio.config(channel=42)

while True:
    display.show(Image.ASLEEP)
    if accelerometer.was_gesture("shake"):
        display.show(Image.SAD)
        radio.send("alerte")
        sleep(1000)
