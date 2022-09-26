import pygame
from pygame.math import Vector2

from ..gui import GuiPanel, GuiButton
from .view_manager import ViewManager

class ViewHome(ViewManager):

    def __init__(self, *args):
        super().__init__(*args)

    def view_logic(self):


        components_gui = pygame.sprite.Group()
        # panel
        panel_left_size = Vector2(250, self.app.win_height)
        panel_left = GuiPanel(Vector2(0, 0), panel_left_size, self.app, self.app.background, None, {})
        components_gui.add(panel_left)

        # button
        def action(event: dict):
            if 'MOUSE_LEFT' not in event:
                return
            print("preess")

        button = GuiButton("New Shape", Vector2((panel_left_size.x / 2), 50), None,
                           self.app, panel_left.image, panel_left, {})
        button.add_event_listener("click", action)
        # add child to panel
        panel_left.children_add(button)




        # button button_navigate_about
        def view_about(event: dict):
            if 'MOUSE_LEFT' not in event:
                return
            self.app.view_current = "about"
            self.close_view = True

        button_navigate_about = GuiButton("About", Vector2((panel_left_size.x / 2), self.app.win_height - 50), None,
                           self.app, panel_left.image, panel_left, {
                'background_color': pygame.Color("grey"),
                'border_color': pygame.Color("grey")
                                          })
        button_navigate_about.add_event_listener("click", view_about)
        # add child to panel
        panel_left.children_add(button_navigate_about)

        def _update():
            components_gui.draw(self.app.background)
            components_gui.update()

        return _update