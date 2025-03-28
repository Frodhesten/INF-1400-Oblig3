import pygame
import config
from obstacle import Obstacle
from config import GRAVITY, STARTING_FUEL
from bullet import Bullet
from landing_pad import Landing_pad

class Spaceship(pygame.sprite.Sprite):

    bullet_group = pygame.sprite.Group()

    def __init__(self, x, y, images_rocket):
        super().__init__()
        self.original_image = pygame.image.load(images_rocket)  
        self.image = self.original_image.copy()
        self.original_image = pygame.transform.scale(self.original_image,(150,150))
        self.rect = self.image.get_rect(center=(x, y))
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.angle = 0
        self.fuel = STARTING_FUEL
        self.thrust_vector = pygame.math.Vector2(0, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.score = 0
        self.last_shot = 0

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
        if key[pygame.K_LEFT]:
            self.angle -= 5
        self.image = pygame.transform.rotate(self.original_image, - self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    def shoot(self):
        now = pygame.time.get_ticks()
        cooldown = 1000

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            if now - self.last_shot >= cooldown:
                bullet_speed = 10
                bullet_velocity = pygame.math.Vector2.from_polar((bullet_speed, self.angle - 90))
                
                bullet = Bullet(self.position.x, self.position.y, "images/bullet.png", bullet_velocity, self.angle - 90)
                Spaceship.bullet_group.add(bullet)
                self.last_shot = now

    def gravity(self):
        self.velocity[1] += GRAVITY

    def fuel_ship(self, fuel_group):
        if pygame.sprite.spritecollide(self, fuel_group, False):  #chat
            self.fuel = STARTING_FUEL

    def reset_position(self):
        start_pos = pygame.math.Vector2(100, 300)
        self.position = start_pos
        self.rect.topleft = (100, 300)
        self.angle = 0
        self.velocity = pygame.math.Vector2(0, 0)

    def wall_crash(self):
        if self.position.x < 0: 
            self.reset_position()
        # points -= 1
        elif self.position.x > config.SCREEN_X:  
            self.reset_position()
        # points -= 1
        elif self.position.y < 0:  
            self.reset_position()
        # points -= 1
        elif self.position.y > config.SCREEN_Y:  
            self.reset_position()
        # points -= 1
        
    def update(self, fuel_group, obstacle_group):
        self.gravity()
        self.fuel_ship(fuel_group)
        self.thrust()
        self.rotate()
        self.shoot()
        self.wall_crash()

        self.position += self.velocity

        if pygame.sprite.spritecollide(self, obstacle_group, False, pygame.sprite.collide_mask):
            self.reset_position()

        self.rect.center = self.position
        self.rect.center = (int(self.position.x), int(self.position.y))




