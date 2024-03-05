import pygame
import os

class Click(pygame.sprite.Sprite):
    def __init__(self, image, px, py):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = px, py


    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_event(self, event,callback):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                callback()


class Ikon(pygame.sprite.Sprite):
    def __init__(self, image, px, py):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = px, py

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Objective(pygame.sprite.Sprite):
    def __init__(self, image, px, py,speed_x,speed_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = px, py
        self.speed_x = speed_x
        self.speed_y=speed_y

    def update(self):
        self.rect.move_ip(self.speed_x, self.speed_y)

    def draw(self,surface):
        surface.blit(self.image,self.rect)

class Text:
    def __init__(self, text, text_colour, px, py, font_type=None, font_size=74):
        self.text = str(text)
        font = pygame.font.SysFont(font_type, font_size)
        self.image = font.render(self.text, True, text_colour)
        self.rect = self.image.get_rect()
        self.rect.center = px, py

    def draw(self, surface):
        surface.blit(self.image, self.rect)
