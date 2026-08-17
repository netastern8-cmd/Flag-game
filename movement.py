import pygame
import screen
import game_field

def move_soldier_right(row,col):
   screen.moving_screen()
   screen.draw_OG_soldier((row,col+1))
   game_field.mark_soldier_position(row,col+1)
   pygame.time.wait(200)

def move_soldier_left(row,col):
    screen.moving_screen()
    screen.draw_OG_soldier((row,col-1))
    game_field.mark_soldier_position(row,col-1)
    pygame.time.wait(200)

def move_soldier_up(row,col):
    screen.moving_screen()
    screen.draw_OG_soldier((row+1,col))
    game_field.mark_soldier_position(row+1,col)
    pygame.time.wait(200)

def move_soldier_down(row,col):
    screen.moving_screen()
    screen.draw_OG_soldier((row-1,col))
    game_field.mark_soldier_position(row-1,col)
    pygame.time.wait(200)