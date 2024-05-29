from random import randint
from pygame.image import load
from .constants import CLOUD_PATH , CLOUD_SPEED, \
                       CLOUD_MIN_X, CLOUD_MAX_X, \
                       CLOUD_MIN_Y, CLOUD_MAX_Y, \
                       WDTH


class Cloud:
    WIDTH = WDTH
    PATH  = CLOUD_PATH
    SPEED = CLOUD_SPEED
    MIN_X = CLOUD_MIN_X
    MAX_X = CLOUD_MAX_X
    MIN_Y = CLOUD_MIN_Y
    MAX_Y = CLOUD_MAX_Y

    def __init__(self):
        self.init_coords()

        self.image = load(self.PATH)
        self.width = self.image.get_width()

    def init_coords(self):
        self.x = randint(self.MIN_X, self.MAX_X) + self.WIDTH
        self.y = randint(self.MIN_Y, self.MAX_Y)

    def update(self):
        self.x -= self.SPEED

        if self.x + self.width < 0:
            self.init_coords()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
