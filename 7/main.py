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
glEnable(GL_LIGHT2)
glEnable(GL_LIGHT3)

x = True
y = True
z = True


a = bind()
dis = [screen.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_visible(False)

glMatrixMode(GL_PROJECTION)
gluPerspective(120, (display[0] / display[1]), 0.1, 600.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(10, 0, 0, 0, 0, 0, 0, 0, 1)

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

    if keypress[pygame.K_1]:
        glDisable(GL_LIGHT1)
        x = False
    if keypress[pygame.K_2]:
        glEnable(GL_LIGHT1)
        x = True

    if keypress[pygame.K_3]:
        glDisable(GL_LIGHT2)
        y = False
    if keypress[pygame.K_4]:
        glEnable(GL_LIGHT2)
        y = True

    if keypress[pygame.K_5]:
        glDisable(GL_LIGHT3)
        z = False
    if keypress[pygame.K_6]:
        glEnable(GL_LIGHT3)
        z = True

    if keypress[pygame.K_7]:
        glDisable(GL_TEXTURE_2D)
    if keypress[pygame.K_8]:
        glEnable(GL_TEXTURE_2D)

    glRotatef(mouseMove[0] * 0.1, 0.0, 0.1, 0.0)
    glRotatef(mouseMove[0] * 0.1, 0.0, 0.0, 0.1)

    glMultMatrixf(matrix)
    matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    space()
    glTranslatef(50, 63, -29)
    glBindTexture(GL_TEXTURE_2D, a[8])
    box()
    glTranslatef(13, -13, 0)
    glBindTexture(GL_TEXTURE_2D, a[9])
    box()
    glTranslatef(0, 13, 13)
    glBindTexture(GL_TEXTURE_2D, a[7])
    box()
    glTranslatef(-100, -100, -20)
    glPushMatrix()
    candle1(x)
    glLightfv(GL_LIGHT1, GL_SPECULAR, [0, 0, 1])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0, 0, 1])
    glLightfv(GL_LIGHT1, GL_AMBIENT, [0, 0, 0.7])
    glLightfv(GL_LIGHT1, GL_POSITION, [0.0, 0.0, 0.0, 1])
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.09)
    glPopMatrix()
    glTranslatef(70, 0, 0)
    glPushMatrix()
    candle2(y)
    glLightfv(GL_LIGHT2, GL_SPECULAR, [1, 0, 0])
    glLightfv(GL_LIGHT2, GL_DIFFUSE, [1, 0, 0])
    glLightfv(GL_LIGHT2, GL_AMBIENT, [0.7, 0, 0])
    glLightfv(GL_LIGHT2, GL_POSITION, [0.0, 0.0, 0.0, 1])
    glLightf(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.09)
    glPopMatrix()
    glTranslatef(-70, 70, 0)
    glPushMatrix()
    candle3(z)
    glLightfv(GL_LIGHT3, GL_SPECULAR, [1, 1, 1])
    glLightfv(GL_LIGHT3, GL_DIFFUSE, [0, 1, 0])
    glLightfv(GL_LIGHT3, GL_AMBIENT, [0, 1, 0])
    glLightfv(GL_LIGHT3, GL_POSITION, [0.0, 0.0, 0.0, 1])
    glLightf(GL_LIGHT3, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT3, GL_LINEAR_ATTENUATION, 0.09)
    glPopMatrix()
    glTranslatef(40, -40, 19)
    tree()
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
