from entities.obj import *
import pygame
import math
from common.defs import *

class Laser(Obj):
    def __init__(self, pos: pygame.Vector2, angle, width = 3, height = 3) -> None:
        self.speed = 4
        self.angle = angle
        self.pos = pygame.Vector2(pos.x + math.cos(math.radians(self.angle)) * SPACESHIP_WIDTH, pos.y - math.sin(math.radians(self.angle)) * SPACESHIP_WIDTH)
        self.width = width
        self.height = height

    def render(self, screen) -> None:
        "render laser"
        pygame.draw.rect(screen, WHITE, (self.pos.x, self.pos.y, self.width, self.height))

    def update(self) -> None:
        "update laser"
        self.pos.x += math.cos(math.radians(self.angle)) * self.speed
        self.pos.y += -(math.sin(math.radians(self.angle))) * self.speed

