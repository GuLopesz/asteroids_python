import pygame
from pygame.locals import *
import math
from common.defs import *

class Game:
    def __init__(self, angle = 90) -> None:
        "init game stuff"
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Asteroids")

        self.clock = pygame.time.Clock()

        self.running = True

        self.spaceship_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.angle = angle

    def handle_input(self) -> None:
            "handle keyboard input"
            keys = pygame.key.get_pressed()
            if keys[K_w]:
                self.spaceship_pos.x += math.cos(math.radians(self.angle)) * SPACESHIP_SPEED
                self.spaceship_pos.y += -(math.sin(math.radians(self.angle))) * SPACESHIP_SPEED
            if keys[K_a]:
                self.angle = (self.angle + 5) % 360 
            if keys[K_d]:
                self.angle = (self.angle - 5) % 360

    def run(self) -> None:
        "main game loop"
        while self.running:
            self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_input()
                
            self.screen.fill("black")

            spaceship_surface = pygame.Surface((SPACESHIP_WIDTH, SPACESHIP_HEIGHT), pygame.SRCALPHA)
            pygame.draw.rect(spaceship_surface, WHITE, (0, 0, SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

            rotated_spaceship = pygame.transform.rotate(spaceship_surface, self.angle-90)
            rotated_rect = rotated_spaceship.get_rect(center=self.spaceship_pos)

            self.screen.blit(rotated_spaceship, rotated_rect)

            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    game: Game = Game()
    game.run()