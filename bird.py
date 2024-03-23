import pygame
import os
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join('bird.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)
        self.velocity = 0
        self.score = 0

    def update(self):
        self.velocity += 0.5
        self.rect.y += self.velocity

    def jump(self):
        self.velocity = -8
