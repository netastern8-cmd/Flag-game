import pygame

BACKGROUND_MOVING=(34, 139, 34)
BACKGROUND_FROZEN=(6, 10, 9)
LINE_COLOR=(17, 101, 102)
BLACK = (0, 0, 0)

WIDTH=1000
HEIGHT=WIDTH//2
BLOCK_SIZE=WIDTH//50


GRASS = pygame.image.load("grass.png")
FLAG=pygame.image.load("flag.png")
MINE=pygame.image.load("mine.png")

FLAG_HEIGHT=FLAG.get_rect().height
FLAG_WIDTH=FLAG.get_rect().width

FONT_NAME="Anton"
FONT_SIZE = 0.15 * WIDTH
FONT_COLOR = BLACK
MESSAGE_LOCATION= (0.2 * WIDTH, HEIGHT / 2 - (FONT_SIZE / 2))
LOSE_MESSAGE = "You Lost!"
WIN_MESSAGE = "You Won!"

FPS=60



