# CamJam Edukit 1 - Basics
# Worksheet 6 - Morse Code

# Import Libraries
import os  # Gives Python access to Linux commands
import time  # Proves time related commands
from gpiozero import LED  # The GPIO Zero buzzer functions

# Set pin 22 as a buzzer
#buzzer = Buzzer(22)
led = LED(18)

# Define some 'user-defined functions'
def o():  # A single Morse dot
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.1)


def i():  # A single Morse dash
    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(0.1)


def letter_space():  # The space between letters
    time.sleep(0.2)


def word_space():  # The space between words
    time.sleep(0.6)

morse = {
    'A': 'oi', 'B': 'iooo', 'C': 'ioio', 'D': 'ioo', 'E': 'o',
    'F': 'ooio', 'G': 'iio', 'H': 'oooo', 'I': 'oo', 'J':'oiii',
    'K': 'ioi', 'L': 'oioo', 'M': 'ii', 'N': 'io', 'O': 'iii',
    'P': 'oiio', 'Q': 'iioi', 'R': 'oio', 'S': 'ooo', 'T': 'i',
    'U': 'ooi', 'V': 'oooi', 'W': 'oii', 'X': 'iooi', 'Y': 'ioii',
    'Z': 'iioo'
}


os.system('clear')  # Clears the terminal window

print("Morse Code")

while True:
    phrase = input('Enter phrase: ')

    def code(phrase):
        for ch in phrase:
            if ch == ' ':
                word_space()
            else:
                for dit in morse[ch.upper()]:
                    if dit == 'i':
                        i()
                    elif dit == 'o':
                        o()
                letter_space()

    code(phrase)
