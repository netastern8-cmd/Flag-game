import pygame
import game_field
import soldier
import screen
import movement

state = {
    "is_soldier_on_mine": False,
    "is_soldier_on_flag": False,
    "enter_key_on": False,
    "running": True,
    "arrow_key_on": False,
}

def main():
    pygame.init()
    screen.place_mines()
    screen.creat_moving_screen()
    screen.draw_game(state)
    while state["running"]:
        screen.moving_screen()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state["running"] = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state["enter_key_on"] = True
                    screen.switch_screen(state)

        if not state["enter_key_on"]:
            soldier_movement()
            pygame.time.wait(200)

        if win(soldier.find_soldier_position(game_field.FIELD)):
            state["is_soldier_on_flag"] = True

        elif lose(soldier.find_soldier_position(game_field.FIELD)):
            state["is_soldier_on_mine"] = True

    pygame.quit()


def win(position):
    body=soldier.soldier_body(position[0],position[1])
    if game_field.check_flag(body):
        return True
    return False

def lose(position):
    legs = soldier.soldier_legs(position[0],position[1])
    if game_field.check_mines(legs):
        return True
    return False

def position_valid(position):
    if position[0]>21 or position[0]<0:
        return False
    elif position[1]>48 or position[1]<0:
        return False
    else:
        return True

def soldier_movement():
    positon=soldier.find_soldier_position(game_field.FIELD)
    keys_pressed = pygame.key.get_pressed()
    if position_valid(positon):
        if keys_pressed[pygame.K_RIGHT]:
         movement.move_soldier_right(positon[0],positon[1])

        elif keys_pressed[pygame.K_LEFT]:
         movement.move_soldier_left(positon[0],positon[1])

        elif keys_pressed[pygame.K_UP]:
         movement.move_soldier_up(positon[0],positon[1])

        elif keys_pressed[pygame.K_DOWN]:
         movement.move_soldier_down(positon[0],positon[1])

main()