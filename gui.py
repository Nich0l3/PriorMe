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
        self.buttonBox_menu = QDialogButtonBox(self.page1)
        self.buttonBox_menu.setObjectName(u"buttonBox")
        self.buttonBox_menu.setGeometry(QRect(290, 20, 81, 241))
        self.buttonBox_menu.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox_menu.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
'''

'''
        self.label_0 = QLabel(self.page1)
        self.label_0.setObjectName("label_0")
        self.label_0.setScaledContents(False)
        self.label_0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page1_layout.addWidget(self.label_0, 0, 0, 1, 1)

        self.label_1 = QLabel(self.page1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setScaledContents(False)
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page1_layout.addWidget(self.label_1, 1, 0, 1, 1)

        self.label_2 = QLabel(self.page1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page1_layout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.page1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page1_layout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_4 = QLabel(self.page1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page1_layout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_5 = QLabel(self.page1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page1_layout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_6 = QLabel(self.page1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page1_layout.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_7 = QLabel(self.page1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page1_layout.addWidget(self.label_7, 7, 0, 1, 1)


        self.label_8 = QLabel(self.page1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page1_layout.addWidget(self.label_8, 8, 0, 1, 1)

        self.label_9 = QLabel(self.page1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page1_layout.addWidget(self.label_9, 9, 0, 1, 1)

        ########### label ends

        self.push_button_0 = QPushButton(self.page1)
        self.push_button_0.setObjectName(u"push_button_0")
        self.page1_layout.addWidget(self.push_button_0, 0, 1, 1, 1)

        self.push_button_1 = QPushButton(self.page1)
        self.push_button_1.setObjectName(u"push_button_1")
        self.page1_layout.addWidget(self.push_button_1, 1, 1, 1, 1)

        self.push_button_2 = QPushButton(self.page1)
        self.push_button_2.setObjectName(u"push_button_2")
        self.page1_layout.addWidget(self.push_button_2, 2, 1, 1, 1)

        self.push_button_3 = QPushButton(self.page1)
        self.push_button_3.setObjectName(u"push_button_3")
        self.page1_layout.addWidget(self.push_button_3, 3, 1, 1, 1)

        self.push_button_4 = QPushButton(self.page1)
        self.push_button_4.setObjectName(u"push_button_4")
        self.page1_layout.addWidget(self.push_button_4, 4, 1, 1, 1)

        self.push_button_5 = QPushButton(self.page1)
        self.push_button_5.setObjectName(u"push_button_5")
        self.page1_layout.addWidget(self.push_button_5, 5, 1, 1, 1)

        self.push_button_6 = QPushButton(self.page1)
        self.push_button_6.setObjectName(u"push_button_6")
        self.page1_layout.addWidget(self.push_button_6, 6, 1, 1, 1)

        self.push_button_7 = QPushButton(self.page1)
        self.push_button_7.setObjectName(u"push_button_7")
        self.page1_layout.addWidget(self.push_button_7, 7, 1, 1, 1)

        self.push_button_8 = QPushButton(self.page1)
        self.push_button_8.setObjectName(u"pushButtun_8")
        self.page1_layout.addWidget(self.push_button_8, 8, 1, 1, 1)

        self.push_button_9 = QPushButton(self.page1)
        self.push_button_9.setObjectName(u"push_button_9")
        self.page1_layout.addWidget(self.push_button_9, 9, 1, 1, 1)

'''


class Label(QLabel):
        def __init__(self,parent=None,text='label'):
                super().__init__(parent)
                self.setObjectName("label_0")
                self.setScaledContents(False)
                self.setAlignment(Qt.AlignCenter)


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
        label = QLabel("world")
        self.button_layout.addWidget(label)
        label = QLabel("hell241o")
        self.button_layout.addWidget(label)
        label = QLabel("hel341lo")
        self.button_layout.addWidget(label)
        label = QLabel("hell1432o")
        self.button_layout.addWidget(label)
        label = QLabel("hell12312")
        self.button_layout.addWidget(label)
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