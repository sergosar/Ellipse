from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets  import QGraphicsScene
from PyQt5.QtCore import Qt, QPointF, pyqtSignal, QObject, QPoint


class Communicate(QObject):
    mouseClick = pyqtSignal()
class myScene(QtWidgets.QGraphicsScene):

    def __init__(self):
        super().__init__()
        self.point = QPointF()
        self.c = Communicate()


        

    def mousePressEvent(self, event):
        self.point = event.scenePos()
        self.c.mouseClick.emit()
     #   print(self.point)


