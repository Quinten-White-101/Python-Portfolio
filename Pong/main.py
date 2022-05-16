import pygame as pg, sys, random
import time
pg.init()

WIDTH, HEIGHT = 1280, 720

FONT = pg.font.SysFont("ARIAL", int(WIDTH / 20))

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pong")
CLOCK = pg.time.Clock()
#paddles
player = pg.Rect(WIDTH-110, HEIGHT/2-50, 10, 100)
opponent = pg.Rect(110, HEIGHT/2-50, 10, 100)
player_score, opponent_score = 0,0
win_score = 11
label = FONT.render(str("You Win"), True, "white")
label1 = FONT.render(str("Wpponent Wins"), True, "white")


#making the ball
ball = pg.Rect(WIDTH/2-10, HEIGHT/2-10,20,20)
x_speed, y_speed = 1,1
loop = True
while loop is True:
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        if player.top > 0:
            player.top -= 2
    if keys[pg.K_DOWN]:
        if player.bottom < HEIGHT:
            player.bottom += 2

    if ball.y >= HEIGHT:
        y_speed=-1
    if ball.y <= 0 :
        y_speed = 1
    if ball.x <= 0:
        player_score += 1
        ball.center = (WIDTH/2, HEIGHT/2)
        x_speed,y_speed = random.choice([1,-1]),random.choice([1,-1])
    if ball.x >= WIDTH:
        opponent_score += 1
        ball.center = (WIDTH / 2, HEIGHT / 2)
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
    if player.x - ball.width <= ball.x <= player.x and ball.y in range\
                (player.top-ball.width, player.bottom+ball.width):
        x_speed = -1
    if opponent.x - ball.width <= ball.x <= opponent.x and ball.y in range\
                (opponent.top-ball.width, opponent.bottom+ball.width):
        x_speed = 1

    ball.x += x_speed*2
    ball.y += y_speed *2

    if opponent.y <ball.y:
        opponent.top += 1.5
    if opponent.bottom > ball.y:
        opponent.bottom -= 1.5

    player_score_text = FONT.render(str(player_score), True, "white")
    opponent_score_text = FONT.render(str(opponent_score), True, "white")


    SCREEN.fill("Black")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.draw.rect(SCREEN, "white", player)
    pg.draw.rect(SCREEN, "white", opponent)
    pg.draw.circle(SCREEN, "white", ball.center, 10)

    SCREEN.blit(player_score_text, (WIDTH/2 +50, 50))
    SCREEN.blit(opponent_score_text, (WIDTH / 2 - 50, 50))
    if player_score == 11:
        SCREEN.blit(label, (WIDTH/2-50, HEIGHT/2))
        loop = False
    if opponent_score == 11:
        SCREEN.blit(label1, (WIDTH/2-50, HEIGHT/2))
        loop = False
    pg.display.update()
    CLOCK.tick(300)

