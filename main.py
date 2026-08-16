import pygame
import screen

state={"is_soldier_on_mine":False,
       "is_soldier_on_flag":False,
       "is_enter":False,
       "is_window_open":True}




def main():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
    pygame.quit()

if __name__ == "__main__":
    main()