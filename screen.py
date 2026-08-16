import pygame

import consts

WINDOW = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("FLAG GAME!")

def moving_screen():
    WINDOW.fill(consts.BACKGROUND_MOVING)

    pygame.display.update()

def frozen_screen():
    WINDOW.fill(consts.BACKGROUND_FROZEN)

    pygame.display.update()

def drew_bush():



