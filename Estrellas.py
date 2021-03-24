from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import random


class Estrellas: 
    def dibujar(self):
        glPointSize(2)
        glBegin(GL_POINTS)
        xrandom = random.uniform(-1.0,1.0) 
        yrandom = random.uniform(-1.0,1.0) 
        zrandom = random.random()
        glColor3f(1, 1, 1)

        glVertex3d( xrandom, yrandom, zrandom)

        glEnd()