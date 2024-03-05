import pygame
import os
from my_class.shop_class import *
pygame.init()

screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption("Kapiswim")

clock = pygame.time.Clock()

path = os.path.join('.', 'image')
file_names = sorted(os.listdir(path))
Backgroud = pygame.image.load(os.path.join(path, '1tlo_main.png')).convert()
plus_img=pygame.image.load(os.path.join(path,"strzalka_w_prawo.png")).convert_alpha(Backgroud)
minus_img=pygame.image.load(os.path.join(path,"strzalka_w_lewo.png")).convert_alpha(Backgroud)
end_img=pygame.image.load(os.path.join(path,'x.png')).convert_alpha(Backgroud)
def main_shop(level):
    end=End(end_img,1500,60)
    tlo=Ikon_update(level.take_image_b_mini,300,200)
    hero=Ikon_update(level.player.take_image,300,367)
    hero_all=Ikon_update(level.player.take_image,1200,420)
    object=Ikon_update(level.take_image_O_mini,370,550)
    all_back=Ikon_update(level.take_image_all,1200,380)
    plus1=Plus(plus_img,860,200)
    mius1=Minus(minus_img,660,200)
    plus2=Plus1(plus_img,860,500)
    mius2=Minus1(minus_img,660,500)
    plus3=Plus2(plus_img,860,350)
    mius3=Minus2(minus_img,660,350)
    window_open=[True]
    while window_open[0]:
        screen.blit(Backgroud, (0, 0))
        tlo.draw(screen)
        end.draw(screen)
        hero.draw(screen)
        object.draw(screen)
        all_back.draw(screen)
        hero_all.draw(screen)
        plus1.draw(screen)
        mius1.draw(screen)
        plus2.draw(screen)
        mius2.draw(screen)
        plus3.draw(screen)
        mius3.draw(screen)
        tlo.change(level.take_image_b_mini)
        hero.change(level.player.take_image)
        all_back.change(level.take_image_all)
        hero_all.change(level.player.take_image)
        object.change(level.take_image_O_mini)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                window_open[0] = False
            plus1.handle_event(event,level)
            mius1.handle_event(event,level)
            plus2.handle_event(event,level)
            mius2.handle_event(event,level)
            plus3.handle_event(event,level)
            mius3.handle_event(event,level)
            end.handle_event(event,window_open)

        pygame.display.flip()
        clock.tick(30)
