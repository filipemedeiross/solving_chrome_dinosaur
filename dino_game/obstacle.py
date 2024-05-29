from pygame.sprite import Sprite
from pygame.mask import from_surface
from .constants import WDTH, SPEED_GAME, \
                       SPEED_ANIMATION


class SingleObstacle(Sprite):
    WIDTH = WDTH
    SPEED = SPEED_GAME

    def __init__(self, image, y):
        Sprite.__init__(self)

        self.image = image
        self.mask  = from_surface(image)
        self.rect  = self.image.get_rect(topleft=(self.WIDTH, y))

    def update(self):
        self.x -= self.SPEED

        if self.right < 0:
            self.kill()

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, x):
        self.rect.x = x

    @property
    def right(self):
        return self.rect.right


class MultiObstacle(Sprite):
    WIDTH = WDTH
    SPEED = SPEED_GAME
    TIME  = SPEED_ANIMATION

    def __init__(self, images, y):
        Sprite.__init__(self)

        self.init_sprites(images, y)

    def update(self):
        self.update_index()
        self.update_sprite(self.idx // self.TIME, self.topleft)

        self.x -= self.SPEED

        if self.right < 0:
            self.kill()

    def init_sprites(self, images, y):
        self.images = images
        self.masks  = [from_surface(image)
                       for image in self.images]

        self.idx = 0
        self.max = len(self.images) * self.TIME

        self.update_sprite(self.idx, (self.WIDTH, y))

    def update_index(self):
        self.idx = (self.idx + 1) % self.max

    def update_sprite(self, idx, topleft):
        self.image = self.images[idx]
        self.mask  = self.masks [idx]
        self.rect  = self.image.get_rect(topleft=topleft)

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, x):
        self.rect.x = x

    @property
    def right(self):
        return self.rect.right

    @property
    def topleft(self):
        return self.rect.topleft
