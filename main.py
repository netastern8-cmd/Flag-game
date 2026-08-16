import pygame
import screen
import soldier

state={"is_soldier_on_mine":False,
       "is_soldier_on_flag":False,
       "enter_key_on":False,
       "running":True,
       "arrow_key_on":False,}


def main():
    while state["running"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state["running"]=False


    pygame.quit()

'''
def soldier_movmement(key):
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_RIGHT]:


    if keys_pressed[pygame.K_LEFT]:

    if keys_pressed[pygame.K_UP]:

    if keys_pressed[pygame.K_DOWN]:
'''


if __name__ == "__main__":
    main()