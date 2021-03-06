import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def init():
    global v
    global dis
    global mouseMove
    pygame.init()
    display = (1000, 1000)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL | OPENGLBLIT)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 1000.0)
    glEnable(GL_LIGHTING)
    glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, -45, 0, 0, 0, 0, 0, 0, 0.5)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    v = glGetFloatv(GL_MODELVIEW_MATRIX)
    dis = [screen.get_size()[i] // 2 for i in range(2)]
    mouseMove = [0, 0]

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


def start():
    global textura
    global q
    textura = []
    for i in range(1, 9):
        textura.append(load('img/{}.jpg'.format(i)))
    q = gluNewQuadric()
    gluQuadricTexture(q, GL_TRUE)


def mic():
    glBindTexture(GL_TEXTURE_2D, textura[7])
    gluCylinder(q, 5, 1, 5, 30, 30)
    gluCylinder(q, 1.3, 1.3, 50, 30, 30)
    glRotatef(60, 60, 0, 0)
    glTranslatef(0, 43, 17)
    gluCylinder(q, 1.7, 1.7, 15, 40, 40)
    glTranslatef(0, 0, 17)
    glBindTexture(GL_TEXTURE_2D, textura[6])
    gluSphere(q, 3.5, 50, 50)
    glTranslatef(0, 0, -17)
    glBindTexture(GL_TEXTURE_2D, textura[7])
    gluSphere(q, 1.7, 50, 50)


def sphere():
    glColor3fv((0, 0, 0))
    glBindTexture(GL_TEXTURE_2D, textura[4])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 32)
    gluSphere(q, 10, 100, 100)


def svet():
    glColor3fv((1, 1, 1))
    glBindTexture(GL_TEXTURE_2D, textura[4])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-5.0, -5.0, 5.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(5.0, -5.0, 5.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(5.0, 5.0, 5.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-5.0, -5.0, -5.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-5.0, 5.0, -5.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(5.0, 5.0, -5.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(5.0, -5.0, -5.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-5.0, 5.0, -5.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(5.0, 5.0, 5.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(5.0, 5.0, -5.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-5.0, -5.0, -5.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(5.0, -5.0, -5.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(5.0, -5.0, 5.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-5.0, -5.0, 5.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(5.0, -5.0, -5.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(5.0, 5.0, -5.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(5.0, 5.0, 5.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(5.0, -5.0, 5.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-5.0, -5.0, -5.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-5.0, -5.0, 5.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-5.0, 5.0, -5.0)
    glEnd()

def scene():

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, (1, 1, 1))
    glBindTexture(GL_TEXTURE_2D, textura[0])

    glBegin(GL_QUADS)

    glTexCoord2f(1.0, 0.0)
    glVertex3f(-100.0, -50.0, -10.0)
    glNormal3f(-100.0, -50.0, -10.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-100.0, 50.0, -10.0)
    glNormal3f(-100.0, 50.0, -10.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(100.0, 50.0, -10.0)
    glNormal3f(100.0, 50.0, -10.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(100.0, -50.0, -10.0)
    glNormal3f(100.0, -50.0, -10.0)
    glEnd()

    glTranslatef(0, 0, 35)
    glBindTexture(GL_TEXTURE_2D, textura[1])
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-100.0, -50.0, -45.0)
    glNormal3f(-100.0, -50.0, -45.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(100.0, -50.0, -45.0)
    glNormal3f(100.0, -50.0, -45.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(100.0, -50.0, 45.0)
    glNormal3f(100.0, -50.0, 45.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-100.0, -50.0, 45.0)
    glNormal3f(-100.0, -50.0, 45.0)
    glEnd()

    glTranslatef(0, 0, -65)
    glBindTexture(GL_TEXTURE_2D, textura[0])

    glBegin(GL_QUADS)

    glTexCoord2f(1.0, 1.0)
    glVertex3f(-100.0, 50.0, -20.0)
    glNormal3f(-100.0, 50.0, -20.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(100.0, 50.0, -20.0)
    glNormal3f(100.0, 50.0, -20.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(100.0, 50.0, 20.0)
    glNormal3f(100.0, 50.0, 20.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-100.0, 50.0, 20.0)
    glNormal3f(-100.0, 50.0, 20.0)
    glEnd()
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(100.0, -50.0, -20.0)
    glNormal3f(100.0, -50.0, -20.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(100.0, 50.0, -20.0)
    glNormal3f(100.0, 50.0, -20.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(100.0, 50.0, 20.0)
    glNormal3f(100.0, 50.0, 20.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(100.0, -50.0, 20.0)
    glNormal3f(100.0, -50.0, 20.0)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(-100.0, -50.0, -20.0)
    glNormal3f(-100.0, -50.0, -20.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-100.0, -50.0, 20.0)
    glNormal3f(-100.0, -50.0, 20.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-100.0, 50.0, 20.0)
    glNormal3f(-100.0, 50.0, 20.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-100.0, 50.0, -20.0)
    glNormal3f(-100.0, 50.0, -20.0)
    glEnd()


def boombox():
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, (1, 1, 1))
    glBindTexture(GL_TEXTURE_2D, textura[2])
    glColor3fv((1, 1, 1))
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-10, -7.5, 15)
    glNormal3f(-10, -7.5, 15)
    glTexCoord2f(1, 0.0)
    glVertex3f(10, -7.5, 15)
    glNormal3f(10, -7.5, 15)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(10, 7.5, 15)
    glNormal3f(10, 7.0, 15)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-10, 7.5, 15)
    glNormal3f(-10, 7.5, 15)
    glEnd()

    glTranslatef(0, -6.5, 0)
    glBindTexture(GL_TEXTURE_2D, textura[3])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-10, 14.0, -15)
    glNormal3f(-10, 14.0, -15)
    glTexCoord2f(0.0, 2.0)
    glVertex3f(-10, 14.0, 15)
    glNormal3f(-10, 14.0, 15)
    glTexCoord2f(1.0, 2.0)
    glVertex3f(10, 14.0, 15)
    glNormal3f(10, 14.0, 15)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(10, 14.0, -15)
    glNormal3f(10, 14.0, -15)
    glEnd()
    glTranslatef(0, -0.5, 0)

    glBindTexture(GL_TEXTURE_2D, textura[2])
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-10, -0.25, -15)
    glNormal3f(-10, -0.25, -15)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(10, -0.25, -15)
    glNormal3f(10, -0.25, -15)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(10, -0.25, 15)
    glNormal3f(10, -0.25, 15)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-10, -0.25, 15)
    glNormal3f(-10, -0.25, 15)
    glEnd()
    glTranslatef(0, 7, 0)

    glBindTexture(GL_TEXTURE_2D, textura[2])
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(10, -7.5, -15)
    glNormal3f(10, -7.5, -15)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(10, 7.5, -15)
    glNormal3f(10, 7.5, -15)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(10, 7.5, 15)
    glNormal3f(10, 7.5, 15)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(10, -7.5, 15)
    glNormal3f(10, -7.5, 15)
    glEnd()

    glTranslatef(-2, 0, 0)
    glBindTexture(GL_TEXTURE_2D, textura[2])

    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-8, -7.5, -15)
    glNormal3f(-8, -7.5, -15)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-8, 7.5, -15)
    glNormal3f(-8, 7.5, -15)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-8, 7.5, 15)
    glNormal3f(-8, 7.5, 15)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-8, -7.5, 15)
    glNormal3f(-8, -7.5, 15)
    glEnd()


def redisplay():

    glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 0, 0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 0, 0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [1, 0, 0])
    glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 0.0, 0.0, 1])
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.001)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.03)
    svet()

    glTranslatef(150, -60, 0)

    glLightfv(GL_LIGHT1, GL_SPECULAR, [1, 1, 1])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [1, 1, 1])
    glLightfv(GL_LIGHT1, GL_AMBIENT, [1, 1, 1])
    glLightfv(GL_LIGHT1, GL_POSITION, [0.0, 0.0, 0.0, 1])
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.001)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.035)
    svet()

    glTranslatef(-75, 35, -75)
    scene()
    glTranslatef(-75, 10, 36)
    boombox()
    glTranslatef(150, 0, 0)
    boombox()
    glTranslatef(-72, -30, 35)
    sphere()
    glTranslatef(0, 50, -50)
    mic()


init()
start()

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

    glRotatef(mouseMove[0] * 0.1, 0.0, 0.1, 0.0)
    glRotatef(mouseMove[1] * 0.1, 0.1, 0.0, 0.0)

    glMultMatrixf(v)
    v = glGetFloatv(GL_MODELVIEW_MATRIX)

    redisplay()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
