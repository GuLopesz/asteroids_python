from entities.obj import *
import math
import pygame
from pygame.locals import *
from common.defs import *

class Spaceship(Obj):
    def __init__ (self, angle = 90) -> None:
        self.pos   = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.angle = angle
        self.speed: float        = 0
        self.acceleration: float = 0.15
        self.max_speed: float    = 3
        self.friction: float     = 0.03
        self.foward_angle = angle
        self.boost_tick: int = 0

    def render(self, screen) -> None:
        "render spaceship"
        triangle_points = self.get_triangle_points()

        pygame.draw.polygon(screen, WHITE, triangle_points, 1)

    def update(self) -> None:
        "update spaceship"
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        
        if self.speed > 0:
            self.speed -= self.friction

        if self.speed <= 0:
            self.speed = 0
        
        self.pos.x += math.cos(math.radians(self.foward_angle)) * self.speed
        self.pos.y += -(math.sin(math.radians(self.foward_angle))) * self.speed
        self.pos.x %= SCREEN_WIDTH
        self.pos.y %= SCREEN_HEIGHT
        self.handle_input()
        self.boost_tick += 1
        
    def handle_input(self) -> None:
        "handle keyboard input"
        keys = pygame.key.get_pressed()

        if keys[K_w]:
            self.speed += self.acceleration
            self.foward_angle = self.angle
        elif keys[K_a]:
            self.angle = (self.angle + 5) % 360 
        elif keys[K_d]:
            self.angle = (self.angle - 5) % 360
        
    def get_triangle_points(self, size = SPACESHIP_WIDTH) -> list:
        "calculate points for the spaceship triangle"
        half_size = size / 2

        front_point = (
            self.pos.x + math.cos(math.radians(self.angle)) * size,
            self.pos.y - math.sin(math.radians(self.angle)) * size
        )
        left_point = (
            self.pos.x + math.cos(math.radians(self.angle + 120)) * half_size,
            self.pos.y - math.sin(math.radians(self.angle + 120)) * half_size
        )
        right_point = (
            self.pos.x + math.cos(math.radians(self.angle - 120)) * half_size,
            self.pos.y - math.sin(math.radians(self.angle - 120)) * half_size
        )

        return [front_point, left_point, right_point]