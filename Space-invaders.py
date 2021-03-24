

###---DISPARAR AL OBJETIVO ROJO---###

from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import random
from Bala import *
from Carrito import *
from Obstaculo import *

obstaculos= []


carrito = Carrito()
obstaculo = Obstaculo(0.4, 0.6)
segundoObstaculo = Obstaculo(-0.5, 0.3)

xObstaculo = random.uniform(-.7,.7)
print('este es el obsta : ' + str(xObstaculo))
yObstaculo = random.uniform(0,.7)
print('este es el obsta : ' + str(yObstaculo))
obstaculoVivo = True
xObstaculo1 = random.uniform(-.7,.7)
print('este es el obsta : ' + str(xObstaculo1))
yObstaculo1 = random.uniform(0,.7)
print('este es el obsta : ' + str(yObstaculo1))
obstaculoVivo1 = False


colisionando = False

angulo = 0
# el desfase es debido a que el triangulo en 0 grados voltea
# hacia arriba y no hacia la derecha



velocidad_angular = 180

tiempo_anterior = 0

# Indicador si hay "bala" viva o no
disparando = False



def inicializarObstaculos():
    global obstaculos
    obstaculos.append(Obstaculo(random.uniform(-.7,.7), random.uniform(.3,.7)))
    obstaculos.append(Obstaculo(random.uniform(-.7,.7), random.uniform(.3,.7)))
    obstaculos.append(Obstaculo(random.uniform(-.7,.7), random.uniform(.3,.7)))
    



def actualizar(window):
    global tiempo_anterior
    global carrito
    global obstaculos

    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior

    carrito.actualizar(window, tiempo_delta)

    for obstaculo in obstaculos:
        if obstaculo.vivo:
            carrito.checar_colisiones(obstaculo)
            if carrito.colisionando:
                break
    
    tiempo_anterior = tiempo_actual

def dibujarfigura():
    glBegin(GL_QUADS)
    glColor3f(.41,.1,0.6)
    glVertex3f(0.12,-.28,0.0)
    glVertex3f(0.20,-.28,0.0)
    glVertex3f(0.20,-.17,0.0)
    glVertex3f(0.12,-.17,0.0)
    glEnd()

def dibujarCirculo():
    glColor3f(.011, .011, .6588)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.05 -.6, sin(angulo) * 0.05 +.2, 0.0)
    glEnd()


def dibujarCirculo2():
    glColor3f(0.19, 0.054, 0.27)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.03 +.7, sin(angulo) * 0.03 , 0.0)
    glEnd()
    
def dibujarPoligono():
    
    glBegin(GL_POLYGON)
    glColor3f(1, 0, 0.7)
    glVertex(-0.3,-0.3,0.0)
    glVertex(-0.3,-0.2,0.0)
    glVertex(-0.25,-0.15,0.0)
    glVertex(-0.2,-0.2,0.0)
    glVertex(-0.2,-0.3,0.0)
    glEnd()

def dibujarTriangulo():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0.7)
    glVertex3f(-0.85,.1,0)
    glVertex3f(-0.9,-0.1,0)
    glVertex3f(-0.85,-0.15,0)
    glEnd()
   
def dibujarCirculo3():
    glColor3f(1, 0, 0.7)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.03 +.02, sin(angulo) * 0.01 +.07, 0.0)
    glEnd()
    
def dibujarCirculo4():
    glColor3f(.011, .011, .6588)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 +.02, sin(angulo) * 0.08 -.5, 0.0)
    glEnd()
    
def dibujarPoligono2():
    
    glBegin(GL_POLYGON)
    glColor3f(.011, .011, .6588)
    glVertex(0.4,0.3,0.0)
    glVertex(0.4,0.2,0.0)
    glVertex(0.3,0.15,0.0)
    glVertex(0.3,0.2,0.0)
    glVertex(0.3,0.3,0.0)
    glEnd()

def dibujarPoligono3():
    
    glBegin(GL_POLYGON)
    glColor3f(.011, .011, .6588)
    glVertex(0.4,-0.5,0.0)
    glVertex(0.4,-0.4,0.0)
    glVertex(0.6,-0.4,0.0)
    glVertex(0.6,-0.35,0.0)
    
    glEnd()

def dibujarTriangulo3():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0.7)
    glVertex3f(0.85,.1,0)
    glVertex3f(0.9,-0.1,0)
    glVertex3f(0.85,0.15,0)
    glEnd()
    
def dibujarTriangulo4():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0.7)
    glVertex3f(-0.6,-0.5,0)
    glVertex3f(-0.4,-0.4,0)
    glVertex3f(-0.6,-0.4,0)
    glEnd()

def figuronas():

    a = random.uniform(-0.5,0.5)
    b = random.uniform(-0.5,0.5)
    c = random.uniform(-0.5,5)

    glBegin(GL_QUADS)
    glColor3f(0.19, 0.054, 0.27)
    glVertex3f(-1,-.7,0)
    glVertex3f(1,-.7,0)
    glVertex3f(1,-1,0)
    glVertex3f(-1,-1,0)
    glEnd()

    glColor3f(1,1,0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-8,-.8,0)
    glVertex3f(-.85,-0.8,0)
    glVertex3f(-0.8,-0.75,0)
    
    glEnd()

    glColor3f(1,1,0.6)
    glBegin(GL_TRIANGLES)
    glVertex3f(-.68,-.5,0)
    glVertex3f(-.75,-0.5,0)
    glVertex3f(-0.68,-0.45,0)
    
    glEnd()

    glColor3f(1,.1,0.6)
    glBegin(GL_TRIANGLES)
    glVertex3f(.68,-.5,0)
    glVertex3f(.75,-0.5,0)
    glVertex3f(0.68,-0.65,0)
    
    glEnd()
    glColor3f(.1,.1,0.6)
    glBegin(GL_TRIANGLES)
    glVertex3f(.68,-.85,0)
    glVertex3f(.75,-0.85,0)
    glVertex3f(0.68,-0.65,0)
    
    glEnd()
    
    glColor3f(.41,.1,0.6)
    glBegin(GL_TRIANGLES)
    glVertex3f(.868,-.5,0)
    glVertex3f(.875,-0.5,0)
    glVertex3f(0.868,-0.6,0)
    
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(.50, 1.0, .50)
    glVertex3f(-.8,.9,0)
    glVertex3f(-.77,.9,0)
    glVertex3f(-.77,.8,0)
    glVertex3f(-.8,.8,0)
    glEnd()




def dibujarObstaculo():
    global xObstaculo
    global yObstaculo

    if obstaculoVivo:
        glPushMatrix()
        glTranslate(xObstaculo, yObstaculo, 0.0)
        glBegin(GL_TRIANGLES)
        colores = random.uniform(1,-1)
        glColor3f(1.0, 0.0, .0)
        glVertex3f(0.0, -0.40, 0.0)
        glVertex3f(0.15, -0.15, 0.0)
        glVertex3f(-0.15, -0.15, 0.0)
        glEnd()
        glPopMatrix()

def dibujarObstaculo1():
    global xObstaculo1
    global yObstaculo1

    if obstaculoVivo1:
        glPushMatrix()
        glTranslate(xObstaculo1, yObstaculo1, 0.0)
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, .0)
        glVertex3f(0.0, -0.30, 0.0)
        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(-0.1, -0.1, 0.0)
        glEnd()
        glPopMatrix()





def estrellas(): 
    glPointSize(2)
    glBegin(GL_POINTS)
    xrandom = random.uniform(-1.0,1.0) 
    yrandom = random.uniform(-1.0,1.0) 
    zrandom = random.random()
    glColor3f(1, 1, 1)
    
    glVertex3d( xrandom, yrandom, zrandom)

    glEnd()



def dibujar():
    #rutinas de dibujo
    global carrito
    global obstaculos
  
    # rutinas de dibujo
   
   
    estrellas()
    #figuronas()
    #dibujarfigura()
    #dibujarCirculo2()
    #dibujarCirculo()
    #dibujarPoligono()
    #dibujarTriangulo()
    #dibujarCirculo3()
    #dibujarCirculo4()
    #dibujarPoligono2()
    #dibujarPoligono3()
    #dibujarObstaculo()
    #dibujarObstaculo1()
    for obstaculo in obstaculos:
       obstaculo.dibujar()
    carrito.dibujar()

  
    
    #dibujarTriangulo3()
    #dibujarTriangulo4()
    
    

def key_callback(window, key, scancode, action, mods):
    global carrito
    if not carrito.disparando and key == glfw.KEY_SPACE and action == glfw.PRESS:
        carrito.disparar()
        

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"space invaders", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)
    glfw.set_key_callback(window, key_callback)
#-----------------#
    inicializarObstaculos()

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0.0,0.0,0.0,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        actualizar(window)
        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()


if __name__ == "__main__":
    main()