import pygame
from pygame.locals import *
from entities.spaceship import *
from entities.laser import *
from common.defs import *
from typing import List

class Game:

    def __init__(self) -> None:
        "init game stuff"
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Asteroids")

        self.clock = pygame.time.Clock()
        self.running = True

        self.player: Spaceship = Spaceship()
        self.lasers: List[Laser] = []

    def handle_input(self) -> None:
        "handle game input"
        keys = pygame.key.get_pressed()

        if keys[K_SPACE]:
            self.lasers.append(Laser(self.player.pos, self.player.angle))

    
    def render(self) -> None:
        "render stuff"
        for l in self.lasers:
            l.render(self.screen)

        self.player.render(self.screen)
        pygame.display.flip()

    def run(self) -> None:
        "main game loop"
        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_input()

            self.player.update()
            for l in self.lasers:
                l.update()
                
            self.screen.fill("black")
            self.render()

        pygame.quit()

if __name__ == '__main__':
    game: Game = Game()
    game.run()
