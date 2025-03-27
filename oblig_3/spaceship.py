import pygame
import obstacle


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, images_rocket):
        super().__init__()
        self.original_image = pygame.image.load(images_rocket)  
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.angle = 0
        self.fuel = 100  

    def thrust(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            if self.fuel > 0:   
                self.velocity += 1
                self.fuel -= 1 

    def rotate(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.angle += 5
        if key[pygame.K_RIGHT]:
            self.angle -= 5
            
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    #def shoot(self):
        

    #def gravity(self):

    def update(self):
        self.gravity()
        self.position += self.velocity
        self.rect.center = self.position
