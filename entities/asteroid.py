import random
from entities.obj import *
import math
import pygame
from pygame.locals import *
from common.defs import *
from common.asteroid_type import AsteroidType

class Asteroid(Obj):
    def __init__(self, pos: pygame.Vector2, angle, kind: AsteroidType):
        self.pos = pygame.Vector2(pos.x, pos.y)
        self.angle = angle
        self.kind = kind
        match kind:
            case AsteroidType.SMALL:
                self.radius = 15
                self.points = self.gen_random_polygon(5, (0, 0), self.radius, 5)
            case AsteroidType.BIG:
                self.radius = 30
                self.points = self.gen_random_polygon(6, (0, 0), self.radius, 10)
            case AsteroidType.MEGA:
                self.radius = 45
                self.points = self.gen_random_polygon(7, (0, 0), self.radius, 10)
            case _:
                self.radius = 45
                self.points = self.gen_random_polygon(7, (0, 0), self.radius, 10)
        self.speed = 2
        self.t_points = [(x + self.pos.x, y + self.pos.y) for x, y in self.points]
        

    def render(self, screen) -> None:
        "render asteroid"
        pygame.draw.polygon(screen, WHITE, self.t_points, 1)

    def update(self) -> None:
        "update asteroid"
        self.pos.x += math.cos(math.radians(self.angle)) * self.speed
        self.pos.y += -(math.sin(math.radians(self.angle))) * self.speed
        if self.pos.x - self.radius > SCREEN_WIDTH:
            self.pos.x = 0 - self.radius
        elif self.pos.x + self.radius < 0:
            self.pos.x = SCREEN_WIDTH + self.radius

        if self.pos.y - self.radius > SCREEN_HEIGHT:
            self.pos.y = 0 - self.radius
        elif self.pos.y + self.radius < 0:
            self.pos.y = SCREEN_HEIGHT + self.radius
        
        self.t_points = [(x + self.pos.x, y + self.pos.y) for x, y in self.points]

    def gen_random_polygon(self, sides, center, radius, noise) -> list:
        "generate random polygon points"
        points = []
        angle = 0
        for _ in range(sides):
            x = center[0] + (radius + random.uniform(-noise, noise)) * math.cos(angle)
            y = center[1] + (radius + random.uniform(-noise, noise)) * math.sin(angle)
            points.append((x, y))
            angle += 2 * math.pi / sides
        return points

    def check_collision(self, pos: pygame.Vector2) -> bool:
        "collision detection"
        n = len(self.t_points)
        inside = False
        p1x, p1y = self.t_points[0]
        for i in range(n + 1):
            p2x, p2y = self.t_points[i % n]
            if pos.y > min(p1y, p2y):
                if pos.y <= max(p1y, p2y):
                    if pos.x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (pos.y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or pos.x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside