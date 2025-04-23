'''
Authors: Frode Eggenfellner and Magnus Moi Tytlandsvik

Bullet module:
    This module creates a bullet that the spaceships shoot at eachother and try to destroy the opponents ship

Usage:
    This is being used everytime a spaceship wants to shoot, then a bullet is drawn
'''

import pygame
import spaceship

class Bullet(pygame.sprite.Sprite): # Creates a class for every bullet with the needed variables

    def __init__(self, x, y, image_path, velocity, angle):
        super().__init__()

        original_image = pygame.image.load(image_path).convert_alpha()
        rotated_image = pygame.transform.rotate(original_image, - angle)
        self.image = pygame.transform.scale(rotated_image, (50, 50))
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect(center=(x, y))
        self.position = pygame.math.Vector2(x, y)
        self.velocity = velocity

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y


    
    