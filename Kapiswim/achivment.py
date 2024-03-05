import pygame
import os
from my_class.class_baz import Ikon,Text
from my_class.achivment_class import *
pygame.init()

screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption("Kapiswim")

clock = pygame.time.Clock()

path = os.path.join('.', 'image')
Black=pygame.color.THECOLORS['green']
Backgroud = pygame.image.load(os.path.join(path, '1tlo_main.png')).convert()
trophies_img1=pygame.image.load(os.path.join(path, 'Poziom1.png')).convert()
trophies_img1a=pygame.image.load(os.path.join(path, '1Poziom1a.png')).convert()
trophies_img2=pygame.image.load(os.path.join(path, 'Poziom2.png')).convert()
trophies_img2a=pygame.image.load(os.path.join(path, '1Poziom2a.png')).convert()
trophies_img3=pygame.image.load(os.path.join(path, 'Poziom33.png')).convert()
trophies_img3a=pygame.image.load(os.path.join(path, '1Poziom33a.png')).convert()
star_img3=pygame.image.load(os.path.join(path, 'gwiazdki3.png')).convert_alpha(trophies_img1)
star_img1=pygame.image.load(os.path.join(path, 'gwiazdki1.png')).convert_alpha(trophies_img1)
star_img2=pygame.image.load(os.path.join(path, 'gwiazdki2.png')).convert_alpha(trophies_img1)
cup_img=pygame.image.load(os.path.join(path, 'puchar.png')).convert_alpha(Backgroud)
back_img=pygame.image.load(os.path.join(path, 'x.png')).convert_alpha(Backgroud)
trophies_1=Ikon_acivment(trophies_img1a,[trophies_img1a,trophies_img1],520,200)
trophies_2=Ikon(star_img1,520,200)
trophies_3=Ikon_acivment(trophies_img1a,[trophies_img1a,trophies_img1],880,200)
trophies_4=Ikon(star_img2,880,200)
trophies_5=Ikon_acivment(trophies_img1a,[trophies_img1a,trophies_img1],1240,200)
trophies_6=Ikon(star_img3,1240,200)
trophies_7=Ikon_acivment(trophies_img2a,[trophies_img2a,trophies_img2],520,422)
trophies_8=Ikon(star_img1,520,422)
trophies_9=Ikon_acivment(trophies_img2a,[trophies_img2a,trophies_img2],880,422)
trophies_10=Ikon(star_img2,880,422)
trophies_11=Ikon_acivment(trophies_img2a,[trophies_img2a,trophies_img2],1240,422)
trophies_12=Ikon(star_img3,1240,422)
trophies_13=Ikon_acivment(trophies_img3a,[trophies_img3a,trophies_img3],520,644)
trophies_14=Ikon(star_img1,520,644)
trophies_15=Ikon_acivment(trophies_img3a,[trophies_img3a,trophies_img3],880,644)
trophies_16=Ikon(star_img2,880,644)
trophies_17=Ikon_acivment(trophies_img3a,[trophies_img3a,trophies_img3],1240,644)
trophies_18=Ikon(star_img3,1240,644)
back=Back(back_img,1500,50)
cup=Ikon(cup_img,180,200)

def main_achivment(level):
    window_open = [True]
    text = Text(level.name,Black,1600//2,50,font_size=65 )
    while window_open[0]:
        screen.blit(Backgroud, (0, 0))
        trophies_1.draw(screen,level.number_A[0][0])
        trophies_2.draw(screen)
        trophies_3.draw(screen,level.number_A[0][1])
        trophies_4.draw(screen)
        trophies_5.draw(screen,level.number_A[0][2])
        trophies_6.draw(screen)
        trophies_7.draw(screen,level.number_A[1][0])
        trophies_8.draw(screen)
        trophies_9.draw(screen,level.number_A[1][1])
        trophies_10.draw(screen)
        trophies_11.draw(screen,level.number_A[1][2])
        trophies_12.draw(screen)
        trophies_13.draw(screen,level.number_A[2][0])
        trophies_14.draw(screen)
        trophies_15.draw(screen,level.number_A[2][1])
        trophies_16.draw(screen)
        trophies_17.draw(screen,level.number_A[2][2])
        trophies_18.draw(screen)
        cup.draw(screen)
        back.draw(screen)
        text.draw(screen)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                window_open[0] = False
            back.handle_event(event,window_open)

        pygame.display.flip()
        clock.tick(30)
