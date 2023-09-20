from microbit import *
import radio

radio.on()
radio.config(channel=42)

while True:
    display.show("?")
    if button_a.was_pressed():
        radio.send("température")
    elif button_b.was_pressed():
        radio.send("luminosité")

    message = radio.receive()
    if message:
        display.scroll(message)

