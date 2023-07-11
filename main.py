import sys
import pygame
from settings import Settings
from background import Background
from player import Player
from bone import Bone


class Game:
    """
    Overall class to manage game assets and behavior.
    """
    def __init__(self):
        """
        Initialize the game and create game resources.
        """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('')
        self.background = Background(self)
        self.player = Player(self)
        self.bones = pygame.sprite.Group()
        self.bone_spawn_counter = 0
        self.bone_spawn_timer = 0
        self.clock = pygame.time.Clock()
        self.game_active = False
        self.screen.fill(self.settings.bg_color)
        pygame.display.update()

    def run_game(self):
        self.game_active = True
        while self.game_active:
            self._check_events()
            self.player.update()
            self.bone_spawn_timer += 1
            if self.bone_spawn_timer % 180 == 0:
                self._spawn_bones()
            self._check_collisions()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self.player.moving_right = True
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.player.moving_left = True
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.player.moving_up = True
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.player.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self.player.moving_right = False
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.player.moving_left = False
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.player.moving_up = False
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.player.moving_down = False

    # noinspection PyTypeChecker
    def _check_collisions(self):
        for bone in self.bones:
            collisions = pygame.sprite.collide_rect(self.player, bone)
            if collisions:
                bone.kill()
                self.bone_spawn_counter -= 1

    # noinspection PyTypeChecker
    def _spawn_bones(self):
        if self.bone_spawn_counter < 5:
            new_bone = Bone(self)
            self.bones.add(new_bone)
            self.bone_spawn_counter += 1

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.background.blitme()
        self.player.blitme()
        self.bones.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
