import pygame
import math
import obstacle

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, images_bullet):
        super().__init__()
        self.original_image = pygame.image.load(images_bullet)  
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
    
    