import pygame
import math
import os
import settings
import ammo

class Weapon(object):
    def __init__(self,image_nr):
        self.id = image_nr
        self.file = "Cannon" + str(image_nr) + ".png"
        self.image = pygame.image.load(os.path.join("Pliki", self.file))
        self.image_base = self.image
        self.image_matrix = self.image.get_rect()
        self.weapon_len = int(self.image.get_rect().size[0]/2)
        self.degree = 0
        self.powerUp = 0

        self.xb = 0
        self.yb = 0



    def get_image(self):
        return self.image
    def get_box(self):
        return self.image_matrix
    def set_weapon_loc(self, (x,y)):
        self.xb = x
        self.yb = y
        self.image_matrix = self.image.get_rect(center = (self.xb, self.yb))

    def rotate(self, (x, y)):
        radians = math.atan2(-(y - self.yb), x - self.xb)
        radians %= 2*math.pi
        self.degree = math.degrees(radians)
        self.image = pygame.transform.rotate(self.image_base, self.degree)
        self.image_matrix = self.image.get_rect(center = (self.xb, self.yb))

    def power(self, (xm,ym)):

        self.yEnd = self.yb - math.sin(math.radians(self.degree))*self.weapon_len
        self.xEnd = self.xb + math.cos(math.radians(self.degree))*self.weapon_len

        dist = math.sqrt((xm-self.xEnd)**2+(self.yEnd-ym)**2)
        dist = int(dist)

        distMultiplier = settings.config().get_DISTMULTIPLIER()
        triangleAngle = settings.config().get_TRIANGLESIZE()

        if dist > 100 * distMultiplier:
            dist = 100 * distMultiplier

        r = 5
        g = 255
        b = 0

        self.powerUp = dist/distMultiplier
        for x in xrange(1, self.powerUp+1):
            if r != 255:
                r+=5
            elif g != 0:
                g-=5
            else:
                print "Color error?"

        color = (r,g,b)

        degree1 = self.degree + triangleAngle
        degree2 = self.degree - triangleAngle

        x1 = self.xEnd + dist*math.cos(math.radians(degree1))
        y1 = self.yEnd - dist*math.sin(math.radians(degree1))
        x2 = self.xEnd + dist*math.cos(math.radians(degree2))
        y2 = self.yEnd - dist*math.sin(math.radians(degree2))

        return color, ((self.xEnd,self.yEnd), (x1,y1), (x2,y2))

    def shoot(self):
        return ammo.Ammo(self.id,(self.xEnd,self.yEnd), self.powerUp, self.degree)









