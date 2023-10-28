from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.setWindowTitle("Easy Editor")
window.resize(800, 600)

column1 = QVBoxLayout()
column2 = QVBoxLayout()
horizontal1 = QHBoxLayout()
horizontal2 = QHBoxLayout()
horizontal3 = QHBoxLayout()

folder_btn = QPushButton("Папка")
horizontal1.addWidget(folder_btn, alignment=Qt.AlignLeft)

img_list = QListWidget()
img_holder = QWidget()

rotate_left_btn = QPushButton("Вліво")
rotate_right_btn = QPushButton("Вправо")
mirror_btn = QPushButton("Відзеркалити")
blur_btn = QPushButton("Размити")
black_btn = QPushButton("Ч\Б")

horizontal3.addWidget(rotate_left_btn)
horizontal3.addWidget(rotate_right_btn)
horizontal3.addWidget(mirror_btn)
horizontal3.addWidget(blur_btn)
horizontal3.addWidget(black_btn)

column1.addLayout(horizontal1)
column1.addWidget(img_list)
column2.addWidget(img_holder)
column2.addLayout(horizontal3)

horizontal2.addLayout(column1, stretch=1)
horizontal2.addLayout(column2, stretch=2)
window.setLayout(horizontal2)