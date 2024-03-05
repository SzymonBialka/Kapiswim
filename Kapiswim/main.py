import pygame
import os
from my_class.class_baz import Click
from menu import main1
from my_class.start_class import *

pygame.init()

screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption("Kapiswim")
clock = pygame.time.Clock()

path = os.path.join('.', 'image')
backgroud = pygame.image.load(os.path.join(path, '1tlo_main.png')).convert()
button=pygame.image.load(os.path.join(path,'strzalka_w_prawo.png')).convert_alpha(backgroud)
kapi_1jpg=pygame.image.load(os.path.join(path,'sklep_postac1.png')).convert_alpha(backgroud)
kapi_2jpg=pygame.image.load(os.path.join(path,'sklep_postac2.png')).convert_alpha(backgroud)
back_img=pygame.image.load(os.path.join(path, 'x.png')).convert_alpha(backgroud)
font = pygame.font.Font(None, 66)
text_color = (0, 0, 0)
input_rect = pygame.Rect(1600//2-200, 900// 2-50, 390, 80)
input_text = ""
max_characters = 10

click=Click(button,1000, 440)
kapi=Kapi(kapi_1jpg,0,300,3,0)
kapi1=Kapi(kapi_2jpg,0,500,3,0)
back_window=Back(back_img,1500,50)
def callback_function():
    main1(input_text)

window_open = True
if __name__== '__main__':
    while window_open:
        screen.blit(backgroud, (0, 0))
        kapi.draw(screen)
        back_window.draw(screen)
        kapi.update()
        kapi.check()
        kapi1.draw(screen)
        kapi1.update()
        kapi1.check()
        click.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False
                elif event.key == pygame.K_RETURN:
                    print(input_text)
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if len(input_text) < max_characters:
                        input_text += event.unicode
            back_window.handle_event(event)
        click.handle_event(event,callback_function)

        pygame.draw.rect(screen, (255, 255, 255), input_rect, 0)
        pygame.draw.rect(screen, (0, 0, 0), input_rect, 2)

        input_surface = font.render(input_text, True, text_color)
        input_rect.width = max(300, input_surface.get_width() + 10)
        screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))

        pygame.display.flip()
        clock.tick(30)

pygame.quit()