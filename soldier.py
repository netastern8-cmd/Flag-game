import pygame
import consts
import screen


def move_soldier_right(row,col):
   soldier= screen.drew_OG_soldier(row,col+1)
   return soldier
def move_soldier_left(row,col):
    soldier= screen.drew_OG_soldier(row,col-1)
    return soldier
def move_soldier_up(row,col):
    soldier= screen.drew_OG_soldier(row+1,col)
    return soldier
def move_soldier_down(row,col):
    soldier= screen.drew_OG_soldier(row-1,col)
    return soldier
