import random
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
        self.running: bool = True
        self.can_laser: bool = True
        self.laser_tick: int = 0

        self.player: Spaceship = Spaceship()
        self.lasers: List[Laser] = []
        self.asteroid = self.gen_random_polygon(7, (100, 100), 65, 30)

    def handle_input(self) -> None:
        "handle game input"
        keys = pygame.key.get_pressed()

        if keys[K_SPACE] and self.laser_tick == 0:
            self.lasers.append(Laser(self.player.pos, self.player.angle))
            self.can_laser = False
            self.asteroid = self.gen_random_polygon(7, (100, 100), 65, 30)
    
    def clear_lasers(self) -> None:
        "delete lasers that outbounds the screen"
        for l in self.lasers:
            if l.pos.x >= SCREEN_WIDTH or l.pos.x < 0 or l.pos.y >= SCREEN_HEIGHT or l.pos.y < 0:
                self.lasers.remove(l)

    def gen_random_polygon(self, sides, center, radius, noise) -> list:
        points = []
        angle = 0
        for _ in range(sides):
            x = center[0] + (radius + random.uniform(-noise, noise)) * math.cos(angle)
            y = center[1] + (radius + random.uniform(-noise, noise)) * math.sin(angle)
            points.append((x, y))
            angle += 2 * math.pi / sides
        return points
    
    def render_asteroids(self) -> None:
        pygame.draw.polygon(self.screen, BLUE, self.asteroid, 0)

    def render(self) -> None:
        "render stuff"
        for l in self.lasers:
            l.render(self.screen)

        self.player.render(self.screen)

        self.render_asteroids()

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

            self.screen.fill(BLACK)
            self.render()
            self.clear_lasers()
            if self.can_laser == False:
                self.laser_tick += 1
                if self.laser_tick >= 40:
                    self.laser_tick = 0
                    self.can_laser = True

        pygame.quit()

if __name__ == '__main__':
    game: Game = Game()
    game.run()
