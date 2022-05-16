#SETTINGS
TITLE = "Sky Bunny"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = "arial"
HS_FILE = "highscore.txt"

#player Propeties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.5
PLAYER_JUMP = 18
SPRITESHEET = "spritesheet_jumper.png"


#game properties
BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER =  2
CLOUD_LAYER = 0


#STARTING PLATFORMS
PLATFORM_LIST = [(0, HEIGHT - 60, ),
                 (WIDTH / 2 -50, HEIGHT * 3/4),
                 (125,HEIGHT-350),
                 (350,200),
                 (175,100)]

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
LIGHTBLUE = (135,206,235)
BGCOLOR = LIGHTBLUE

#PLATFORM SETTINGS
num_platforms = 5
SKINNY = 40
THICK = 100




