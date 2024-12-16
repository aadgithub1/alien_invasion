import pygame

class Ship():
    """Adds a basic ship."""
    
    def __init__(self, alien_invasion_instance):
        """Initializes the ship."""
        self.screen = alien_invasion_instance.screen
        self.screen_rect = alien_invasion_instance.screen.get_rect()
        
        self.image = pygame.image.load('server.png')
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)