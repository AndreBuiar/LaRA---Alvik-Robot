# This program was created in Arduino Lab for MicroPython

from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)
  
#andar e voltar aprox 30cm 

def loop():
  alvik.set_wheels_speed(9.36, 9.36)
  delay(6000)
  alvik.set_wheels_speed(0, 0)
  delay(1000)
  alvik.set_wheels_speed(-9.36, -9.36)
  delay(6000)
  alvik.set_wheels_speed(0, 0)
  delay(5000)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)
