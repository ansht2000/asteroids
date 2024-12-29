import pygame
from constants import *
from render_utils import render_text
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from game import Game
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    game_state = START_MENU
    # initialize game to be empty
    game = None

    while(1):
        if game_state == START_MENU:
            game_state = start_menu(screen)
        if game_state == GAME:
            # if an instance of a game is running
            # delete it and create another
            if game:
                del game
            game = Game(screen, clock, dt)
            game_state = game.run()
        if game_state == GAME_OVER:
            game_state = game_over(screen)

def start_menu(screen):
    while(1):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("Arial", 36)
        start_text, start_rect = render_text(font, "Start Game", (255, 255, 255), (pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2 - 50))
        quit_text, quit_rect = render_text(font, "Quit Game", (255, 255, 255), (pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2 + 50))
        screen.blits(((start_text, start_rect), (quit_text, quit_rect)))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  start_rect.collidepoint(event.pos):
                    return GAME
                if quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

def game_over(screen):
    while(1):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("Arial", 36)
        retry_text, retry_rect = render_text(font, "Try Again", (255, 255, 255), (pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2 - 50))
        quit_text, quit_rect = render_text(font, "Quit to Main Menu", (255, 255, 255), (pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2 + 50))
        screen.blits(((retry_text, retry_rect), (quit_text, quit_rect)))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_rect.collidepoint(event.pos):
                    return GAME  # Switch back to the game state
                if quit_rect.collidepoint(event.pos):
                    return START_MENU

if __name__ == "__main__":
    main()