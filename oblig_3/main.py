import pygame
from spaceship import Spaceship
import obstacle
import config
import spaceship

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

#spaceship1 = Spaceship(100, 300, "rocket.png")

spaceship_group = pygame.sprite.Group()
for _ in range(2):
    spaceship_group.add(Spaceship(100, 300, "rocket.png"))

def start_game(self):
    pass

if __name__ == "__name__":
    start_game.start()


