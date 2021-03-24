
from glew_wish import *
import glfw
from math import *
import random


class Obstaculo1:
    posicionX = random.uniform(-.7,.7)
    posicionY = random.uniform(0,.7)
    vivo = False

    def __init__(self, x, y):
        self.posicionX = x
        self.posicionY = y

    def dibujar(self):
        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)
            glBegin(GL_TRIANGLES)   
            glColor3f(1.0, 0.0, .0)
            glVertex3f(0.0, -0.40, 0.0)
            glVertex3f(0.15, -0.15, 0.0)
            glVertex3f(-0.15, -0.15, 0.0)
            glEnd()
            glPopMatrix()
