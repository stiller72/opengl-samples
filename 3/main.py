import pygame
from pygame.locals import *
from MeshRenderer import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (900, 640)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glMatrixMode(GL_PROJECTION)
gluPerspective(60, (display[0] / display[1]), 0.1, 6000.0)

glEnable(GL_LIGHTING)
glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
glEnable(GL_LIGHT0)
glEnable(GL_LIGHT1)
glEnable(GL_LIGHT2)
glEnable(GL_DEPTH_TEST)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_TEXTURE_2D)
glShadeModel(GL_SMOOTH)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, 90, 90, 0, -1, 0, 0, 0, 0.5)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
displayCenter = [screen.get_size()[i] // 2 for i in range(2)]
BindTexture()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    keypress = pygame.key.get_pressed()

    if keypress[pygame.K_1]:
        glDisable(GL_LIGHT0)
    if keypress[pygame.K_2]:
        glEnable(GL_LIGHT0)
    if keypress[pygame.K_3]:
        glDisable(GL_LIGHT1)
    if keypress[pygame.K_4]:
        glEnable(GL_LIGHT1)
    if keypress[pygame.K_5]:
        glDisable(GL_LIGHT2)
    if keypress[pygame.K_6]:
        glEnable(GL_LIGHT2)
    if keypress[pygame.K_7]:
        glDisable(GL_TEXTURE_2D)
    if keypress[pygame.K_8]:
        glEnable(GL_TEXTURE_2D)

    if keypress[pygame.K_w]:
        glTranslatef(0, 0, 1)
    if keypress[pygame.K_s]:
        glTranslatef(0, 0, -1)
    if keypress[pygame.K_d]:
        glTranslatef(-1, 0, 0)
    if keypress[pygame.K_a]:
        glTranslatef(1, 0, 0)
    if keypress[pygame.K_q]:
        glTranslatef(0, 1, 0)
    if keypress[pygame.K_e]:
        glTranslatef(0, -1, 0)
    if keypress[pygame.K_UP]:
        glRotatef(1, -1, 0, 0)
    if keypress[pygame.K_DOWN]:
        glRotatef(1, 1, 0, 0)
    if keypress[pygame.K_LEFT]:
        glRotatef(1, 0, -1, 0)
    if keypress[pygame.K_RIGHT]:
        glRotatef(1, 0, 1, 0)

    glMultMatrixf(viewMatrix)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

    table()
    glTranslatef(-20, -15, 50)
    lamp()
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, 0, 1.0])
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.07)

    glTranslatef(0, -20, 0)
    lamp()
    glLightfv(GL_LIGHT1, GL_AMBIENT, [0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT1, GL_SPECULAR, [0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT1, GL_POSITION, [0, 0, 0, 1.0])
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 1)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.07)
    glTranslatef(0, -20, 0)
    lamp()
    glLightfv(GL_LIGHT2, GL_AMBIENT, [0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT2, GL_DIFFUSE, [0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT2, GL_SPECULAR, [0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT2, GL_POSITION, [0, 0, 0, 1.0])
    glLightf(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 1)
    glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.07)
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
