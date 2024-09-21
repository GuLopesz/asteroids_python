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
        self.max_speed: float    = 6
        self.friction: float     = 0.03
        self.foward_angle = angle
        self.boost_tick: int = 0
        self.boost_particles = []
        self.acc_flag: bool = True

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

        [front_point, _, _] = self.get_triangle_points()
        if front_point[0] - (SPACESHIP_WIDTH / 2) > SCREEN_WIDTH:
            self.pos.x = 0 - (SPACESHIP_WIDTH / 2)
        elif front_point[0] + (SPACESHIP_WIDTH / 2) < 0:
            self.pos.x = SCREEN_WIDTH + (SPACESHIP_WIDTH / 2)
        
        if front_point[1] - (SPACESHIP_WIDTH / 2) > SCREEN_HEIGHT:
            self.pos.y = 0 - (SPACESHIP_WIDTH / 2)
        elif front_point[1] + (SPACESHIP_WIDTH / 2) < 0:
            self.pos.y = SCREEN_HEIGHT + (SPACESHIP_HEIGHT / 2)


        self.handle_input()
        self.boost_tick += 1
        
    def handle_input(self) -> None:
        "handle keyboard input"
        keys = pygame.key.get_pressed()

        if keys[K_w]:
            angle_diff = abs(self.angle - self.foward_angle) % 360
            if angle_diff > 180:
                angle_diff = 360 - angle_diff  

            if angle_diff > 0:
                self.speed -= 0.05  
                if self.speed < 0:
                    self.speed = 0  
                self.acc_flag = False
            else:
                self.acc_flag = True  
            
            if self.speed == 0 and angle_diff > 60:
                self.acc_flag = True
            if self.speed <= 4.5 and angle_diff > 0 and angle_diff <= 60:
                self.acc_flag = True

            if self.acc_flag:
                self.speed += self.acceleration
                self.foward_angle = self.angle  
        else:
            self.acc_flag = False
            if keys[K_a]:
                self.angle = (self.angle + 5) % 360 
            if keys[K_d]:
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