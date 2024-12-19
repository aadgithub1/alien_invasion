from pygame.sprite import Sprite

import pygame
class Alien(Sprite):
    
    def __init__(self, ai_instance):
        super().__init__()
        self.screen = ai_instance.screen
        self.screen_rect = ai_instance.screen.get_rect()
        
        self.image = pygame.image.load('./alien_invasion/alien.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.actual_x = float(self.rect.x) #for precision
        self.settings = ai_instance.settings
        
    def update(self):
        """Updates the alien position"""
        self.actual_x += self.settings.alien_speed
        self.rect.x = self.actual_x