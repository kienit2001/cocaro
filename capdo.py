
import pygame, sys
from pygame.locals import *
from game import danhvoiamy


WINDOWWIDTH = 1000
WINDOWHEIGHT = 700

WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)


pygame.init()

DISPLAYSURF = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Hello world!')
font = pygame.font.SysFont('consolas', 20)
textSurface = font.render('de', True, GREEN, RED)
textSurface1 = font.render('trung binh', True, GREEN, RED)
textSurface2 = font.render('kho', True, GREEN, RED)

def choncapdo(muc):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return muc

            if event.type == pygame.MOUSEBUTTONDOWN:  # 2
                spot = event.pos  # 3
                print(spot)
                if 300 <= spot[0] <= 470 and 80 <= spot[1] <= 130:
                    return 1
                if 300 <= spot[0] <= 470 and 150 <= spot[1] <= 200:
                    return 2
                if 300 <= spot[0] <= 470 and 220 <= spot[1] <= 270:
                    return 3
        DISPLAYSURF.fill((255, 255, 255))
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (300, 80, 170, 50))
        DISPLAYSURF.blit(textSurface, (320, 90))
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (300, 150, 170, 50))
        DISPLAYSURF.blit(textSurface1, (320, 170))
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (300, 220, 170, 50))
        DISPLAYSURF.blit(textSurface2, (320, 240))
        pygame.display.update()
#print(choncapdo())