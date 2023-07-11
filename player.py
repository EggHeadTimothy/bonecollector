import pygame


class Player:

    def __init__(self, game):
        # Initialize the player and set its starting position.
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load the image
        dog_image = pygame.image.load('dog.png')
        scaled_dog_image = pygame.transform.scale(dog_image, (80, 80))
        self.image = scaled_dog_image
        self.rect = self.image.get_rect()

        # floats for horizontal (x) position and vertical (y) position
        self.rect.x = (self.settings.screen_width - 80) / 2
        self.rect.y = (self.settings.screen_height - 80) / 2
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.player_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.player_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # Draw the player at its current location
        self.screen.blit(self.image, self.rect)
