# This program was created in Arduino Lab for MicroPython

from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)

#aprox 20cm em 5 rpm (≃ 22,5s) 

def loop():
  alvik.set_wheels_speed(5, 5)
  delay(22429)
  alvik.set_wheels_speed(0, 0)
  delay(5000)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)

'''
CÁLCULO:

td = C.revolutions.t/60000

200(mm)= 106,8 . 5(rpm) .t/60000

200mm = 534 . t/60000

200 . 60000 = 534t

12,000,000 = 534t

t= 22429
'''
