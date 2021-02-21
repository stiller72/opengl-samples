import pygame
from pygame.locals import *
from MeshRenderer import *
from OpenGL.GL import *
from OpenGL.GLU import *
# import time

pygame.init()
display = (900, 640)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glMatrixMode(GL_PROJECTION)
gluPerspective(60, (display[0] / display[1]), 0.1, 6000.0)

glEnable(GL_LIGHTING)
glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
glEnable(GL_LIGHT1)
# glEnable(GL_LIGHT0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_TEXTURE_2D)
glShadeModel(GL_SMOOTH)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, 120, 120, 0, -1, 0, 0, 0, 0.5)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
displayCenter = [screen.get_size()[i] // 2 for i in range(2)]
ball_1 = gen2(10, 6.20, 0.05)
ball_2 = gen1(-10, 6.20, 0.05)
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

    # if keypress[pygame.K_1]:
    #     glDisable(GL_LIGHT0)
    # if keypress[pygame.K_2]:
    #     glEnable(GL_LIGHT0)
    if keypress[pygame.K_1]:
        glDisable(GL_LIGHT1)
    if keypress[pygame.K_2]:
        glEnable(GL_LIGHT1)
    if keypress[pygame.K_3]:
        glDisable(GL_TEXTURE_2D)
    if keypress[pygame.K_4]:
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

    glLightfv(GL_LIGHT1, GL_AMBIENT, [0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT1, GL_SPECULAR,[0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT1, GL_POSITION, [50.0, 25.0, 50.0, 1.0])
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.04)
    glPushMatrix()
    const()
    glPopMatrix()
    glRotatef(-20, 20, 0, 0)
    glTranslatef(-20, -15, 40)
    glPushMatrix()
    glTranslatef(0.2, 0, 0)
    next(ball_1)
    ball()
    glPopMatrix()
    glTranslatef(10, 0, 0)
    glPushMatrix()
    ball()
    glPopMatrix()
    glTranslatef(10, 0, 0)
    glPushMatrix()
    ball()
    glPopMatrix()
    glTranslatef(10, 0, 0)
    glPushMatrix()
    ball()
    glPopMatrix()
    glTranslatef(10, 0, 0)
    glPushMatrix()
    glTranslatef(-0.2, 0, 0)
    next(ball_2)
    ball()
    glPopMatrix()
    
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
