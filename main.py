from app_window import *
from PIL import Image
from PIL import ImageFilter
import os


class ImageEditor:
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.edited = []

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            QMessageBox.warning(window, "Помилка", "Файл не знайдено!")
        self.original.show()


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


def ShowImg():
    img = ImageEditor(workdir + img_list.selectedItems()[0].text())
    print(workdir + "/" + img_list.selectedItems()[0].text())
    img.open()


folder_btn.clicked.connect(choseDirectory)
img_list.itemClicked.connect(ShowImg)

window.show()
app.exec_()
