from arduino import *
from arduino_alvik import ArduinoAlvik
alvik = ArduinoAlvik()
flag =0
def setup():
  alvik.begin()
  delay(1000)
def loop():
  while flag<5:
      
    alvik.set_wheels_speed(40, 40)
    delay(5618) # 400 mm em 40 rev 
    alvik.set_wheels_speed(0, 15)
    delay(5300) #virou esquerda
    alvik.set_wheels_speed(40, 40)
    delay(2809) #anda 20 mm 
    alvik.set_wheels_speed(0, 15)
    delay(5300)#virou esquerda
    alvik.set_wheels_speed(40, 40)
    delay(5618)#anda 20 mm 
    alvik.set_wheels_speed(0, 15)
    delay(5300)#virou esquerda
    alvik.set_wheels_speed(40, 40)
    delay(2809)#anda 20 mm
    alvik.set_wheels_speed(0, 15)
    delay(5300)#virou esquerda
    
alvik.set_wheels_speed(0, 0)
delay(10000)
  
def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)
