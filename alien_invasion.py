import sys
import pygame

from settings import Settings

class AlienInvasion():
    
    def __init__(self):
        """Initializes pygame."""
        pygame.init()
        self.settings = Settings()
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        
    def run_game(self):
        """Runs the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
            self.clock.tick(60)
            
if __name__ == '__main__':
    #Make an instance
    invasion = AlienInvasion()
    invasion.run_game()