from app_window import *
from PIL import Image
from PIL import ImageFilter
from PyQt5.QtGui import QPixmap
import os


class ImageEditor:
    def __init__(self):
        self.directory = None
        self.filename = None
        self.original = None
        self.path = None
        self.edited_dir = "Modified"

    def open(self, directory, filename):
        self.filename = filename
        self.directory = directory
        self.path = os.path.join(self.directory, self.filename)

        try:
            self.original = Image.open(self.path)
        except:
            QMessageBox.warning(window, "Помилка", "Файл не знайдено!")


    def ShowImg(self):
        print('3', self.path)
        pixmapimg = QPixmap(self.path)
        width, height = img_holder.width(), img_holder.height()
        pixmapimg = pixmapimg.scaled(width, height, Qt.KeepAspectRatio)
        img_holder.setPixmap(pixmapimg)

    def SaveImage(self):
        path = os.path.join(workdir, self.edited_dir)
        if not os.path.exists(path) or os.path.isdir(path):
            os.makedirs(path, exist_ok=True)
        fullname = os.path.join(path, self.filename)

        self.path = fullname
        self.original.save(fullname)

    def rotateLeft(self):
        self.original = self.original.transpose(Image.ROTATE_90)
        self.SaveImage()
        image_path = os.path.join(workdir, self.edited_dir, self.filename)
        self.ShowImg()


workdir = ''


def filter_files(name):
    exceptions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
    for exc in exceptions:
        if exc in name:
            return True
        else:
            return False


def FillPhotoList():

    files = filter(filter_files, os.listdir(workdir))
    img_list.clear()
    for file in files:
        img_list.addItem(file)


def choseDirectory():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    img_holder.setText(workdir)
    FillPhotoList()


def show_chosen_picture():
    img_name = img_list.currentItem().text()
    image.open(workdir, img_name)
    image.ShowImg()


image = ImageEditor()

folder_btn.clicked.connect(choseDirectory)
img_list.itemClicked.connect(show_chosen_picture)
rotate_left_btn.clicked.connect(image.rotateLeft)

window.show()
app.exec_()
