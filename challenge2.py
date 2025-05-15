from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)


def loop():

  alvik.set_wheels_speed(40, 40)
  delay(4213.5) # 300 mm em 40 rev 
  
  alvik.set_wheels_speed(0, 15)
  delay(5300) #virou esquerda
  
  alvik.set_wheels_speed(40, 40)
  delay(2809) #anda 20 mm 
  
  alvik.set_wheels_speed(0, 15)
  delay(5300)#virou esquerda
  
  alvik.set_wheels_speed(40, 40)
  delay(2809)#anda 20 mm 
  
  alvik.set_wheels_speed(15, 0)
  delay(5300)#virou direita
  
  alvik.set_wheels_speed(40, 40)
  delay(2809)#anda 20 mm
  
  alvik.set_wheels_speed(0, 15)
  delay(5300)#virou esquerda
  
  alvik.set_wheels_speed(40, 40)
  delay(2809)#anda 20 mm
  
  alvik.set_wheels_speed(0, 15)
  delay(5300)#virou esquerda
  
  alvik.set_wheels_speed(40, 40)
  delay(2809)#anda 20 mm
  
  alvik.set_wheels_speed(15, 0)
  delay(5300)#virou direita
  
  alvik.set_wheels_speed(40, 40)
  delay(2809)#anda 20 mm
  
  alvik.set_wheels_speed(0, 15)
  delay(5300)#virou esquerda
  
  alvik.set_wheels_speed(40, 40)
  delay(2809)#anda 20 mm
  
  alvik.set_wheels_speed(0, 15)
  delay(5300)#virou esquerda
  
  alvik.set_wheels_speed(40, 40)
  delay(4213.5)#anda 30 mm
  

  
  
  
  alvik.set_wheels_speed(0, 0)
  delay(10000)
  
def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)

