import pygame
import screen
import random
import soldier

MINE_LST=[]
FLAG_INDEXES = []
FIELD = [["_" for _ in range(50)] for _ in range(25)]


def place_mines():
    while len(MINE_LST)<20:
        row,col=random.randint(0,24),random.randint(0,47)
        if valid_mine_placement(row,col):
            MINE_LST.append((row, col))
            mark_mine_in_field(row,col)
            screen.draw_mine(row, col)

def valid_mine_placement(row,col):
    valid=False
    if (row, col) != (soldier.soldier_legs(0, 0) or soldier.soldier_body(0, 0)):
        if (row, col) not in MINE_LST:
            if FIELD[row][col] != "x":
                valid=True
    return valid

def mark_mine_in_field(row,col):
    for i in range(3):
        FIELD[row][col+i] = "x"

def mark_soldier_position(s_row,s_col):
    for row in range(len(FIELD)):
        for col in range(len(FIELD[0])):
            if FIELD[row][col]=="s":
                FIELD[row][col]="_"
    FIELD[s_row][s_col]="s"

def mark_flag():
    for row in range(22, 25):
        for col in range(46, 50):
            FLAG_INDEXES.append((row, col))

def switch_screen():
    screen.frozen_screen()
    pygame.time.delay(1000)
    screen.moving_screen()


def check_mines(legs):
    for item in legs:
        (row,col) =item[0],item[1]
        if FIELD[row][col] == "x":
            return True
    return False


def check_flag(body):
    for item in body:
        (row,col) =item[0],item[1]
        if (row, col) in FLAG_INDEXES:
            return True
    return False
