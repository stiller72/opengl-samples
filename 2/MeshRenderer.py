from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import math
# import time
# import asyncio


def rad(r, angle):
    y = r * math.sin(angle)
    sp = glRotatef(-y, 0, y, 0)
    return sp


def rad2(r, angle):
    y = r * math.sin(angle)
    sp = glRotatef(y, 0, y, 0)
    return sp


def motion(r, angle):
    y = r * math.sin(angle)
    sp = glTranslatef(y, 0, 0)
    return sp


def gen1(r, angle, speed):
    side = False
    while True:
        if angle < 3.20:
            angle = 6.20
            if side:
                side = False
            else:
                side = True
        angle = angle - speed
        if side:
            a = rad(r, angle)
            b = motion(r, angle)
        else:
            a = None
            b = None
        yield a, b


def gen2(r, angle, speed):
    side = False
    while True:
        if angle < 3.20:
            angle = 6.20
            if side:
                side = False
            else:
                side = True
        angle = angle - speed
        if side:
            a = None
            b = None
        else:
            a = rad2(r, angle)
            b = motion(r, angle)
        yield a, b


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
    for i in range(1, 4):
        loadTexture('image/{}.jpg'.format(i))
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)


def const():
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.1, 0.1, 0.1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.1, 0.1, 0.1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.5, 0.5, 0.5))
    glMaterialfv(GL_FRONT, GL_SHININESS, 128)
    glBindTexture(GL_TEXTURE_2D, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-30, -15, 30)
    glTexCoord2f(30, 0.0)
    glVertex3f(30, -15, 30)
    glTexCoord2f(15, 15)
    glVertex3f(30, 15, 30)
    glTexCoord2f(0.0, 15)
    glVertex3f(-30, 15, 30)
    glEnd()

    glTranslatef(0, 0, 25)
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

    glBindTexture(GL_TEXTURE_2D, 3)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1.0))
    glMaterialfv(GL_FRONT, GL_SHININESS, 32)

    glTranslatef(25, 10, 5)
    gluCylinder(qobj, 1, 1, 40, 40, 70)

    glTranslatef(-50, 0, 0)
    gluCylinder(qobj, 1, 1, 40, 40, 70)

    glTranslatef(50, -20, 0)
    gluCylinder(qobj, 1, 1, 40, 40, 70)

    glTranslatef(-50, 0, 0)
    gluCylinder(qobj, 1, 1, 40, 40, 70)

    glRotatef(90, 0, 90, 0)
    glTranslatef(-39.5, 0, 0)
    gluCylinder(qobj, 1, 1, 50.5, 50, 70)
    glTranslatef(0, 20, 0)
    gluCylinder(qobj, 1, 1, 50.5, 50, 70)


def ball():

    glBindTexture(GL_TEXTURE_2D, 2)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 32)
    gluSphere(qobj, 5, 60, 60)
    gluCylinder(qobj, 0.3, 0.3, 28, 50, 50)
    glRotatef(-40, -40, 0, 0)
    gluCylinder(qobj, 0.3, 0.3, 28, 50, 50)
    glRotatef(40, 40, 0, 0)

def ball2():

    glBindTexture(GL_TEXTURE_2D, 2)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 32)
    gluSphere(qobj, 5, 60, 60)
    gluCylinder(qobj, 0.3, 0.3, 28, 50, 50)
    glRotatef(-40, -40, 0, 0)
    gluCylinder(qobj, 0.3, 0.3, 28, 50, 50)
