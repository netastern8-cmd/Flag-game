
import screen
import game_field

def move_soldier_right(row,col):
   game_field.mark_soldier_position(row,col+1)
   screen.draw_OG_soldier((row,col+1))

def move_soldier_left(row,col):
    game_field.mark_soldier_position(row,col-1)
    screen.draw_OG_soldier((row,col-1))

def move_soldier_up(row,col):
    game_field.mark_soldier_position(row - 1, col)
    screen.draw_OG_soldier((row+1,col))

def move_soldier_down(row,col):
    game_field.mark_soldier_position(row+1,col)
    screen.draw_OG_soldier((row-1,col))
