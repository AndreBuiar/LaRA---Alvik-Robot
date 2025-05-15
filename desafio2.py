from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)


def loop():

  alvik.set_wheels_speed(40, 40)
  delay(4214) # 400 mm em 40 rev 
  
  alvik.set_wheels_speed(0, 30)
  delay(2600)  #virou esquerda
  
  alvik.set_wheels_speed(40, 40)
  delay(2809) #anda 20 mm 
  
  alvik.set_wheels_speed(0, 30)
  delay(2600)  #virou esquerda
  
  alvik.set_wheels_speed(40, 40)
  delay(2809) #anda 20 mm 
  
  alvik.set_wheels_speed(30, 0)
  delay(2600) #virou direita
  
  alvik.set_wheels_speed(40, 40)
  delay(2809) #anda 20 mm
  
  alvik.set_wheels_speed(0, 30)
  delay(2600)  #virou esquerda
  
  alvik.set_wheels_speed(40, 40)
  delay(2809) #anda 20 mm
  
  alvik.set_wheels_speed(0, 30)
  delay(2600)  #virou esquerda
  
  alvik.set_wheels_speed(40, 40)
  delay(2809) #anda 20 mm
  
  alvik.set_wheels_speed(30, 0)
  delay(2600) #virou direita
  
  alvik.set_wheels_speed(40, 40)
  delay(2809) #anda 20 mm
  
  alvik.set_wheels_speed(0, 30)
  delay(2600)  #virou esquerda
  
  alvik.set_wheels_speed(40, 40)
  delay(2809) #anda 20 mm
  
  alvik.set_wheels_speed(0, 30)
  delay(2600)  #virou esquerda
  
  alvik.set_wheels_speed(40, 40)
  delay(4214) #anda 40 mm
  
  alvik.set_wheels_speed(0, 0)
  delay(10000)


  
def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)