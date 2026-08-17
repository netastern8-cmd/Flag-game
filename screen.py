import pygame
import consts
import random
import game_field
import soldier

WINDOW = pygame.display.set_mode((consts.WIDTH,consts.HEIGHT))
pygame.display.set_caption("FLAG GAME!")


grass_lst=[]


def matrix_to_pixels(row,col):
    y_pixels=row*20
    x_pixels=col*20
    return x_pixels,y_pixels

def creat_moving_screen():
    WINDOW.fill(consts.BACKGROUND_MOVING)
    place_grass()
    pygame.display.update()

def creat_frozen_screen():
    WINDOW.fill(consts.BACKGROUND_FROZEN)
    frozen_grid()
    game_field.place_mines()
    pygame.display.update()

def moving_screen():
    WINDOW.fill(consts.BACKGROUND_MOVING)
    for block in grass_lst:
        drew_grass(block[0],block[1])
    pygame.display.update()

def frozen_screen():
    WINDOW.fill(consts.BACKGROUND_FROZEN)
    frozen_grid()
    for block in game_field.MINE_LST:
        drew_mine(block[0],block[1])
    pygame.display.update()

def frozen_grid():
    x_pixels=consts.BLOCK_SIZE
    y_pixels=consts.BLOCK_SIZE
    for i in range(consts.WIDTH//consts.BLOCK_SIZE):
        pygame.draw.line(WINDOW, consts.LINE_COLOR, [x_pixels,0], [x_pixels, consts.HEIGHT])
        x_pixels+=consts.BLOCK_SIZE
    for j in range(consts.HEIGHT//consts.BLOCK_SIZE):
        pygame.draw.line(WINDOW, consts.LINE_COLOR, [0,y_pixels], [consts.WIDTH,y_pixels])
        y_pixels+=consts.BLOCK_SIZE


def drew_grass(row,col):
    consts.GRASS=pygame.transform.scale(consts.GRASS, (consts.BLOCK_SIZE*3,consts.BLOCK_SIZE*3))
    WINDOW.blit(consts.GRASS,(matrix_to_pixels(row,col)))
    pygame.display.update()


def place_grass():
    while len(grass_lst)<20:
        row,col=random.randint(0,22),random.randint(0,47)
        if (row,col) not in grass_lst:
            grass_lst.append((row,col))
            drew_grass(row, col)

def drew_mine(row,col):
    consts.MINE=pygame.transform.scale(consts.MINE, (consts.BLOCK_SIZE*3,consts.BLOCK_SIZE))
    WINDOW.blit(consts.MINE,(matrix_to_pixels(row,col)))
    pygame.display.update()

def drew_OG_soldier(row,col):
    soldier.OG_SOLDIER=pygame.transform.scale(soldier.OG_SOLDIER, \
                (soldier.SOLDIER_WIDTH*0.15,soldier.SOLDIER_HEIGHT*0.15))
    WINDOW.blit(soldier.OG_SOLDIER,(matrix_to_pixels(row,col-1)))
    pygame.display.update()

def drew_frozen_soldier(row,col):
    soldier.FROZEN_SOLDIER=pygame.transform.scale(soldier.FROZEN_SOLDIER, \
                (soldier.SOLDIER_WIDTH*0.15,soldier.SOLDIER_HEIGHT*0.15))
    WINDOW.blit(soldier.FROZEN_SOLDIER,(matrix_to_pixels(row,col-1)))
    pygame.display.update()

def drew_injured_soldier(row,col):
    soldier.INJURED_SOLDIER=pygame.transform.scale(soldier.INJURED_SOLDIER, \
                (soldier.INJURED_WIDTH*0.18,soldier.INJURED_HEIGHT*0.18))
    WINDOW.blit(soldier.INJURED_SOLDIER,(matrix_to_pixels(row,col-1)))
    pygame.display.update()

def drew_flag():
    consts.FLAG = pygame.transform.scale(consts.FLAG, (consts.FLAG_WIDTH*0.14,consts.FLAG_HEIGHT*0.11))
    WINDOW.blit(consts.FLAG, (consts.WIDTH - consts.FLAG_WIDTH*0.14, consts.HEIGHT - consts.FLAG_HEIGHT*0.11))
    pygame.display.update()

