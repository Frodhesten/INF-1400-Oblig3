'''
Authors: Frode Eggenfellner and Magnus Moi Tytlandsvik

Spaceship module:
    This module creates a spaceship that can thrust, rotate and shoot. I also uses fuel while thrusting

Usage:
    This is used in the main file to draw two spaceships that can fight eachother
'''

import pygame
import config
from config import GRAVITY, STARTING_FUEL
from bullet import Bullet

class Spaceship(pygame.sprite.Sprite): # Class for a spaceship

    bullet_1_group = pygame.sprite.Group()
    bullet_2_group = pygame.sprite.Group()

    def __init__(self, x, y, images_rocket, player_num):
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
        self.points = 0
        self.last_shot = 0
        self.player = player_num

    def thrust(self): # Method for the ship to thrust forward
        if self.player == 2:
            key = pygame.key.get_pressed() 
            if key[pygame.K_UP]: # Checks if the button is pressed
                if self.fuel > 0: 
                    thrust_velocity = pygame.math.Vector2.from_polar((0.03, self.angle - 90)) # finds where the ship is looking
                    self.velocity += thrust_velocity
                    self.fuel -= 0.1
                    
        elif self.player == 1:
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                if self.fuel > 0: 
                    thrust_velocity = pygame.math.Vector2.from_polar((0.03, self.angle - 90))
                    self.velocity += thrust_velocity
                    self.fuel -= 0.3

    def rotate(self): # Method to rotate the ship left or right
        if self.player == 2:
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
                self.angle += 2
            if key[pygame.K_LEFT]:
                self.angle -= 2

        elif self.player == 1:
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                self.angle += 2
            if key[pygame.K_a]:
                self.angle -= 2

        self.image = pygame.transform.rotate(self.original_image, - self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    def shoot(self): # Method to make the ship shoot
        if self.player == 2:
            now = pygame.time.get_ticks()
            cooldown = 500
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]: # Checks if button is pressed
                if now - self.last_shot >= cooldown: # Cooldown for the shooting ability
                    bullet_speed = 10
                    bullet_velocity = pygame.math.Vector2.from_polar((bullet_speed, self.angle - 90)) # Finds where ship is looking
                    
                    bullet = Bullet(self.position.x, self.position.y, "images/bullet.png", bullet_velocity, self.angle - 90)
                    Spaceship.bullet_1_group.add(bullet)
                    self.last_shot = now

        elif self.player == 1:
            now = pygame.time.get_ticks()
            cooldown = 500
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                if now - self.last_shot >= cooldown:
                    bullet_speed = 10
                    bullet_velocity = pygame.math.Vector2.from_polar((bullet_speed, self.angle - 90))
                    
                    bullet = Bullet(self.position.x, self.position.y, "images/bullet.png", bullet_velocity, self.angle - 90)
                    Spaceship.bullet_2_group.add(bullet)
                    self.last_shot = now

    def gravity(self):
        self.velocity[1] += GRAVITY

    def fuel_ship(self, fuel_group):
        if pygame.sprite.spritecollide(self, fuel_group, False, pygame.sprite.collide_mask):
            self.fuel = STARTING_FUEL

    def reset_position(self): # Resets ships position when it is destroyed
        if self.player == 1:
            start_pos = pygame.math.Vector2(100, 300)
            self.position = start_pos
            self.rect.topleft = (100, 300)
            self.angle = 0
            self.velocity = pygame.math.Vector2(0, 0)
            self.fuel = STARTING_FUEL

        elif self.player == 2:
            start_pos = pygame.math.Vector2(config.SCREEN_X-100, 300)
            self.position = start_pos
            self.rect.topleft = (config.SCREEN_X-100, 300)
            self.angle = 0
            self.velocity = pygame.math.Vector2(0, 0)
            self.fuel = STARTING_FUEL

    def wall_crash(self):
        if self.position.x < 0: 
            self.reset_position()
            self.points -= 1
        elif self.position.x > config.SCREEN_X:  
            self.reset_position()
            self.points -= 1
        elif self.position.y < 0:  
            self.reset_position()
            self.points -= 1
        elif self.position.y > config.SCREEN_Y:  
            self.reset_position()
            self.points -= 1
        
    def update(self, fuel_group, obstacle_group, spaceship_group):
        self.gravity()
        self.fuel_ship(fuel_group)
        self.thrust()            
        self.rotate()
        self.shoot()
        self.wall_crash()

        self.position += self.velocity
        
        # Checks if ship is colliding with anything
        if pygame.sprite.spritecollide(self, obstacle_group, False, pygame.sprite.collide_mask):
            self.reset_position()
            self.points -= 1

        if self.player == 2:
            if pygame.sprite.spritecollide(self, Spaceship.bullet_2_group, True, pygame.sprite.collide_mask):
                self.reset_position()
                for spaceship in spaceship_group:
                    if spaceship.player == 1:
                        spaceship.points += 1

        if self.player == 1:
            if pygame.sprite.spritecollide(self, Spaceship.bullet_1_group, True, pygame.sprite.collide_mask):
                self.reset_position()
                for spaceship in spaceship_group:
                    if spaceship.player == 2:
                        spaceship.points += 1
    

        self.rect.center = self.position
        self.rect.center = (int(self.position.x), int(self.position.y))




