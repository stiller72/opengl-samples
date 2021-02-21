from OpenGL.GL import *
from OpenGL.GLU import *
import pygame


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
    for i in range(1, 14):
        loadTexture('image/{}.jpg'.format(i))
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)


def ground():
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1000.0, -1000.0, 1000.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1000.0, -1000.0, 1000.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1000.0, 1000.0, 1000.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1000.0, 1000.0, 1000.0)
    glEnd()


def snowich():
    gluSphere(qobj, 50, 100, 100)
    glTranslatef(0, 0, 55)
    gluSphere(qobj, 35, 100, 100)
    glTranslatef(0, 0, 40)
    gluSphere(qobj, 20, 100, 100)
    glRotatef(90, 90, 0, 0)
    gluCylinder(qobj, 1.7, 1.7, 15, 40, 40)
