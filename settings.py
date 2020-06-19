import random
import configparser
class config:
    def __init__(self):
        self.color_list = ["red","green","blue","white","black","yellow"]
        self.config = configparser.ConfigParser()
        self.config.read_file(open('configX.ini'))
        self.FPS = self.config.getint('SETTINGS','FPS')
        self.sound_volume = self.config.getint('SETTINGS','SOUND')
        self.music_volume = self.config.getint('SETTINGS','MUSIC')
        self.Color1 = self.config.get('P1','Color')
        self.Color2 = self.config.get("P2","Color")
        self.RGB_ground = (0,160,0)
        self.RGB_p1 = (255,0,0)
        self.RGB_p2 = (0,255,0)
        self.Scr_height = self.config.getint('SETTINGS','resolutionY')
        self.Scr_len = self.config.getint('SETTINGS','resolutionX')
        self.GEN_TYPE = 2      #1 - stary, 2 - nowy
        self.WHO_BEGINS = self.config.getint('SETTINGS','BEGIN')   #0 - random,1 - p1, 2- p2
        self.GRAVITY_STRENGH = self.config.getint('SETTINGS','gravity') #0.4 rec
        self.FLYING_MULTIPLIER = 1
        self.DIST_MULTIPLIER = 2
        self.powerReduce = 5
        self.BG_COLOR = (165,243,243)
        self.P1_SKIN = self.config.getint('P1','SKIN')
        self.P2_SKIN = self.config.getint('P2','SKIN')
        self.TRIANGLESIZE = 10
        self.terrainMultiplier = 1 #wiecej gorek
        self.terrainAgression = 1 #wieksza roznica wysokosci


    def get_FPS(self):
        return self.FPS
    def color_rename(self,color):
        if color == "red":
            id = (255,0,0)
        elif color == "green":
            id = (0,255,0)
        elif color =="blue":
            id = (0,255,255)
        elif color == "white":
            id = (255,255,255)
        elif color == "black":
            id = (0,0,0)
        elif color == "yellow":
            id = (255,255,0)
        return id

    def get_RGBG(self):
        return self.RGB_ground
    def get_RGB1(self):
        color = self.config.get('P1','Color')
        c = config().color_rename(color)
        return c
    def get_RGB2(self):
        color = self.config.get('P2','Color')
        c = config().color_rename(color)
        return c

    def get_ScreenSize(self):
        return (self.Scr_len, self.Scr_height)
    def get_GENTYPE(self):
        return self.GEN_TYPE
    def get_GRAVITYSTRENGH(self):
        a = float(self.config.getint('SETTINGS','gravity'))
        return a/10
    def get_FLYINGMULTIPLIER(self):
        return self.FLYING_MULTIPLIER
    def get_BGCOLOR(self):
        return self.BG_COLOR
    def get_skins(self):
        return (self.P1_SKIN,self.P2_SKIN)
    def get_DISTMULTIPLIER(self):
        return self.DIST_MULTIPLIER
    def get_TRIANGLESIZE(self):
        return self.TRIANGLESIZE
    def get_REDUCEPOWER(self):
        return self.powerReduce
    def get_TERRAINMULTIPLIER(self):
        return self.terrainMultiplier
    def get_TERRAINAGRESSION(self):
        return self.terrainAgression
    def get_SOUND_VOLUME(self):
        return self.sound_volume
    def get_MUSIC_VOLUME(self):
        return self.music_volume
    def get_COLOR1(self):
        return self.Color1
    def get_COLOR2(self):
        return self.Color2
    def get_BEGIN(self):
        return self.WHO_BEGINS

##    def get_WHO(self):
##        if self.WHO_BEGINS == 0:
##            los = random.randint(1,2)
##            if los == 1:
##                WHO_BEGINSs = True
##            else:
##                WHO_BEGINSs = False
##        elif self.WHO_BEGINS == 1:
##            WHO_BEGINSs = True
##        else:
##            WHO_BEGINSs = False
##        return WHO_BEGINSs

    def change_range(self,h1,end_left,end_right,scale,sign):
        if sign == "+":
            if h1 == end_right :
                h2 = end_right
            else:
                h2 = h1+scale
        else:
            if h1 == end_left:
                h2 = end_left
            else:
                h2 = h1 - scale
        return h2

    def get_config(self,change,sign,where='SETTINGS'):
        self.config.read_file(open('configX.ini'))
        h1 = self.config.getint(where,change)

        if  change == "FPS" :
                scale = 20
                end_right = 300
                end_left = 10
        elif change == "gravity":
                scale = 1
                end_right = 10
                end_left = 1
        elif change =="BEGIN":
                scale = 1
                end_right = 2
                end_left = 0
        elif change =="MUSIC":
                scale = 1
                end_right = 100
                end_left = 0
        elif change =="SOUND":
                scale =1
                end_right = 100
                end_left = 0
        elif change =="SKIN":
                scale =1
                end_right=3
                end_left=0
        h2 = config().change_range(h1,end_left,end_right,scale,sign)
        self.config.set(where, change, str(h2))
        with open('configX.ini', 'w') as configfile:
            self.config.write(configfile)
        return self.config.getint(where,change)
    def customize(self,change,sign,where):
        self.config.read_file(open('configX.ini'))
        h1 = self.config.get(where,change)
        if change =="Color":
            for v in self.color_list:
                if h1 == v:
                    z = self.color_list.index(h1)
            if sign =="+":
                if z+1 == len(self.color_list):
                    h2 = self.color_list[0]
                else:
                    h2=self.color_list[z+1]
            else:
                if z-1 < 0:
                    h2 = self.color_list[-1]
                else:
                    h2 = self.color_list[z-1]

        self.config.set(where, change, str(h2))
        with open('configX.ini', 'w') as configfile:
            self.config.write(configfile)
        return self.config.get(where,change)

    def get_WHO(self):
        if self.WHO_BEGINS == 0:
            self.WHO_BEGINS = random.randint(1,2)
            if self.WHO_BEGINS == 1:
                self.WHO_BEGINS = True
            else:
                self.WHO_BEGINS = False
        elif self.WHO_BEGINS == 1:
            self.WHO_BEGINS = True
        else:
            self.WHO_BEGINS = False
        return self.WHO_BEGINS

