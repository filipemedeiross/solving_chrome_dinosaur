import pygame
from pygame.sprite import Group,           \
                          collide_mask,    \
                          spritecollideany

from pickle import load
from random import choice, \
                   randint

from .base      import Base
from .cloud     import Cloud
from .dinosaur  import Dinosaur
from .enemies   import SmallCactus, \
                       LargeCactus, \
                       Bird
from .constants import *


class DinoChrome:
    def __init__(self):
        # Initializing the pygame
        pygame.init()

        # Init the screen, clock, font and mixer
        self.screen = pygame.display.set_mode(SIZE)
        self.clock  = pygame.time.Clock()
        self.font   = pygame.font.Font(FONT_TYPE, FONT_SIZE)

        pygame.display.set_caption('Dino Chrome')

        self.music_game = pygame.mixer.Sound(GAME_THEME_PATH)
        self.music_lose = pygame.mixer.Sound(GAME_EFFCT_PATH)

        self.channel_music = pygame.mixer.Channel(0)
        self.channel_effct = pygame.mixer.Channel(1)

        # Initializing game objects
        self.score = 0
        self.agent = self.load_agent()

        self.cloud = Cloud()
        self.dino  = Dinosaur()
        self.base  = Base(BASE_Y)
        self.obstacles = Group()

    def init_game(self):
        while True:
            self.main_screen()
            self.play()

    def main_screen(self):
        self.play_theme()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit(0)
                if event.type == KEYDOWN:
                    return

            moves = self.features

            self.move_objects(moves)
            self.display_main_screen()

            self.clock.tick(FRAMERATE)

    def play(self):
        self.score = 0

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit(0)

            moves = pygame.key.get_pressed()

            self.move_objects(moves)
            self.display_play_screen()

            if self.check_lose():
                return

            self.clock.tick(FRAMERATE)

    def display_main_screen(self):
        self.screen.fill(WHITE)

        self.draw_objects()
        self.display_text()

        pygame.display.flip()

    def display_play_screen(self):
        self.screen.fill(WHITE)

        self.draw_objects()
        self.display_score()

        pygame.display.flip()

    def display_text(self):
        text = self.font.render('Press Any Key to Start', True, BLACK)
        rect = text.get_rect(center=TEXT_INDENT)

        self.screen.blit(text, rect)

        if self.score:
            score = self.font.render(f'Your Score: {self.score}', True, BLACK)
            rect  = score.get_rect(center=(MAIN_INDENT))

            self.screen.blit(score, rect)

    def display_score(self):
        self.score += 1

        text = self.font.render(f'Score: {self.score}', True, BLACK)
        rect = text.get_rect(center=PLAY_INDENT)

        self.screen.blit(text, rect)

    def update_obstacles(self):
        if not self.obstacles:
            op = randint(0, 2)

            if   op == 0:
                self.obstacles.add(SmallCactus())
            elif op == 1:
                self.obstacles.add(LargeCactus())
            elif op == 2:
                self.obstacles.add(Bird())

    def move_objects(self, moves):
        self.base.update()
        self.cloud.update()
        self.dino.update(moves)

        self.update_obstacles()

        self.obstacles.update()

    def draw_objects(self):
        self.base.draw(self.screen)
        self.cloud.draw(self.screen)
        self.obstacles.draw(self.screen)
        self.dino.draw(self.screen)

    def check_lose(self):
        if self.collide(self.dino, self.obstacles):
            self.play_lose_effect()

            return True

    def play_theme(self):
        if not self.channel_music.get_busy():
            self.channel_music.play(self.music_game, -1)

    def play_lose_effect(self):
        self.channel_music.stop()
        self.channel_effct.play(self.music_lose)

        pygame.time.delay(DELAY)

    def load_agent(self):
        path = choice([TREE_PATH, SVM_PATH])

        with open(path, 'rb') as f:
            return load(f)

    def predict(self, x, obs):
        return self.agent.predict([[x, obs]])[0]

    @property
    def features(self):
        features = {K_UP   : False,
                    K_DOWN : False}

        if self.obstacles:
            obs  = self.obstacles.sprites()[0]
            pred = self.predict(obs.x - self.dino.right,
                                self.is_cactus(obs))

            if pred == 1:
                features[K_UP  ] = True
            elif pred == 2:
                features[K_DOWN] = True

        return features

    @staticmethod
    def collide(sprite, group):
        return spritecollideany(sprite, group, collided=collide_mask)

    @staticmethod
    def is_cactus(obs):
        return 0 if isinstance(obs, Bird) else 1
