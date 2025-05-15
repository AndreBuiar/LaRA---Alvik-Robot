#WALK ARDUINO ALVIK

# This program was created in Arduino Lab for MicroPython

from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)

#aprox 20 cm frente, volta 10 cm 


def loop():
  alvik.set_wheels_speed(10, 10)
  delay(12000)
  alvik.set_wheels_speed(0, 0)
  delay(1000)
  alvik.set_wheels_speed(-10, -10)
  delay(6000)
  alvik.set_wheels_speed(0, 0)
  delay(5000)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)

