import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()