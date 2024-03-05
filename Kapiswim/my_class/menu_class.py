import pygame
import os
import random
import mysql.connector
from my_class.class_baz import Objective,Click,Text

class Level:
    def __init__(self, player,img_o_a1,img_o_a2,img_back1,img_back2,black,img_all,name,img_apple):
        self.player = player
        self.obstacles=pygame.sprite.Group()
        self._number_0 = 0
        self._number_b = 0
        self.image_array_0_mini=img_o_a1
        self.back_mini=self.take_image_O_mini
        self.image_array_0_big=img_o_a2
        self.text = Text(self.player.coins, black, 1450, 150, font_size=85)
        self.img_back_array_mini=img_back1
        self.img_back_array_big=img_back2
        self.img_all=img_all
        self.name=name
        self.black=black
        self.speed=30.0
        self.number_A=[[0,0,0],[0,0,0],[0,0,0]]
        self.apple_img=img_apple
        self.apple_obj=pygame.sprite.Group()
        self.number_apple=0

    @property
    def number_0(self):
        return self._number_0
    @number_0.setter
    def number_0(self,number):
        if self._number_0+number>=0 and self._number_0+number<=2:
            self._number_0+=number
        else:
            self._number_0=self._number_0
    @property
    def number_b(self):
        return self._number_b
    @number_b.setter
    def number_b(self,number):
        if self._number_b+number>=0 and self._number_b+number<=2:
            self._number_b+=number
        else:
            self._number_b=self._number_b
    @property
    def take_image_O_mini(self):
        return self.image_array_0_mini[self._number_b][self._number_0]
    @property
    def take_image_b_mini(self):
        return self.img_back_array_mini[self._number_b]

    @property
    def take_image_all(self):
        return self.img_all[self._number_b][self._number_0]

    @property
    def take_image_b_big(self):
        return self.img_back_array_big[self._number_b]
    @property
    def take_image_O_big(self):
        return self.image_array_0_big[self._number_b][self._number_0]

    def text_update(self):
        self.text=Text(self.player.coins, self.black, 1450, 150, font_size=85)

    def handle_event_obstacles(self,check_movement):
        choice_img = random.choice(self.take_image_O_big)
        x=self.player.take_image_width/(self.speed*0.3)
        if check_movement[0]>x:
            choice_location=random.choice([580,350])
            obctacles=Obstacles(choice_img,1600,choice_location,-self.speed,0)
            self.obstacles.add(obctacles)
            check_movement[0]=0
            self.number_apple+=1
        if self.number_apple==15:
            if choice_location==580:
                apple=Obstacles(self.apple_img,1600,350,-self.speed,0)
                self.apple_obj.add(apple)
                self.number_apple=0
            else:
                apple=Obstacles(self.apple_img,1600,580,-self.speed,0)
                self.apple_obj.add(apple)
                self.number_apple=0

    def check_price(self):
        if pygame.sprite.spritecollide(self.player, self.apple_obj, True):
            self.player.coins+=3
            for apple in self.apple_obj:
                apple.kill()

    def draw_obstacles(self,screen):
        self.obstacles.draw(screen)

    def update_obstacles(self):
        self.obstacles.update()

    def give_coins(self):
        for obstacle in self.obstacles:
            if obstacle.rect.left<0:
                self.player.coins += 1
                obstacle.kill()

    def kill_player(self,end_open):
        if pygame.sprite.spritecollide(self.player, self.obstacles, True):
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="ranking"
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO rankings (name, points) VALUES (%s, %s)"
            val = (self.name, self.player.coins)
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            self.player.coins=0
            self.speed=30.0
            for object in self.obstacles:
                object.kill()
            end_open[0]=True
    def check_back(self):
        if self.player.coins>20 and self.player.coins<=40:
            return self.take_image_b_big[1]
        elif self.player.coins>40:
            return self.take_image_b_big[2]
        else:
            return self.take_image_b_big[0]

class Player(pygame.sprite.Sprite):
    def __init__(self, image, px, py,img_mini):
        super().__init__()
        self.image_array = img_mini
        self._number = 0
        self.image_array_b=image
        self.image = self.take_image_b
        self.rect = self.image.get_rect()
        self.rect.center = px, py
        self.coins=1



    @property
    def take_image(self):
        return self.image_array[self._number]
    @property
    def take_image_b(self):
        return self.image_array_b[self._number]

    @property
    def take_image_width(self):
        return self.image_array_b[self._number].get_width()
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self,plus_minus):
        if self._number+plus_minus>=0 and self._number+plus_minus<=2:
            self._number+=plus_minus
        else:
            self._number=self._number

    def draw(self, surface):
        surface.blit(self.take_image_b, self.rect)

    def handle_event(self,keys):
        if keys[pygame.K_LEFT] :
            self.rect.center=300,350
        if keys[pygame.K_RIGHT]:
            self.rect.center=300,580


class Obstacles(Objective):
    def __init__(self, image, px, py,speed_x,speed_y):
        super().__init__( image, px, py,speed_x,speed_y)
class Kapi(Objective):

    def __init__(self, image, px, py,speed_x,speed_y):
        super().__init__( image, px, py,speed_x,speed_y)
        self.screen_width = pygame.display.get_surface().get_width()
        self.x=px

    def check(self):
        if self.rect.right>self.screen_width:
            self.rect.right=self.x



class Music(Click):
    def __init__(self, image, px, py,image_1):
        super().__init__(image, px, py,)
        self.plus_img=image
        self.minus_img=image_1
    def handle_event(self, event,music_enable):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if music_enable[0]==True:
                    music_enable[0]=False
                    self.image=self.minus_img
                else:
                    music_enable[0]=True
                    self.image=self.plus_img


class Back(Click):
    def __init__(self, image, px, py):
        super().__init__(image, px, py)

    def handle_event(self, event, window_open):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                window_open[0]=False


