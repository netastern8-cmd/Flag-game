import screen
import game_field

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