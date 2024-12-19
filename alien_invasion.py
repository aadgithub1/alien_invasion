import sys
import pygame

from bullet import Bullet
from settings import Settings
from ship import Ship

class AlienInvasion():
    """Creates a game of alien invasion."""
    def __init__(self):
        """Initializes pygame."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        
        self.bullets = pygame.sprite.Group()
        self.ship = Ship(self)
        pygame.display.set_caption('Alien Invasion')
        
    def _do_keydown(self, event):
        """Performs keydown actions (i.e. set the ship in motion)."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _do_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        """Create a bullet."""
        bullet = Bullet(self)
        self.bullets.add(bullet)
    
    def _check_events(self):
        """Checks whether user has selected exit."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._do_keydown(event)
                elif event.type == pygame.KEYUP:
                    self._do_keyup(event)
                    
        
    def run_game(self):
        """Runs the game."""
        #Continually check for events
        while True: #look at each event in even list
            self._check_events()
            self.ship.update()
            self.bullets.update()
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
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        
            
if __name__ == '__main__':
    #Make an instance
    invasion = AlienInvasion()
    invasion.run_game()