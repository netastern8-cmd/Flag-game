import pygame
import consts
import screen
import random

field=[]
mine_lst=[]

def create():
 global field
 field = [[0 for _ in range(25)] for _ in range(50)]
 print(len(field), len(field[0]))


def place_mines():
    while len(mine_lst)<20:
        row,col=random.randint(0,24),random.randint(0,47)
        if (row,col) not in mine_lst:
            mine_lst.append((row,col))
            screen.drew_mine(row, col)

def drew_mine_in_field(row,col):
    global field
    for row in range(len(field)):
        for col in range(len(field[0])):
            if (row, col) in mine_lst or (row, col - 1) in mine_lst or (row, col - 2) in mine_lst:
                field[row][col] = "x"
