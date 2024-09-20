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

    def get_triangle_points(self, pos, angle, size) -> list:
        "calculate points for the spaceship triangle"
        half_size = size / 2

        front_point = (
            pos.x + math.cos(math.radians(angle)) * size,
            pos.y - math.sin(math.radians(angle)) * size
        )
        left_point = (
            pos.x + math.cos(math.radians(angle + 120)) * half_size,
            pos.y - math.sin(math.radians(angle + 120)) * half_size
        )
        right_point = (
            pos.x + math.cos(math.radians(angle - 120)) * half_size,
            pos.y - math.sin(math.radians(angle - 120)) * half_size
        )

        return [front_point, left_point, right_point]

    def run(self) -> None:
        "main game loop"
        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_input()
                
            self.screen.fill("black")

            triangle_points = self.get_triangle_points(self.spaceship_pos, self.angle, SPACESHIP_WIDTH)

            pygame.draw.polygon(self.screen, WHITE, triangle_points)

            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    game: Game = Game()
    game.run()
