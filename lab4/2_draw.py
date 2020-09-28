import numpy
from pygame import *
import pygame
pygame.init()

def d_cir(y, x):
    draw.circle(screen, (255,255,255), (y,x), 15)
    draw.circle(screen, (0, 0, 0), (y, x), 15, 1)



FPS = 30
screen = pygame.display.set_mode((600, 402))
screen.fill((255, 255, 255))

#backgroung
draw.rect(screen, (255, 255, 0), (0, 282, 600, 120))
draw.rect(screen, (0, 0, 255), (0, 202, 600, 80))
draw.rect(screen, (209, 255, 255), (0, 0, 600, 202))

#cloud
d_cir(100, 25)
d_cir(115, 26)
d_cir(129, 22)
d_cir(90, 40)
d_cir(105, 41)
d_cir(125, 39)
d_cir(140, 42)

#SUN
draw.circle(screen, (255, 255, 0), (500, 60), 40)

#umbrella
draw.rect(screen, (137, 74, 0), (100, 260, 6, 120))
draw.polygon(screen, (255, 0, 0), ((103, 230),
             (50+3, 260), (150+3, 260)))
draw.aalines(screen, (0,0,0), False, ((103, 230),
                                      (50+3+10, 260)))
draw.aalines(screen, (0,0,0), False, ((103, 230),
                                      (50+3+10+10, 260)))
draw.aalines(screen, (0,0,0), False, ((103, 230),
                                      (50+3+10+10+10, 260)))
draw.aalines(screen, (0,0,0), False, ((103, 230),
                                      (50+3+10+10+10+10, 260)))
draw.aalines(screen, (0,0,0), False, ((103, 230),
                                      (103, 260)))
draw.aalines(screen, (0,0,0), False, ((103, 230),
                                      (113, 260)))
draw.aalines(screen, (0,0,0), False, ((103, 230),
                                      (123, 260)))
draw.aalines(screen, (0,0,0), False, ((103, 230),
                                      (133, 260)))
draw.aalines(screen, (0,0,0), False, ((103, 230),
                                      (143, 260)))

#ship
draw.rect(screen, (137, 74, 0), (320, 220, 200, 30))
draw.polygon(screen, (137, 74, 0), ((520, 220),
             (520, 250), (590, 220)))
draw.aalines(screen, (0,0,0), False, ((520, 220),
                                      (520, 250)))
r = 30
for i in range(90):
    draw.aalines(screen, (137, 74, 0), False, ((320, 220),
                                                (320 - r*numpy.cos(i*numpy.pi/180), 220 +r*numpy.sin(i*numpy.pi/180))))
draw.aalines(screen, (0,0,0), False, ((320, 220),
                                      (320, 250)))
draw.rect(screen, (0,0,0), (400, 100, 7, 120))

#sail
draw.polygon(screen, (255, 255, 203), ((400+7, 100),
                                       (400 + 20, 160),
                                       (400 + 80, 160)))
draw.polygon(screen, (255, 255, 203), ((400+7, 220),
                                       (400 + 20, 160),
                                       (400 + 80, 160)))
draw.aalines(screen, (0,0,0), False, ((400 + 20, 160),
                                       (400 + 80, 160)))

#hole in the ship
draw.circle(screen, (0,0,0), (540, 231), 10)
draw.circle(screen, (255,255,255), (540, 231), 7)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()