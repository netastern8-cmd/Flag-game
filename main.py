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
    screen.draw_game(state)
    while state["running"]:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state["running"] = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state["enter_key_on"] = True

        if not state["enter_key_on"]:
            soldier_movement()

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


def soldier_movement():
 for row in range(len(game_field.FIELD)):
     for col in game_field[row]:
      keys_pressed = pygame.key.get_pressed()
      if keys_pressed[pygame.K_RIGHT]:
         movement.move_soldier_right(game_field.FIELD[row],game_field.FIELD[row][col])

      if keys_pressed[pygame.K_LEFT]:
         movement.move_soldier_left(game_field.FIELD[row],game_field.FIELD[row][col])


      if keys_pressed[pygame.K_UP]:
         movement.move_soldier_up(game_field.FIELD[row],game_field.FIELD[row][col])


      if keys_pressed[pygame.K_DOWN]:
         movement.move_soldier_down(game_field.FIELD[row],game_field.FIELD[row][col])



main()