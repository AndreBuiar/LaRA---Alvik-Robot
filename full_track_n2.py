from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

import my_functions

def setup():
  alvik.begin()
  delay(1000)

def desvio_objeto():
  alvik.set_wheels_speed(22,30)
  delay(5000)
  alvik.set_wheels_speed(0, 0)
  alvik.set_wheels_speed(30,18)
  delay(4000)
  alvik.set_wheels_speed(0, 0)

def curva_longa():
  alvik.set_wheels_speed(30,30)
  delay(200)
  alvik.set_wheels_speed(20,30)
  delay(8000)
  alvik.set_wheels_speed(20,20)
  delay(1800)
  alvik.set_wheels_speed(0, 0)

def frente(R, t):
	alvik.set_wheels_speed(R, R)
	delay(t)
	alvik.set_wheels_speed(0, 0)

def tras(R, t):
	alvik.set_wheels_speed(-R, -R)
	delay(t)
	alvik.set_wheels_speed(0, 0)

def turn_90_dir():
	alvik.set_wheels_speed(30, 0)
	delay(2600)
	alvik.set_wheels_speed(0, 0)

def turn_90_esq():
	alvik.set_wheels_speed(0, 30)
	delay(2600)
	alvik.set_wheels_speed(0, 0)

def turn_180_dir():
	alvik.set_wheels_speed(30, 0)
	delay(5600)
	alvik.set_wheels_speed(0, 0)

def turn_180_esq():
	alvik.set_wheels_speed(0, 30)
	delay(5600)
	alvik.set_wheels_speed(0, 0)

def pivot_360_esq():
	alvik.set_wheels_speed(0, 30)
	delay(11200)
	alvik.set_wheels_speed(0, 0)

def pivot_360_dir():
	alvik.set_wheels_speed(30, 0)
	delay(11200)
	alvik.set_wheels_speed(0, 0)
 
def smooth_turn_dir():
	alvik.set_wheels_speed(30, 15)
	delay(10600)
	alvik.set_wheels_speed(0, 0)
 
def smooth_turn_esq():
	alvik.set_wheels_speed(15,30)
	delay(10600)
	alvik.set_wheels_speed(0, 0)

def spin_360_dir():
	alvik.set_wheels_speed(15,-15)
	delay(11200)
	alvik.set_wheels_speed(0, 0)

def spin_180_dir():
	alvik.set_wheels_speed(15,-15)
	delay(5300)
	alvik.set_wheels_speed(0, 0)

def spin_180_esq():
	alvik.set_wheels_speed(-15,15)
	delay(5300)
	alvik.set_wheels_speed(0, 0)

def spin_360_esq():
	alvik.set_wheels_speed(-15,15)
	delay(11200)
	alvik.set_wheels_speed(0, 0)

def spin_90_esq():
	alvik.set_wheels_speed(-15,15)
	delay(2650)
	alvik.set_wheels_speed(0, 0)
 
def spin_90_dir():
	alvik.set_wheels_speed(15,-15)
	delay(2650)
	alvik.set_wheels_speed(0, 0)
 
def spin_45_dir():
	alvik.set_wheels_speed(15,-15)
	delay(1325)
	alvik.set_wheels_speed(0, 0)
 
def spin_45_esq():
	alvik.set_wheels_speed(-15,15)
	delay(1325)
	alvik.set_wheels_speed(0, 0)

def loop():
  #importante: frente(30,5600) =aprox 300 mm

  frente(30, 10300) #ponto 1 ao ponto 3 na mesa de testes (manter porporção 30 - 5600)
  frente(0,500)
  spin_90_esq()
  frente(24, 4400) #manter a proporcional velocidade de rotação (30-5600)
  frente(0,2000)
  frente(25,2500)
  tras(20,1800)
  spin_90_esq()
 
  desvio_objeto()
  frente(20,5600)
  spin_45_esq()
  spin_90_esq()
  spin_360_dir()

  curva_longa()
  tras(30,5800)
 
  frente(0,10000)
 

def cleanup():
  alvik.stop()
 
start(setup, loop, cleanup)
