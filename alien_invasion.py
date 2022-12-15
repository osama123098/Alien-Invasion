import sys
from time import sleep

import pygame
import sound_effect as se
import bullet
from gameStats import GameStats
from button import Button
from ship import Ship
from settings import Settings
from alien import Alien
from score_board import Scoreboard


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self._display()

    def _display(self):

        # Start Alien Invasion in an inactive state.
        self.game_active = False
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self._starting_the_game()

        # Create an instance to store game statistics and create a score board
        self.stats = GameStats(self)
        self.ships = Ship(self)
        self.sb = Scoreboard(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.alien_bullet = pygame.sprite.Group()
        self._create_fleet_of_alien()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_event()

            # When the ship is zero
            if self.game_active:
                self.ships.update()
                self._update_bullets()
                self._update_aliens()
                self._update_alien_bullet()
            self._update_screen()
            self.clock.tick(60)

    def _starting_the_game(self):
        """starting the game display button and wait for click on play button to start the game."""
        # make the  buttons.
        self.Title_Display = Button(self, 'ALIEN INVASION', (900, 200), font=(None, 128))
        self.play_button = Button(self, "Play")
        self.made_by = Button(self, "Made By: Osama Shaikh", font=(None, 24))

        # manage the display of button
        self.Title_Display.rect.centery -= 100
        self.Title_Display.msg_image_rect.centery -= 100
        self.play_button.rect.centery += 50
        self.play_button.msg_image_rect.centery += 50
        self.made_by.rect.bottomleft = self.Title_Display.rect.bottomleft
        self.made_by.msg_image_rect.bottomleft = self.Title_Display.rect.bottomleft
        self.made_by.msg_image_rect.top -= 5
        self.made_by.msg_image_rect.left += 5

        # Draw The button on screen
        self.play_button.draw_button()
        self.Title_Display.draw_button()
        self.made_by.draw_button()
        pygame.display.flip()
        self._check_pressing_the_play_button()

    def _check_pressing_the_play_button(self):
        """Check the play button is press to start the game."""
        while True:
            if pygame.event.get(pygame.MOUSEBUTTONDOWN) and self.play_button.rect.collidepoint(pygame.mouse.get_pos()):
                self.game_active = True

                # Recenter the Button
                self.play_button.rect.center = self.screen.get_rect().center
                self.play_button.msg_image_rect.center = self.screen.get_rect().center

                # Hide the mouse Cursor
                pygame.mouse.set_visible(False)
                break

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edges"""
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Check if the fleet is at edge, then Update the position of all aliens in the feet"""
        self._check_fleet_edges()
        self.aliens.update()
        # Look for alien-ship Collisions
        if pygame.sprite.spritecollideany(self.ships, self.aliens):
            self._ship_hit()
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # decrement ships_left.
            self.stats.ships_left -= 1
            self.sb.pre_ships()

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet_of_alien()
            self.ships.center_ship()

            # Pause.
            sleep(0.5)

        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet_of_alien(self):
        """Create the fleet of aliens"""
        # Create an alien and keep adding aliens until there's no room left self.aliens.sprites()
        # make an alien.
        alien = Alien(self)

        # Spacing between aliens is one width.
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height + 20

        while current_y < (self.settings.screen_height - 6 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row: reset x value amd increment y
            current_y += 2 * alien_height
            current_x = alien_width

    def _create_alien(self, x_position, y_position):
        """Create an aliens and place in a row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
    #    self._alien_fire(new_alien.rect)
        self.aliens.add(new_alien)

    def _alien_fire(self, rect):
        """Creating the fire of aliens"""
        a_bullet = bullet.Alien_bullet(self, rect)
        self.alien_bullet.add(a_bullet)

    def _update_alien_bullet(self):
        """Update the position of aliens fire and get rid of old fire."""
        self.alien_bullet.update()

        # Get rid of alien bullet that have disappeared.
        for alien_blt in self.alien_bullet.copy():
            if alien_blt.rect.height <= 0:
                self.alien_bullet.remove(alien_blt)
            self._check_ship_alienbullet_collision()

    def _check_ship_alienbullet_collision(self):
        """Check the bullet is strike the ship"""
        # If so, get rid of bullet and alien

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Check for any bullets that have hit the aliens.
        # If so, get rid of bullet and the alien.
        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collision:
            for aliens in collision.values():
                self.stats.score += self.settings.alien_point * len(aliens)
                self.sb.pre_score()
                self.sb.check_best_score()
                se.alien_sound.play()

        # Check if the fleet is empty
        if not self.aliens:
            # Destroy exiting bullets and create new fleet.
            self.stats.score += 10000
            self.sb.pre_score()
            self.bullets.empty()
            self._create_fleet_of_alien()
            self.settings.increase_speed()

            # Increase The Level
            self.stats.level += 1
            self.sb.pre_level()

    def _update_screen(self):
        """Update image on the screen and flip to thr new screen"""
        self.screen.fill(self.settings.bg_color)

        # Drawing the bullet on screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Drawing the aliens bullet on screen
        for alien_bullet in self.alien_bullet.sprites():
            alien_bullet.draw_bullet()

        # Drawing the ships
        self.ships.build_me()

        # Drawing the aliens
        self.aliens.draw(self.screen)

        # Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()

        # Draw the score Information
        self.sb.show_score()

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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, position):
        """Start a new game when the player clicks play"""

        if self.play_button.rect.collidepoint(position) and not self.game_active:
            # Reset the game settings
            self.settings.initialize_dynamic_settings()

            # Reset the game statistics.
            self.stats.reset_stats()
            self.sb.pre_ships()
            self.sb.pre_level()
            self.sb.pre_score()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet_of_alien()
            self.ships.center_ship()

    def _check_keydown_event(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            # Move ship to right
            self.ships.moving_right = True
        elif event.key == pygame.K_LEFT:

            # Move ship tp left
            self.ships.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            with open("Best_score", 'w') as f:
                f.write(str(self.stats.best_score))
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_p:
            # if event key is p pause the game
            # temp is variable to break the loop
            self._pause_the_game()

    def _pause_the_game(self):
        """Pause the game by sleep in 0 sec"""
        temp = True
        while temp:
            # pause the game until p is not press again
            sleep(0)
            for event in pygame.event.get(pygame.KEYDOWN):
                if event.key == pygame.K_p:
                    temp = False
                    break
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    with open("Best_score", 'w') as f:
                        f.write(str(self.stats.best_score))
                    sys.exit()

    def _check_keyup_event(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ships.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ships.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = bullet.Bullet(self)
            self.bullets.add(new_bullet)
            se.bullet_sound.play()


if __name__ == '__main__':
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
