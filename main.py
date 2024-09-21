import pygame
from pygame.locals import *
from entities.spaceship import *
from entities.laser import *
from entities.asteroid import *
from common.defs import *
from typing import List
from common.asteroid_type import AsteroidType

class Game:

    def __init__(self) -> None:
        "init game stuff"
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption("Asteroids")

        self.clock = pygame.time.Clock()
        self.running: bool = True
        self.can_laser: bool = True
        self.laser_tick: int = 0

        self.player: Spaceship = Spaceship()
        self.lasers: List[Laser] = []
        self.asteroids: List[Asteroid] = [Asteroid(pygame.Vector2(500, 100), 270, AsteroidType.MEGA)]

    def handle_input(self) -> None:
        "handle game input"
        keys = pygame.key.get_pressed()

        if keys[K_SPACE] and self.laser_tick == 0:
            self.lasers.append(Laser(self.player.pos, self.player.angle))
            self.can_laser = False
            self.boost_tick = 0
        
        if keys[K_ESCAPE]:
            self.running = False

    
    def clear_lasers(self) -> None:
        "delete lasers that outbounds the screen"
        for l in self.lasers:
            if l.pos.x >= SCREEN_WIDTH or l.pos.x < 0 or l.pos.y >= SCREEN_HEIGHT or l.pos.y < 0:
                self.lasers.remove(l)
        

    def render(self) -> None:
        "render stuff"
        self.screen.fill(BLACK)
        
        for l in self.lasers:
            l.render(self.screen)

        for a in self.asteroids:
            a.render(self.screen)

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
            
            [player_front, player_left, player_right] = self.player.get_triangle_points()
            for a in self.asteroids:
                a.update()
                if (a.check_collision(pygame.Vector2(player_front[0], player_front[1])) or
                    a.check_collision(pygame.Vector2(player_left[0], player_left[1])) or
                    a.check_collision(pygame.Vector2(player_right[0], player_right[1]))):
                    # TODO: game over
                    print("game over")

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
