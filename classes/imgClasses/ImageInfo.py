try:
    import pygame as pg
except ImportError:
    raise ImportError("pygame not found")


class ImageInfo:
    name: str
    path: str
    image = None

    def __init__(self, name: str="", path: str=""):
        self.name = name
        self.path = path
        self.load_img()

    def adjust_image(self, size=64):
        self.image = pg.transform.scale(self.image, (size, size))

    def load_img(self):
        """loads img from given path"""
        self.image = pg.image.load(self.path)
        self.adjust_image()
