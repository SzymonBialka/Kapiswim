import pygame
import os
from my_class.class_baz import Click,Ikon


class Plus(Click):
    def __init__(self, image, px, py):
        super().__init__(image, px, py)



    def handle_event(self, event,level):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                level.number_b=1

class Minus(Click):
    def __init__(self, image, px, py):
        super().__init__(image, px, py)



    def handle_event(self, event,level):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                level.number_b=-1

class Plus1(Click):
    def __init__(self, image, px, py):
        super().__init__(image, px, py)



    def handle_event(self, event,level):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                level.number_0=1

class Minus1(Click):
    def __init__(self, image, px, py):
        super().__init__(image, px, py)



    def handle_event(self, event,level):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                level.number_0=-1

class Plus2(Click):
    def __init__(self, image, px, py):
        super().__init__(image, px, py)



    def handle_event(self, event,level):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                level.player.number=1

class Minus2(Click):
    def __init__(self, image, px, py):
        super().__init__(image, px, py)



    def handle_event(self, event,level):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                level.player.number=-1

class Ikon_update(Ikon):
    def __init__(self, image, px, py):
        super().__init__( image, px, py)


    def change(self,img):
        self.image=img

class End(Click):

    def handle_event(self, event,window_open):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                window_open[0]=False

