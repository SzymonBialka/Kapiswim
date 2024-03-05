import pygame
import os
from my_class.class_baz import Click
from my_class.menu_class import *
from achivment import main_achivment
from shop import main_shop
from play import main_play
from ranking import main_ranking
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption("Kapiswim")


clock = pygame.time.Clock()
pygame.mixer.music.load(os.path.join('.','mp','muzyka.mp3'))
pygame.mixer.music.play(-1)
path = os.path.join('.', 'image')
file_names=sorted(os.listdir(path))
Backgroud = pygame.image.load(os.path.join(path, '1tlo_main.png')).convert()
Images_B={}
Images_P=[]
Images_PS=[]
Images_BS_mini=[]
Images_B_all={}
Images_O={}
Images_A=[]
Images_G=[]
for file_name in file_names:
    image_name=file_name[:3].upper()
    if image_name=="TLO":
        Images_B[file_name]=pygame.image.load(os.path.join(path,file_name)).convert()
    elif image_name=="POS":
        Images_P.append(pygame.image.load(os.path.join(path,file_name)).convert_alpha(Backgroud))
    elif image_name=="PRZ":
        Images_O[file_name]=pygame.image.load(os.path.join(path,file_name)).convert_alpha()
    elif image_name=="SKP":
        Images_BS_mini.append(pygame.image.load(os.path.join(path,file_name)).convert_alpha(Backgroud))
    elif image_name=="ALL":
        Images_B_all[file_name]=pygame.image.load(os.path.join(path,file_name)).convert()
    elif image_name=="GWI":
        Images_G.append(pygame.image.load(os.path.join(path,file_name)).convert_alpha(Backgroud))
    elif image_name=="POZ":
        Images_A.append(pygame.image.load(os.path.join(path,file_name)).convert_alpha(Backgroud))
    elif image_name=="SKL":
        Images_PS.append(pygame.image.load(os.path.join(path, file_name)).convert_alpha(Backgroud))
Images_b_all=[[Images_B_all["all_sklep_tlo11a.png"],Images_B_all["all_sklep_tlo11b.png"],Images_B_all["all_sklep_tlo11c.png"]],[Images_B_all["all_sklep_tlo22a.png"],Images_B_all["all_sklep_tlo22b.png"],Images_B_all["all_sklep_tlo22c.png"]],[Images_B_all["all_sklep_tlo33a.png"],Images_B_all["all_sklep_tlo33c.png"],Images_B_all["all_sklep_tlo33b.png"]]]
Images_O_mini=[[Images_O["przeszkoda1a.png"],Images_O["przeszkoda1b.png"],Images_O["przeszkoda1c.png"]],[Images_O["przeszkoda2a.png"],Images_O["przeszkoda2b.png"],Images_O["przeszkoda2e.png"]],[Images_O["przeszkoda3a.png"],Images_O["przeszkoda3c.png"],Images_O["przeszkoda3f.png"]]]
Images_B_big=[[Images_B["tlo1.png"],Images_B["tlo2.png"],Images_B["tlo3.png"]],[Images_B["tlo11.png"],Images_B["tlo22.png"],Images_B["tlo33.png"]],[Images_B["tlo111.png"],Images_B["tlo222.png"],Images_B["tlo333.png"]]]
Images_O_game=[[[Images_O["przeszkoda1a.png"],Images_O["przeszkoda1e.png"]],[Images_O["przeszkoda1b.png"],Images_O["przeszkoda1f.png"],Images_O["przeszkoda3d.png"]],[Images_O["przeszkoda1c.png"],Images_O["przeszkoda1d.png"],Images_O["przeszkoda3e.png"]]],[[Images_O["przeszkoda2a.png"],Images_O["przeszkoda2d.png"]],[Images_O["przeszkoda2b.png"],Images_O["przeszkoda2c.png"]],[Images_O["przeszkoda2e.png"],Images_O["przeszkoda2f.png"]]],[[Images_O["przeszkoda3a.png"],Images_O["przeszkoda3b.png"]],[Images_O["przeszkoda3c.png"],Images_O["przeszkoda3c.png"]],[Images_O["przeszkoda3f.png"],Images_O["przeszkoda3f.png"]]]]
play_img=pygame.image.load(os.path.join(path,'play1.png')).convert_alpha(Backgroud)
shop_img=pygame.image.load(os.path.join(path,'shop1.png')).convert_alpha(Backgroud)
achivment_img=pygame.image.load(os.path.join(path,'nagrody1.png')).convert_alpha(Backgroud)
ranking_img=pygame.image.load(os.path.join(path,'puchar.png')).convert_alpha(Backgroud)
music_img1=pygame.image.load(os.path.join(path,'muzyka.png')).convert_alpha(Backgroud)
music_img2=pygame.image.load(os.path.join(path,'muzyka2.png')).convert_alpha(Backgroud)
apple_img=pygame.image.load(os.path.join(path,'apple.png')).convert_alpha(Backgroud)
back_img=pygame.image.load(os.path.join(path, 'x.png')).convert_alpha(Backgroud)
play=Click(play_img,1600 // 2, 350)
shop=Click(shop_img,1600//2,450)
kapi=Kapi(Images_P[0],0,270,3,0)
kapi_2=Kapi(Images_P[2],300,510,3,0)
achivment=Click(achivment_img,1600//2,550)
music=Music(music_img1,1510,850,music_img2)
player=Player(Images_P,300,580,Images_PS)
BLACK=pygame.color.THECOLORS['black']
ranking=Click(ranking_img,120,780)
back_window=Back(back_img,1500,50)



def main1(text):
    def callback_function_shop():
        main_shop(level)

    def callback_function_play():
        main_play(level,Images_A,Images_G)

    def callback_function_achivment():
        main_achivment(level)

    def callback_funktion_ranking():
        main_ranking(level)


    level = Level(player, Images_O_mini,Images_O_game,Images_BS_mini,Images_B_big,BLACK,Images_b_all,text,apple_img)
    window_open = [True]
    music_enable=[True]
    while window_open:
        screen.blit(Backgroud, (0, 0))
        kapi.draw(screen)
        kapi_2.draw(screen)
        kapi.update()
        kapi_2.update()
        kapi.check()
        kapi_2.check()
        play.draw(screen)
        shop.draw(screen)
        achivment.draw(screen)
        ranking.draw(screen)
        music.draw(screen)
        back_window.draw(screen)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                window_open[0] = False
            back_window.handle_event(event,window_open)
            achivment.handle_event(event,callback_function_achivment)
            music.handle_event(event,music_enable)
            shop.handle_event(event,callback_function_shop)
            play.handle_event(event,callback_function_play)
            ranking.handle_event(event,callback_funktion_ranking)
        if music_enable[0]:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

        pygame.display.flip()
        clock.tick(30)


