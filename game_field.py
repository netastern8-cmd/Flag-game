import pygame
import consts
import screen
import random

MINE_LST=[]
FIELD = [["_" for _ in range(50)] for _ in range(25)]



def place_mines():
    while len(MINE_LST)<20:
        row,col=random.randint(0,24),random.randint(0,47)
        if (row,col) not in MINE_LST:
            MINE_LST.append((row, col))
            screen.drew_mine(row, col)

def mark_mine_in_field():
    for row in range(len(FIELD)):
        for col in range(len(FIELD[0])):
            if (row, col) in MINE_LST or (row, col - 1) in MINE_LST or (row, col - 2) in MINE_LST:
                FIELD[row][col] = "x"

def mark_soldier_position(s_row,s_col):
    for row in range(len(FIELD)):
        for col in range(len(FIELD[0])):
            if FIELD[row][col]=="s":
                FIELD[row][col]="_"
    FIELD[s_row][s_col]="s"

def switch_screen():
    screen.frozen_screen()
    pygame.time.delay(1000)
    screen.moving_screen()


