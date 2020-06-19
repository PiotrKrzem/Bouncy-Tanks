import pygame
import settings
import math
import os
import weapon
import funcX

class Tonk(object):
    def __init__(self, tank_color, tank_skin_number, (starting, location), starting_cannon_number, if_flipped):
        self.tonkRGB = tank_color
        self.file_name_tonk = ("Tonk" + str(tank_skin_number) + ".png")
        self.is_flipped = if_flipped
        self.tankBase = pygame.image.load(os.path.join("Pliki", self.file_name_tonk))
        self.flipBase()
        self.tank = self.tankBase
        self.tankRect = self.tankBase.get_rect(center=(starting, location))
        self.file_name_cannon = ("Cannon" + str(starting_cannon_number)+".png")
        self.cannon = pygame.image.load(os.path.join("Pliki", self.file_name_cannon))
        self.flipCannon()
        self.location = (starting,location)
        self.x = self.location[0]
        self.y = self.location[1]
        self.angle = 0
        self.N = tank_skin_number
        self.flyMP = settings.config().get_FLYINGMULTIPLIER()

        self.status = "Idle"
        self.whatlocation = "Ground"
        self.rotateAmountBase = 3

        self.velocityUp = 0
        self.vectorHorizon = 0
        self.gravity = float(settings.config().get_GRAVITYSTRENGH())

        self.bounceball = False
        self.bounceballXY = (0,0)
        self.bounceAmountX = 0
        self.bounceAmountY = 0


#### KONFIGURACJA SKINOW #####
        self.hp0 = 200
        self.hp1 = 300
        self.hp2 = 250
        self.hp3 = 400

        self.fuel0 = 300
        self.fuel1 = 200
        self.fuel2 = 200
        self.fuel3 = 50

        self.speed0 = 2
        self.speed1 = 2
        self.speed2 = 3
        self.speed3 = 4

        self.radius0 = 30
        self.radius1 = 30
        self.radius2 = 30
        self.radius3 = 30
##############################

        self.make_stats()
        self.fuelmax = self.fuel
        self.maxhp=self.hp

        self.weapon = weapon.Weapon(0)
        self.rotateAmount = self.rotateAmountBase*self.speed

    def make_stats(self):
        if self.N == 0:
            self.hp = self.hp0
            self.fuel = self.fuel0
            self.speed = self.speed0
            self.radius = self.radius0
        elif self.N == 1:
            self.hp = self.hp1
            self.fuel = self.fuel1
            self.speed = self.speed1
            self.radius = self.radius1
        elif self.N == 2:
            self.hp = self.hp2
            self.fuel = self.fuel2
            self.speed = self.speed2
            self.radius = self.radius2
        elif self.N == 3:
            self.hp = self.hp3
            self.fuel = self.fuel3
            self.speed = self.speed3
            self.radius = self.radius3
        elif self.N == 4:
            self.hp = self.hp4
            self.fuel = self.fuel4
            self.speed = self.speed4
            self.radius = self.radius4

    def flipBase(self):
        if self.is_flipped:
            self.tankBase = pygame.transform.flip(self.tankBase, True, False)
    def flipCannon(self):
        if self.is_flipped:
            self.cannon = pygame.transform.flip(self.cannon, True, False)

    def get_rect(self):
        return self.tankRect
    def get_image(self):
        return self.tank
    def get_radius(self):
        return self.radius
    def update(self,x,y):
        self.location = (x,y)
        self.tank = pygame.transform.rotate(self.tankBase, self.angle)
        self.tankRect = self.tank.get_rect(center = self.location)
    def get_location(self):
        return self.location
    def change_status(self, x):
        self.status = x
    def get_status(self):
        return self.status
    def reset_status(self):
        self.status = "Idle"
####################
    def flyingUp(self, tab):
        self.fuel-=2
        self.velocityUp -= self.speed*self.flyMP
        if self.velocityUp < -self.speed*self.flyMP*4:
            self.velocityUp = -self.speed*self.flyMP*4
        y = self.location[1]
        self.location = (self.location[0], y + self.velocityUp)
        self.tank = pygame.transform.rotate(self.tankBase, self.angle)
        self.tankRect = self.tank.get_rect(center = self.location)
    def sayHelloToGravity(self):
        self.velocityUp += self.gravity
        y = self.location[1]
        self.location = (self.location[0], y + self.velocityUp)
        self.tank = pygame.transform.rotate(self.tankBase, self.angle)
        self.tankRect = self.tank.get_rect(center = self.location)
    def Move(self, where, tab):


        r = self.radius
        ScreenLen = settings.config().get_ScreenSize()[0]

        if where == "Back":
            speed = -self.speed
            self.angle+=self.rotateAmountBase*self.speed
        elif where == "Fwd":
            speed = self.speed
            self.angle-=self.rotateAmountBase*self.speed
        else:
            speed = 0

        if where != "None":
            self.fuel-=1

        if self.angle>360: self.angle-=360
        NoweXKuli = self.location[0]+speed
        if NoweXKuli > ScreenLen:
            NoweXKuli = ScreenLen
        NoweYKuli = tab[NoweXKuli][1]-r



        XX = r
        xA1 = NoweXKuli + XX
        xA2 = NoweXKuli - XX

        if xA1<0:
            xA1 = 0
        if xA2<0:
            xA2=0
        if xA1>ScreenLen:
            xA1=ScreenLen
        if xA2>ScreenLen:
            xA2=ScreenLen


        yMsc1 = tab[xA1][1]
        yMsc2 = tab[xA2][1]

        yKK = NoweYKuli - math.sqrt(r**2-XX**2)

        if  speed>0:
            if yKK>yMsc1:
                NoweXKuli = self.location[0]
        elif speed<0:
            if yKK>yMsc2:
                NoweXKuli = self.location[0]
        while True:
            for X in xrange(-r,r+1):
                xAnalizowane = NoweXKuli + X
                if xAnalizowane > ScreenLen:
                    xAnalizowane = ScreenLen
                yAnalizowane = tab[xAnalizowane][1]
                yK1 = NoweYKuli + math.sqrt(r**2 - X**2)
                yK2 = NoweYKuli - math.sqrt(r**2 - X**2)
                if yK1>=yAnalizowane:
                    NoweYKuli-=1
            break
        if NoweXKuli+r < ScreenLen and NoweXKuli-r>0:
            self.location = (NoweXKuli, NoweYKuli)
        else:
            None
        self.tank = pygame.transform.rotate(self.tankBase, self.angle)
        self.tankRect = self.tank.get_rect(center = self.location)

    def reset_vector(self):
        self.velocityUp = 0

    def rocket_boost(self, tab, where="None"):

        x = self.location[0]
        y = self.location[1]
        if where == "Fwd":
            if self.vectorHorizon + self.speed < self.speed*3:
                self.vectorHorizon += self.speed
        elif where == "Back":
            if self.vectorHorizon - self.speed > -self.speed*3:
                self.vectorHorizon -= self.speed
        if where != "None":
            self.fuel-=2

        if self.vectorHorizon>0:
            self.vectorHorizon -= 0.25
        elif self.vectorHorizon<0:
            self.vectorHorizon += 0.25
        x += self.vectorHorizon

        if x+self.radius < settings.config().get_ScreenSize()[0] and x-self.radius>0 and funcX.Funcs().fallingScan(self.location, tab, self.radius):
            self.update(int(x), y)
        else:
            None

    def get_vectorDown(self):
        return self.velocityUp
    def get_vectorHorizon(self):
        return self.vectorHorizon

    def check_bounceUp(self, tab):
        x = self.location[0]
        y = self.location[1]
        r = self.radius
        bonusrange = 2
        if self.velocityUp>0:
            while True:
                for X in xrange(-r-bonusrange,r+1+bonusrange):
                    xA = x + X
                    yTab = tab[xA][1]
                    yA = y + math.sqrt((r+bonusrange)**2 - X**2)
                    if yTab<yA:
                        self.bounceAmountY = int(self.velocityUp*0.75)
                        self.bounceballXY = (xA, int(yTab))
                        return False
                        break
                break
        self.bounceball = False
        self.bounceballXY = (0,0)
        return True


    def bounceUp(self):
        if self.bounceAmountY < 5:
            self.bounceAmountY = 0
        else:
            self.bounceball = True
            self.velocityUp = -self.bounceAmountY
            y = self.location[1] + self.velocityUp
            x = self.location[0]
            self.update(x,y)

    def bounceBall(self):
        if self.bounceball == True:
            return True
        else:
            return False

####################
    def weapon_update(self):
        self.weapon.set_weapon_loc((self.location[0], self.location[1]-self.radius))
    def get_weapon(self):
         return self.weapon.get_image()
    def get_weapon_box(self):
        return self.weapon.get_box()
    def weapon_angle(self, mouse):
        self.weapon.rotate(mouse)
    def power(self, mouse):
        self.weapon_update()
        return self.weapon.power(mouse)
    def SHOOT(self):
        self.weapon_update()
        return self.weapon.shoot()
    def takeDmg(self,dmg):
        if dmg != 0:
            self.hp -= dmg
            if self.hp<0:
                self.hp = 0

    def get_hp(self):
        return self.hp
    def get_fuel(self):
        if self.fuel <0:
            self.fuel = 0
        return self.fuel
    def replenish(self):
        self.fuel = self.fuelmax
    def reset_hp(self):
        self.hp=self.maxhp
    def make_stats_again(self):
        self.make_stats()
        self.maxhp=self.hp
        self.fuelmax=self.fuel


