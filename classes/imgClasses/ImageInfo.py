try:
    import pygame as pg
except ImportError:
    raise ImportError("pygame not found")

class ImageInfo:
    name: str
    path:str
    image = None

    def __init__(self, name: str="", path: str=""):
        self.name = name
        self.path = name

    def adjust_image(self, size):
        self.image = pg.transform.scale(self.image, (size, size))