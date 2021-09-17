import pygame

from classes.imgClasses.ImageLoader import ImageLoader
from classes.sprites.MySprite import MySprite

try:
    import pygame as pg
except ImportError:
    raise ImportError("pygame not found")


class Window:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((500, 500))
        pg.display.set_caption("Window")
        self.clock = pg.time.Clock()
        self.run = True
        self.imgl = ImageLoader.get_instance()
        self.set_up()

    def set_up(self):
        self.all_sprites = pg.sprite.Group()
        self.imgl.load_image("img1.png")
        self.player = MySprite(self, 0, 0)


    def mainloop(self):
        while self.run:
            self.dt = self.clock.tick(60) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((122, 0, 122))
        self.screen.blit(self.player.image, (0, 0))
        pg.display.update()

    def quit(self):
        self.run = False
        pg.quit()

