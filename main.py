import sys

import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic  
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self) # Загрузка дизайна
        self.pushButton.clicked.connect(self.paint) # вызов разрешения на рисование
        self.do_paint = False # пока не нажата, рисования не будет

    
    def paintEvent(self, event): # стандартная функция организации рисования
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self): # выдача разрешения на рисование
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp): # рисование желтого круга
        qp.setBrush(QColor(255, 255, 0))
        d = random.randint(20, 150)
        qp.drawEllipse(100 - d // 2, 100 - d // 2, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
