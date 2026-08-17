import pygame
import game_field


OG_SOLDIER=pygame.image.load("OGsoldier.png")
FROZEN_SOLDIER = pygame.image.load("frozen_soldier.png")
INJURED_SOLDIER = pygame.image.load("injured_soldier.png")

SOLDIER_HEIGHT=OG_SOLDIER.get_rect().height
SOLDIER_WIDTH=OG_SOLDIER.get_rect().width
INJURED_HEIGHT=INJURED_SOLDIER.get_rect().height
INJURED_WIDTH=INJURED_SOLDIER.get_rect().width
import consts
import screen

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

def find_soldier_position():
    for row in range(len(game_field.FIELD)):
        for col in range(len(game_field.FIELD[row])):
            if game_field.FIELD[row][col]=="s":
                return (row,col)
    return (0,0)

def move_soldier_right(row,col):
   screen.draw_OG_soldier(row,col+1)
   game_field.mark_soldier_position(row,col+1)

def move_soldier_left(row,col):
    screen.draw_OG_soldier(row,col-1)
    game_field.mark_soldier_position(row,col-1)

def move_soldier_up(row,col):
    screen.draw_OG_soldier(row+1,col)
    game_field.mark_soldier_position(row+1,col)

def move_soldier_down(row,col):
    screen.draw_OG_soldier(row-1,col)
    game_field.mark_soldier_position(row-1,col)
