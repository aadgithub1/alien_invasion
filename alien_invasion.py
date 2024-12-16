import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion():
    """Creates a game of alien invasion."""
    def __init__(self):
        """Initializes pygame."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        
        self.ship = Ship(self)
        pygame.display.set_caption('Alien Invasion')
    
    def _check_events(self):
        """Checks whether user has selected exit."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
    def run_game(self):
        """Runs the game."""
        #Continually check for events
        while True: #look at each event in even list
            self._check_events()
            self._update_screen()
            pygame.display.flip()
            self.clock.tick(60)
            
    def _update_screen(self):
        """Updates the screen and draws ship
        with new position."""
        #refill the screen with color chose in settings
        #make stuff visible
        #syncronize display and frame rate
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
            
if __name__ == '__main__':
    #Make an instance
    invasion = AlienInvasion()
    invasion.run_game()