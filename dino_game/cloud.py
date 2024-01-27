from random import randint
from pygame.image import load
from pygame.mask  import from_surface
from .constants import SCREEN_WDTH, CLOUD_SPEED, \
                       CLOUD_MIN_X, CLOUD_MAX_X, \
                       CLOUD_MIN_Y, CLOUD_MAX_Y, \
                       CLOUD_PATH


class Cloud:
    MIN_X = CLOUD_MIN_X
    MAX_X = CLOUD_MAX_X
    MIN_Y = CLOUD_MIN_Y
    MAX_Y = CLOUD_MAX_Y
    WIDTH = SCREEN_WDTH
    SPEED = CLOUD_SPEED
    PATH_SPRITE = CLOUD_PATH

    def __init__(self):
        self.init_coords()
        self.image = load(self.PATH_SPRITE)
        self.width = self.image.get_width()

    def init_coords(self):
        self.x = randint(self.MIN_X, self.MAX_X) + self.WIDTH
        self.y = randint(self.MIN_Y, self.MAX_Y)

    def update(self):
        self.x -= self.SPEED
        if self.x < -self.width:
            self.init_coords()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
