from random import randint
from pygame.image import load
from pygame.mask  import from_surface
from .constants import SCREEN_WDTH, SPEED_GAME, \
                       CLOUD_MIN_X, CLOUD_MAX_X, \
                       CLOUD_MIN_Y, CLOUD_MAX_Y, \
                       CLOUD_PATH


class Cloud:
    WIDTH = SCREEN_WDTH
    SPEED = SPEED_GAME
    PATH_SPRITE = CLOUD_PATH

    def __init__(self):
        self.init_coords()

        self.image = load(self.PATH_SPRITE)
        self.mask  = from_surface(self.image)

        self.width = self.image.get_width()

    def init_coords(self):
        self.x = randint(CLOUD_MIN_X, CLOUD_MAX_X) + self.WIDTH
        self.y = randint(CLOUD_MIN_Y, CLOUD_MAX_Y)

    def update(self):
        self.x -= self.SPEED
        if self.x < -self.width:
            self.init_coords()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
