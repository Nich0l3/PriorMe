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
    QWidget, QButtonGroup)

from edit import *

'''            
        self.buttonBox_menu = QDialogButtonBox(self.page1)
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

        self.menuWidget.setMinimumSize(QSize(150, 100))
        self.menuWidget.setMaximumSize(QSize(1000000, 1000000))
        
        self.palette1 = QPalette()
        button_brush1 = QBrush(QColor(Qt.black))
        button_brush2 = QBrush(QColor(Qt.white))
#        button_brush.setStyle(Qt.SolidPattern) 
                       # color role       brush  
        self.palette1.setBrush(QPalette.Window, button_brush1)
        self.palette1.setBrush(QPalette.Highlight, button_brush2) 
        
        
        self.menuWidget.setPalette(self.palette1)
        self.menuWidget.setAutoFillBackground(True)

        self.menuLayout = QVBoxLayout(self.menuWidget)
        self.menuLayout.setObjectName("menuLayout")
#        self.menuLayout.setContentsMargins()

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

        self.page1 = QWidget()
        self.page1.setObjectName("page1")
        
        self.page1_layout = QHBoxLayout()
        self.page1_layout.setObjectName("page1_layout")
        self.page1.setLayout(self.page1_layout)

        self.label_widget = QWidget()
        self.label_layout = QVBoxLayout(self.label_widget)
        self.page1_layout.addWidget(self.label_widget)
    
        self.button_widget = QWidget()
        self.button_layout = QVBoxLayout(self.button_widget)
        self.page1_layout.addWidget(self.button_widget)
        
        self.stackedWidget.addWidget(self.page1)

################################  stack - 1 Button and label_ ends   ##################################

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