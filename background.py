import pygame


class Background:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.size = 600

        background_image = pygame.image.load('grass.png')
        scaled_background_image = pygame.transform.scale(background_image, (self.size, self.size))
        self.image = scaled_background_image
        self.rect = self.image.get_rect()

    def blitme(self):
        # Draw the player at its current location
        self.screen.blit(self.image, (0, 0))
