import pygame
import random
from pygame.sprite import Sprite


class Bone(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load image
        self.size = 40
        bone_image = pygame.image.load('bone.png')
        scaled_bone_image = pygame.transform.scale(bone_image, (self.size, self.size))
        self.image = scaled_bone_image
        self.rect = self.image.get_rect()

        # Initialize position randomly
        self.rect.x = random.randint(0, self.settings.screen_width - self.size)
        self.rect.y = random.randint(0, self.settings.screen_height - self.size)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
