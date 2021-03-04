from math import pi, cos, sin
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame


def load(file_name):

    textureSurface = pygame.image.load(file_name)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)

    width = textureSurface.get_width()
    height = textureSurface.get_height()

    texid = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texid)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid


def bind():
    global texid
    global qobj
    texid = []
    for i in range(1, 11):
        texid.append(load('image/{}.jpg'.format(i)))
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)
    return texid


def circle(x):
    posx, posy = 0, 0
    sides = 30
    radius = x

    glBegin(GL_POLYGON)
    for i in range(100):

        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
        glTexCoord2f(0.0, 0.0)

    glEnd()


def sphere():
    glPushMatrix()
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0, 0, 0))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 0, 0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0, 0.5, 0))
    glMaterialfv(GL_FRONT, GL_SHININESS, 12)
    gluSphere(qobj, 3, 50, 50)
    glPopMatrix()


def space():
    glBindTexture(GL_TEXTURE_2D, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-500.0, -500.0, -10.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-500.0, 500.0, -10.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(500.0, 500.0, -10.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(500.0, -500.0, -10.0)
    glEnd()


def tree():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, 5)
    gluCylinder(qobj, 27, 1, 30, 30, 30)
    circle(27)
    glTranslatef(0, 0, -10)
    gluCylinder(qobj, 30, 1, 35, 30, 30)
    circle(30)
    glPopMatrix()
    glTranslatef(0, 0, -10)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0, 0, 0))

    glPushMatrix()
    glTranslatef(-25, 0, 7)
    glBindTexture(GL_TEXTURE_2D, texid[3])
    sphere()
    glTranslatef(50, 0, 0)
    glBindTexture(GL_TEXTURE_2D, texid[8])
    sphere()
    glTranslatef(-25, 25, 0)
    glBindTexture(GL_TEXTURE_2D, texid[7])
    sphere()
    glTranslatef(0, -50, 0)
    glBindTexture(GL_TEXTURE_2D, texid[9])
    sphere()
    glPopMatrix()
    glTranslatef(0, 0, 20)
    glBindTexture(GL_TEXTURE_2D, 5)
    gluCylinder(qobj, 23, 1, 25, 30, 30)
    circle(23)
    glPushMatrix()
    glTranslatef(-15.5, 15.5, -3)
    glBindTexture(GL_TEXTURE_2D, texid[7])
    sphere()
    glTranslatef(31, -31, 0)
    glBindTexture(GL_TEXTURE_2D, texid[3])
    sphere()
    glTranslatef(0, 31, 0)
    glBindTexture(GL_TEXTURE_2D, texid[5])
    sphere()
    glTranslatef(-31, -31, 0)
    glBindTexture(GL_TEXTURE_2D, texid[9])
    sphere()
    glPopMatrix()

    glBindTexture(GL_TEXTURE_2D, texid[4])
    glTranslatef(0, 0, -5)

    glPushMatrix()
    glTranslatef(-17, 0, 11)
    glBindTexture(GL_TEXTURE_2D, texid[5])
    sphere()
    glTranslatef(34, 0, 0)
    glBindTexture(GL_TEXTURE_2D, texid[7])
    sphere()
    glTranslatef(-17, 17, 0)
    glBindTexture(GL_TEXTURE_2D, texid[6])
    sphere()
    glTranslatef(0, -34, 0)
    glBindTexture(GL_TEXTURE_2D, texid[9])
    sphere()

    glPopMatrix()

    glBindTexture(GL_TEXTURE_2D, texid[4])
    glTranslatef(0, 0, 24)
    gluCylinder(qobj, 14, 0, 20, 30, 30)
    circle(14)

    glPushMatrix()
    glTranslatef(-9, 9, -3)
    glBindTexture(GL_TEXTURE_2D, texid[8])
    sphere()
    glTranslatef(18, -18, 0)
    glBindTexture(GL_TEXTURE_2D, texid[7])
    sphere()
    glTranslatef(-18, 0, 0)
    glBindTexture(GL_TEXTURE_2D, texid[6])
    sphere()
    glTranslatef(18, 18, 0)
    glBindTexture(GL_TEXTURE_2D, texid[5])
    sphere()
    glPopMatrix()

    glBindTexture(GL_TEXTURE_2D, texid[4])
    glTranslatef(0, 0, -10)
    gluCylinder(qobj, 18, 0, 25, 30, 30)
    circle(18)

    glTranslatef(0, 0, -38)
    glBindTexture(GL_TEXTURE_2D, texid[2])
    gluCylinder(qobj, 5, 5, 10, 30, 30)
