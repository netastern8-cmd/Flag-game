import pygame
import game_field
import soldier

from game_field import switch_screen
from soldier import soldier_body
from tests import print_matrix

state = {
    "is_soldier_on_mine": False,
    "is_soldier_on_flag": False,
    "enter_key_on": False,
    "running": True,
    "arrow_key_on": False,
}

game_field.place_mines()
game_field.mark_soldier_position(0,0)

print_matrix(game_field.FIELD)

def main():
    pygame.init()

    while state["running"]:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state["running"] = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state["enter_key_on"] = True

                    game_field.switch_screen()

                    state["enter_key_on"] = False


        if not state["enter_key_on"]:
            soldier_movement()
    pygame.quit()


def check_flag():
    pass


def check_mines(lst_mines):
    for row,col in lst_mines:
        if game_field.FIELD[row][col] == "x":
            return True

        return False


def soldier_movement():
 for row in game_field.FIELD:
    for col in row:
     keys_pressed = pygame.key.get_pressed()
     if keys_pressed[pygame.K_RIGHT]:
        soldier.move_soldier_right(game_field.FIELD[row], game_field.FIELD[col])

     if keys_pressed[pygame.K_LEFT]:
         soldier.move_soldier_left(game_field.FIELD[row], game_field.FIELD[col])


     if keys_pressed[pygame.K_UP]:
         soldier.move_soldier_up(game_field.FIELD[row], game_field.FIELD[col])


     if keys_pressed[pygame.K_DOWN]:
         soldier.move_soldier_down(game_field.FIELD[row], game_field.FIELD[col])



main()