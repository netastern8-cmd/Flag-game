import pygame

import consts

WINDOW = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("FLAG GAME!")

def create():
    WINDOW.fill(consts.BACKGROUND_GREEN)
    pygame.display.update()

