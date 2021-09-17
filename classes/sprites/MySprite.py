import pygame.sprite

from classes.imgClasses.ImageLoader import ImageLoader

try:
    import pygame as pg
except ImportError:
    raise ImportError("pygame not found")


class MySprite(pg.sprite.Sprite):
    """ Basic Sprite class adjusted to use ImageLoader """
    def __init__(self, window, x: int, y: int):
        self.groups = window.all_sprites
        self.imgl = ImageLoader.get_instance()
        pg.sprite.Sprite.__init__(self, self.groups)
        self.window = window
        self.image = self.imgl.images["img1"].image
        # self.image.fill((255, 0, 0))
        self.x = x
        self.y = y

    def update(self):
        self.image = self.imgl.images["img1"].image



