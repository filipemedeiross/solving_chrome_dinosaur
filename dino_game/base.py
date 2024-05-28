from pygame.image import load
from .constants import BASE_PATH, SPEED_GAME


class Base:
    PATH  = BASE_PATH
    SPEED = SPEED_GAME

    def __init__(self, y):
        self.x = 0
        self.y = y

        self.image  = load(self.PATH)
        self.width  = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.x -= self.SPEED

        if self.x + self.width < 0:
            self.x += self.width

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        surface.blit(self.image, (self.x + self.width, self.y))
