'''
Authors: Frode Eggenfellner and Magnus Moi Tytlandsvik

Classes: Landing_pad
    This class creates landing pads for the spaceships to refuel at

Usage:
    This is being used by the main file to draw the refuel stations
'''
import pygame


class Landing_pad(pygame.sprite.Sprite): # Creates a class for the landing bads with needed variables

    def __init__(self, images_landing_pad, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.original_image = pygame.image.load(images_landing_pad)  
        self.image = pygame.transform.scale(self.original_image, (100, 100))  
        self.position = pygame.math.Vector2(self.x, self.y)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)