from classes.imgClasses.ImageLoader import ImageLoader

try:
    import pygame as pg
except ImportError:
    raise ImportError("pygame not found")


class ImageResizer:
    """ Class that works with ImageLoader and resizes all ImageLoader.images to a proper size"""
    def __init__(self, window, imgLoader: ImageLoader, size_div: float = 7.8):
        self.window = window
        self.img_loader = imgLoader
        self.img_size_w: int = 0
        self.img_size_h: int = 0
        self.size_div = size_div

    def resize_imgs(self) -> None:
        """ Resizes all images loaded by ImageLoader"""
        self.calculate_img_size()
        for imageInfo in self.img_loader.images.values():
            imageInfo.set_size(self.img_size_w, self.img_size_h)
            imageInfo.load_img()

    def calculate_img_size(self):
        """Image size depends on screen width and height"""
        width, height = self.get_screen_size()
        self.img_size_w = int(width / self.size_div)
        self.img_size_h = int(height / self.size_div)

        print(self.img_size_w)

    def get_screen_size(self):
        """ gets the screen size"""
        return self.window.screen.get_size()
