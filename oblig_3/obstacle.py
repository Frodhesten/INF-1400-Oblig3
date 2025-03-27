import pygame
import obstacle


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, images_obstacle):
        super().__init__()
        self.original_image = pygame.image.load(images_obstacle)  
        self.image = self.original_image.copy()
        self.position = pygame.math.Vector2(self.x, self.y)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    
      