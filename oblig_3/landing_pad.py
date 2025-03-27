import pygame


class Landing_pad(pygame.sprite.Sprite):

    def __init__(self, images_landing_pad, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.original_image = pygame.image.load(images_landing_pad)  
        self.image = pygame.transform.scale(self.original_image, (100, 100))  
        self.position = pygame.math.Vector2(self.x, self.y)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))