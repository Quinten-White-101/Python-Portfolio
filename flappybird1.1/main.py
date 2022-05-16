# quinten white
#4/27/2022

#imports
import pygame as pg
from pygame.locals import *
import random

#initialize pygame
pg.init()
clock = pg.time.Clock()
fps = 60

#screen specs
width = 864
height = 936

screen = pg.display.set_mode((width, height))
pg.display.set_caption("Flappy Bird")

#define font
font = pg.font.SysFont('ARIAL', 40)
#define colors
white = (255,255,255)


#define game variables
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 170
pipe_frequency = 1500  #1.5 seceonds
last_pipe = pg.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False


#load images
bg = pg.image.load("imgs/bg.png")
ground = pg.image.load("imgs/ground.png")
bttn_img = pg.image.load('imgs/restart.png')

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x,y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(height/2)
    score = 0
    return score


class Bird(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pg.image.load(f"imgs/bird{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.clicked = False


    def update(self):
        #gravity
        if flying == True:
            self.vel += 0.5

            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

            if game_over == False:

                #jumping/fly
                if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.vel =- 10
                if pg.mouse.get_pressed()[0] == 0:
                    self.clicked = False

                #animations
                self.counter += 1
                flap_cooldown = 5

                if self.counter > flap_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.images):
                        self.index = 0
                self.image = self.images[self.index]

                #rotates the bird / animates it
                self.image = pg.transform.rotate(self.images[self.index], self.vel * -2)
            else:
                self.image = pg.transform.rotate(self.images[self.index], -90)

class Pipe(pg.sprite.Sprite):
    def __init__(self, x,y, position):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('imgs/pipe.png')
        self.rect = self.image.get_rect()
        #POSITION  1 IS FROM THE TOP, -1 IS FROM THE BOTTOM
        if position == 1:
            self.image = pg.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x,y - int(pipe_gap/2)]
        if position == -1:
            self.rect.topleft = [x,y + int(pipe_gap/2)]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()

class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):

        action = False

        #get the mouse pos
        pos = pg.mouse.get_pos()

        #check if mouse is over bttn
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                action = True

        #draws the button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
#birs image groups
bird_group = pg.sprite.Group()
pipe_group = pg.sprite.Group()

flappy = Bird(100, int(height / 2))

bird_group.add(flappy)

#creates the restart button
button = Button(width//2 - 50 , height // 2 -100, bttn_img)


run = True
while run:
    clock.tick(fps)

    #draws background
    screen.blit(bg, (0,0))

    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)


    #draws the ground
    screen.blit(ground, (ground_scroll, 768))

    #check the score
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
            and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
            and pass_pipe == False:
            pass_pipe = True
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False

    draw_text(str(score), font, white, int(width/2), 20)






    #pipe collsions
    if pg.sprite.groupcollide(bird_group, pipe_group,False, False) or flappy.rect.top < 0:
        game_over = True


    #check if bird has hit the ground
    if flappy.rect.bottom >= 768:
        game_over = True
        flying = False


    if game_over == False and flying == True:
        #generate new pipes
        time_now = pg.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100,100)
            btm_pipe = Pipe(width, int(height / 2) + pipe_height,-1)
            top_pipe = Pipe(width, int(height / 2) + pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now


        # draw and scrolls the ground
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
        pipe_group.update()

    # checks for the game over and restart bttn
    if game_over == True:
        if button.draw() == True:
            game_over = False
            score = reset_game()



    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    pg.display.update()
pg.quit()

