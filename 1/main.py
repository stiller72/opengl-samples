import pygame
from pygame.locals import *
from MeshRenderer import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (900, 640)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glMatrixMode(GL_PROJECTION)
gluPerspective(60, (display[0] / display[1]), 0.1, 3000.0)

glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, 1)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT1)

glEnable(GL_COLOR_MATERIAL)
glEnable(GL_TEXTURE_2D)
glShadeModel(GL_SMOOTH)
glEnable(GL_NORMALIZE)
glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -500, 500, 0, -1, 0, 0, 0, 0.5)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
displayCenter = [screen.get_size()[i] // 2 for i in range(2)]
BindTexture()


mercury_gen = gen(130, 1, 0.001)
venus_gen = gen(200, 360, 0.001)
mars_gen = gen(380, 87, 0.001)
jupiter_gen = gen(500, 34, 0.001)
saturn_gen = gen(650, 350, 0.001)
uranus_gen = gen(750, 1, 0.001)
neptune_gen = gen(850, 140, 0.001)
lune_gen = gen(35, 1, 0.008)
earth_gen = gen(300, 138, 0.001)
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
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
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
        glTranslatef(0, 0, 2)
    if keypress[pygame.K_s]:
        glTranslatef(0, 0, -2)
    if keypress[pygame.K_d]:
        glTranslatef(-2, 0, 0)
    if keypress[pygame.K_a]:
        glTranslatef(2, 0, 0)
    if keypress[pygame.K_q]:
        glTranslatef(0, 2, 0)
    if keypress[pygame.K_e]:
        glTranslatef(0, -2, 0)
    if keypress[pygame.K_UP]:
        glRotatef(3, -3, 0, 0)
    if keypress[pygame.K_DOWN]:
        glRotatef(3, 3, 0, 0)
    if keypress[pygame.K_LEFT]:
        glRotatef(3, 0, -3, 0)
    if keypress[pygame.K_RIGHT]:
        glRotatef(3, 0, 3, 0)

    glMultMatrixf(viewMatrix)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

    sky()
    glLightfv(GL_LIGHT1, GL_AMBIENT, [0.8, 0.7, 0.7])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.8, 0.7, 0.7])
    glLightfv(GL_LIGHT1, GL_SPECULAR, [0.8, 0.7, 0.7])
    glLightfv(GL_LIGHT1, GL_POSITION, [0.0, 0.0, 0.0, 1])
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.001)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.01)
    sun()

    glPushMatrix()
    next(mercury_gen)
    mercury()
    glPopMatrix()

    glPushMatrix()
    next(venus_gen)
    venus()
    glPopMatrix()

    glPushMatrix()
    next(earth_gen)
    earth()
    glPushMatrix()
    next(lune_gen)
    lune()
    glPopMatrix()
    glPopMatrix()

    glPushMatrix()
    next(mars_gen)
    mars()
    glPopMatrix()

    glPushMatrix()
    next(jupiter_gen)
    jupiter()
    glPopMatrix()

    glPushMatrix()
    next(saturn_gen)
    saturn()
    glPopMatrix()

    glPushMatrix()
    next(uranus_gen)
    uranus()
    glPopMatrix()

    glPushMatrix()
    next(neptune_gen)
    neptune()
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
