# CamJam EduKit 2 - Sensors (GPIO Zero)
# Worksheet 4 - Light

# Import Libraries
from gpiozero import LightSensor, LED, Buzzer
import time

# A variable with the LDR reading pin number
ldr = LightSensor(27)
red = LED(18)
blue = LED(24)
buzzer = Buzzer(22)

while True:
    light = ldr.value
    if light > 0.1:
        red.on(); blue.off()
    else:
        red.off(); blue.on()
    if light > 0.9:
        buzzer.on()
    else:
        buzzer.off()
    time.sleep(0.1)
