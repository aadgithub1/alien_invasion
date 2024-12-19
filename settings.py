class Settings():
    """Creates a class to store game settings."""
    
    def __init__(self):
        """Initialize settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.ship_speed = 2.5
        
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (65,65,65)
        self.bullets_allowed = 10
        
        self.alien_speed = 1.5
        
        