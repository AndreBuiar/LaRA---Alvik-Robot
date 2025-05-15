from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)

#giro de 45°

def loop():
  alvik.set_wheels_speed(0, 7.5)
  delay(5300)
  alvik.set_wheels_speed(0, 0)
  delay(10000)


#giro de 90°

def loop():
  alvik.set_wheels_speed(0, 15)
  delay(5300)
  alvik.set_wheels_speed(0, 0)
  delay(10000)



#giro de 180°

def loop():
  alvik.set_wheels_speed(0, 30)
  delay(5300)
  alvik.set_wheels_speed(0, 0)
  delay(10000)
  
#giro de 360

def loop():
  alvik.set_wheels_speed(0, 60)
  delay(5300)
  alvik.set_wheels_speed(0, 0)
  delay(10000)

def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)
