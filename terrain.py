import pygame
import random as hearthstone
import math as jaskola
import settings

class Terrain:
    def generate(self):
        I = settings.config().get_ScreenSize()[0]
        self.terraintab = []
        self.y = settings.config().get_ScreenSize()[1]/2+hearthstone.randint(0,200)
        self.angle = hearthstone.randint(0,180)

        rng1 = hearthstone.randint(0,1) + hearthstone.randint(0,1)
        rng2 = hearthstone.randint(0,1) + hearthstone.randint(0,1)
        while rng1 == rng2:
            rng1 = hearthstone.randint(0,1) + hearthstone.randint(0,1)
            rng2 = hearthstone.randint(0,1) + hearthstone.randint(0,1)
            if rng1!=rng2:
                break
        if rng1>rng2:
            oldrng1=rng1
            rng1=rng2
            rng2=oldrng1
        rng3 = hearthstone.randint(rng1,rng2) + hearthstone.randint(rng1,rng2)
        rng4 = hearthstone.randint(rng1,rng2) + hearthstone.randint(rng1,rng2)
        while rng3 == rng4:
            rng3 = hearthstone.randint(rng1,rng2) + hearthstone.randint(rng1,rng2)
            rng4 = hearthstone.randint(rng1,rng2) + hearthstone.randint(rng1,rng2)
            if rng3 !=rng4:
                break
        if rng3>rng4:
            oldrng3 = rng3
            rng3 = rng4
            rng4 = oldrng3
        self.randomize1 = hearthstone.randint(rng3,rng4)
        self.randomize2 = hearthstone.randint(rng3,rng4)


        Aggro =settings.config().get_TERRAINAGRESSION()+self.randomize1
        Multiplier=(settings.config().get_TERRAINMULTIPLIER()+self.randomize2)/2

        for x in xrange(0,I):
            if self.angle > 360:
                self.angle -=360

            self.y = self.y + jaskola.cos(jaskola.radians(self.angle))*Aggro
            if self.y>settings.config().get_ScreenSize()[1]:
                self.y = settings.config().get_ScreenSize()[1]-10
                self.angle = 180
            if self.y<settings.config().get_ScreenSize()[1]/10:
                self.y = settings.config().get_ScreenSize()[1]/10
                self.angle = 0

            self.angle+=0.35*Multiplier
            self.terraintab.append([x,self.y])
        return self.terraintab

