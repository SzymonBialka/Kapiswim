import pygame
import os
from my_class.class_baz import Ikon,Click

class Achivment_ikon(Ikon):
    def __init__(self, image, px, py,nr):
        self.image_tab=image
        super().__init__( self.image_tab[nr], px, py)

    def draw(self, surface,coin,level):
        if coin>=10 and coin<12:
            surface.blit(self.image, self.rect)
            level.number_A[level.number_b][0]=1
        elif coin>=20 and coin<22:
            surface.blit(self.image, self.rect)
            level.number_A[level.number_b][1]=1
        elif coin>=30 and coin<32:
            surface.blit(self.image, self.rect)
            level.number_A[level.number_b][2]=1

class Achivment_star(Ikon):
    def __init__(self, image, px, py,):
        self.image_tab=image
        super().__init__( self.image_tab[0], px, py)

    def draw(self, surface,coin):
        if coin>=10 and coin<12:
            surface.blit(self.image, self.rect)
        elif coin>=20 and coin<22:
            surface.blit(self.image_tab[1], self.rect)
        elif coin>=30 and coin<32:
            surface.blit(self.image_tab[2], self.rect)

class Cup(Ikon):
    def draw(self, surface,coin):
        if coin>=50 and coin<52:
            surface.blit(self.image,self.rect)

class Back(Click):
    def __init__(self, image, px, py):
        super().__init__(image, px, py)

    def handle_event(self, event, window_open):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                window_open[0]=False
