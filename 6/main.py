import pygame
from pygame.locals import *
from MeshRenderer import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (900, 640)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL )

glMatrixMode(GL_PROJECTION)
gluPerspective(60, (display[0] / display[1]), 0.1, 6000.0)

glEnable(GL_LIGHTING)
glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
glEnable(GL_LIGHT0)
glEnable(GL_LIGHT1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_TEXTURE_2D)
glEnable(GL_LIGHT2)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -90, 0, 0, -1, 0, 0, 0, 0.5)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
displayCenter = [screen.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_visible(False)
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
        if event.type == pygame.MOUSEMOTION:
            mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
            pygame.mouse.set_pos(displayCenter)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    keypress = pygame.key.get_pressed()

    glRotatef(mouseMove[0] * 0.1, 0.0, 0.1, 0.0)
    glRotatef(mouseMove[1] * 0.1, 0.1, 0.0, 0.0)

    if keypress[pygame.K_t]:
        glDisable(GL_LIGHT0)
    if keypress[pygame.K_y]:
        glEnable(GL_LIGHT0)
    if keypress[pygame.K_1]:
        glDisable(GL_LIGHT1)
    if keypress[pygame.K_2]:
        glEnable(GL_LIGHT1)
    if keypress[pygame.K_r]:
        glDisable(GL_TEXTURE_2D)
    if keypress[pygame.K_e]:
        glEnable(GL_TEXTURE_2D)

    if keypress[pygame.K_UP]:
        glTranslatef(0, 0, 1)
    if keypress[pygame.K_DOWN]:
        glTranslatef(0, 0, -1)
    if keypress[pygame.K_RIGHT]:
        glTranslatef(-1, 0, 0)
    if keypress[pygame.K_LEFT]:
        glTranslatef(1, 0, 0)

    glMultMatrixf(viewMatrix)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

    glLightfv(GL_LIGHT1, GL_AMBIENT, [0.3, 0.3, 0.3])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.8, 0.8, 0.8])
    glLightfv(GL_LIGHT1, GL_POSITION, [0.0, 0.0, 0.0, 0.0])

    sphere()
    glTranslatef(0, 0, -20)
    steve()
    glTranslatef(-20, 0, 6.5)
    steve()
    glTranslatef(12, -15, 10)
    cube()
    glTranslatef(0, 10, -10)
    light()
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 0.7, 0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 0.7, 0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [1, 0.7, 0])
    glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 0.0, 0.0, 1])
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.001)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.3)
    glTranslatef(0, 0, 20)
    sphere1()
    glTranslatef(0, 0, -1522)
    ground()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
