from OpenGL.GL import *
from glew_wish import *
import glfw
import random


xObstaculo = 0.0
yObstaculo = 0.2

xNave = 0.0
yNave = -0.8

colisionando = False

def checar_colisiones():
    global colisionando

    #Si extremaDerechaCarrito > extremaIzquierdaObstaculo
    if yNave + 0.01 <  yObstaculo - 0.15:
        colisionando = True
        
    else:
        colisionando = False

def actualizar(window):
    global xNave
    global yNave

   #------------------------movimiento de la nave-----------------------# 

    estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT )
    estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT )
    estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN )
    estadoArriba = glfw.get_key(window, glfw.KEY_UP )
    estadoIzquierda2 = glfw.get_key(window,  glfw.KEY_A)
    estadoDerecha2 = glfw.get_key(window,  glfw.KEY_D)
    estadoAbajo2 = glfw.get_key(window,  glfw.KEY_S)
    estadoArriba2 = glfw.get_key(window, glfw.KEY_W)

    turboDerecha = glfw.get_key(window, glfw.KEY_L)
    turboIzquierda = glfw.get_key(window, glfw.KEY_J)

    if estadoIzquierda == glfw.PRESS:
        xNave -= 0.01
    if estadoDerecha == glfw.PRESS:
        xNave += 0.01
    if estadoAbajo == glfw.PRESS:
        yNave -= 0.01
    if estadoArriba == glfw.PRESS:
        yNave += 0.01
    if estadoIzquierda2 == glfw.PRESS:
        xNave -= 0.01
    if estadoDerecha2 == glfw.PRESS:
        xNave += 0.01
    if estadoAbajo2 == glfw.PRESS:
        yNave -= 0.01
    if estadoArriba2 == glfw.PRESS:
        yNave += 0.01
    if turboDerecha == glfw.PRESS:
        xNave += 0.05
    if turboIzquierda == glfw.PRESS:
        xNave -= 0.05

    checar_colisiones()

def dibujarObstaculo():
    global xObstaculo
    global yObstaculo

    glPushMatrix()
    glTranslate(xObstaculo, yObstaculo, 0.0)
    glBegin(GL_QUADS)
    glColor(0.0, 0.0, 1.0)
    glVertex3f(-0.15, 0.15, 0.0)
    glVertex3f(0.15, 0.15, 0.0)
    glVertex3f(0.15, -0.15, 0.0)
    glVertex3f(-0.15, -0.15, 0.0)
    glEnd()

    glPopMatrix()

def dibujarNave():
    global xNave
    global yNave

    glPushMatrix()
    glTranslate(xNave, yNave, 0.0)
    glBegin(GL_TRIANGLES)

    if colisionando == True:
        glColor3f(1, 1, 1)
    else:
        glColor3f(1, 0, 0)
    

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
    dibujarObstaculo()
    dibujarNave()
    estrellas()

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

#-----------------#

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