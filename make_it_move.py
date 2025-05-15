# This program was created in Arduino Lab for MicroPython

from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)
#aprox 30cm 
def loop():
  alvik.set_wheels_speed(35, 35)
  delay(5000)
  alvik.set_wheels_speed(0, 0)
  delay(1000)
  alvik.set_wheels_speed(-35, -35)
  delay(5000)
  alvik.set_wheels_speed(0, 0)
  delay(5000)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)