from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import math


def loadTexture(file_name):

    textureSurface = pygame.image.load(file_name)
    textureData = pygame.image.tostring(textureSurface, "RGBA", True)

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


def BindTexture():
    global qobj
    for i in range(1, 6):
        loadTexture('image/{}.jpg'.format(i))
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)


def lamp():
    glBindTexture(GL_TEXTURE_2D, 3)
    gluCylinder(qobj, 5, 0.5, 4, 60, 10)
    glBindTexture(GL_TEXTURE_2D, 5)
    gluSphere(qobj, 2.5, 60, 60)


def basket():
    glBindTexture(GL_TEXTURE_2D, 4)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1.0))
    glMaterialfv(GL_FRONT, GL_SHININESS, 32)
    gluCylinder(qobj, 1.5, 3, 7, 60, 10)


def bortik():
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 10.0)
    glVertex3f(-20.0, 20.0, 0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-15.0, 15.0, 0)
    glTexCoord2f(10.0, 0.0)
    glVertex3f(15.0, 15.0, 0)
    glTexCoord2f(10.0, 10.0)
    glVertex3f(20.0, 20.0, 0)
    glEnd()

    glTranslatef(0, 0, -1.5)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-15, 15, -1.5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-15, 15, 1.5)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(15, 15, 1.5)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(15, 15, -1.5)
    glEnd()

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-20, 20, -1.5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-20, 20, 1.5)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(20, 20, 1.5)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(20, 20, -1.5)
    glEnd()


def table():
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.1, 0.1, 0.1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.1, 0.1, 0.1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.5, 0.5, 0.5))
    glMaterialfv(GL_FRONT, GL_SHININESS, 128)
    glBindTexture(GL_TEXTURE_2D, 2)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-40, -20, 0)
    glTexCoord2f(40, 0.0)
    glVertex3f(40, -20, 0)
    glTexCoord2f(20, 20)
    glVertex3f(40, 20, 0)
    glTexCoord2f(0.0, 20)
    glVertex3f(-40, 20, 0)
    glEnd()
    glPushMatrix()
    glTranslatef(0, 20, -6)
    basket()
    glTranslatef(40, 0, 0)
    basket()
    glTranslatef(0, -40, 0)
    basket()
    glTranslatef(-40, 0, 0)
    basket()
    glTranslatef(-40, 0, 0)
    basket()
    glTranslatef(0, 40, 0)
    basket()
    glPopMatrix()

    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.1, 0.1, 0.1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.1, 0.1, 0.1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.5, 0.5, 0.5))
    glMaterialfv(GL_FRONT, GL_SHININESS, 128)
    glBindTexture(GL_TEXTURE_2D, 1)

    glTranslatef(-22.5, 2.5, 1.5)
    bortik()
    glTranslatef(45, 0, 1.5)
    bortik()
    glTranslatef(0, -5, 1.5)
    glRotatef(180, 0, 0, 180)
    bortik()
    glTranslatef(45, 0, 1.5)
    bortik()
    glRotatef(90, 0, 0, 90)
    glTranslatef(-2.5, 45.5, 1.5)
    bortik()
    glRotatef(180, 0, 0, 180)
    glTranslatef(0, 46, 1.5)
    bortik()
    glTranslatef(3, 0, 0.9)
    ballpull(1)
    glTranslatef(-6, -50, 0)
    ball()
    glTranslatef(17, -17, -18)
    glBindTexture(GL_TEXTURE_2D, 1)
    gluCylinder(qobj, 1, 2, 15, 60, 10)
    glTranslatef(-34, 0, 0)
    gluCylinder(qobj, 1, 2, 15, 60, 10)
    glTranslatef(0, 70, 0)
    gluCylinder(qobj, 1, 2, 15, 60, 10)
    glTranslatef(34, 0, 0)
    gluCylinder(qobj, 1, 2, 15, 60, 10)


def ballpull(n):
    if n == 6:
        return
    else:
        for i in range(0, n):
            glTranslatef(-2, 0, 0)
            ball()
    glTranslatef(2.25 * n, 2, 0)

    return ballpull(n + 1)


def ball():

    glBindTexture(GL_TEXTURE_2D, 5)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 32)
    gluSphere(qobj, 1, 60, 60)
