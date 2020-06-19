import pygame
import sound
import terrain
import funcX
import settings
import weapon
import tonk
import random
import math
import time
import os


class Particle:
    def __init__(self, r, (x,y)):
        image = pygame.image.load(os.path.join("Pliki", "Boomboom.png"))
        self.clockmax = 2
        self.loc = (x,y)
        self.stage = 0
        self.stageclock = 0
        scale0=r/3*3
        scale1=r/2*3
        scale2=r*3
        (x0,y0)=(int(scale0),int(scale0))
        (x1,y1)=(int(scale1),int(scale1))
        (x2,y2)=(int(scale2),int(scale2))
        angle0 = 30
        angle1 = -30
        angle2 = 0
        image0r = pygame.transform.rotate(image, angle0)
        image1r = pygame.transform.rotate(image, angle1)
        image2r = pygame.transform.rotate(image, angle2)
        self.image0 = pygame.transform.scale(image0r,(x0,y0))
        self.image1 = pygame.transform.scale(image1r,(x1,y1))
        self.image2 = pygame.transform.scale(image2r,(x2,y2))

        self.imageact = None
        self.imagebox = None

    def get_img(self):
        self.stageclock+=1
        if self.stageclock == self.clockmax:
            self.stage+=1
            self.stageclock-=self.clockmax

        if self.stage == 1:
            self.imageact = self.image1
        elif self.stage ==2:
            self.imageact = self.image2
        elif self.stage == 0:
            self.imageact = self.image0
        elif self.stage == 3:
            self.imageact = self.image2
        self.imagebox = self.imageact.get_rect(center = self.loc)

        return self.imageact
    def done(self):
        if self.stage == 3:
            return True
        else:
            return False
    def box(self):
        return self.imagebox

