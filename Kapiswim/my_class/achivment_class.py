import pygame
import os
from my_class.class_baz import Click,Ikon


class Back(Click):
    def __init__(self, image, px, py):
        super().__init__(image, px, py)

    def handle_event(self, event, window_open):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                window_open[0]=False

class Ikon_acivment(Ikon):
    def __init__(self,img, image, px, py):
        super().__init__(img, px, py)
        self.image_tab=image

    def draw(self, surface,number_A):
        surface.blit(self.image_tab[number_A], self.rect)