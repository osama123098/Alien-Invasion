class Settings:
    """A class to store all setting for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Setting
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (176, 224, 230)
        # Ship setting
        self.ship_speed = 1.5