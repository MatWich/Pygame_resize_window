from classes.imgClasses.ImageInfo import ImageInfo
import re
try:
    import os
except ImportError:
    raise ImportError("os wasn't imported")


class ImageLoader:
    # this class allows you to add any image that is in imgs folder
    def __init__(self):
        self.regex_imgs = re.compile("imgs$")
        self.regex_git = re.compile("\.git")
        self.regex_idea = re.compile("\.idea$")
        self.regex_pycache = re.compile('__pycache__$')
        self.regex_projDir = re.compile("Resize_window$")
        self.imgFolderPath = os.getcwd()
        self.get_img_dir()
        self.images = {}

    def loadImage(self, imageName: str) -> None:
        if imageName not in list(self.images.keys()):
            img_name = os.path.splitext(imageName)[0]
            # self.images[imgName] = ImageInfo(imgName)
            self.images[img_name] = "placeholder"

    def get_img_dir(self):
        finding = True
        while finding:
            possible_dirs = [x[0] for x in os.walk(self.imgFolderPath)
                             if not self.regex_git.search(x[0])
                             or self.regex_pycache.search(x[0])]

            for paths in possible_dirs:
                if not finding:
                    break
                if self.regex_git.search(paths) or self.regex_idea.search(paths):
                    continue
                if self.regex_imgs.search(paths):
                    finding = False
                    self.imgFolderPath = paths
                    self.imgFolderPath = os.path.join(self.imgFolderPath, "imgs")

            self.imgFolderPath = os.path.abspath(os.path.join(self.imgFolderPath, os.pardir))


if __name__ == '__main__':
    imgl = ImageLoader()
    imgl.loadImage("img1.png")
    my_path = os.getcwd()

    regex = re.compile("test$")
    my_list = ["csdcjk/test", "fdsdfs", "fsbcs"]

    for element in my_list:
        if regex.search(element):
            print(element)
    print("------------")
    print(imgl.images)
    print(imgl.imgFolderPath)

    # while True:
    #     posibble_dirs = [x[0] for x in os.walk(my_path)]
    #     print(posibble_dirs)
    #     if "imgs" in posibble_dirs:
    #         my_path = os.path.join(my_path, "imgs")



