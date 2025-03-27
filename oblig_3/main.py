import pygame
import obstacle
import config
import spaceship

pygame.init()

BG_FILENAME = "images/BG.jpeg"
screen = pygame.display.set_mode((config.SCREEN_X, config.SCREEN_Y))
background = pygame.image.load(BG_FILENAME)
background = pygame.transform.scale(background, (config.SCREEN_X, config.SCREEN_Y))
background.convert()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

#spaceship1 = Spaceship(100, 300, "rocket.png")

spaceship_group = pygame.sprite.Group()
for _ in range(2):
    spaceship_group.add(spaceship.Spaceship(100, 300, "images/rocket.png"))

obstacle_group = pygame.sprite.Group()
obstacle_group.add(obstacle.Obstacle("images/obstacle.png"))

def start_game(self):
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        
        screen.blit(background, (0, 0))

        pygame.sprite.groupcollide(spaceship_group, obstacle_group, False, True)

        spaceship_group.update()
        spaceship_group.draw(screen)

        obstacle_group.draw(screen)

        bullet_group.update()
        bullet_group.draw(screen)

        pygame.display.update()

if __name__ == "__name__":
    start_game.start()


