from random import randint
from pygame.image import load
from .obstacle import SingleObstacle, MultiObstacle
from .constants import SMALL_CACTUS_Y, SMALL_CACTUS_PATHS, \
                       LARGE_CACTUS_Y, LARGE_CACTUS_PATHS, \
                       BIRD_Y, BIRD_PATHS


class SmallCactus(SingleObstacle):
    def __init__(self):
        super().__init__(load(SMALL_CACTUS_PATHS[randint(0, 1)]),
                         SMALL_CACTUS_Y)


class LargeCactus(SingleObstacle):
    def __init__(self):
        super().__init__(load(LARGE_CACTUS_PATHS[randint(0, 1)]),
                         LARGE_CACTUS_Y)


class Bird(MultiObstacle):
    def __init__(self):
        super().__init__([load(path) for path in BIRD_PATHS],
                         BIRD_Y)
