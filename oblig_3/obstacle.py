'''
Authors: Frode Eggenfellner and Magnus Moi Tytlandsvik

Obstacle module:
    The obstacle module creates the obstacle with the needed variables to be drawn

Usage:
    This is used in the main file to draw the obstacle
'''

import pygame
import obstacle
import config


class Obstacle(pygame.sprite.Sprite): # Creates a class for the obstacle with the needed variables

    def __init__(self, images_obstacle, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.original_image = pygame.image.load(images_obstacle)  
        self.image = pygame.transform.scale(self.original_image, (150, 150))  
        self.position = pygame.math.Vector2(self.x, self.y)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)

        
