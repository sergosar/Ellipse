from PyQt5 import QtCore, QtWidgets
import sys
from el import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, qApp, QAction, QGraphicsView, QGraphicsScene, \
    QGraphicsSceneMouseEvent
from PyQt5.QtCore import QSize, Qt, QRect, QRectF
from PyQt5.QtGui import QBrush, QPen,QPainter
from myScene import myScene

# Наследуемся от QMainWindow
class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #buttons
        self.ui.FLButton.clicked.connect(self.btnClicked)
        self.ui.SLButton.clicked.connect(self.btnClicked)
        self.ui.EllCenButton.clicked.connect(self.btnClicked)
        self.ui.TPointButton.clicked.connect(self.btnClicked)
        self.btnCheck = False

        self.scene = myScene()

        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.centerOn(0,0)
        self.scene.c.mouseClick.connect(self.drawItems)

     #   self.ui.graphicsView.mouse

    def initScene(self):
        self.greenBrush=QBrush(Qt.green)
        self.pen=QPen(Qt.red)



    def drawItems(self):
        rad=1.0
        p = self.scene.point
        self.scene.addRect(QRectF(p.x(),p.y(),1,1),QPen(Qt.black),QBrush(Qt.red))
        '''self.scene.addEllipse(p.x()-rad, p.y()-rad, rad*2.0, rad*2.0,
            QPen(), QBrush(Qt::SolidPattern));'''
        print(p)
        print(self.ui.FLButton.isChecked())

    def btnClicked(self):
        sender = self.sender()
        if not self.btnCheck:
            self.btnCheck = True
            sender.setChecked(sender.isChecked())

            print(sender.isChecked())


        self.ui.lineEdit.setText("ляляля")

#       ellipse= self.scene.addEllipse(20,20,200,200,QPen(Qt.black),QBrush(Qt.red))

        # Если не использовать, то часть текста исчезнет.



app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())

