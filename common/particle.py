import pygame
import random
import math
from entities.obj import *

class Particle(Obj):
    def __init__(self, x, y, angle, speed, color, size, lifespan):
        self.pos = pygame.Vector2(x, y)
        self.angle = angle
        self.speed = speed
        self.color = color
        self.size = size
        self.lifespan = lifespan

    def update(self):
        "update particle"
        self.pos.x += math.cos(math.radians(self.angle)) * self.speed
        self.pos.y += -math.sin(math.radians(self.angle)) * self.speed
        self.lifespan -= 1

    def render(self, screen):
        "render particle"
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.size)

def create_cone_particles(x, y, num_particles, cone_angle, spread_angle, speed_range, lifespan_range, color, size):
    particles = []
    for _ in range(num_particles):
        
        angle = random.uniform(cone_angle - spread_angle / 2, cone_angle + spread_angle / 2)
        
        speed = random.uniform(speed_range[0], speed_range[1])
        
        lifespan = random.randint(lifespan_range[0], lifespan_range[1])
        
        particle = Particle(x, y, angle, speed, color, size, lifespan)
        particles.append(particle)
    return particles