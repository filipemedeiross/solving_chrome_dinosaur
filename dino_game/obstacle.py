from pygame.sprite import Sprite
from pygame.mask import from_surface
from .constants import SCREEN_WDTH, SPEED_GAME, SPEED_ANIMATION


class SingleObstacle(Sprite):
    WIDTH = SCREEN_WDTH
    SPEED = SPEED_GAME

    def __init__(self, image, y):
        Sprite.__init__(self)

        self.image = image
        self.mask  = from_surface(self.image)
        self.rect  = self.image.get_rect(topleft=(self.WIDTH, y))

    def update(self):
        self.rect.x -= self.SPEED
        if self.rect.x < -self.rect.width:
            self.kill()


class MultiObstacle(Sprite):
    WIDTH = SCREEN_WDTH
    SPEED = SPEED_GAME
    TIME_ANIMATION = SPEED_ANIMATION

    def __init__(self, images, y):
        Sprite.__init__(self)

        self.imgs = images
        self.msks = [from_surface(img) for img in self.imgs]

        self.idx = 0
        self.max_idx = len(self.imgs) * self.TIME_ANIMATION

        self.image = self.imgs[self.idx]
        self.mask  = self.msks[self.idx]
        self.rect  = self.image.get_rect(topleft=(self.WIDTH, y))

    def update(self):
        self.idx = (self.idx + 1) % self.max_idx
        self.image = self.imgs[self.idx // self.TIME_ANIMATION]
        self.mask  = self.msks[self.idx // self.TIME_ANIMATION]

        self.rect.x -= self.SPEED
        if self.rect.x < -self.rect.width:
            self.kill()
