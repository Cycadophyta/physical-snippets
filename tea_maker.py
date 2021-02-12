### Tea Maker ###

## Libraries ##
from gpiozero import LED, Buzzer, Button
from w1thermsensor import W1ThermSensor
import time

## Settings ##
temp_set = 26
temp_range = 5
brew_time = 5

## GPIO ##
sensor = W1ThermSensor()
red = LED(18)
blue = LED(24)
buzzer = Buzzer(22)
button = Button(25)

while True:
    temp = sensor.get_temperature(W1ThermSensor.DEGREES_C)

    if temp > temp_set:
        red.on()
    else:
        red.off()
    if temp < temp_set + temp_range:
        blue.on()
    else:
        blue.off()

    if button.is_pressed:
        red.off()
        blue.off()
        buzzer.on()
        time.sleep(0.1)
        buzzer.off()
        time.sleep(brew_time)
        for i in range(3):
            for j in range(3):
                buzzer.on()
                time.sleep(0.1)
                buzzer.off()
                time.sleep(0.1)
            time.sleep(0.3)





