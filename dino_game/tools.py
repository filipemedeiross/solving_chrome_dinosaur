from random import choice
from pygame.image import load


def load_image(paths):
    return load(choice(paths))

def load_images(paths):
    return [load(path) for path in paths]
