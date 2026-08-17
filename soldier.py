import pygame
OG_SOLDIER=pygame.image.load("OGsoldier.png")
FROZEN_SOLDIER = pygame.image.load("frozen_soldier.png")
INJURED_SOLDIER = pygame.image.load("injured_soldier.png")

SOLDIER_HEIGHT=OG_SOLDIER.get_rect().height
SOLDIER_WIDTH=OG_SOLDIER.get_rect().width
INJURED_HEIGHT=INJURED_SOLDIER.get_rect().height
INJURED_WIDTH=INJURED_SOLDIER.get_rect().width

SOLDIER_BLOCK_HEIGHT=4
SOLDIER_BLOCK_WIDTH=2

def soldier_legs(row,col):
    return [(row+3,col),(row+3,col+1)]

def soldier_body(row,col):
    body_lst=[]
    for i in range(3):
        for j in range(2):
            body_lst.append((row+i,col+j))
    return body_lst
