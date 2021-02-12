from gpiozero import MotionSensor, LED
from signal import pause

pir = MotionSensor(17)
led = LED(18)

pir.when_motion = led.on
pir.when_no_motion = led.off

pause()
