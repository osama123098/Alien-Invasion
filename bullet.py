import pygame
from pygame.sprite import Sprite
from alien import Alien


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create Bullet object at the ship's Current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.color = self.setting.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = ai_game.ships.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the exact position of the bullet
        self.y -= self.setting.bullet_speed

        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Alien_bullet(Bullet):
    """A class to manage alien bullets"""

    def __init__(self, ai_game,rect):
        """Create the bullet on screen at mid of aliens"""
        Bullet.__init__(self,ai_game)
        Sprite.__init__(self)
        self.color = self.setting.alien_bullet_color

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.setting.alien_bullet_width, self.setting.alien_bullet_height)
        self.rect.midtop = rect.midbottom

        # Store the alien fire position as float
        self.y =float(self.rect.y)

    def update(self):
        """Move the bullet down the screen"""
        # Update the exact position of the alien bullet
        self.y += self.setting.alien_bullet_speed

        # Update the rect position
        self.rect.y = self.y
