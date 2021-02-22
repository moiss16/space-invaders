
#---------------area de estres mental de como randomizar los enemigos-----------------#
contador = random.uniform(1,5)
#print("el contador es: " + contador)
def enemigos(): 
    contador2= contador 
    if contador2 < 5:
        xEnemigos = random.uniform(-1.0,1.0) 
        yEnemigos = random.uniform(0,1)

        glBegin(GL_TRIANGLES)
        glVertex3f(xEnemigos, yEnemigos, 0.0)
        glVertex3f(xEnemigos-0.05, yEnemigos+0.05, 0.0)
        glVertex3f(xEnemigos+0.05, yEnemigos+0.05, 0.0)


        glEnd()
        contador2 += 1 

