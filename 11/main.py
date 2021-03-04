import pygame
from pygame.locals import *
from obj import *
from OpenGL.GL import *
from OpenGL.GLU import *


pygame.init()
display = (1000, 700)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glEnable(GL_LIGHTING)
glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)

glEnable(GL_DEPTH_TEST)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_NORMALIZE)
glShadeModel(GL_SMOOTH)
glEnable(GL_TEXTURE_2D)
glEnable(GL_LIGHT1)
bind()
dis = [screen.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_visible(False)

glMatrixMode(GL_PROJECTION)
gluPerspective(60, (display[0] / display[1]), 0.1, 600.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(-100, 45, 45, 0, -2, 0, 0, 0, 0.5)

matrix = glGetFloatv(GL_MODELVIEW_MATRIX)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEMOTION:
            mouseMove = [event.pos[i] - dis[i] for i in range(2)]
            pygame.mouse.set_pos(dis)

    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    keypress = pygame.key.get_pressed()

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

    glRotatef(mouseMove[0] * 0.1, 0.0, 0.1, 0.0)
    glRotatef(mouseMove[0] * 0.1, 0.0, 0.0, 0.1)

    glMultMatrixf(matrix)
    matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    space()
    glTranslatef(0, 0, 10)
    tree()
    glLightfv(GL_LIGHT1, GL_AMBIENT, [0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT1, GL_SPECULAR, [0.7, 0.7, 0.7])
    glLightfv(GL_LIGHT1, GL_POSITION, [50.0, 25.0, 50.0, 1.0])
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.04)
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
