import pygame
from constants import *
from game import Game
from start_menu import StartMenu
from game_over_menu import GameOverMenu
from pause_menu import PauseMenu

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    game_state = START_MENU
    # initialize game to be empty
    game = None
    start_menu = StartMenu(screen)
    game_over_menu = GameOverMenu(screen)
    pause_menu = PauseMenu(screen)

    while True:
        if game_state == START_MENU:
            game_state = start_menu.run()
        if game_state == NEW_GAME:
            # if an instance of a game is running
            # delete it and create another
            if game:
                del game
            game = Game(screen, clock, dt)
            game_state = game.run()
        if game_state == GAME_OVER:
            game_state = game_over_menu.run()
        if game_state == PAUSE_MENU:
            game_state = pause_menu.run()
        if game_state == RESUME_GAME:
            game_state = game.run()

if __name__ == "__main__":
    main()