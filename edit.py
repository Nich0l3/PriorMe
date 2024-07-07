# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QHBoxLayout,
    QLineEdit, QSizePolicy, QSpacerItem, QTimeEdit,
    QVBoxLayout, QWidget, QMainWindow)

class Ui_ediPanel(object):
    def setupUiEdit(self, editPanel):
        if not editPanel.objectName():
            editPanel.setObjectName(u"editPanel")
        editPanel.resize(495, 244)
        
        self.vertical_widget = QWidget(editPanel)
        self.verticalLayout = QVBoxLayout(self.vertical_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.horizontal_widget = QWidget()
        self.horizontalLayout = QHBoxLayout(self.horizontal_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.timeEdit = QTimeEdit()
        self.timeEdit.setObjectName(u"timeEdit")
#        self.timeEdit.setMinimumSize(QSize(150, 0))
        self.timeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.timeEdit)

        self.lineEdit = QLineEdit(editPanel)
        self.lineEdit.setObjectName(u"lineEdit")
#        self.lineEdit.setMinimumSize(QSize(200, 0))
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.verticalLayout.addWidget(self.horizontal_widget)

        self.buttonBox = QDialogButtonBox(editPanel)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)

        #self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        #self.verticalLayout.addItem(self.verticalSpacer)

        #self.retranslateUiEdit(editPanel)
        QMetaObject.connectSlotsByName(editPanel)

class MainWindow(QMainWindow, Ui_ediPanel):
    def __init__(self):
        super().__init__()
        self.setupUiEdit(self)
        #self.retranslateUiEdit()

    def retranslateUiEdit(self):
        self.setWindowTitle("editPanel")
        self.lineEdit.setText("")


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()

