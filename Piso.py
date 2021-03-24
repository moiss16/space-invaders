from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import random


class Piso:
    posicionX=0
    posicionY=0


    def dibujar(self):
        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glBegin(GL_POLYGON)
        glColor3f(0.0941, 0, 0.27058)
        glVertex(-1,-1,0.0)
        glVertex(1,-1,0.0)
        glVertex(1,-.7,0.0)
        glVertex(-1,-.7,0.0)
        glEnd()
        glPopMatrix()