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
import particle
terrain = terrain.Terrain()
config = settings.config()
class Main:

    def __init__(self):
        gra = Gra()
        gra.Run()
class Gra:
    def __init__(self):
        config.__init__
        self.Name = "Bouncy Tonks"
        self.clock = pygame.time.Clock()
        self.tab = terrain.generate()
        self.display_width = config.get_ScreenSize()[0]
        self.display_height = config.get_ScreenSize()[1]
        self.FPS = config.get_FPS()
        self.BEGIN = config.get_BEGIN()
        self.player1turn = config.get_WHO()
        self.WYBIERZ_GEN = config.get_GENTYPE()
        self.G_color = config.get_RGBG()
        self.P1_color = config.get_RGB1()
        self.P2_color = config.get_RGB2()
        (self.P1, self.P2) = settings.config().get_skins()
        self.endclock = 60
        self.rangemin = 50
        self.rangemax = 500
        self.TURN_ACTIVE = True
        self.SHOOTING = False
        self.GameEnd = False
        self.mousepos1 = (int(self.display_width/2),int(self.display_height/2))
        self.mousepos2 = (int(self.display_width/2),int(self.display_height/2))
        self.GAME_STATE = 1
        self.d = float(self.display_width)/1280
        self.k = float(self.display_height)/900
        self.music = config.get_MUSIC_VOLUME()
        self.sound = config.get_SOUND_VOLUME()
        self.current_music = 0
        self.gravity = settings.config().get_GRAVITYSTRENGH()
        self.Name_Of_Color1 = config.get_COLOR1()
        self.Name_Of_Color2 = config.get_COLOR2()
        self.UP = False
        self.RIGHT = False
        self.LEFT = False
        self.leftClick = False
        self.tonk1 = tonk.Tonk(self.P1_color, self.P1, (0,0), 0, False)
        self.tonk2 = tonk.Tonk(self.P2_color, self.P2, (0,0), 0, True)
        self.SPsearch()
        self.tonk1.update(self.x1,self.y1)
        self.tonk2.update(self.x2, self.y2)
        self.ammo = []
        self.particles = []
        self.printB = False
        if self.WYBIERZ_GEN == 2:
            self.tab.append((self.display_width, self.display_height))
            self.tab.append((0, self.display_height))
    def Run(self):
        gameDisplay = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.key.set_repeat(0,40)
        sound.Music().music_menu()
        self.tonk1.make_stats_again()
        self.tonk2.make_stats_again()
        while not self.GameEnd:
            while self.GAME_STATE == 1 and self.GameEnd == False :
                pygame.display.set_caption(self.Name + " FPS: " + str(self.clock.get_fps()))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.GameEnd = True
                gameDisplay.fill((220,220,220))
                Tittle_Color = (138,7,7)
                Button_Color = (138,7,7)
                Letter_Color = (0,0,0)
                funcX.Funcs().message("BOUNCY TANKS",Tittle_Color,"large",(self.display_width / 2),(self.display_height / 2)-300*self.d,gameDisplay)
                Button1 = funcX.Funcs().button("PLAY",Letter_Color,Button_Color,"medium",(self.display_width / 2),(self.display_height / 2)-150*self.k,30,1,gameDisplay)
                Button2 = funcX.Funcs().button("OPTIONS",Letter_Color,Button_Color,"medium",(self.display_width / 2),(self.display_height / 2),30,1,gameDisplay)
                Button3 = funcX.Funcs().button("QUIT",Letter_Color,Button_Color,"medium",(self.display_width / 2),(self.display_height / 2)+300*self.k,30,1,gameDisplay)
                Button4 = funcX.Funcs().button("CUSTOMIZE PLAYERS",Letter_Color,Button_Color,"medium",(self.display_width / 2),(self.display_height / 2)+150*self.k,30,1,gameDisplay)
                if Button1 == True:
                 self.GAME_STATE = 2
                if Button2 == True:
                 self.GAME_STATE = 3
                if Button3 == True:
                  self.GameEnd= True
                if Button4 == True:
                    self.GAME_STATE=4
                self.clock.tick(200)
                pygame.display.update()
            while self.GAME_STATE ==3 and self.GameEnd == False:
                to_change = None
                pygame.display.set_caption(self.Name + " FPS: " + str(self.clock.get_fps()))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.GameEnd = True
                gameDisplay.fill((220,220,220))
                k1 = 500*self.d
                k2 = 800*self.d
                k3 = 900*self.d
                k4 = 1000*self.d
                w1 = 200*self.k
                w2 = 300*self.k
                w3 = 400*self.k
                w4 = 500*self.k
                w5 = 600*self.k
                a = 25*self.d
                funcX.Funcs().button("  Ilosc FPS ",Letter_Color,Button_Color,"medium",k1,w1,80*self.d,None,gameDisplay)
                L_Arrow_1 = funcX.Funcs().button("<-",Letter_Color,Button_Color,"medium",k2,w1,25,4,gameDisplay)
                R_Arrow_1 = funcX.Funcs().button("->",Letter_Color,Button_Color,"medium",k4,w1,a,5,gameDisplay)
                funcX.Funcs().button(str(self.FPS),Letter_Color,Button_Color,"medium",k3,w1,20*self.d,None,gameDisplay)
                funcX.Funcs().button("   Gravity  ",Letter_Color,Button_Color,"medium",k1,w2,100,None,gameDisplay)
                L_Arrow_2 = funcX.Funcs().button("<-",Letter_Color,Button_Color,"medium",k2,w2,a,6,gameDisplay)
                R_Arrow_2 = funcX.Funcs().button("->",Letter_Color,Button_Color,"medium",k4,w2,a,7,gameDisplay)
                funcX.Funcs().button(str(self.gravity),Letter_Color,Button_Color,"medium",k3,w2,20,None,gameDisplay)
                funcX.Funcs().button(" Who Begins  ",Letter_Color,Button_Color,"medium",k1,w3,30*self.d,None,gameDisplay)
                L_Arrow_3 = funcX.Funcs().button("<-",Letter_Color,Button_Color,"medium",k2,w3,a,8,gameDisplay)
                R_Arrow_3 = funcX.Funcs().button("->",Letter_Color,Button_Color,"medium",k4,w3,a,9,gameDisplay)
                funcX.Funcs().button(str(self.BEGIN),Letter_Color,Button_Color,"medium",k3,w3,20*self.d,None,gameDisplay)
                funcX.Funcs().button("Sound Volume",Letter_Color,Button_Color,"medium",k1,w4,30*self.d,None,gameDisplay)
                L_Arrow_4 = funcX.Funcs().button("<-",Letter_Color,Button_Color,"medium",k2,w4,a,10,gameDisplay)
                R_Arrow_4 = funcX.Funcs().button("->",Letter_Color,Button_Color,"medium",k4,w4,a,11,gameDisplay)
                funcX.Funcs().button(str(self.sound),Letter_Color,Button_Color,"medium",k3,w4,20*self.d,None,gameDisplay)
                funcX.Funcs().button("Music Effect",Letter_Color,Button_Color,"medium",k1,w5,30*self.d,None,gameDisplay)
                L_Arrow_5 = funcX.Funcs().button("<-",Letter_Color,Button_Color,"medium",k2,w5,a,12,gameDisplay)
                R_Arrow_5 = funcX.Funcs().button("->",Letter_Color,Button_Color,"medium",k4,w5,a,13,gameDisplay)
                funcX.Funcs().button(str(self.music),Letter_Color,Button_Color,"medium",k3,w5,20*self.d,None,gameDisplay)
                Back_Button = funcX.Funcs().button("BACK",Letter_Color,Button_Color,"medium",1150*self.d,75*self.d,25*self.d,14,gameDisplay)
                if L_Arrow_1 == True:
                    self.FPS = settings.config().get_config('FPS',"-")
                elif R_Arrow_1 == True:
                    self.FPS = settings.config().get_config('FPS',"+")
                elif L_Arrow_2 == True:
                    self.gravity = settings.config().get_config('gravity',"-")
                elif R_Arrow_2 == True:
                    self.gravity = settings.config().get_config('gravity',"+")
                elif L_Arrow_3 == True:
                    self.BEGIN = settings.config().get_config('BEGIN',"-")
                    self.player1turn = config.get_WHO()
                elif R_Arrow_3 == True:
                    self.BEGIN = settings.config().get_config('BEGIN',"+")
                    self.player1turn = config.get_WHO()
                elif L_Arrow_4 == True:
                    self.sound = settings.config().get_config('SOUND',"-")
                elif R_Arrow_4 == True:
                    self.sound = settings.config().get_config('SOUND',"+")
                elif L_Arrow_5 == True:
                    self.music = settings.config().get_config('MUSIC',"-")
                    sound.Music().music_menu()
                elif R_Arrow_5 == True:
                    self.music = settings.config().get_config('MUSIC',"+")
                    sound.Music().music_menu()
                elif Back_Button == True :
                    self.GAME_STATE = 1
                self.clock.tick(10)
                pygame.display.update()
            while self.GAME_STATE == 4 and self.GameEnd == False:
                pygame.display.set_caption(self.Name + " FPS: " + str(self.clock.get_fps()))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.GameEnd = True
                gameDisplay.fill((220,220,220))
                Button1 = funcX.Funcs().button("Player 1",Letter_Color,Button_Color,"medium",(self.display_width / 2),(self.display_height / 2)-150*self.k,30,1,gameDisplay)
                Button2 = funcX.Funcs().button("Player 2",Letter_Color,Button_Color,"medium",(self.display_width / 2),(self.display_height / 2),30,1,gameDisplay)
                Back_Button = funcX.Funcs().button("BACK",Letter_Color,Button_Color,"medium",1150*self.d,75*self.d,25*self.d,14,gameDisplay)
                if Button1 == True:
                    self.GAME_STATE = 5
                elif Button2 == True:
                    self.GAME_STATE = 6
                elif Back_Button== True:
                    self.GAME_STATE = 1
                self.clock.tick(10)
                pygame.display.update()
            while self.GAME_STATE == 5 and self.GameEnd == False:
                pygame.display.set_caption(self.Name + " FPS: " + str(self.clock.get_fps()))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.GameEnd = True
                gameDisplay.fill((220,220,220))
                funcX.Funcs().button("Color",Letter_Color,Button_Color,"medium",500*self.d,200*self.k,25*self.d,None,gameDisplay)
                L_Arrow_1 = funcX.Funcs().button("<-",Letter_Color,Button_Color,"medium",750*self.d,200*self.k,25,4,gameDisplay)
                R_Arrow_1 = funcX.Funcs().button("->",Letter_Color,Button_Color,"medium",1050*self.d,200*self.k,25*self.d,5,gameDisplay)
                funcX.Funcs().button(str(self.Name_Of_Color1),Letter_Color,Button_Color,"medium",900*self.d,200*self.k,20*self.d,None,gameDisplay)
                funcX.Funcs().button("Skin",Letter_Color,Button_Color,"medium",500*self.d,350*self.k,200,None,gameDisplay)
                L_Arrow_2 = funcX.Funcs().button("<-",Letter_Color,Button_Color,"medium",750*self.d,350*self.k,25*self.d,6,gameDisplay)
                R_Arrow_2 = funcX.Funcs().button("->",Letter_Color,Button_Color,"medium",1050*self.d,350*self.k,25*self.d,7,gameDisplay)
                funcX.Funcs().button(str(self.P1),Letter_Color,Button_Color,"medium",900*self.d,350*self.k,20,None,gameDisplay)
                Back_Button = funcX.Funcs().button("BACK",Letter_Color,Button_Color,"medium",1150*self.d,75*self.d,25*self.d,14,gameDisplay)
                pygame.draw.circle(gameDisplay, self.P1_color,(200,300), self.tonk1.get_radius()-2, 0)
                pygame.draw.circle(gameDisplay, (0,0,0),(200,300), self.tonk1.get_radius() , 3)
                gameDisplay.blit(pygame.image.load(os.path.join("Pliki", "Tonk" + str(self.P1) + ".png")),(170,269))
                gameDisplay.blit(self.tonk1.get_weapon(), (170,239))
                if L_Arrow_1 == True:
                    self.Name_Of_Color1 = config.customize("Color","-","P1")
                    self.P1_color = config.get_RGB1()
                elif R_Arrow_1 == True:
                    self.Name_Of_Color1 = config.customize("Color","+","P1")
                    self.P1_color = config.get_RGB1()
                elif Back_Button == True:
                    self.GAME_STATE=4
                elif L_Arrow_2 == True:
                    self.P1 = config.get_config("SKIN","-","P1")
                elif R_Arrow_2 == True:
                    self.P1 = config.get_config("SKIN","+","P1")
                self.clock.tick(10)
                pygame.display.update()
            while self.GAME_STATE == 6 and self.GameEnd == False:
                pygame.display.set_caption(self.Name + " FPS: " + str(self.clock.get_fps()))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.GameEnd = True
                gameDisplay.fill((220,220,220))
                funcX.Funcs().button("Color",Letter_Color,Button_Color,"medium",500*self.d,200*self.k,80*self.d,None,gameDisplay)
                L_Arrow_1 = funcX.Funcs().button("<-",Letter_Color,Button_Color,"medium",750*self.d,200*self.k,25,4,gameDisplay)
                R_Arrow_1 = funcX.Funcs().button("->",Letter_Color,Button_Color,"medium",1050*self.d,200*self.k,25*self.d,5,gameDisplay)
                funcX.Funcs().button(str(self.Name_Of_Color2),Letter_Color,Button_Color,"medium",900*self.d,200*self.k,20*self.d,None,gameDisplay)
                funcX.Funcs().button("Skin",Letter_Color,Button_Color,"medium",500*self.d,350*self.k,20*self.d,None,gameDisplay)
                L_Arrow_2 = funcX.Funcs().button("<-",Letter_Color,Button_Color,"medium",750*self.d,350*self.k,25*self.d,6,gameDisplay)
                R_Arrow_2 = funcX.Funcs().button("->",Letter_Color,Button_Color,"medium",1050*self.d,350*self.k,25*self.d,7,gameDisplay)
                funcX.Funcs().button(str(self.P2),Letter_Color,Button_Color,"medium",900*self.d,350*self.k,20,None,gameDisplay)
                Back_Button = funcX.Funcs().button("BACK",Letter_Color,Button_Color,"medium",1150*self.d,75*self.d,25*self.d,14,gameDisplay)
                pygame.draw.circle(gameDisplay, self.P2_color,(200,300), self.tonk2.get_radius()-2, 0)
                pygame.draw.circle(gameDisplay, (0,0,0),(200,300), self.tonk2.get_radius() , 3)
                gameDisplay.blit(pygame.image.load(os.path.join("Pliki", "Tonk" + str(self.P2) + ".png")),(170,269))
                gameDisplay.blit(self.tonk2.get_weapon(), (170,239))
                if L_Arrow_1 == True:
                    self.Name_Of_Color2 = config.customize("Color","-","P2")
                    self.P2_color = config.get_RGB2()
                elif R_Arrow_1 == True:
                    self.Name_Of_Color2 = config.customize("Color","+","P2")
                    self.P2_color = config.get_RGB2()
                elif Back_Button == True:
                    self.GAME_STATE=4
                elif L_Arrow_2 == True:
                    self.P2 = config.get_config("SKIN","-","P2")
                elif R_Arrow_2 == True:
                    self.P2 = config.get_config("SKIN","+","P2")
                self.clock.tick(10)
                pygame.display.update()
            while self.GAME_STATE == 2 and self.GameEnd == False:
                if self.current_music == 0:
                    sound.Music().music_game()
                    self.current_music = 1
                self.Controls()
                self.clock.tick(self.FPS)
                pygame.display.set_caption(self.Name + " FPS: " + str(self.clock.get_fps()))
                gameDisplay.fill(settings.config().get_BGCOLOR())
                self.Controls()
                self.clock.tick(self.FPS)
                pygame.display.set_caption(self.Name + " FPS: " + str(self.clock.get_fps()))
                gameDisplay.fill(settings.config().get_BGCOLOR())
                if self.WYBIERZ_GEN == 1:
                    for x in self.tab:
                        pygame.draw.line(gameDisplay,self.G_color,(x[0],x[1]),(x[0],720))
                elif self.WYBIERZ_GEN == 2:
                    pygame.draw.polygon(gameDisplay, self.G_color, self.tab, 0)
                self.Behaviour()
                self.tonk1.weapon_update()
                self.tonk2.weapon_update()
                hp1,hp2 = self.tonk1.get_hp(), self.tonk2.get_hp()
                if hp1<=0 or hp2<=0:
                    self.SHOOTING = False
                    self.leftClick = False
                if self.leftClick:
                    if self.player1turn:
                        self.mousepos1 = pygame.mouse.get_pos()
                        self.tonk1.weapon_angle(self.mousepos1)
                    else:
                        self.mousepos2 = pygame.mouse.get_pos()
                        self.tonk2.weapon_angle(self.mousepos2)
                pygame.draw.circle(gameDisplay, self.P1_color,(self.x1,int(self.y1)), self.tonk1.get_radius()-2, 0)
                pygame.draw.circle(gameDisplay, (0,0,0),(self.x1,int(self.y1)), self.tonk1.get_radius() , 3)
                gameDisplay.blit(self.tonk1.get_image(), self.tonk1.get_rect())
                gameDisplay.blit(self.tonk1.get_weapon(), self.tonk1.get_weapon_box())
                pygame.draw.circle(gameDisplay, self.P2_color,(self.x2,int(self.y2)),self.tonk2.get_radius()-2, 0)
                pygame.draw.circle(gameDisplay, (0,0,0),(self.x2,int(self.y2)), self.tonk1.get_radius(), 3)
                gameDisplay.blit(self.tonk2.get_image(), self.tonk2.get_rect())
                gameDisplay.blit(self.tonk2.get_weapon(), self.tonk2.get_weapon_box())
                if self.player1turn and hp1!=0 and hp2!=0:
                    power1 = self.tonk1.power(self.mousepos1)
                    if self.TURN_ACTIVE:
                        pygame.draw.polygon(gameDisplay, power1[0], power1[1])
                    if self.SHOOTING:
                        self.leftClick = False
                        self.missile = self.tonk1.SHOOT()
                        self.ammo = self.ammo[::-1]
                        self.ammo.append(self.missile)
                        self.SHOOTING = False
                        self.ammo = self.ammo[::-1]
                        self.player1turn = False
                        self.t1tab=[]
                        self.t2tab=[]
                        t1 = self.tonk1.get_location()
                        t2 = self.tonk2.get_location()
                        self.LEFT = False
                        self.RIGHT = False
                        self.UP = False
                        self.tonk1.replenish()
                        self.tonk2.replenish()
                        for x in xrange(-30,31):
                            self.t1tab.append([t1[0]+x,t1[1]-math.sqrt(30**2-x**2)])
                            self.t2tab.append([t2[0]+x,t2[1]-math.sqrt(30**2-x**2)])
                elif hp1 != 0 and hp2!=0:
                    power2 = self.tonk2.power(self.mousepos2)
                    if self.TURN_ACTIVE:
                        pygame.draw.polygon(gameDisplay, power2[0], power2[1])
                    if self.SHOOTING:
                        self.leftClick = False
                        self.missile = self.tonk2.SHOOT()
                        self.ammo = self.ammo[::-1]
                        self.ammo.append(self.missile)
                        self.SHOOTING = False
                        self.ammo = self.ammo[::-1]
                        self.player1turn = True
                        self.t1tab=[]
                        self.t2tab=[]
                        t1 = self.tonk1.get_location()
                        t2 = self.tonk2.get_location()
                        self.LEFT = False
                        self.RIGHT = False
                        self.UP = False
                        self.tonk1.replenish()
                        self.tonk2.replenish()
                        for x in xrange(-30,31):
                            self.t1tab.append([t1[0]+x,t1[1]-math.sqrt(30**2-x**2)])
                            self.t2tab.append([t2[0]+x,t2[1]-math.sqrt(30**2-x**2)])
                if len(self.ammo) != 0:
                    t1 = self.tonk1.get_location()
                    t2 = self.tonk2.get_location()
                    self.TURN_ACTIVE = False
                    for x in self.ammo:
                        x.update(self.tab)
                        image = x.get_image()
                        imageM = x.get_imageM()
                        gameDisplay.blit(image, imageM)
                        xpos = (x.get_x(), x.get_y())
                        if x.get_y()>self.display_height:
                            self.ground = funcX.Funcs().updateTab(self.tab, int(x.boom_data()[0]),int(x.boom_data()[1]),x.boom_data()[2], self.display_width)
                            dmg = x.damage(t1,t2)
                            self.ammo = self.ammo[::-1]
                            self.ammo.remove(x)
                            self.ammo = self.ammo[::-1]
                            self.tonk1.takeDmg(dmg[0])
                            self.tonk2.takeDmg(dmg[1])
                            r = x.get_r()
                            p = particle.Particle(r,(xpos))
                            self.particles.append(p)
                            for x in self.tab:
                                xa=x[0]
                                xb=x[1]
                                if x[1]>self.display_height-50 and (xa!=0 and xa!=self.display_width+1 and xa!=self.display_width):
                                    x=[xa,self.display_height-50]
                                    self.tab[xa]=x
                        elif x.get_x()>=self.display_width or x.get_x() <= 0:
                            x.bounceH()
                        elif self.tab[int(x.get_x())][1]<=int(x.get_y()):
                            self.ground = funcX.Funcs().updateTab(self.tab, int(x.boom_data()[0]),int(x.boom_data()[1]),x.boom_data()[2], self.display_width)
                            sound.Music().play(1)
                            self.ammo = self.ammo[::-1]
                            self.ammo.remove(x)
                            self.ammo = self.ammo[::-1]
                            dmg = x.damage(t1,t2)
                            self.tonk1.takeDmg(dmg[0])
                            self.tonk2.takeDmg(dmg[1])
                            r = x.get_r()
                            p = particle.Particle(r,(xpos))
                            self.particles.append(p)
                            for x in self.tab:
                                xa=x[0]
                                xb=x[1]
                                if x[1]>self.display_height-50 and (xa!=0 and xa!=self.display_width+1 and xa!=self.display_width):
                                    x=[xa,self.display_height-50]
                                    self.tab[xa]=x
                        else:
                            if self.player1turn:
                                for xx in self.t1tab:
                                    if (xx[0]==int(xpos[0]) or xx[0]==int(xpos[0])+1 or xx[0]==int(xpos[0])-1) and xx[1]<=xpos[1] and xx[1]>=xpos[1]-60:
                                        self.ground = funcX.Funcs().updateTab(self.tab, int(x.boom_data()[0]),int(x.boom_data()[1]),x.boom_data()[2], self.display_width)
                                        sound.Music().play(1)
                                        self.ammo = self.ammo[::-1]
                                        self.ammo.remove(x)
                                        self.ammo = self.ammo[::-1]
                                        dmg = x.damage(t1,t2)
                                        self.tonk1.takeDmg(dmg[0])
                                        self.tonk2.takeDmg(dmg[1])
                                        r = x.get_r()
                                        p = particle.Particle(r,(xpos))
                                        self.particles.append(p)
                                        for x in self.tab:
                                            xa=x[0]
                                            xb=x[1]
                                            if x[1]>self.display_height-50 and (xa!=0 and xa!=self.display_width+1 and xa!=self.display_width):
                                                x=[xa,self.display_height-50]
                                                self.tab[xa]=x
                                        break
                            else:
                                for xx in self.t2tab:
                                    if (xx[0]==int(xpos[0]) or xx[0]==int(xpos[0])+1 or xx[0]==int(xpos[0])-1) and xpos[1]>=xx[1] and xx[1]>=xpos[1]-60:
                                        self.ground = funcX.Funcs().updateTab(self.tab, int(x.boom_data()[0]),int(x.boom_data()[1]),x.boom_data()[2], self.display_width)
                                        sound.Music().play(1)
                                        self.ammo = self.ammo[::-1]
                                        self.ammo.remove(x)
                                        self.ammo = self.ammo[::-1]
                                        dmg = x.damage(t1,t2)
                                        self.tonk1.takeDmg(dmg[0])
                                        self.tonk2.takeDmg(dmg[1])
                                        r = x.get_r()
                                        p = particle.Particle(r,(xpos))
                                        self.particles.append(p)
                                        for x in self.tab:
                                            xa=x[0]
                                            xb=x[1]
                                            if x[1]>self.display_height-50 and (xa!=0 and xa!=self.display_width+1 and xa!=self.display_width):
                                                x=[xa,self.display_height-50]
                                                self.tab[xa]=x
                                        break
                if len(self.particles)!=0:
                    for x in self.particles:
                        img = x.get_img()
                        imgbox = x.box()
                        gameDisplay.blit(img,imgbox)
                        if x.done():
                            self.particles.remove(x)
                if len(self.ammo) == 0 and len(self.particles)==0:
                    self.TURN_ACTIVE = True
                pygame.draw.line(gameDisplay, (0,0,255), (0,self.display_height-50),(self.display_width,self.display_height-50))
                f1,f2 = self.tonk1.get_fuel(), self.tonk2.get_fuel()
                hp1,hp2 = self.tonk1.get_hp(), self.tonk2.get_hp()
                pygame.draw.polygon(gameDisplay, (255,0,0), ((self.display_width-100,self.display_height-20), (self.display_width-100, self.display_height-20-hp2), (self.display_width-75, self.display_height-20-hp2),(self.display_width-75, self.display_height-20)), 0)
                pygame.draw.polygon(gameDisplay, (255,255,0), ((self.display_width-50,self.display_height-20), (self.display_width-50, self.display_height-20-f2), (self.display_width-25, self.display_height-20-f2),(self.display_width-25, self.display_height-20)), 0)
                funcX.Funcs().message("P2",Letter_Color,"small",self.display_width-120,self.display_height-25,gameDisplay)
                pygame.draw.polygon(gameDisplay, (255,0,0), ((25,self.display_height-20), (25, self.display_height-20-hp1), (50, self.display_height-20-hp1),(50, self.display_height-20)), 0)
                pygame.draw.polygon(gameDisplay, (255,255,0), ((75,self.display_height-20), (75, self.display_height-20-f1), (100, self.display_height-20-f1),(100, self.display_height-20)), 0)
                funcX.Funcs().message("P1",Letter_Color,"small",115,self.display_height-30,gameDisplay)
                if hp1 == 0 or hp2 == 0:
                    if hp1 != 0 and hp2 == 0:
                        funcX.Funcs().message("PLAYER 1 WINS",Letter_Color,"large",self.display_width/2,self.display_height/2,gameDisplay)
                    elif hp1 ==0 and hp2 != 0 :
                        funcX.Funcs().message("PLAYER 2 WINS",Letter_Color,"large",self.display_width/2,self.display_height/2,gameDisplay)
                    elif hp1 ==0 and hp2 ==0:
                        funcX.Funcs().message("REMIS",Letter_Color,"large",self.display_width/2,self.display_height/2,gameDisplay)
                    self.endclock-=1
                    if self.endclock==0:
                        self.GAME_STATE = 1
                        self.SPsearch()
                        self.tab = terrain.generate()
                        xxx=settings.config().get_ScreenSize()[1]
                        a=0
                        for x in self.tab:
                            if x[1]>xxx-100:
                                a+=1
                        while a>10:
                            a=0
                            self.tab = terrain.generate()
                            for x in self.tab:
                                if x[1]>xxx-100:
                                    a+=1
                        self.SPsearch()
                        self.tonk1.update(self.x1,self.y1)
                        self.tonk2.update(self.x2, self.y2)
                        if self.WYBIERZ_GEN == 2:
                            self.tab.append((self.display_width, self.display_height))
                            self.tab.append((0, self.display_height))
                        self.tonk1.reset_hp()
                        self.tonk2.reset_hp()
                        self.tonk1.replenish()
                        self.tonk2.replenish()
                        self.endclock=60
                        self.tonk1.make_stats_again()
                        self.tonk2.make_stats_again()
                pygame.display.update()
                self.clock.tick(self.FPS)
            while self.GameEnd == True:
                pygame.quit()
                quit()
    def Behaviour(self):
        hp1,hp2 = self.tonk1.get_hp(), self.tonk2.get_hp()
        f1,f2 = self.tonk1.get_fuel(), self.tonk2.get_fuel()
        if f1<=0 or f2<=0 or hp1<=0 or hp2<=0:
            self.LEFT = False
            self.RIGHT = False
            self.UP = False
        if self.UP:
            if self.player1turn:
                self.tonk1.flyingUp(self.tab)
                self.tonk1.change_status("Flying")
            else:
                self.tonk2.flyingUp(self.tab)
                self.tonk2.change_status("Flying")
        if self.LEFT:
            if self.player1turn == True and (self.tonk1.get_status() == "Driving" or self.tonk1.get_status() == "Idle"):
                self.tonk1.Move("Back", self.tab)
                self.tonk1.change_status("Driving")
            if  self.player1turn == False and (self.tonk2.get_status() == "Driving" or self.tonk2.get_status() == "Idle"):
                self.tonk2.Move("Back", self.tab)
                self.tonk2.change_status("Driving")
        if self.RIGHT:
            if self.player1turn == True and (self.tonk1.get_status() == "Driving" or self.tonk1.get_status() == "Idle"):
                self.tonk1.Move("Fwd", self.tab)
                self.tonk1.change_status("Driving")
            if  self.player1turn == False and (self.tonk2.get_status() == "Driving" or self.tonk2.get_status() == "Idle"):
                self.tonk2.Move("Fwd", self.tab)
                self.tonk2.change_status("Driving")
        if self.UP == False and funcX.Funcs().fallingScan(self.tonk1.get_location(), self.tab, self.tonk1.get_radius()) == True and self.tonk1.get_status() != "Driving":
            self.tonk1.change_status("Falling")
        if self.UP == False and funcX.Funcs().fallingScan(self.tonk2.get_location(), self.tab, self.tonk2.get_radius()) == True and self.tonk2.get_status() != "Driving":
            self.tonk2.change_status("Falling")
        if self.tonk1.get_status() == "Falling":
            if funcX.Funcs().fallingScan(self.tonk1.get_location(), self.tab, self.tonk1.get_radius()):
                self.tonk1.sayHelloToGravity()
            else:
                self.tonk1.Move("None", self.tab, 0)
                (self.x1, self.y1) = self.tonk1.get_location()
                self.tonk1.reset_status()
                self.tonk1.reset_vector()
        if self.tonk2.get_status() == "Falling":
            if funcX.Funcs().fallingScan(self.tonk2.get_location(), self.tab, self.tonk2.get_radius()):
                self.tonk2.sayHelloToGravity()
            else:
                self.tonk2.Move("None", self.tab, 0)
                (self.x2, self.y2) = self.tonk2.get_location()
                self.tonk2.reset_status()
                self.tonk2.reset_vector()
        if self.player1turn == True and (self.tonk1.get_status() == "Flying" or self.tonk1.get_status() == "Falling") and (self.LEFT == True or self.RIGHT == True):
            if self.LEFT == True:
                self.tonk1.rocket_boost(self.tab,"Back")
            elif self.RIGHT == True:
                self.tonk1.rocket_boost( self.tab,"Fwd")
        if self.player1turn == False and (self.tonk2.get_status() == "Flying" or self.tonk2.get_status() == "Falling") and (self.LEFT == True or self.RIGHT == True):
            if self.LEFT == True:
                self.tonk2.rocket_boost( self.tab, "Back")
            elif self.RIGHT == True:
                self.tonk2.rocket_boost( self.tab, "Fwd")
        self.tonk1.rocket_boost(self.tab, "None")
        self.tonk2.rocket_boost(self.tab, "None")
        if self.tonk1.get_status() == "Falling":
            if self.tonk1.check_bounceUp(self.tab) == False:
                self.tonk1.bounceUp()
        if self.tonk2.get_status() != "Flying":
            if self.tonk2.check_bounceUp(self.tab) == False:
                self.tonk2.bounceUp()
        if self.LEFT == False and self.RIGHT == False and self.tonk1.get_status() == "Driving":
            self.tonk1.reset_status()
            self.tonk1.reset_vector()
        if self.LEFT == False and self.RIGHT == False and self.tonk2.get_status() == "Driving":
            self.tonk2.reset_status()
            self.tonk2.reset_vector()
        if funcX.Funcs().fallingScan(self.tonk1.get_location(), self.tab, self.tonk1.get_radius(),1) == False:
            self.tonk1.reset_status()
            self.tonk1.reset_vector()
        if funcX.Funcs().fallingScan(self.tonk2.get_location(), self.tab, self.tonk2.get_radius(),1) == False:
            self.tonk2.reset_status()
            self.tonk2.reset_vector()
        (self.x1, self.y1) = self.tonk1.get_location()
        (self.x2, self.y2) = self.tonk2.get_location()
        if self.printB:
            print self.tonk1.get_status(), self.tonk2.get_status()
    def Controls(self):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.GAME_STATE=1
                if event.type == pygame.QUIT:
                    self.GameEnd = True
                if event.type == pygame.KEYDOWN and self.TURN_ACTIVE:
                    if event.key == pygame.K_UP:
                        self.UP = True
                    if event.key == pygame.K_LEFT:
                        self.LEFT = True
                    if event.key == pygame.K_RIGHT:
                        self.RIGHT = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.UP = False
                    if event.key == pygame.K_LEFT:
                        self.LEFT = False
                    if event.key == pygame.K_RIGHT:
                        self.RIGHT = False
                    if event.key == pygame.K_SPACE:
                        if self.player1turn:
                            self.player1turn = False
                        else:
                            self.player1turn = True
                    if event.key == pygame.K_1:
                        self.tab = terrain.generate()
                        xxx=settings.config().get_ScreenSize()[1]
                        a=0
                        for x in self.tab:
                            if x[1]>xxx-100:
                                a+=1
                        while a>10:
                            a=0
                            self.tab = terrain.generate()
                            for x in self.tab:
                                if x[1]>xxx-100:
                                    a+=1
                        self.SPsearch()
                        self.tonk1.update(self.x1,self.y1)
                        self.tonk2.update(self.x2, self.y2)
                        if self.WYBIERZ_GEN == 2:
                            self.tab.append((self.display_width, self.display_height))
                            self.tab.append((0, self.display_height))
                    if event.key == pygame.K_2:
                        if self.TURN_ACTIVE:
                            self.TURN_ACTIVE = False
                        else:
                            self.TURN_ACTIVE = True
                if event.type == pygame.MOUSEBUTTONDOWN and self.TURN_ACTIVE:
                    if event.button == 1:
                        self.leftClick = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.leftClick = False
                    if event.button == 3 and self.TURN_ACTIVE:
                        self.SHOOTING = True
                    if event.button == 2:
                       r = 100
                       xy = pygame.mouse.get_pos()
                       x = xy[0]
                       y = xy[1]
                       self.ground = funcX.Funcs().updateTab(self.tab,x,y,r, self.display_width)
    def SPsearch(self):
        if self.rangemin <self.tonk1.get_radius() or self.rangemin < self.tonk2.get_radius() or self.rangemax > self.display_width/2:
            print "OSTRZEZENIE! NIEPOPRAWNY ZASIEG STARTOWYCH POZYCJI; MOZE STWARZAC PROBLEMY"
        self.x1 = random.randint(self.rangemin, self.rangemax)
        self.x2 = self.display_width - random.randint(self.rangemin, self.rangemax)
        found1 = False
        found2 = False
        while not found2:
            while not found1:
                for x in xrange(len(self.tab)):
                    if self.x1 == self.tab[x][0]:
                        found1 = True
                        self.y1 = self.tab[x][1]-self.tonk1.get_radius()
            for x in xrange(len(self.tab)):
                if self.x2 == self.tab[x][0]:
                    found2 = True
                    self.y2 = self.tab[x][1]-self.tonk2.get_radius()
m = Main()
m.__init__