import pygame
import sys
from menu import Menu
from render_utils import render_text
from constants import *

class GameOverMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        start_text, start_rect = render_text(
            self.font,
            "Try Again",
            (255, 255, 255),
            (pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2 - 50)
        )
        self.buttons["again"] = (start_text, start_rect)
        quit_text, quit_rect = render_text(
            self.font,
            "Quit To Main Menu",
            (255, 255, 255),
            (pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2 + 50)
        )
        self.buttons["quit"] = (quit_text, quit_rect)

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.screen.blits((
                (self.buttons["again"][0], self.buttons["again"][1]),
                (self.buttons["quit"][0], self.buttons["quit"][1])
            ))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if  self.buttons["again"][1].collidepoint(event.pos):
                        return NEW_GAME
                    if self.buttons["quit"][1].collidepoint(event.pos):
                        return START_MENU