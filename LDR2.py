from gpiozero import LightSensor, PWMLED
from signal import pause

sensor = LightSensor(27)
led = PWMLED(18)

led.source = sensor

pause()
