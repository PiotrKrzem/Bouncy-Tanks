import pygame
import os
import settings

class Music(object):
    def __init__(self):
        pygame.mixer.init()
        self.sound_volume = float(settings.config().get_SOUND_VOLUME())/100
        self.music_volume = float(settings.config().get_MUSIC_VOLUME())/100
    def music_menu(self):
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.load(os.path.join("Pliki","music.wav"))
        pygame.mixer.music.play(-1)
    def music_game(self):
        pygame.mixer.music.play
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.load(os.path.join("Pliki","music2.wav"))
        pygame.mixer.music.play(-1)

    def play(self,Sound_Number):
        if Sound_Number ==1:
            file = os.path.join("Pliki","1.wav")
            Boom = pygame.mixer.Sound(file)
            Boom.set_volume(self.sound_volume)
            Boom.play()
