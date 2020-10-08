from PyQt5 import QtCore, QtWidgets, QtGui
import sys
from el import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, qApp, QAction, QGraphicsView, QGraphicsScene, \
    QGraphicsSceneMouseEvent, QGraphicsLineItem, QGraphicsEllipseItem
from PyQt5.QtCore import QSize, Qt, QRect, QRectF, QLineF, QPointF
from PyQt5.QtGui import QBrush, QPen, QPainter
from myScene import MyScene
from ellCalc import *
from math import sqrt, atan, pi

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
        self.ui.calcButton.clicked.connect(self.ellipseCalc)
        self.ui.gridButton.clicked.connect(self.addGrid)
        self.btnCheck = False
        self.btnList = [self.ui.FLButton, self.ui.SLButton, self.ui.TPointButton, self.ui.EllCenButton]
        self.currentBtn = None


        self.scene = MyScene()

        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.centerOn(0, 0)
        self.scene.c.mouseClick.connect(self.drawItems)

        self.tanP = None

     #   self.ui.graphicsView.mouse


    def ellipseCalc(self):

        self.removesItems(self.scene.groupEllipse)
        if len(self.scene.line1) > 0 and len(self.scene.line2)>0\
                and self.tanP is not None\
                and self.scene.ellipseCenterP is not None:

            ellipse = realEllipse(self.tanP, self.scene.line1, self.scene.line2, self.scene.ellipseCenterP)

            A = ellipse['A']; B = ellipse['B']; C = ellipse['C'];
            F = ellipse['F'];
            if B**2 - 4 * A * C < 0:
                #ellipse
                a = -sqrt(2*(B**2 - 4*A*C)*F*(A + C + sqrt((A-C)**2+B**2)))/(B**2 - 4*A*C)
                b = -sqrt(2*(B**2 - 4*A*C)*F*(A + C - sqrt((A-C)**2+B**2)))/(B**2 - 4*A*C)
                # ellipse rotation angle
                if b != 0:
                    angle = atan((C-A-sqrt((A-C)**2 + B*B))/B)
                elif A < C:
                    angle = 0
                else:
                    angle = pi/2
                angleD = angle*180/pi

                cp = self.scene.ellipseCenterP
                ellipse = QGraphicsEllipseItem(-a, -b, 2*a, 2*b)
                ellipse.setPen(QPen(Qt.green))
                rotate = QtGui.QTransform().rotate(angleD)
                translate = QtGui.QTransform().translate(cp.x(), cp.y())

                ellipse.setTransform(rotate * translate)
                self.scene.groupEllipse.addToGroup(ellipse)
            else: self.ui.lineEdit.setText("ellipse extinction error")
#____________________________

       #  #TEST!
       #  line1=[]
       #  line1.append(QPointF(0.0, 60.0))
       #  line1.append(QPointF(-60.0, 0.0))
       #  lineItem = QGraphicsLineItem(QLineF(line1[0], line1[1]))
       #  lineItem.setPen(QPen(Qt.red, 3))
       #  self.scene.groupLine1.addToGroup(lineItem)
       #  #print(getLineParameters(line1))
       #
       #  line2=[]
       #  line2.append(QPointF(0.0, 60.0))
       #  line2.append(QPointF(60, 0.0))
       #  lineItem = QGraphicsLineItem(QLineF(line2[0], line2[1]))
       #  lineItem.setPen(QPen(Qt.red, 3))
       #  self.scene.groupLine2.addToGroup(lineItem)
       #  #print(getLineParameters(line2))
       #
       #  elcx = 0.0
       #  elcy = 20.0
       #  pointT = {'x': 20.0, 'y': 40.0}
       #  pointC = QPointF(elcx,elcy)
       #
       #  ellipse = realEllipse(pointT, line1, line2, pointC)
       #  print("ellipse = ")
       #  print(ellipse)
       #  A = ellipse['A'];
       #  B = ellipse['B'];
       #  C = ellipse['C'];
       #  F = ellipse['F'];
       #  a = -sqrt(2 * (B ** 2 - 4 * A * C) * F * (A + C + sqrt((A - C) ** 2 + B ** 2))) / (B ** 2 - 4 * A * C)
       #  b = -sqrt(2*(B**2 - 4*A*C)*F*(A + C - sqrt((A-C)**2+B**2)))/(B**2 - 4*A*C)
       #  if b != 0:
       #      angle = atan((C-A-sqrt((A-C)**2 + B*B))/B)
       #  elif A < C:
       #      angle = 0
       #  else:
       #      angle = pi/2
       #  angleD = angle*180/pi
       #  ellipse = QGraphicsEllipseItem(- a, - b, 2 * a, 2 * b)
       # # item = QGraphicsEllipseItem
       #  ellipse.setPen(QPen(Qt.green))
       #
       #  ellipse.setTransform(QtGui.QTransform().rotate(angleD)*QtGui.QTransform().translate(elcx, elcy))
       #  self.scene.groupEllipse.addToGroup(ellipse)
       #



       # print("Ellcalc")

    def addGrid(self):

        if self.scene.grid is False:
            self.scene.grid = True
            itemPoint = QGraphicsEllipseItem( - 5, - 5, 10, 10)
            itemPoint.setPen(QPen(Qt.red, 1))
            itemPoint.setBrush(QBrush(Qt.red))
            self.scene.groupGrid.addToGroup(itemPoint)
            for i in range(4):
                for j in range(-1,2,2):
                    for k in range(-1,2,2):
                        itemPoint = QGraphicsEllipseItem(100*i*j-3, 100*i*k-3, 6, 6)
                        self.scene.groupGrid.addToGroup(itemPoint)
        else:
            self.removesItems(self.scene.groupGrid)
            self.scene.grid=False




    # def initScene(self):
    #     self.greenBrush = QBrush(Qt.green)
    #     self.pen = QPen(Qt.red)



    def drawItems(self):
        self.switchBtn(self.currentBtn)
        p = self.scene.point
     #   print(p)


    def setBtnsDisable(self):
        for btn in self.btnList:
            btn.setDisabled(True)
        self.ui.lineEdit.setText("")

    def setBtnsEnable(self):
        for btn in self.btnList:
            btn.setEnabled(True)

    def btnClicked(self):
        self.currentBtn = self.sender()
        self.setBtnsDisable()
        self.btnActions(self.currentBtn)

      #  self.ui.lineEdit.setText("ляляля")

#       ellipse= self.scene.addEllipse(20,20,200,200,QPen(Qt.black),QBrush(Qt.red))

#Actions by Btn
    # take away in func
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
#code repeat?
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
        self.scene.tangentPoint = self.scene.point

        if len(self.scene.line1)>0 and len(self.scene.line2) > 0:
            line1 = getLineParameters(self.scene.line1)
            line2 = getLineParameters(self.scene.line2)
            point1 = self.scene.tangentPoint
            point = {'x': point1.x(), "y": point1.y()}
            if distBetweenPnL(point, line1) < distBetweenPnL(point, line2):
                line = line1
            else: line = line2

             # doesnt work properly, fix according math :fixed
            p = tangentPoint(point, line)
            self.tanP = p
            itemPoint = QGraphicsEllipseItem(p['x']-5, p['y']-5, 10, 10)
            itemPoint.setPen(QPen(Qt.black, 1))
            itemPoint.setBrush(QBrush(Qt.black))
            self.scene.groupTangentPoint.addToGroup(itemPoint)

        self.endButtonAction()


    def ellCenButtonAction(self):
        self.scene.ellipseCenterP = self.scene.point
        p = self.scene.ellipseCenterP
        itemPoint = QGraphicsEllipseItem(p.x() - 5, p.y() - 5, 10, 10)
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

