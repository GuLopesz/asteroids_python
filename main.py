import pygame
from pygame.locals import * 
import sys
import math 

pygame.init()

##SCREEN CONFIGS 
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()
running = True

##SPACESHIP CONFIGS
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 30, 50
spaceship_pos = pygame.Vector2((screen.get_width() / 2), (screen.get_height() / 2))
SPACESHIP_COLOR = (255, 255, 255)
SPACESHIP_SPEED = 3
angle = 0

##INÍCIO DO LOOP 
while running:
    clock.tick(60) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_w]:
        spaceship_pos.x += math.cos(math.radians(angle)) * SPACESHIP_SPEED
        spaceship_pos.y += -(math.sin(math.radians(angle))) * SPACESHIP_SPEED
        spaceship_pos.x %= screen.get_width()
        spaceship_pos.y %= screen.get_height()
    
    if keys[K_a]:
        angle = (angle + 5) % 360

    if keys[K_d]:
        angle = (angle - 5) % 360

    screen.fill("black")

    ## CÓDIGO DE ROTAÇÃO
    spaceship_surface = pygame.Surface((SPACESHIP_HEIGHT, SPACESHIP_WIDTH), pygame.SRCALPHA)
    pygame.draw.rect(spaceship_surface, (SPACESHIP_COLOR), (0, 0, SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
    rotated_spaceship = pygame.transform.rotate(spaceship_surface, angle-90)
    rotated_rect = rotated_spaceship.get_rect(center=spaceship_pos)
    screen.blit(rotated_spaceship, rotated_rect)
    
    
    pygame.display.flip()

pygame.quit()