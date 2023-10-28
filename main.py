from app_window import *
from PIL import Image
from PIL import ImageFilter


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


window.show()
app.exec_()
