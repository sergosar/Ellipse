from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsItemGroup
from PyQt5.QtCore import Qt, QPointF, pyqtSignal, QObject, QPoint


class Communicate(QObject):
    mouseClick = pyqtSignal()


class MyScene(QtWidgets.QGraphicsScene):

    def __init__(self):
        super().__init__()
        self.point = QPointF()
        self.c = Communicate()

        self.groupLine1 = QGraphicsItemGroup()
        self.groupLine2 = QGraphicsItemGroup()
        self.groupTangentPoint = QGraphicsItemGroup()
        self.groupEllipse = QGraphicsItemGroup()
        self.groupGrid = QGraphicsItemGroup()

        self.addItem(self.groupLine1)
        self.addItem(self.groupLine2)
        self.addItem(self.groupTangentPoint)
        self.addItem(self.groupEllipse)
        self.addItem(self.groupGrid)

        self.line1 = []
        self.line2 = []
        self.tangentPoint = None
        self.ellipseCenterP = None
        self.grid = False

    def mousePressEvent(self, event):
        self.point = event.scenePos()
        self.c.mouseClick.emit()
     #   print(self.point)


