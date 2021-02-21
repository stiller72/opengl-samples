from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import math
# import time
# import asyncio


def rad(r, angle):
    y = r * math.sin(angle)
    x = r * math.cos(angle)
    sp = glTranslatef(x, y, 0)
    return sp


def gen(r, angle, speed):
    while True:
        angle = angle + speed
        a = rad(r, angle)
        yield a


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
    for i in range(1, 12):
        loadTexture('image/{}.jpg'.format(i))
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)


def sky():
    glBindTexture(GL_TEXTURE_2D, 4)
    glColor(0.2, 0.2, 0.2)
    gluSphere(qobj, 1000, 60, 60)


def sun():
    glColor(1, 1, 1)
    glBindTexture(GL_TEXTURE_2D, 11)
    gluSphere(qobj, 100, 60, 60)

def earth():

    glBindTexture(GL_TEXTURE_2D, 3)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.1, 0.1, 1.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.1, 0.1, 1.0))
    glMaterialfv(GL_FRONT, GL_SHININESS, 30)

    gluSphere(qobj, 20, 60, 60)


def mercury():
    glBindTexture(GL_TEXTURE_2D, 2)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.4, 0.4, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.9, 0.9, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.6, 0.6, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 54)

    gluSphere(qobj, 10, 60, 60)


def venus():
    glBindTexture(GL_TEXTURE_2D, 1)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.4, 0.4, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.9, 0.9, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.6, 0.6, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 32)

    gluSphere(qobj, 20, 60, 60)


def mars():
    glBindTexture(GL_TEXTURE_2D, 6)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.4, 0.4, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.9, 0.9, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.6, 0.6, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 100)

    gluSphere(qobj, 15, 60, 60)


def jupiter():
    glBindTexture(GL_TEXTURE_2D, 7)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.4, 0.4, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.9, 0.9, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.6, 0.6, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 100)

    gluSphere(qobj, 50, 60, 60)


def saturn():
    glBindTexture(GL_TEXTURE_2D, 8)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.4, 0.4, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.9, 0.9, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.6, 0.6, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 32)

    gluSphere(qobj, 45, 60, 60)
    glBindTexture(GL_TEXTURE_2D, 7)
    glRotatef(30, 30, 0, 0)
    gluCylinder(qobj, 60, 0.1, 0.1, 50, 50)


def uranus():
    glBindTexture(GL_TEXTURE_2D, 9)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.4, 0.4, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.9, 0.9, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.6, 0.6, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 100)

    gluSphere(qobj, 25, 60, 60)


def neptune():
    glBindTexture(GL_TEXTURE_2D, 10)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.4, 0.4, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.9, 0.9, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.6, 0.6, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 100)

    gluSphere(qobj, 25, 60, 60)


def lune():
    glBindTexture(GL_TEXTURE_2D, 5)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.4, 0.4, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.9, 0.9, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.6, 0.6, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 100)

    gluSphere(qobj, 4, 60, 60)
