import pygame
import screen

from game_field import switch_screen
from soldier import soldier_body

state = {
    "is_soldier_on_mine": False,
    "is_soldier_on_flag": False,
    "enter_key_on": False,
    "running": True,
    "arrow_key_on": False,
}
soldier_body(0,0)
def main():
    pygame.init()

    while state["running"]:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state["running"] = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state["enter_key_on"] = True




                    state["enter_key_on"] = False


        if not state["enter_key_on"]:
            soldier_movement()

    pygame.quit()


def check_flag():
    pass


def check_mines():
    pass


def soldier_movement():
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_RIGHT]:
        soldier.move_right()
        pass
    if keys_pressed[pygame.K_LEFT]:
        pass

    if keys_pressed[pygame.K_UP]:
        pass

    if keys_pressed[pygame.K_DOWN]:
        pass


main()