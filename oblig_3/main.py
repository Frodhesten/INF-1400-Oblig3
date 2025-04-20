'''
Authors: Frode Eggenfellner and Magnus Moi Tytlandsvik

'''

import pygame
import obstacle
import config
import spaceship
import landing_pad

pygame.init()

BG_FILENAME = "images/BG.jpeg"
FUEL_FILENAME = "images/fuel.png"

fuel_img = pygame.image.load(FUEL_FILENAME)
fuel_img = pygame.transform.scale(fuel_img, (20, 20))

screen = pygame.display.set_mode((config.SCREEN_X, config.SCREEN_Y))

background = pygame.image.load(BG_FILENAME)
background = pygame.transform.scale(background, (config.SCREEN_X, config.SCREEN_Y))
background = background.convert()

clock = pygame.time.Clock()

class Game:

    spaceship_group = pygame.sprite.Group()
    spaceship_group.add(spaceship.Spaceship(100, 300, "images/rocket.png", 1))
    spaceship_group.add(spaceship.Spaceship(config.SCREEN_X-100, 300, "images/rocket2.png", 2))

    obstacle_group = pygame.sprite.Group()
    obstacle_group.add(obstacle.Obstacle("images/obstacle.png", config.SCREEN_X / 2, config.SCREEN_Y / 2))

    fuel_group = pygame.sprite.Group()
    fuel_group.add(landing_pad.Landing_pad("images/fuel.png", 50, config.SCREEN_Y/2))

    fuel_group.add(landing_pad.Landing_pad("images/fuel_flipped.png", config.SCREEN_X-150, config.SCREEN_Y/2))
                                    
    def print_text(self, message, x=10, y=10): # written by ChatGPT

        TEXT_COLOR = (255, 255, 255)
        font_obj = pygame.font.Font(None, 32)
        text_surface = font_obj.render(message, True, TEXT_COLOR)
        screen.blit(text_surface, (x, y))

    def start_game(self):

        while True:

            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break

            screen.blit(background, (0, 0))

            Game.fuel_group.draw(screen)

            Game.spaceship_group.update(Game.fuel_group, Game.obstacle_group, Game.spaceship_group)
            Game.spaceship_group.draw(screen)

            Game.obstacle_group.draw(screen)

            spaceship.Spaceship.bullet_1_group.update()
            spaceship.Spaceship.bullet_1_group.draw(screen)

            spaceship.Spaceship.bullet_2_group.update()
            spaceship.Spaceship.bullet_2_group.draw(screen)

            for spaceship_instance in Game.spaceship_group: 
                if spaceship_instance.player == 1:
                    self.print_text(f"Fuel: {int(spaceship_instance.fuel)}", 10, 10)
                    self.print_text(f"Points: {int(spaceship_instance.points)}", 10, 30)
                    
                elif spaceship_instance.player == 2:
                    self.print_text(f"Fuel: {int(spaceship_instance.fuel)}", config.SCREEN_X - 100, 10)
                    self.print_text(f"Points: {int(spaceship_instance.points)}", config.SCREEN_X - 100, 30)
            
            pygame.display.set_caption('Oblig 3 INF-1400')
            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    Game().start_game()


