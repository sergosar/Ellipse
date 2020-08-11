from PyQt5 import QtCore, QtWidgets
import sys
from el import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, qApp, QAction, QGraphicsView, QGraphicsScene, \
    QGraphicsSceneMouseEvent, QGraphicsLineItem
from PyQt5.QtCore import QSize, Qt, QRect, QRectF, QLineF
from PyQt5.QtGui import QBrush, QPen,QPainter
from myScene import MyScene

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
        self.ui.graphicsView.centerOn(0,0)
        self.scene.c.mouseClick.connect(self.drawItems)

     #   self.ui.graphicsView.mouse

    def initScene(self):
        self.greenBrush=QBrush(Qt.green)
        self.pen=QPen(Qt.red)



    def drawItems(self):
 #       rad=1.0
 #        for btn in self.btnList:
 #            if btn.
        self.switchBtn(self.currentBtn)


        p = self.scene.point

  #      self.scene.addRect(QRectF(p.x(),p.y(),1,1),QPen(Qt.black),QBrush(Qt.red))
        '''self.scene.addEllipse(p.x()-rad, p.y()-rad, rad*2.0, rad*2.0,
            QPen(), QBrush(Qt::SolidPattern));'''

        print(p)
        # print(self.ui.FLButton.isChecked())

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
    def btnActions(self,btn):
        if btn == self.ui.FLButton:
            self.removesItems(self.scene.groupLine1)
        elif btn == self.ui.SLButton:
            self.removesItems(self.scene.groupLine2)
        elif btn == self.ui.TPointButton:
            self.removesItems(self.scene.groupTangentPoint)
        elif btn == self.ui.EllCenButton:
            self.removesItems(self.scene.groupEllipse)
        else:
            pass

    # foreach(QGraphicsItem * item, _scene->items(group->boundingRect() ) ) {
    # if (item->group() == group ) {
    #     delete
    # item;
    # }
    # }
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
        if len(self.scene.line1)==0:
            self.scene.line1.append(self.scene.point)
        else:
            self.scene.line1.append(self.scene.point)
            line=self.scene.line1
            lineItem = QGraphicsLineItem(QLineF(line[0], line[1]))
            lineItem.setPen(QPen(Qt.red, 3))

            self.scene.groupLine1.addToGroup(lineItem)
     #       self.scene.groupLine1.show()

    def slButtonAction(self):
        print(2)

    def tPointButtonAction(self):
        print(3)

    def ellCenButtonAction(self):
        print(4)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())

