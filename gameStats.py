class GameStats:
    """Track statistcs for Alien Invasion."""
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score never to be reset
        self.best_score = int(self._read_data())
        self.score = 0
        self.level = 1

    def reset_stats(self):
        """Initialize statistics  that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _read_data(self):
        """Read the best score from file"""
        with open('Best_score','r') as f:
            return f.read()

