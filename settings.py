class Settings:
    """A class to store all setting for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen Setting
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # Ship setting
        self.ship_speed = 5
        self.ship_limit = 2

        # Bullet Settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 10

        # Alien Bullet setting
        self.alien_bullet_speed = 2.0
        self.alien_bullet_width = 3
        self.alien_bullet_height = 3
        self.alien_bullet_color = (0, 130, 0)
        self.alien_bullet_speed = 1.0

        # Alien Setting
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # Fleet_direction of 1 represent right; -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""

        self.ship_speed = 5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # Live scoring
        self.alien_point = 50

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)

