try:
    import OpenGL as ogl
    try:
        import OpenGL.GL   # this fails in <=2020 versions of Python on OS X 11.x
    except ImportError:
        print('Drat, patching for Big Sur')
        from ctypes import util
        orig_util_find_library = util.find_library
        def new_util_find_library( name ):
            res = orig_util_find_library( name )
            if res: return res
            return '/System/Library/Frameworks/'+name+'.framework/'+name
        util.find_library = new_util_find_library
except ImportError:
    pass


from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
import random

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


xNave = 0.0
yNave = -0.8

colisionando = False

angulo = 0
# el desfase es debido a que el triangulo en 0 grados voltea
# hacia arriba y no hacia la derecha
desfase = 90

velocidad = 1
velocidad_angular = 180

tiempo_anterior = 0

# Indicador si hay "bala" viva o no
disparando = False
xBala = 0
yBala = 0






def actualizar_bala(tiempo_delta):
    global disparando
    global xBala
    global yBala
    global anguloBala
    global velocidad
    global obstaculoVivo
    global obstaculoVivo1
    global xObstaculo
    global yObstaculo
    global xObstaculo1
    global yObstaculo1
    if disparando:
        if xBala >= 1:
            disparando = False
        elif xBala <= -1:
            disparando = False
        elif yBala >= 1:
            disparando = False
        elif yBala <= -1:
            disparando = False
        print("Disparando")
        yBala = yBala + \
            (sin((anguloBala + desfase) * 3.14159 / 180) * velocidad * tiempo_delta)
        xBala = xBala + \
            (cos((anguloBala + desfase) * 3.14159 / 180) * velocidad * tiempo_delta)
        # checar colision con obstaculo si sigue "vivo"
        if obstaculoVivo and xBala + 0.01 > xObstaculo - 0.15 and xBala - 0.01 < xObstaculo + 0.15 and yBala + 0.01 > yObstaculo - 0.15 and yBala - 0.01 < yObstaculo + 0.15:
           
            obstaculoVivo = False
            disparando = False
            obstaculoVivo1 = True

            xObstaculo1 = random.uniform(-.7,.7)

            yObstaculo1 = random.uniform(0,.7)




        if obstaculoVivo1 and xBala + 0.01 > xObstaculo1 - 0.15 and xBala - 0.01 < xObstaculo1 + 0.15 and yBala + 0.01 > yObstaculo1 - 0.15 and yBala - 0.01 < yObstaculo1 + 0.15:
         
            obstaculoVivo1 = False
            disparando = False
            obstaculoVivo = True

            xObstaculo = random.uniform(-.7,.7)

            yObstaculo = random.uniform(0,.7)

            
            



def actualizar(window):
    global tiempo_anterior
    global angulo
    global xNave
    global yNave

    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior

    estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
    estadoArriba = glfw.get_key(window, glfw.KEY_UP)

    if estadoAbajo == glfw.PRESS:
        yNave -= 0.001

    if estadoIzquierda == glfw.PRESS:
        angulo = angulo + (velocidad_angular * tiempo_delta)
        if angulo > 360:
            angulo = 0
    if estadoDerecha == glfw.PRESS:
        angulo = angulo - (velocidad_angular * tiempo_delta)
        if angulo < 0:
            angulo = 360

    if estadoArriba == glfw.PRESS:
        yNave = yNave + \
            (sin((angulo + desfase) * 3.14159 / 180) * velocidad * tiempo_delta)
        xNave = xNave + \
            (cos((angulo + desfase) * 3.14159 / 180) * velocidad * tiempo_delta)

   
    actualizar_bala(tiempo_delta)
    tiempo_anterior = tiempo_actual

def dibujarfigura():
    glBegin(GL_QUADS)
    glColor3f(0,0.9,1.0)
    glVertex3f(0.12,-.28,0.0)
    glVertex3f(0.20,-.28,0.0)
    glVertex3f(0.20,-.17,0.0)
    glVertex3f(0.12,-.17,0.0)
    glEnd()

def dibujarCirculo():
    glColor3f(.0, 1.0, .0)
    glBegin(GL_POLYGON)
    for x in range (360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.07 -.6, sin(angulo) * 0.07 +.2, 0.0)
    glEnd()

def figuronas():

    a = random.uniform(-0.5,0.5)
    b = random.uniform(-0.5,0.5)
    c = random.uniform(-0.5,5)

    glBegin(GL_QUADS)
    glColor3f(.0, 1.0, .0)
    glVertex3f(-1,-.9,0)
    glVertex3f(1,-.9,0)
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


def dibujar_bala():
    global disparando
    global xBala
    global yBala
    if disparando == True:
        glPushMatrix()
        glTranslate(xBala, yBala, 0.0)
        glRotate(anguloBala, 0.0, 0.0, 1.0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(-0.01, 0.01, 0.0)
        glVertex3f(0.01, 0.01, 0.0)
        glVertex3f(0.01, -0.01, 0.0)
        glVertex3f(-0.01, -0.01, 0.0)
        glEnd()
        glPopMatrix()


def dibujarNave():
    global colisionando
    global xNave
    global yNave
    glPushMatrix()
    glTranslate(xNave, yNave, 0.0)
    glRotate(angulo, 0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    if colisionando == True:
        glColor3f(1.0, 1.0, 1.0)
    else:
        glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.0, 0.05, 0.0)
    glVertex3f(-0.05, -0.05, 0.0)
    glVertex3f(0.05, -0.05, 0.0)
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
    estrellas()
    figuronas()
    dibujarfigura()
    dibujarCirculo()
    dibujarObstaculo()
    dibujarObstaculo1()
    dibujarNave()
    dibujar_bala()
    

def key_callback(window, key, scancode, action, mods):
    global disparando
    global anguloBala
    global xBala
    global yBala
    if not disparando and key == glfw.KEY_SPACE and action == glfw.PRESS:
        disparando = True
        xBala = xNave
        yBala = yNave
        anguloBala = angulo
        

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(1600,1600,"space invaders", None, None)

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

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,1600,1600)
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