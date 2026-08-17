import pygame

BACKGROUND_MOVING=(34, 139, 34)
BACKGROUND_FROZEN=(6, 10, 9)
LINE_COLOR=(17, 101, 102)

WIDTH=1000
HEIGHT=WIDTH//2
BLOCK_SIZE=WIDTH//50


GRASS = pygame.image.load("grass.png")
FLAG=pygame.image.load("flag.png")
MINE=pygame.image.load("mine.png")

FLAG_HEIGHT=FLAG.get_rect().height
FLAG_WIDTH=FLAG.get_rect().width

WIN_MESSAGE="you win!"
LOSE_MESSAGE="you lose!"

FPS=60



