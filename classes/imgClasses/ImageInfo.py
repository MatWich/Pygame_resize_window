try:
    import pygame as pg
except ImportError:
    raise ImportError("pygame not found")


class ImageInfo:
    """All important stuff about Images"""
    name: str
    path: str
    size_w: int
    image = None

    def __init__(self, name: str="", path: str="", size: int = 32):
        self.name = name
        self.path = path
        self.size_w = size
        self.size_h = size
        self.load_img()

    def adjust_image(self) -> None:
        self.image = pg.transform.scale(self.image, (self.size_w, self.size_h))

    def load_img(self) -> None:
        """loads img from given path"""
        self.image = pg.image.load(self.path)
        self.adjust_image()

    def set_size(self, size_w: int, size_h: int):
        self.size_w = size_w
        self.size_h = size_h