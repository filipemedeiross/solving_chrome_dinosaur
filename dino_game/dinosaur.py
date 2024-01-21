from pygame import K_UP, K_DOWN
from pygame.sprite import Sprite
from pygame.image import load
from pygame.mask import from_surface
from .constants import DINO_X, DINO_Y, DINO_Y_DUCK, \
                       DINO_SPEED, DINO_ACCELERATION, SPEED_ANIMATION, \
                       DINO_JUMP_PATH, DINO_RUN_PATHS, DINO_DUCK_PATHS


class Dinosaur(Sprite):
    X = DINO_X
    Y = DINO_Y
    Y_DUCK = DINO_Y_DUCK
    
    SPEED  = DINO_SPEED
    ACCELERATION   = DINO_ACCELERATION
    TIME_ANIMATION = SPEED_ANIMATION

    PATH_JUMP  = DINO_JUMP_PATH
    PATHS_RUN  = DINO_RUN_PATHS
    PATHS_DUCK = DINO_DUCK_PATHS

    def __init__(self):
        Sprite.__init__(self)

        self.load_images()
        self.load_masks()

        self.init_sprite()
        self.init_moves()

    def load_images(self):
        self.jump_img  = load(self.PATH_JUMP)
        self.run_imgs  = [load(path) for path in self.PATHS_RUN]
        self.duck_imgs = [load(path) for path in self.PATHS_DUCK]

    def load_masks(self):
        self.jump_msk  = from_surface(self.jump_img)
        self.run_msks  = [from_surface(img) for img in self.run_imgs]
        self.duck_msks = [from_surface(img) for img in self.duck_imgs]

    def init_sprite(self):
        self.idx = 0
        self.m_idx = len(self.run_imgs) * self.TIME_ANIMATION
        self.speed = self.SPEED

        self.image = self.run_imgs[self.idx]
        self.mask  = self.run_msks[self.idx]
        self.rect  = self.image.get_rect(topleft=(self.X, self.Y))

    def init_moves(self):
        self.dino_jump = False
        self.dino_duck = False

    def update(self, move):
        if not self.dino_jump:
            if move[K_UP]:
                self.dino_duck = False
                self.dino_jump = True
            elif move[K_DOWN]:
                self.dino_duck = True
                self.dino_jump = False
            else:
                self.dino_duck = False
                self.dino_jump = False

        if self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        else:
            self.run()

    def jump(self):
        if not self.image is self.jump_img:
            self.image = self.jump_img
            self.mask  = self.jump_msk
            self.rect  = self.image.get_rect(topleft=self.rect.topleft)

        self.rect.y += 4 * self.speed
        self.speed  += self.ACCELERATION

        if self.speed > -self.SPEED:
            self.speed = self.SPEED
            self.dino_jump = False

    def run(self):
        self.update_sprite(self.run_imgs, self.run_msks, self.Y)
    
    def duck(self):
        self.update_sprite(self.duck_imgs, self.duck_msks, self.Y_DUCK)

    def update_sprite(self, imgs, msks, new_y):
        self.idx = (self.idx + 1) % self.m_idx
        self.image = imgs[self.idx // self.TIME_ANIMATION]
        self.mask  = msks[self.idx // self.TIME_ANIMATION]
        self.rect  = self.image.get_rect(topleft=(self.rect.x, new_y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y
