import pygame
import obstacle
import config


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, images_obstacle, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.original_image = pygame.image.load(images_obstacle)  
        self.image = pygame.transform.scale(self.original_image, (200, 200))  
        self.position = pygame.math.Vector2(self.x, self.y)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
