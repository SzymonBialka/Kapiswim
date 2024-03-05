import pygame
import os
import mysql.connector
from my_class.class_baz import Text,Ikon
from my_class.achivment_class import *
pygame.init()

screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption("Kapiswim")

clock = pygame.time.Clock()
path = os.path.join('.', 'image')
Black=pygame.color.THECOLORS['black']
Backgroud = pygame.image.load(os.path.join(path, '1tlo_main.png')).convert()
back_img=pygame.image.load(os.path.join(path, 'x.png')).convert_alpha(Backgroud)
rank_img=pygame.image.load(os.path.join(path, 'rank.png')).convert_alpha(Backgroud)
back=Back(back_img,1500,50)
def get_top_scores():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ranking"
    )

    cursor = connection.cursor()

    query = "SELECT name, points FROM rankings ORDER BY points DESC LIMIT %s"
    limit=10
    cursor.execute(query, (limit,))
    top_scores = cursor.fetchall()

    cursor.close()
    connection.close()

    return top_scores

score=get_top_scores()
rank=Ikon(rank_img,1600//2,900//2)
ranking_N1=Text(score[0][0],Black,722,250,font_size=55 )
ranking_N2=Text(score[1][0],Black,722,295,font_size=55 )
ranking_N3=Text(score[2][0],Black,722,340,font_size=55 )
ranking_N4=Text(score[3][0],Black,722,382,font_size=55 )
ranking_N5=Text(score[4][0],Black,722,427,font_size=55 )
ranking_N6=Text(score[5][0],Black,722,469,font_size=55 )
ranking_N7=Text(score[6][0],Black,722,516,font_size=55 )
ranking_N8=Text(score[7][0],Black,722,560,font_size=55 )
ranking_N9=Text(score[8][0],Black,722,605,font_size=55 )
ranking_N10=Text(score[9][0],Black,722,650,font_size=55 )
ranking_S1=Text(score[0][1],Black,1080,250,font_size=55 )
ranking_S2=Text(score[1][1],Black,1080,295,font_size=55 )
ranking_S3=Text(score[2][1],Black,1080,340,font_size=55 )
ranking_S4=Text(score[3][1],Black,1080,382,font_size=55 )
ranking_S5=Text(score[4][1],Black,1080,427,font_size=55 )
ranking_S6=Text(score[5][1],Black,1080,469,font_size=55 )
ranking_S7=Text(score[6][1],Black,1080,516,font_size=55 )
ranking_S8=Text(score[7][1],Black,1080,560,font_size=55 )
ranking_S9=Text(score[8][1],Black,1080,605,font_size=55 )
ranking_S10=Text(score[9][1],Black,1080,650,font_size=55 )

def main_ranking(level):
    window_open = [True]
    text = Text(level.name,Black,1600//2,50,font_size=65 )
    while window_open[0]:
        screen.blit(Backgroud, (0, 0))
        rank.draw(screen)
        back.draw(screen)
        text.draw(screen)
        ranking_N1.draw(screen)
        ranking_N2.draw(screen)
        ranking_N3.draw(screen)
        ranking_N4.draw(screen)
        ranking_N5.draw(screen)
        ranking_N6.draw(screen)
        ranking_N7.draw(screen)
        ranking_N8.draw(screen)
        ranking_N9.draw(screen)
        ranking_N10.draw(screen)
        ranking_S1.draw(screen)
        ranking_S2.draw(screen)
        ranking_S3.draw(screen)
        ranking_S4.draw(screen)
        ranking_S5.draw(screen)
        ranking_S6.draw(screen)
        ranking_S7.draw(screen)
        ranking_S8.draw(screen)
        ranking_S9.draw(screen)
        ranking_S10.draw(screen)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                window_open[0] = False
            back.handle_event(event,window_open)

        pygame.display.flip()
        clock.tick(30)
