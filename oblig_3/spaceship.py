import pygame
from obstacle import Obstacle
from config import GRAVITY, STARTING_FUEL
from bullet import Bullet
from landing_pad import Landing_pad

class Spaceship(pygame.sprite.Sprite):

    def __init__(self, x, y, images_rocket):
        super().__init__()
        self.original_image = pygame.image.load(images_rocket)  
        #self.image = self.original_image.copy()
        self.image = pygame.transform.scale(self.original_image,(100,100))
        self.rect = self.image.get_rect(center=(x, y))
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.angle = 0
        self.fuel = STARTING_FUEL
        self.thrust_vector = pygame.math.Vector2(0, 0)
        self.bullet_group = pygame.sprite.Group()
        self.mask = pygame.mask.from_surface(self.image)

    def thrust(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            #if self.fuel > 0: 
            thrust_velocity = pygame.math.Vector2.from_polar((0.1, self.angle - 90))
            self.velocity += thrust_velocity
            #self.fuel -= 1 

    def rotate(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.angle += 5
            #pygame.transform.rotate(self.image, 5)
        if key[pygame.K_LEFT]:
            self.angle -= 5
            #pygame.transform.rotate(self.image, -5)
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def shoot(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            bullet_velocity = pygame.math.Vector2(self.angle)
            bullet_velocity.clamp_magnitude_ip(2)
            self.bullet_group.add(Bullet(self.position[0], self.position[1], "images/bullet.png", bullet_velocity))

    def gravity(self):
        self.velocity[1] += GRAVITY

    def fuel_ship(self, fuel_group):
        if pygame.sprite.spritecollide(self, fuel_group, False):  #chat
            self.fuel = STARTING_FUEL

    def update(self, fuel_group):
        self.gravity()
        self.fuel_ship(fuel_group)
        self.thrust()
        self.rotate()
        self.position += self.velocity
        self.rect.center = self.position
        



