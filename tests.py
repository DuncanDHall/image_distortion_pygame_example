import pygame
import sys
from pygame import *

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('broken image load')

circle_bmp = pygame.image.load('circle.BMP')
circle_png = pygame.image.load('circle2.png')
check_png = pygame.image.load('check.png')

while True:
    screen.fill(pygame.Color(200, 200, 200))
    screen.blit(circle_bmp, (10, 10))
    screen.blit(circle_png, (10, 40))
    screen.blit(check_png, (30, 10))
    for event in pygame.event.get():
        print event
    if event.type == QUIT:
        pygame.quit()
        sys.exit()

    pygame.display.update()
