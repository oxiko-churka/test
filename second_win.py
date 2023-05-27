from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit



class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.name = QLabel(txt_name)
        self.hintname = QLineEdit(txt_hintname)

        self.age = QLabel(txt_age)
        self.hintage = QLineEdit(txt_hintage)

        self.test1 = QLabel(txt_test1)
        self.starttest1 = QPushButton(txt_starttest1)
        self.hinttest1 = QLineEdit(txt_hinttest1)

        self.test2 = QLabel(txt_test2)
        self.timer = QLabel(txt_timer)
        self.starttest2 = QPushButton(txt_starttest2)

        self.test3 = QLabel(txt_test3)
        self.starttest3 = QPushButton()
        self.h_line = QHBoxLayout()
        self.v_line = QVBoxLayout()
        self.v2_line = QVBoxLayout()
        self.v_line.addWidget(txt_name, alignment = Qt.AlignLeft)
        self.v_line.addWidget(txt_hintname, alignment = Qt.AlignLeft)
        self.v_line.addWidget(txt_age, alignment = Qt.AlignLeft)
        self.v_line.addWidget(hintage, alignment = Qt.AlignLeft)
        self.v_line.addWidget(txt_text1, alignment = Qt.AlignLeft)
        self.v_line.addWidget(txt_starttest1, alignment = Qt.AlignLeft)
        self.v_line.addWidget(txt_hinttest1, alignment = Qt.AlignLeft)
        self.v_line.addWidget(txt_test2, alignment = Qt.AlignLeft)
        self.v2_line.addWidget(txt_timer, alignment = Qt.AlignRight)
        self.v_line.addWidget(txt_starttest2, alignment = Qt.AlignLeft)
        self.v_line.addWidget(txt_test3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(txt_starttest, alignment = Qt.AlignLeft)
        self.v_line.addWidget(txt_hinttest1,alignment = Qt.AlignLeft)
        self.v_line.addWidget(txt_hinttese2, alignment = Qt.AlignLeft)
        self.v_line.addWidget(txt_hinttest3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(txt_sendresults, alignment = Qt.AlignCenter)

    def connects():
        pass
    def show():
        pass