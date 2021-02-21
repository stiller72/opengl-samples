from pygame.locals import *
from models import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame


pygame.init()
display = (1600, 900)  # set display resolution
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL | OPENGLBLIT) #default setup

glMatrixMode(GL_PROJECTION) #choose matrix for display
gluPerspective(60, (display[0] / display[1]), 0.1, 6000.0) #setup perspective, where first varible - FOV, 
                                                            #last variable is detail distance

glEnable(GL_LIGHTING) # turn on light for project

glEnable(GL_NORMALIZE) #turn on normalization for best experiance (better light)

glEnable(GL_LIGHT0) #turn on first light by default (can be commented)
glEnable(GL_LIGHT1) #turn on second light by default (can be commented)
glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, 0)
glEnable(GL_DEPTH_TEST)#turn on depth for better experince 

glEnable(GL_COLOR_MATERIAL)#turn on color for material, show true colors for texture when affected by light

glMatrixMode(GL_MODELVIEW) #turn on model matrix (this matrix for "drawing" our objects)

glShadeModel(GL_SMOOTH)# turn on smooth for high quality edges of textures

gluLookAt(0, -15, 0, 0, 0, 0, 0, 0, 0.5) #settings for point of view, first three arguments for user "camera", second for objects, last argument prefably dont touch

glEnable(GL_TEXTURE_2D)# our main settings for our texture, by enabling it we can use our textures

viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)#set up default arguments for our matrix, used further

displayCenter = [screen.get_size()[i] // 2 for i in range(2)] #calculating our center of display, needed for mouse controling

mouseMove = [0, 0]# set default list for mouse controlling

pygame.mouse.set_visible(False)# turn of our mouse cursor 

start()# this function load all texture(models include)

while True:# standart while-loop (body)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:# press esc button for close appllication
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEMOTION:
            mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]# change mouse constants (x,y)
            pygame.mouse.set_pos(displayCenter)

    glLoadIdentity()#load default matrix
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)#clear visible buffer

    glRotatef(mouseMove[0] * 0.1, 0.0, 0.1, 0.0)#mouse rotation by x-cord
    glRotatef(mouseMove[1] * 0.1, 0.1, 0.0, 0.0)#mouse rotation by y-cord

    keypress = pygame.key.get_pressed()#event for buttons
    if keypress[pygame.K_w]:
        glTranslatef(0, 0, 2)
    if keypress[pygame.K_s]:
        glTranslatef(0, 0, -2)
    if keypress[pygame.K_d]:
        glTranslatef(-2, 0, 0)
    if keypress[pygame.K_a]:
        glTranslatef(2, 0, 0)
    if keypress[pygame.K_1]:
        glDisable(GL_LIGHT0)
    if keypress[pygame.K_2]:
        glEnable(GL_LIGHT0)
    if keypress[pygame.K_3]:
        glDisable(GL_LIGHT1)
    if keypress[pygame.K_4]:
        glEnable(GL_LIGHT1)
    if keypress[pygame.K_5]:
        glDisable(GL_TEXTURE_2D)
    if keypress[pygame.K_6]:
        glEnable(GL_TEXTURE_2D)

    glMultMatrixf(viewMatrix)# multiply matrix for change position, affected by moving 
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)# save our new postion

    glPushMatrix()#drawing

    sphere()#draw sphere (see 'models')
    glTranslatef(-15, 5, 0) 

    for i in range(3):
        glTranslatef(0, 2, 0)
        for i in range(5):
            creeper()
            glTranslatef(0, 5, 0)
    glTranslatef(5, -80, 0)
    for i in range(3):
        glTranslatef(0, 2, 0)
        for i in range(5):
            creeper()
            glTranslatef(0, 5, 0)

    glTranslatef(-5, 5, -15.7)
    ground()
    glTranslatef(0, -45, 25.7)
    draw_cube()

    glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 0, 0])#choose specular color for light0
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0, 0])#choose diffuse color for light0
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.7, 0, 0])#choose ambient color for light0
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, -4, 1.0])#position for light0
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.01)#constant of attenuation
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.2)#linear method to set attenuation
    glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_FALSE)
    glLightfv(GL_LIGHT1, GL_AMBIENT, [0.2, 0.2, 0.2])
    glLightfv(GL_LIGHT1, GL_POSITION, [0.0, 0.0, 1.0, 0.0])
    glTranslatef(-15, 0, 0)

    blik()
    glPopMatrix()
    pygame.display.flip()#redraw
    pygame.time.wait(10)#FPS more->lower FPS


pygame.quit()
