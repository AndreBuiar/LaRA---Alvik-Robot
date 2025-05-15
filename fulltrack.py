#PISTA COMPLETA

from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

import my_functions 
#This command imports a functions file that allows Alvik move.

def setup():
  alvik.begin()
  delay(1000)


def loop():
  #frente(30,5600) =aprox 300 mm
 
  frente(30, 10267)   
  frente(0,500)
  turn_90_esq()  
  frente(20,4480)
  spin_90_esq()
 
  frente(0,10000)
 

def cleanup():
  alvik.stop()
 
start(setup, loop, cleanup)

#point 1 to point 3 on the test table (keep the ratio 30 - 5600). APPLIED LOGIC: if I travel 300 mm at 5600, how far did I travel (keeping the same rotation x time ratio) to travel 550 mm?

#keep the proportional rotation speed (30-5600). Same logic applied to the previous example.
