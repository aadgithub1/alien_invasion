import pygame

class Ship():
    """Adds a basic ship."""
    
    def __init__(self, alien_invasion_instance):
        """Initializes the ship."""
        self.settings = alien_invasion_instance.settings
        self.screen = alien_invasion_instance.screen
        self.screen_rect = alien_invasion_instance.screen.get_rect()
        
        self.image = pygame.image.load('./alien_invasion/server.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.actual_x = float(self.rect.x)
        
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Checks to see if the ship should be moving."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.actual_x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.actual_x -= self.settings.ship_speed
            
        self.rect.x = self.actual_x
        
        
    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)