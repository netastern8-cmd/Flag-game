import pygame
import consts
import screen
import random

from main import state

FIELD=[]
mine_lst=[]

def create():
 FIELD = [[0 for _ in range(25)] for _ in range(50)]



def place_mines():
    while len(mine_lst)<20:
        row,col=random.randint(0,24),random.randint(0,47)
        if (row,col) not in mine_lst:
            mine_lst.append((row,col))
            screen.drew_mine(row, col)

def mark_mine_in_field(row,col):
    for row in range(len(FIELD)):
        for col in range(len(FIELD[0])):
            if (row, col) in mine_lst or (row, col - 1) in mine_lst or (row, col - 2) in mine_lst:
                FIELD[row][col] = "x"


def switch_screen():
    screen.frozen_screen()
    pygame.time.delay(1000)
    screen.moving_screen()


def check_mines(lst_mines):
    for row,col in lst_mines:
        if FIELD[row][col] == "x":
            return True

        return False