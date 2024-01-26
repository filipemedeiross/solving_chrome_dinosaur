from pygame.image import load
from .constants import SPEED_ANIMATION, BASE_PATH


class Base:
    SPEED = SPEED_ANIMATION
    PATH  = BASE_PATH

    def __init__(self, y):
        self.image = load(self.PATH)

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.y = y
        self.x0 = 0
        self.x1 = self.width

    def move(self):
        self.x0 -= self.SPEED
        self.x1 -= self.SPEED

        if self.x0 + self.width < 0:
            self.x0 = self.x1 + self.width
        elif self.x1 + self.width < 0:
            self.x1 = self.x0 + self.width

    def draw(self, screen):
        screen.blit(self.image, (self.x0, self.y))
        screen.blit(self.image, (self.x1, self.y))
