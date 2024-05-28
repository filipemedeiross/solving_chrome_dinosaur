from .tools import load_image, load_images
from .obstacle import SingleObstacle, MultiObstacle
from .constants import SMALL_CACTUS_Y, SMALL_CACTUS_PATHS, \
                       LARGE_CACTUS_Y, LARGE_CACTUS_PATHS, \
                       BIRD_Y, BIRD_PATHS


class SmallCactus(SingleObstacle):
    def __init__(self):
        super().__init__(load_image(SMALL_CACTUS_PATHS), SMALL_CACTUS_Y)


class LargeCactus(SingleObstacle):
    def __init__(self):
        super().__init__(load_image(LARGE_CACTUS_PATHS), LARGE_CACTUS_Y)


class Bird(MultiObstacle):
    def __init__(self):
        super().__init__(load_images(BIRD_PATHS), BIRD_Y)
