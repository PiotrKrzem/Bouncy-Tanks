import pygame
import math
import random


class Funcs:
    def updateTab(self, tabterenu, punkt_uderzeniaX, punkt_uderzeniaY, promien, screen_len):

        for X in xrange(-promien, promien+1):
            sX = punkt_uderzeniaX + X
            if sX > -1 and sX < screen_len:
                sY = tabterenu[sX][1]
                kY = punkt_uderzeniaY + math.sqrt(promien**2 - X**2)
                if sY<kY:
                    tabterenu[sX][1] = kY
        return tabterenu

    def QuickFix(self,x,y,r,tab):
        while True:
            for X in xrange(-r,r+1):
                xA = x + X
                yA = tab[xA][1]
                yK = y + math.sqrt(r**2 - X**2)
                if yK>=yA:
                    y-=1
            break
        return (x,y)

    def fallingScan(self, (x,y), tab, r, version=0):
        while True:
            for X in xrange(-r,r+1):
                xA = x + X
                yTab = tab[xA][1]
                yA = y + math.sqrt(r**2 - X**2)
                if yTab<yA:
                    ##uderzy w teren
                    return False
                    break
                if yTab+1<yA:
                    return False
                    break
            break
        ##moze spasc
        return True

    def inside((x0,y0,x1,y1),(xm,ym)):
        None

    def message(self,msg,letter_color,size,x,y,where):
        pygame.font.init()
        smallfont = pygame.font.SysFont("comicsansms", 25)
        medfont = pygame.font.SysFont("comicsansms", 50)
        largefont = pygame.font.SysFont("comicsansms", 80)

        if size == "small":
            textSurface = smallfont.render(msg, True, letter_color)
        elif size == "medium":
            textSurface = medfont.render(msg, True, letter_color)
        elif size == "large":
            textSurface = largefont.render(msg, True, letter_color)
        textSurf = textSurface
        textRect = textSurface.get_rect()
        textRect.center = x,y

        where.blit(textSurf,textRect)

    def creat_text (self,msg,letter_color,size):
            pygame.font.init()
            smallfont = pygame.font.SysFont("comicsansms", 25)
            medfont = pygame.font.SysFont("comicsansms", 50)
            largefont = pygame.font.SysFont("comicsansms", 80)

            if size == "small":
                textSurface = smallfont.render(msg, True, letter_color)
            elif size == "medium":
                textSurface = medfont.render(msg, True, letter_color)
            elif size == "large":
                textSurface = largefont.render(msg, True, letter_color)

            textSurf = textSurface
            textRect = textSurface.get_rect()

            return textSurf , textRect

    def button(self,msg,letter_color,button_color,size,x,y,border,action,where):
            Button_What_Do = False
            textSurf , textRect  = Funcs().creat_text(msg,letter_color,size)
            textRect.center = x,y
            rect_y = textRect[3]
            rect_x = textRect[2]
##            where1 = pygame.Surface((rect_x,rect_y))
##            where1.fill(0,0,0)
            if action == None :
                responisve_button_color = button_color
            else:
                responisve_button_color = (220,20,60)
                (x_mouse,y_mouse)=pygame.mouse.get_pos()
                if x_mouse>x-((border + rect_x)/2) and x_mouse<(x+((border + rect_x)/2)) and y_mouse>y-((rect_y)/2) and y_mouse<y+((rect_y)/2):
                    button_color=responisve_button_color
                    if pygame.mouse.get_pressed() == (1,0,0):
                            Button_What_Do = True
            pygame.draw.rect(where,button_color,(x-((border + rect_x)/2),y-((rect_y)/2),rect_x+border,rect_y))
            pygame.draw.rect(where,letter_color,(x-((border + rect_x)/2),y-((rect_y)/2),rect_x+border,rect_y),5)
            where.blit(textSurf,textRect)
            return Button_What_Do































