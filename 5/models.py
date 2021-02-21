from creeper_cord import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame


def textu(file_name):

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


def start():
    global texid
    global qobj
    texid = []
    for i in range(1, 8):
        texid.append(textu('image/{}.jpg'.format(i)))
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)

    return texid


def ground():
    glBindTexture(GL_TEXTURE_2D, texid[0])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-600.0, -600.0, 10.0)
    glTexCoord2f(20.0, 0.0)
    glVertex3f(600.0, -600.0, 10.0)
    glTexCoord2f(20.0, 20.0)
    glVertex3f(600.0, 600.0, 10.0)
    glTexCoord2f(0.0, 20.0)
    glVertex3f(-600.0, 600.0, 10.0)
    glEnd()


def draw_cube():
    glMaterialfv(GL_BACK, GL_AMBIENT, (0, 0, 0))
    glMaterialfv(GL_BACK, GL_DIFFUSE, (0, 0, 0))
    glMaterialfv(GL_BACK, GL_SPECULAR, (0, 0, 0))
    glBindTexture(GL_TEXTURE_2D, texid[6])

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2.0, -2.0, 2.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2.0, -2.0, 2.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(2.0, 2.0, 2.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2.0, 2.0, 2.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2.0, -2.0, -2.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2.0, 2.0, -2.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(2.0, 2.0, -2.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(2.0, -2.0, -2.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2.0, 2.0, -2.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2.0, 2.0, 2.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2.0, 2.0, 2.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(2.0, 2.0, -2.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2.0, -2.0, -2.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(2.0, -2.0, -2.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(2.0, -2.0, 2.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2.0, -2.0, 2.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2.0, -2.0, -2.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(2.0, 2.0, -2.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(2.0, 2.0, 2.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(2.0, -2.0, 2.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2.0, -2.0, -2.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2.0, -2.0, 2.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2.0, 2.0, 2.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2.0, 2.0, -2.0)
    glEnd()


def blik():
    glBindTexture(GL_TEXTURE_2D, texid[2])
    glColor3fv((1, 1, 1))
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.5, 0.5, 0.5))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.8, 0.8, 0.8))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SHININESS, 42)
    gluSphere(qobj, 2, 100, 100)


def sphere():
    glColor3fv((1, 1, 1))
    glBindTexture(GL_TEXTURE_2D, texid[1])
    gluSphere(qobj, 600, 100, 100)


def creeper():
    a = 1
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1, 1, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1))

    glBindTexture(GL_TEXTURE_2D, texid[5])
    glBegin(GL_QUADS)
    for face in creeper_face:
        for vertex in face:
            if a == 1:
                glTexCoord2f(0.0, 0.0)
                a += 1
            elif a == 2:
                glTexCoord2f(2, 0.0)
                a += 1
            elif a == 3:
                glTexCoord2f(2, 2)
                a += 1
            elif a == 4:
                glTexCoord2f(0, 2)
                a = 1

            glVertex3fv(creeper_vert[vertex])

    glEnd()

    glBindTexture(GL_TEXTURE_2D, texid[4])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0000004768371582, 0.999999463558197, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, 0.9999999403953552, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.9999993443489075, -1.0000005960464478, 1.0)
    glEnd()
