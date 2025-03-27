import pygame
import obstacle
import config
import spaceship

pygame.init()


screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

spaceship1 = spaceship.Spaceship(100, 300, "rocket.png")

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


