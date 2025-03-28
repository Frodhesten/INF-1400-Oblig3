import pygame
import math
import obstacle

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, images_bullet, velocity):
        super().__init__()
        self.original_image = pygame.image.load(images_bullet).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.position = pygame.math.Vector2(x, y)
        self.velocity = velocity

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
    
    
    