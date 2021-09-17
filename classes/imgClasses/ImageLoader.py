from classes.imgClasses.ImageInfo import ImageInfo
import re
try:
    import os
except ImportError:
    raise ImportError("os wasn't imported")


class ImageLoader:
    _instance = None
    # this class allows you to add any image that is in imgs folder
    # This class will be probably a singleton
    @staticmethod
    def get_instance():
        if ImageLoader._instance == None:
            ImageLoader()
        return ImageLoader._instance

    def __init__(self):
        if ImageLoader._instance != None:
            raise Exception("You cannot create second instance of this class")
        else:
            ImageLoader._instance = self

        self.regex_imgs = re.compile("imgs$")
        self.regex_git = re.compile("\.git")
        self.regex_idea = re.compile("\.idea$")
        self.regex_pycache = re.compile('__pycache__$')
        self.regex_projDir = re.compile("Resize_window$")
        self.imgFolderPath = os.getcwd()
        self.get_img_dir()
        self.images = {}

    def load_image(self, imageName: str) -> None:
        if imageName not in list(self.images.keys()):
            img_name = os.path.splitext(imageName)[0]
            path_to_img = os.path.join(self.imgFolderPath, imageName)
            self.images[img_name] = ImageInfo(img_name, path_to_img)

    def get_img_dir(self):
        """ Method that fire only one to find a correct dir """
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
    imgl = ImageLoader.get_instance()
    imgl.load_image("img1.png")
    print(f" Image Loader Images name: {imgl.images['img1'].name}")
    print(f" Image Loader Images path: {imgl.images['img1'].path}")
    print(f" Image Loader Images image: {imgl.images['img1'].image}")
    print(imgl.imgFolderPath)




