import sys
import pygame
from ship import Ship
from settings import Settings


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self._display()

    def _display(self):
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_event()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        """Update image on the screen and flip to thr new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn visible
        pygame.display.flip()

    def _check_event(self):
        """Respond to key presses and mouse event"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            # Move ship to right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship tp left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == '__main__':
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
