#Quinten White
#Tile Map Game

#imports
import pygame as pg
import sys
from settings import *
from sprites import *
from os import path
game_loop = True
pg.init()


font_name = pg.font.match_font("Comic Sans MS")
screen = pg.display.set_mode((WIDTH,HEIGHT))
score = 0
class Game:
    def __init__(self,game_loop):
        pg.init()
        self.loop = game_loop
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.score = 0
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        pg.mouse.set_visible(0)


    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.player_group = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.food_group = pg.sprite.Group()
        # mouse_x = WIDTH/2
        # mouse_y = HEIGHT/2
        # pg.mouse.set_pos((mouse_x,mouse_y))

        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self,col,row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'F':
                    self.food = Food(self)

    def run(self):

        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()

            self.update()
            self.draw()
            score = 0

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()


    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):

        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

        hits = pg.sprite.groupcollide(self.player_group, self.walls,True, False)
        if hits:
            self.playing = False
            self.loop = False

        hit = pg.sprite.spritecollide(self.player,self.food_group, True)
        if hit:
            self.score += 1
            self.food = Food(self)
        hits = pg.sprite.groupcollide(self.food_group, self.walls, True, False)
        if hits:
            self.food = Food(self)



    def show_start_screen(self):
        pass

    def show_go_screen(self):
        print("in game o screen")
        return False
def draw_text(surf,text, size, x,y, color):
    font = pg.font.Font(font_name,size)
    text_surf = font.render(text,True,color)
    text_rect = text_surf.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surf,text_rect)

# create the game object

g = Game(game_loop)
g.show_start_screen()

while game_loop:
    g.new()
    g.run()
    game_loop = g.show_go_screen()
draw_text(screen,str(score), 25, WIDTH/2, 25, WHITE)


pg.quit()