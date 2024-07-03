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
    QVBoxLayout, QWidget)

class Ui_ediPanel(object):
    def setupUiEdit(self, ediPanel):
        if not ediPanel.objectName():
            ediPanel.setObjectName(u"ediPanel")
        ediPanel.resize(495, 248)
        ediPanel.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.verticalLayout = QVBoxLayout(ediPanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.timeEdit = QTimeEdit(ediPanel)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(150, 0))
        self.timeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.timeEdit)

        self.lineEdit = QLineEdit(ediPanel)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 0))
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox_edit = QDialogButtonBox(ediPanel)
        self.buttonBox_edit.setObjectName(u"buttonBox")
        self.buttonBox_edit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.buttonBox_edit.setAutoFillBackground(False)
        self.buttonBox_edit.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox_edit.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox_edit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.retranslateUiEdit(ediPanel)

        QMetaObject.connectSlotsByName(ediPanel)


    def retranslateUi(self, ediPanel):
        ediPanel.setWindowTitle("ediPanel")
        self.lineEdit.setText("")
    

