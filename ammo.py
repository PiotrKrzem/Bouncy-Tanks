import pygame
import math
import os
import settings

class Ammo(object):
    def __init__(self, nr, (x,y), power, angle):
        self.file = "Ammo" + str(nr) + ".png"
        self.image = pygame.image.load(os.path.join("Pliki", self.file))
        self.image_base = self.image
        self.image_matrix = self.image.get_rect()
        self.x = x
        self.y = y
        self.apr = settings.config().get_REDUCEPOWER()
        self.xvector = int(power/self.apr)*math.cos(math.radians(angle))
        self.yvector = -int(power/self.apr)*math.sin(math.radians(angle))
        self.gravity = settings.config().get_GRAVITYSTRENGH()
        self.angle = 0

        if nr == 0:
            (self.r,self.dmg,self.rotation) = 70,50,10
    def update(self, tab):
        self.yvector += self.gravity
        self.x += self.xvector
        self.y += self.yvector

        self.angle+=10
        if self.angle>360: self.angle-=360

        self.image = pygame.transform.rotate(self.image_base, self.angle)
        self.image_matrix = self.image.get_rect(center = (self.x, self.y))
    def get_image(self):
        return self.image
    def get_imageM(self):
        return self.image_matrix
    def get_y(self):
        return self.y
    def get_x(self):
        return self.x
    def boom_data(self):
        return self.x, self.y, self.r
    def bounceH(self):
        self.xvector=-self.xvector
    def get_r(self):
        return self.r
    def damage(self, (x1,y1),(x2,y2)):
        dmg=self.dmg
        dmg1 = 0
        dmg2 = 0
        dist1 = math.sqrt((self.x-x1)**2+(self.y-y1)**2)
        if dist1<=40:
            dmg1=dmg
        elif dist1>40 and dist1 <= 50:
            dmg1=dmg*3/4
        elif dist1>50 and dist1<=60:
            dmg1=dmg/2
        elif dist1>60 and dist1<self.r:
            dmg1=dmg/4
        else:
            dmg1=0

        dmg1 = int(dmg1)

        dist2 = math.sqrt((self.x-x2)**2+(self.y-y2)**2)
        if dist2<=40:
            dmg2=dmg
        elif dist2>40 and dist2 <= 50:
            dmg2=dmg*3/4
        elif dist2>50 and dist2<=60:
            dmg2=dmg/2
        elif dist2>60 and dist2<self.r:
            dmg2=dmg/4
        else:
            dmg2=0

        dmg2 = int(dmg2)

        return (dmg1, dmg2)




