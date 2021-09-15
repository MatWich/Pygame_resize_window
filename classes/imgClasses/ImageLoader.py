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
        self.regex_git = re.compile("\.git$")
        self.regex_idea = re.compile("\.idea$")
        self.regex_projDir = re.compile("Resize_window$")
        self.imgFolderPath = os.getcwd()
        self.getImgDir()
        self.images = {}

    def loadImage(self, imageName: str) -> None:
        if imageName not in list(self.images.keys()):
            imgName = imageName[:-4]
            # self.images[imgName] = ImageInfo(imgName)
            self.images[imgName] = "placeholder"

    def getImgDir(self):
        finding = True
        excluded = [".idea", "__pycache__", ".git"]
        while finding:
            posibble_dirs = [x[0] for x in os.walk(self.imgFolderPath) if x not in excluded]
            for paths in posibble_dirs:
                if not finding:
                    break
                if re.search(self.regex_git, paths) or re.match(self.regex_idea, paths):
                    continue
                if re.search(self.regex_imgs, paths):
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

    print(imgl.imgFolderPath)

    # while True:
    #     posibble_dirs = [x[0] for x in os.walk(my_path)]
    #     print(posibble_dirs)
    #     if "imgs" in posibble_dirs:
    #         my_path = os.path.join(my_path, "imgs")



