def frente(R, t):
    alvik.set_wheels_speed(R, R)
    delay(t)
    alvik.set_wheels_speed(0, 0)

def tras(R, t):
    alvik.set_wheels_speed(-R, -R)
    delay(t)
    alvik.set_wheels_speed(0, 0)

def curva_90_dir():
    alvik.set_wheels_speed(30, 0)
    delay(2600)
    alvik.set_wheels_speed(0, 0)

def curva_90_esq():
    alvik.set_wheels_speed(0, 30)
    delay(2600)
    alvik.set_wheels_speed(0, 0)

def curva_180_dir():
    alvik.set_wheels_speed(30, 0)
    delay(5300)
    alvik.set_wheels_speed(0, 0)

def curva_180_esq():
    alvik.set_wheels_speed(0, 30)
    delay(5300)
    alvik.set_wheels_speed(0, 0)

def giro_360_dir():
  alvik.set_wheels_speed(0, 30)
    delay(10600)
    alvik.set_wheels_speed(0, 0)