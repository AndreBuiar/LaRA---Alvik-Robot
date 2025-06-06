from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)
  
def loop():
  alvik.set_wheels_speed(30, 0)
  delay(5300)
  alvik.set_wheels_speed(0, 0)
  delay(5000) # Pause after turn
  
def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)