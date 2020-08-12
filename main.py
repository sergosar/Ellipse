from PyQt5 import QtCore, QtWidgets
import sys
from el import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, qApp, QAction, QGraphicsView, QGraphicsScene, \
    QGraphicsSceneMouseEvent, QGraphicsLineItem, QGraphicsEllipseItem
from PyQt5.QtCore import QSize, Qt, QRect, QRectF, QLineF
from PyQt5.QtGui import QBrush, QPen,QPainter
from myScene import MyScene
from ellCalc import *

# Наследуемся от QMainWindow

# class DrawItems():
#     def __init__(self):
#         self.


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #buttons
        self.ui.FLButton.clicked.connect(self.btnClicked)
        self.ui.SLButton.clicked.connect(self.btnClicked)
        self.ui.EllCenButton.clicked.connect(self.btnClicked)
        self.ui.TPointButton.clicked.connect(self.btnClicked)
        self.btnCheck = False
        self.btnList = [self.ui.FLButton, self.ui.SLButton, self.ui.TPointButton, self.ui.EllCenButton]
        self.currentBtn = None

        self.scene = MyScene()

        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.centerOn(0, 0)
        self.scene.c.mouseClick.connect(self.drawItems)

     #   self.ui.graphicsView.mouse

    def initScene(self):
        self.greenBrush=QBrush(Qt.green)
        self.pen=QPen(Qt.red)



    def drawItems(self):
        self.switchBtn(self.currentBtn)
        p = self.scene.point
        print(p)


    def setBtnsDisable(self):
        for btn in self.btnList:
            btn.setDisabled(True)

    def setBtnsEnable(self):
        for btn in self.btnList:
            btn.setEnabled(True)

    def btnClicked(self):
        self.currentBtn = self.sender()
        self.setBtnsDisable()
        self.btnActions(self.currentBtn)

        self.ui.lineEdit.setText("ляляля")

#       ellipse= self.scene.addEllipse(20,20,200,200,QPen(Qt.black),QBrush(Qt.red))

#Actions by Btn
    def btnActions(self, btn):
        if btn == self.ui.FLButton:
            self.removesItems(self.scene.groupLine1)
            self.scene.line1.clear()
        elif btn == self.ui.SLButton:
            self.removesItems(self.scene.groupLine2)
            self.scene.line2.clear()
        elif btn == self.ui.TPointButton:
            self.removesItems(self.scene.groupTangentPoint)
            self.scene.tangentPoint=None
        elif btn == self.ui.EllCenButton:
            self.removesItems(self.scene.groupEllipse)
            self.scene.ellipseCenterP = None
        else:
            pass


    def removesItems(self, group):
        for item in self.scene.items():
            if item.group() == group:
                self.scene.removeItem(item)

# ActionSwitcher
    def switchBtn(self, btn):
        if btn == self.ui.FLButton:

            self.flButtonAction()
        elif btn == self.ui.SLButton:
            self.slButtonAction()
        elif btn == self.ui.TPointButton:
            self.tPointButtonAction()
        elif btn == self.ui.EllCenButton:
            self.ellCenButtonAction()
        else:
            pass

# Actions after buttons
    def flButtonAction(self):
        if len(self.scene.line1) == 0:
            self.scene.line1.append(self.scene.point)
        else:
            self.scene.line1.append(self.scene.point)
            line = self.scene.line1
            lineItem = QGraphicsLineItem(QLineF(line[0], line[1]))
            lineItem.setPen(QPen(Qt.red, 3))
            self.scene.groupLine1.addToGroup(lineItem)

            self.endButtonAction()
     #       self.scene.groupLine1.show()

    def slButtonAction(self):
        if len(self.scene.line2) == 0:
            self.scene.line2.append(self.scene.point)
        else:
            self.scene.line2.append(self.scene.point)
            line = self.scene.line2
            lineItem = QGraphicsLineItem(QLineF(line[0], line[1]))
            lineItem.setPen(QPen(Qt.red, 3))
            self.scene.groupLine2.addToGroup(lineItem)
            self.endButtonAction()

    def tPointButtonAction(self):
        self.scene.tangentPoint=self.scene.point  # doesnt work properly, fix according math
        p = self.scene.tangentPoint
        itemPoint = QGraphicsEllipseItem(p.x()-5,p.y()-5, 5, 5)
        itemPoint.setPen(QPen(Qt.black, 1))
        itemPoint.setBrush(QBrush(Qt.black))
        self.scene.groupTangentPoint.addToGroup(itemPoint)

        self.endButtonAction()


    def ellCenButtonAction(self):
        self.scene.ellipseCenterP = self.scene.point
        p = self.scene.ellipseCenterP
        itemPoint = QGraphicsEllipseItem(p.x() - 5, p.y() - 5, 5, 5)
        itemPoint.setPen(QPen(Qt.black, 1))
        itemPoint.setBrush(QBrush(Qt.black))
        self.scene.groupEllipse.addToGroup(itemPoint)

        self.endButtonAction()

    def endButtonAction(self):
        self.setBtnsEnable()
        self.currentBtn = None

app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())

