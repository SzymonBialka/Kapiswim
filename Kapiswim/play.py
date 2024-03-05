import pygame
import os
import mysql.connector
from my_class.play_class import *
pygame.init()



screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption("Kapiswim")

clock = pygame.time.Clock()

path = os.path.join('.', 'image')
file_names = sorted(os.listdir(path))
Backgroud = pygame.image.load(os.path.join(path, '1tlo_main.png')).convert()
cup_img = pygame.image.load(os.path.join(path, 'puchar.png')).convert_alpha(Backgroud)
end_img= pygame.image.load(os.path.join(path, 'game_over.png')).convert_alpha(Backgroud)
OBJECT_EVENT=pygame.USEREVENT+1
pygame.time.set_timer(OBJECT_EVENT,20000)
check_movement=[600]
cup=Cup(cup_img,1200,150)
end=Back(end_img,1600//2,900//2)

def main_play(level,Images_A,Images_G):
    achivment_ikon = Achivment_ikon(Images_A,1600//2,120,level.number_b)
    achivment_star=Achivment_star(Images_G,1600//2,120)
    window_open = [True]
    end_open = [False]
    end_interactions=[False]
    while window_open[0]:
        check_movement[0]+=1
        screen.blit(level.check_back(), (0, 0))
        if not end_interactions[0]:
            level.player.draw(screen)
            achivment_ikon.draw(screen,level.player.coins,level)
            achivment_star.draw(screen,level.player.coins)
            cup.draw(screen,level.player.coins)
            level.handle_event_obstacles(check_movement)
            level.apple_obj.draw(screen)
            level.draw_obstacles(screen)
            level.update_obstacles()
            level.apple_obj.update()
            level.give_coins()
            level.check_price()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                window_open[0] = False
            elif event.type==OBJECT_EVENT:
                level.speed+=0.5
            end.handle_event(event, window_open)
        if end_open[0]==True:
            end.draw(screen)

        level.kill_player(end_open)
        end_interactions=end_open
        keys=pygame.key.get_pressed()
        level.player.handle_event(keys)
        level.text.draw(screen)
        level.text_update()
        pygame.display.flip()
        clock.tick(30)
