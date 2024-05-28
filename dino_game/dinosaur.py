from pygame.sprite import Sprite
from pygame.image import load
from pygame.mask import from_surface
from .constants import K_UP, K_DOWN,                                   \
                       DINO_X, DINO_Y, DINO_Y_DUCK,                    \
                       DINO_SPEED, DINO_ACCEL, SPEED_ANIMATION,        \
                       DINO_JUMP_PATH, DINO_RUN_PATHS, DINO_DUCK_PATHS


class Dinosaur(Sprite):
    X = DINO_X
    Y = DINO_Y
    Y_DUCK = DINO_Y_DUCK

    SPEED = DINO_SPEED
    ACCEL = DINO_ACCEL
    TIME  = SPEED_ANIMATION

    PATH_JUMP  = DINO_JUMP_PATH
    PATHS_RUN  = DINO_RUN_PATHS
    PATHS_DUCK = DINO_DUCK_PATHS

    def __init__(self):
        Sprite.__init__(self)

        self.load_images()
        self.load_masks ()

        self.init_sprite()
        self.init_moves ()

    def load_images(self):
        self.jump_image  = load(self.PATH_JUMP)
        self.run_images  = [load(p) for p in self.PATHS_RUN ]
        self.duck_images = [load(p) for p in self.PATHS_DUCK]

    def load_masks(self):
        self.jump_mask  = from_surface(self.jump_image)
        self.run_masks  = [from_surface(img) for img in self.run_images ]
        self.duck_masks = [from_surface(img) for img in self.duck_images]

    def init_sprite(self):
        self.idx = 0
        self.max = len(self.run_images) * self.TIME

        self.speed = self.SPEED

        self.image = self.run_images[self.idx]
        self.mask  = self.run_masks [self.idx]
        self.rect  = self.image.get_rect(topleft=(self.X, self.Y))

    def init_moves(self):
        self.dino_jump = False
        self.dino_duck = False

    def update(self, move):
        if not self.dino_jump:
            self.move(move)

        if self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        else:
            self.run()

    def move(self, move):
        if move[K_UP]:
            self.dino_duck = False
            self.dino_jump = True
        elif move[K_DOWN]:
            self.dino_duck = True
            self.dino_jump = False
        else:
            self.dino_duck = False
            self.dino_jump = False

    def jump(self):
        if not self.image is self.jump_image:
            self.image = self.jump_image
            self.mask  = self.jump_mask
            self.rect  = self.image.get_rect(topleft=self.topleft)

        self.y += 4 * self.speed
        self.speed += self.ACCEL

        if self.speed + self.SPEED > 0:
            self.speed = self.SPEED
            self.dino_jump  = False

    def run(self):
        self.update_sprite(self.run_images,
                           self.run_masks ,
                           self.Y)

    def duck(self):
        self.update_sprite(self.duck_images,
                           self.duck_masks ,
                           self.Y_DUCK)

    def update_sprite(self, images, masks, y):
        self.idx = (self.idx + 1) % self.max

        self.image = images[self.idx // self.TIME]
        self.mask  = masks [self.idx // self.TIME]

        if self.y != y:
            self.y = y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, y):
        self.rect.y = y

    @property
    def topleft(self):
        return self.rect.topleft
