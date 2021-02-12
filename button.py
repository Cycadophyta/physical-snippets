# Packages
import os
import time
from gpiozero import Button, LED, LEDBoard

# GPIO
'''R = LED(18)
Y = LED(23)
G = LED(24)'''
leds = LEDBoard(red=18, yellow=23, green=24)
button = Button(25)

print("---------------")
print(" Button + GPIO ")
print("---------------")

index = 0

'''def off(): R.off(); Y.off(); G.off()

def red(): R.on(); Y.off(); G.off()

def yellow(): R.off(); Y.on(); G.off()

def green(): R.off(); Y.off(); G.on()

LEDs = (off, red, yellow, green)'''

def off(): leds.value = (0, 0, 0)

def red(): leds.value = (1, 0, 0)

def yellow(): leds.value = (0, 1, 0)

def green(): leds.value = (0, 0, 1)

LEDs = (off, red, yellow, green)

while True:
    for led in LEDs:
        led()
        time.sleep(0.1)
        button.wait_for_press()
'''
while True:
    for led in leds:
        led.on()
        time.sleep(0.2)
        button.wait_for_press()
        led.off()'''
