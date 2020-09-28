import numpy
from pygame import *
import pygame
pygame.init()

def d_cir(y, x, s):
    draw.circle(screen, (255,255,255), (y,x), 15*s)
    draw.circle(screen, (0, 0, 0), (y, x), 15*s, 1)



FPS = 30
screen = pygame.display.set_mode((600, 402))
screen.fill((255, 255, 255))

def background():
    draw.rect(screen, (255, 255, 0), (0, 282, 600, 120))
    draw.rect(screen, (0, 0, 255), (0, 202, 600, 80))
    draw.rect(screen, (209, 255, 255), (0, 0, 600, 202))

def cloud(y, x, s):
    d_cir(y, x, s)
    d_cir(y+15*s, x+1*s, s)
    d_cir(y+29*s, x-3*s, s)
    d_cir(y-10*s, x+ 15*s, s)
    d_cir(y+5*s, x+16*s, s)
    d_cir(y+25*s, x+14*s, s)
    d_cir(y+40*s, x+17*s, s)

def SUN():
    draw.circle(screen, (255, 255, 0), (500, 60), 40)

def umbrella():
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

def ship():
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

background()

#clouds
cloud(100, 25, 1)
cloud(300, 45, 2)
cloud(80, 100, 1)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()