import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import pi, cos, sin


def init():
    global v
    global dis
    global mouseMove
    global textura
    global q
    textura = []
    pygame.init()
    display = (1000, 1000)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL | OPENGLBLIT)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, (display[0] / display[1]), 0.1, 3000.0)
    glEnable(GL_LIGHTING)
    glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(200, 200, 0, 0, 0, 0, 0, 0, 0.5)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    v = glGetFloatv(GL_MODELVIEW_MATRIX)
    dis = [screen.get_size()[i] // 2 for i in range(2)]
    mouseMove = [0, 0]
    for i in range(1, 6):
        textura.append(load('img/{}.jpg'.format(i)))
    q = gluNewQuadric()
    gluQuadricTexture(q, GL_TRUE)

def load(file_name):

    sur = pygame.image.load(file_name)
    data = pygame.image.tostring(sur, "RGBA", 1)

    width = sur.get_width()
    height = sur.get_height()

    textura = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textura)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, data)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return textura


def tank():
    glColor3fv((1, 1, 1))
    glBindTexture(GL_TEXTURE_2D, textura[1])
    glBegin(GL_QUADS)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(-40.0, -20.0, 5.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(40.0, -20.0, 5.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(40.0, 20.0, 5.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-40.0, 20.0, 5.0)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(-40.0, -20.0, -5.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(40.0, -20.0, -5.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(40.0, 20.0, -5.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-40.0, 20.0, -5.0)

    glEnd()
    glPushMatrix()
    glTranslatef(40, 20, 0)
    glRotatef(90, 90, 0, 0)
    for i in range(9):
        glBindTexture(GL_TEXTURE_2D, textura[0])
        gluCylinder(q, 5, 5, 40, 30, 30)
        circle()
        glTranslatef(0, 0, 40)
        circle()
        glTranslatef(0, 0, -40)
        glTranslatef(-10, 0, 0)
    glPopMatrix()

    glPushMatrix()
    glBegin(GL_QUADS)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(-30.0, -15.0, 10.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(30.0, -15.0, 10.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(30.0, 15.0, 10.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-30.0, 15.0, 10.0)
    glEnd()
    glTranslatef(0, 0, 5)
    glBegin(GL_QUADS)

    glTexCoord2f(0.0, 1.0)
    glVertex3f(-40.0, 20.0, -5.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-30.0, 15.0, 5.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(30.0, 15.0, 5.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(40.0, 20.0, -5.0)

    glTexCoord2f(1.0, 1.0)
    glVertex3f(-40.0, -20.0, -5.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(40.0, -20.0, -5.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(30.0, -15.0, 5.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-30.0, -15.0, 5.0)

    glTexCoord2f(1.0, 0.0)
    glVertex3f(40.0, -20.0, -5.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(40.0, 20.0, -5.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(30.0, 15.0, 5.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(30.0, -15.0, 5.0)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(-40.0, -20.0, -5.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-30.0, -15.0, 5.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-30.0, 15.0, 5.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-40.0, 20.0, -5.0)
    glEnd()
    glPopMatrix()
    glTranslatef(0, 0, 7)
    glPushMatrix()
    glMaterialfv(GL_FRONT, GL_AMBIENT, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 20)
    gluSphere(q, 13, 50, 50)
    glBindTexture(GL_TEXTURE_2D, textura[0])
    glTranslatef(0, 0, 7)
    glRotatef(90, 0, 90, 0)
    gluCylinder(q, 1.5, 2, 40, 30, 30)
    glPopMatrix()


def circle():
    posx, posy = 0, 0
    sides = 32
    radius = 5
    glBindTexture(GL_TEXTURE_2D, textura[1])
    glBegin(GL_POLYGON)
    for i in range(100):

        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
        glTexCoord2f(0.0, 0.0)

    glEnd()


def ground():
    glBindTexture(GL_TEXTURE_2D, textura[3])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1000.0, -1000.0, 0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1000.0, -1000.0, 0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1000.0, 1000.0, 0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1000.0, 1000.0, 0)
    glEnd()
    glBindTexture(GL_TEXTURE_2D, textura[4])
    gluSphere(q, 2000, 50, 50)

def light():
    glBindTexture(GL_TEXTURE_2D, textura[2])
    gluSphere(q, 10, 50, 50)

def redisplay():

    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.2, 0, 0])
    glLightfv(GL_LIGHT1, GL_AMBIENT, [0.2, 0, 0])
    glLightfv(GL_LIGHT1, GL_POSITION, [0.0, 0.0, 0.0, 1])

    glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 0.7, 0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 0.7, 0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [1, 0.7, 0])
    glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 0.0, 0.0, 1])
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.001)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.08)
    light()
    glTranslatef(0, -50, -100)
    tank()
    glTranslatef(0,0,-10)
    ground()

init()


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

    if keypress[pygame.K_DOWN]:
        glTranslatef(0, 1, 0)
    if keypress[pygame.K_UP]:
        glTranslatef(0, -1, 0)

    if keypress[pygame.K_1]:
        glDisable(GL_LIGHT0)
    if keypress[pygame.K_2]:
        glEnable(GL_LIGHT0)
    if keypress[pygame.K_3]:
        glDisable(GL_TEXTURE_2D)
    if keypress[pygame.K_4]:
        glEnable(GL_TEXTURE_2D)

    glRotatef(mouseMove[0] * 0.1, 0.0, 0.1, 0.0)

    glMultMatrixf(v)
    v = glGetFloatv(GL_MODELVIEW_MATRIX)

    redisplay()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
