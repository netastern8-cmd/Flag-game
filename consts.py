import pygame

BACKGROUND_MOVING=(34, 139, 34)
BACKGROUND_FROZEN=(6, 10, 9)
WIDTH=1000
HEIGHT=WIDTH//2
BLOCK_SIZE=WIDTH//50


LINE_COLOR=(17, 101, 102)

OG_SOLDIER=pygame.image.load("OGsoldier.png")
FROZEN_SOLDIER = pygame.image.load("frozen_soldier.png")
INJURED_SOLDIER = pygame.image.load("injured_soldier.png")
GRASS = pygame.image.load("grass.png")
FLAG=pygame.image.load("flag.png")
MINE=pygame.image.load("mine.png")
SOLDIER_BLOCK_HEIGHT=4
SOLDIER_BLOCK_WIDTH=2

SOLDIER_HEIGHT=OG_SOLDIER.get_rect().height
SOLDIER_WIDTH=OG_SOLDIER.get_rect().width
INJURED_HEIGHT=INJURED_SOLDIER.get_rect().height
INJURED_WIDTH=INJURED_SOLDIER.get_rect().width
FLAG_HEIGHT=FLAG.get_rect().height
FLAG_WIDTH=FLAG.get_rect().width

WIN_MESSAGE="you win!"
LOSE_MESSAGE="you lose!"

FPS=60



