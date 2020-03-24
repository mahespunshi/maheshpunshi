from random import randint
from time import clock

##=====================================
State = type("State", (object,), {})

class LightON(state):
    def Execute(self):
        print("Light is On!")


class LightOFF(state):
    def Execute(self):
        print("Light is OFF!")

##=====================================
class Transition(object):


##=====================================
