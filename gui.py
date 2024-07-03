# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

from edit import *

'''            
        self.buttonBox_menu = QDialogButtonBox(self.page)
        self.buttonBox_menu.setObjectName(u"buttonBox")
        self.buttonBox_menu.setGeometry(QRect(290, 20, 81, 241))
        self.buttonBox_menu.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox_menu.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)


'''
class Ui_MainWindow(object):
    def setupUiGui(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
       
        MainWindow.resize(400, 300)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

##########################################  centralwidget def ends ###########################        
        
        self.menuWidget = QWidget(self.centralwidget) # parent object
        self.menuWidget.setObjectName("menu")

        self.menuWidget.setMinimumSize(QSize(150, 20))
        self.menuWidget.setMaximumSize(QSize(1000000, 1000000))
        
        palette1 = QPalette()
        button_brush1 = QBrush(QColor(Qt.black))
        button_brush2 = QBrush(QColor(Qt.white))
#        button_brush.setStyle(Qt.SolidPattern) 
                       # color role       brush  
        palette1.setBrush(QPalette.Window, button_brush1)
        palette1.setBrush(QPalette.Highlight, button_brush2) 
        self.menuWidget.setPalette(palette1)
        self.menuWidget.setAutoFillBackground(True)

        self.menuLayout = QVBoxLayout(self.menuWidget)
        self.menuLayout.setObjectName("menuLayout")

        self.option1 = QPushButton(self.menuWidget)
        self.option1.setObjectName('option1')

        self.menuLayout.addWidget(self.option1)
        self.menuWidget.setLayout(self.menuLayout)

        self.horizontalLayout.addWidget(self.menuWidget)
###############################   menu option ends  #################################################

        self.stackedWidget = QStackedWidget(self.centralwidget)     
        self.stackedWidget.setObjectName(u"stackedWidget")


        self.page0 = QWidget()
        self.page0.setObjectName("page0")
        self.stackedWidget.addWidget(self.page0)

################################    stack 0 - empty ends       ######################################

        self.page = QWidget()
        self.page.setObjectName(u"page")
        palette2 = QPalette()
        brush10 = QBrush(QColor(192, 97, 203, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        self.page.setPalette(palette2)
        
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")

        self.label0 = QLabel(self.page)
        self.label0.setObjectName(u"label_0")
        self.label0.setScaledContents(False)
        self.label0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label0, 0, 0, 1, 1)

        self.label1 = QLabel(self.page)
        self.label1.setObjectName(u"label_1")
        self.label1.setScaledContents(False)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label1, 1, 0, 1, 1)

        self.label2 = QLabel(self.page)
        self.label2.setObjectName(u"label_2")
        self.label2.setScaledContents(False)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label2, 2, 0, 1, 1)

        self.label3 = QLabel(self.page)
        self.label3.setObjectName(u"label_3")
        self.label3.setScaledContents(False)
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label3, 3, 0, 1, 1)

        self.label4 = QLabel(self.page)
        self.label4.setObjectName(u"label_4")
        self.label4.setScaledContents(False)
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label4, 4, 0, 1, 1)

        self.label5 = QLabel(self.page)
        self.label5.setObjectName(u"label_5")
        self.label5.setScaledContents(False)
        self.label5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label5, 5, 0, 1, 1)

        self.label6 = QLabel(self.page)
        self.label6.setObjectName(u"label_6")
        self.label6.setScaledContents(False)
        self.label6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label6, 6, 0, 1, 1)

        self.label7 = QLabel(self.page)
        self.label7.setObjectName(u"label_7")
        self.label7.setScaledContents(False)
        self.label7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label7, 7, 0, 1, 1)


        self.label8 = QLabel(self.page)
        self.label8.setObjectName(u"label_8")
        self.label8.setScaledContents(False)
        self.label8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label8, 8, 0, 1, 1)

        self.label9 = QLabel(self.page)
        self.label9.setObjectName(u"label_9")
        self.label9.setScaledContents(False)
        self.label9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label9, 9, 0, 1, 1)

        self.pushButton0 = QPushButton(self.page)
        self.pushButton0.setObjectName(u"pushButton_0")
        self.gridLayout.addWidget(self.pushButton0, 0, 1, 1, 1)

        self.pushButton1 = QPushButton(self.page)
        self.pushButton1.setObjectName(u"pushButton_1")
        self.gridLayout.addWidget(self.pushButton1, 1, 1, 1, 1)

        self.pushButton2 = QPushButton(self.page)
        self.pushButton2.setObjectName(u"pushButton_2")
        self.gridLayout.addWidget(self.pushButton2, 2, 1, 1, 1)

        self.pushButton3 = QPushButton(self.page)
        self.pushButton3.setObjectName(u"pushButton_3")
        self.gridLayout.addWidget(self.pushButton3, 3, 1, 1, 1)

        self.pushButton4 = QPushButton(self.page)
        self.pushButton4.setObjectName(u"pushButton_4")
        self.gridLayout.addWidget(self.pushButton4, 4, 1, 1, 1)

        self.pushButton5 = QPushButton(self.page)
        self.pushButton5.setObjectName(u"pushButton_5")
        self.gridLayout.addWidget(self.pushButton5, 5, 1, 1, 1)

        self.pushButton6 = QPushButton(self.page)
        self.pushButton6.setObjectName(u"pushButton_6")
        self.gridLayout.addWidget(self.pushButton6, 6, 1, 1, 1)

        self.pushButton7 = QPushButton(self.page)
        self.pushButton7.setObjectName(u"pushButton_7")
        self.gridLayout.addWidget(self.pushButton7, 7, 1, 1, 1)

        self.pushButton8 = QPushButton(self.page)
        self.pushButton8.setObjectName(u"pushButtun_8")
        self.gridLayout.addWidget(self.pushButton8, 8, 1, 1, 1)

        self.pushButton9 = QPushButton(self.page)
        self.pushButton9.setObjectName(u"pushButton_9")
        self.gridLayout.addWidget(self.pushButton9, 9, 1, 1, 1)

        self.stackedWidget.addWidget(self.page)

################################  stack - 1 Button and label ends   ##################################

        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        palette4 = QPalette()
        brush13= QBrush(QColor(246, 211, 45, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush13)
        self.page_2.setPalette(palette4)
        self.stackedWidget.addWidget(self.page_2)

#################################   stack - 2   timer   #############################################

        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
