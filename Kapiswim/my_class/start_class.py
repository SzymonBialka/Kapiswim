import pygame
import os
from my_class.class_baz import Objective,Click

class Kapi(Objective):

    def __init__(self, image, px, py,speed_x,speed_y):
        super().__init__( image, px, py,speed_x,speed_y)
        self.screen_width = pygame.display.get_surface().get_width()
        self.x=px

    def check(self):
        if self.rect.right>self.screen_width:
            self.rect.right=self.x

class Back(Click):
    def __init__(self, image, px, py):
        super().__init__(image, px, py)

    def handle_event(self, event,):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                exit(0)


