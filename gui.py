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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)


        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)


        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 5, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.page)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 6, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.page)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 7, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.page)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 8, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.page)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 9, 1, 1, 1)
 
        self.stackedWidget.addWidget(self.page)

################################  stack - 1 Button and label ends   ##################################

        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        palette4 = QPalette()
        brush13 = QBrush(QColor(246, 211, 45, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush13)
        self.page_2.setPalette(palette4)
        self.stackedWidget.addWidget(self.page_2)

#################################   stack - 2   timer   #############################################

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.stackedWidget.setCurrentIndex(0)

#       self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

