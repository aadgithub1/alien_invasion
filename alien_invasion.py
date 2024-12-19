import sys
import pygame

from bullet import Bullet
from settings import Settings
from ship import Ship
from alien import Alien

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
        self.aliens = pygame.sprite.Group()
        self.ship = Ship(self)
        
        self._create_fleet()
        
        pygame.display.set_caption('Alien Invasion')    
        
    def run_game(self):
        """Runs the game."""
        #Continually check for events
        while True: #look at each event in even list
            self._check_events()
            self.ship.update()
            self.update_bullets()
            self._update_aliens()
            self._update_screen()
            pygame.display.flip()
            self.clock.tick(60)
            
    def _check_events(self):
        """Checks whether user has selected exit."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._do_keydown(event)
            elif event.type == pygame.KEYUP:
                self._do_keyup(event)
                
    def _do_keydown(self, event):
        """Performs keydown actions (i.e. set the ship in motion)."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if len(self.bullets) < self.settings.bullets_allowed:
                self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _do_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def update_bullets(self):
        """Updates the bullets and manages the Group."""
        self.bullets.update()
            
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                
    def _update_aliens(self):
        """calls update on all the aliens"""
        self.aliens.update()

    def _update_screen(self):
        """Updates the screen and draws ship
        with new position."""

        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

    def _fire_bullet(self):
        """Create a bullet."""
        bullet = Bullet(self)
        self.bullets.add(bullet)
        
    def _create_fleet(self):
        """Creates a fleet of aliens."""
        alien = Alien(self)
        
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - alien_width * 2):
                self._create_alien(current_x, current_y)
                current_x += alien_width * 2
            
            current_x = alien_width
            current_y += alien_height * 2
                
            
    def _create_alien(self, x_coord, y_coord):
        """Creates a single alien"""
        new_alien = Alien(self)
        new_alien.actual_x = x_coord
        new_alien.rect.x = x_coord
        new_alien.rect.y = y_coord
        self.aliens.add(new_alien)
            
if __name__ == '__main__':
    #Make an instance
    invasion = AlienInvasion()
    invasion.run_game()