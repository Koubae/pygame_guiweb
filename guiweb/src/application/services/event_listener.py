import pygame
from ...config.constants import MOUSE_BUTTON_MAP

class EventListener:


    def __init__(self, app):
        self.app = app
        self.events: dict = {}

    def events_new(self) -> None:
        """Clear the events container"""
        self.events.clear()

    def events_listen(self):
        """Register the events
            NOTE: we could do, as an approach to listen to ALL events and not arbitrarly
            add if - else statemens for target events
        """
        self.events_new()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  # x button and esc terminates the game!
                self.app.switch_off()
                return
            if event.type not in self.events:
                self.events[event.type] = {}

            # ............. Mouse ............. #
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.events[event.type][MOUSE_BUTTON_MAP[event.button]] = True
            # ............. Keyboard ............. #
            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                self.events[event.type][event.key] = True
