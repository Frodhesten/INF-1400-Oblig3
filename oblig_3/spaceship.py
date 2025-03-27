import pygame
import obstacle
from config import GRAVITY, STARTING_FUEL
from bullet import Bullet

class Spaceship(pygame.sprite.Sprite):

    def __init__(self, x, y, images_rocket):
        super().__init__()
        self.original_image = pygame.image.load(images_rocket)  
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.angle = 0
        self.fuel = STARTING_FUEL
        self.thrust_vector = pygame.math.Vector2(0, 0)
        self.bullet_group = pygame.sprite.Group()

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
            #pygame.transform.rotate(self.image, 5)
        if key[pygame.K_RIGHT]:
            self.angle -= 5
            #pygame.transform.rotate(self.image, -5)
            
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def shoot(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            self.bullet_group.add(Bullet(self.position[0], self.position[1], "bullet.png", self.velocity*2))

    def gravity(self):
        self.velocity[1] += GRAVITY

    def update(self):
        self.gravity()
        self.position += self.velocity
        self.rect.center = self.position


