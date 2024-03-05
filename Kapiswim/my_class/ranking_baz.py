import pygame
from my_class.class_baz import Click

class Back(Click):
    def __init__(self, image, px, py):
        super().__init__(image, px, py)

    def handle_event(self, event, window_open):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                window_open[0]=False


