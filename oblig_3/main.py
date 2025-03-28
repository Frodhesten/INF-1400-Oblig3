import pygame
import obstacle
import config
import spaceship
import landing_pad

pygame.init()

BG_FILENAME = "images/BG.jpeg"
FUEL_FILENAME = "images/fuel.png"
OBSTACLE_FILENAME = "images/obstacle.png"

fuel_img = pygame.image.load(FUEL_FILENAME)
fuel_img = pygame.transform.scale(fuel_img, (20, 20))

screen = pygame.display.set_mode((config.SCREEN_X, config.SCREEN_Y))

background = pygame.image.load(BG_FILENAME)
background = pygame.transform.scale(background, (config.SCREEN_X, config.SCREEN_Y))
background = background.convert()

clock = pygame.time.Clock()

#spaceship1 = Spaceship(100, 300, "rocket.png")

class Game:

    spaceship_group = pygame.sprite.Group()
    for _ in range(2):
        spaceship_group.add(spaceship.Spaceship(100, 300, "images/rocket.png"))

    obstacle_group = pygame.sprite.Group()
    obstacle_group.add(obstacle.Obstacle("images/obstacle.png", config.SCREEN_X / 2, config.SCREEN_Y / 2))

    fuel_group = pygame.sprite.Group()
    fuel_group.add(landing_pad.Landing_pad("images/fuel.png", 50, config.SCREEN_Y/2))
    fuel_group.add(landing_pad.Landing_pad("images/fuel.png", config.SCREEN_X-150, config.SCREEN_Y/2))

    bullet_group = pygame.sprite.Group()

    def start_game(self):
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break
            
            screen.blit(background, (0, 0))

            #pygame.sprite.collide_mask(spaceship.Spaceship.image, obstacle.Obstacle.image, True, False)

            Game.spaceship_group.update(Game.fuel_group)
            Game.spaceship_group.draw(screen)

            Game.obstacle_group.draw(screen)
            Game.fuel_group.draw(screen)

            #spaceship.bullet_group.update()
            #spaceship.bullet_group.draw(screen)

            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    #game = Game()
    Game().start_game()


