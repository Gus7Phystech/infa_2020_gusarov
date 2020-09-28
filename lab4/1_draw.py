from pygame import *
import pygame
pygame.init()


FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))

draw.circle(screen, (255, 255, 0), (200, 175), 100)
draw.circle(screen, (0,0,0), (200, 175), 100, 1)

draw.rect(screen, (0, 0, 0), (140, 230, 120, 20))

draw.circle(screen, (255, 0, 0), (150, 150), 25)
draw.circle(screen, (255, 0, 0), (240, 150), 20)
draw.circle(screen, (0, 0, 0), (150, 150), 15)
draw.circle(screen, (0, 0, 0), (240, 150), 10)


draw.polygon(screen, (0,0,0), ((100,100),
                               (80, 110),
                               (180, 130),
                               (180, 115)
                               ))

draw.polygon(screen, (0,0,0), ((200,110),
                               (200, 100),
                               (280, 90),
                               (280, 100)
                               ))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()