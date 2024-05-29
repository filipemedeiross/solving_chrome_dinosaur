from pygame.locals import *


# Settings

DELAY           = 2000
FRAMERATE       =   30
SPEED_GAME      =   20
SPEED_ANIMATION =    5

WHITE = 255, 255, 255
BLACK =   0,   0,   0

FONT_TYPE = 'freesansbold.ttf'
FONT_SIZE = 30

TREE_PATH = 'dino_game/models/dtc.pkl'
SVM_PATH  = 'dino_game/models/svm_linear.pkl'

# Dimensions and indent

WDTH = 1100
HGHT =  600
SIZE = WDTH, HGHT

TEXT_INDENT = WDTH // 2, HGHT // 3
MAIN_INDENT = WDTH // 2, HGHT // 3 + 50
PLAY_INDENT =      1000,             40

# Constants of the game's classes

DINO_X = 80
DINO_Y = 310
DINO_Y_DUCK =  340
DINO_SPEED  = -8.5
DINO_ACCEL  =  0.8
DINO_JUMP_PATH  = 'dino_game/media/dino_jump.png'
DINO_RUN_PATHS  = 'dino_game/media/dino_run1.png', \
                  'dino_game/media/dino_run2.png'
DINO_DUCK_PATHS = 'dino_game/media/dino_duck1.png', \
                  'dino_game/media/dino_duck2.png'

CLOUD_MIN_X =  800
CLOUD_MAX_X = 1000
CLOUD_MIN_Y =   50
CLOUD_MAX_Y =  100
CLOUD_SPEED =   15
CLOUD_PATH = 'dino_game/media/cloud.png'

SMALL_CACTUS_Y = 325
SMALL_CACTUS_PATHS = 'dino_game/media/small_cactus1.png', \
                     'dino_game/media/small_cactus2.png'

LARGE_CACTUS_Y = 300
LARGE_CACTUS_PATHS = 'dino_game/media/large_cactus1.png', \
                     'dino_game/media/large_cactus2.png'

BIRD_Y = 250
BIRD_PATHS = 'dino_game/media/bird1.png', \
             'dino_game/media/bird2.png'

BASE_Y = 380
BASE_PATH = 'dino_game/media/track.png'

GAME_THEME_PATH = 'dino_game/media/sweet_dinosaur.mp3'
GAME_EFFCT_PATH = 'dino_game/media/game_over.ogg'
