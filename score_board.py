import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ai_game):
        """Initialize score keeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information
        self.__text_color = (30, 30, 30)
        self.__font = pygame.font.SysFont(None, 48)

        # Prepare the initial score,best score,level,ship image
        self.pre_score()
        self.pre_best_score()
        self.pre_ships()
        self.pre_level()


    def pre_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number *ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def pre_best_score(self):
        """Turn the high score into rendered image."""
        score_str = f'{self.stats.best_score:,}'
        self.best_score_image = self.__font.render(score_str, True, self.__text_color, self.settings.bg_color)

        # Display the best_score at top of the center
        self.best_score_rect = self.score_image.get_rect()
        self.best_score_rect.centerx = self.screen_rect.centerx
        self.best_score_rect.top = self.score_rect.top

    def pre_score(self):
        """Turns the score into render image """
        score_str = f'{self.stats.score:,}'
        self.score_image = self.__font.render(score_str, True, self.__text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score, level,best score,ship to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.best_score_image, self.best_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_best_score(self):
        """Check to see if there's a new high score"""
        if self.stats.score > self.stats.best_score:
            self.stats.best_score = self.stats.score
            self.pre_best_score()

    def pre_level(self):
        """Turns the level into a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.__font.render(level_str, True, self.__text_color, self.settings.bg_color)

        # Display the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.x = self.best_score_rect.centerx//2
        self.level_rect.top = self.best_score_rect.top
