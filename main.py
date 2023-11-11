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
        self.edited = []

    def open(self, directory, filename):
        self.filename = filename
        self.directory = directory
        self.path = os.path.join(self.directory, self.filename)

        try:
            self.original = Image.open(self.path)
        except:
            QMessageBox.warning(window, "Помилка", "Файл не знайдено!")


    def ShowImg(self):
        pixmapimg = QPixmap(self.path)
        width, height = img_holder.width(), img_holder.height()
        pixmapimg = pixmapimg.scaled(width, height, Qt.KeepAspectRatio)
        img_holder.setPixmap(pixmapimg)


workdir = ''


def FillPhotoList():
    files = os.listdir(workdir)
    for file in files:
        if ".png" in file or ".jpg" in file:
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

window.show()
app.exec_()
