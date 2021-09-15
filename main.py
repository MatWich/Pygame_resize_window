from classes.Window import Window

try:
    import pygame as pg
except ImportError:
    raise ImportError("pygame not found")

if __name__ == '__main__':
    w = Window()
    w.mainloop()


