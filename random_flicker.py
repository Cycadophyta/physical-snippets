from gpiozero import PWMLED
from gpiozero.tools import random_values
from signal import pause

led = PWMLED(18)
led.source = random_values()
led.source_delay = 0.1

pause()
