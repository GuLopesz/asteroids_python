import pygame
from pygame.locals import *
from entities.spaceship import *
from common.defs import *

class Game:
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def __init__(self) -> None:
        "init game stuff"
        pygame.init()
        pygame.display.set_caption("Asteroids")

        self.clock = pygame.time.Clock()

        self.player: Spaceship = Spaceship()

        self.running = True
    
    def render(self) -> None:
        "render stuff"
        
        self.player.render()

        pygame.display.flip()

    def run(self) -> None:
        "main game loop"
        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.player.update()
                
            Game.screen.fill("black")
            self.render()

        pygame.quit()

if __name__ == '__main__':
    game: Game = Game()
    game.run()
