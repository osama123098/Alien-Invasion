class Settings:
    """A class to store all setting for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Setting
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (176, 224, 230)

        # Ship setting
        self.ship_speed = 2.5
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed = 2.0
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 10

        # Alien Setting
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        # Fleet_direction of 1 represent right; -1 represents left
        self.fleet_direction = 1
