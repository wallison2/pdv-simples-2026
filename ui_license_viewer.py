# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'license_viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_License_Viewer(object):
    def setupUi(self, License_Viewer):
        if not License_Viewer.objectName():
            License_Viewer.setObjectName(u"License_Viewer")
        License_Viewer.resize(448, 166)
        License_Viewer.setStyleSheet(u"background: rgba(0,191,255,0.6);")
        self.gridLayout = QGridLayout(License_Viewer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(License_Viewer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background: transparent;\n"
"font: 700 25pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 3)

        self.label_aviso = QLabel(self.frame)
        self.label_aviso.setObjectName(u"label_aviso")
        self.label_aviso.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.label_aviso, 1, 0, 1, 3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.txt_input_chave = QLineEdit(self.frame)
        self.txt_input_chave.setObjectName(u"txt_input_chave")

        self.gridLayout_2.addWidget(self.txt_input_chave, 2, 1, 1, 2)

        self.btn_autenticar = QPushButton(self.frame)
        self.btn_autenticar.setObjectName(u"btn_autenticar")
        self.btn_autenticar.setStyleSheet(u"\n"
"    QPushButton {\n"
"        background-color: #394568;\n"
"        border: 2px solid #394568;\n"
"        border-radius: 8px;\n"
"        font: 700 8pt \"Segoe UI\";\n"
"		color: rgb(255, 255, 255);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #44537c;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #2c3650;\n"
"    }\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.btn_autenticar, 3, 1, 1, 1)

        self.btn_continuar = QPushButton(self.frame)
        self.btn_continuar.setObjectName(u"btn_continuar")
        self.btn_continuar.setStyleSheet(u"\n"
"    QPushButton {\n"
"        background-color: #394568;\n"
"        border: 2px solid #394568;\n"
"        border-radius: 8px;\n"
"        font: 700 8pt \"Segoe UI\";\n"
"		color: rgb(255, 255, 255);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #44537c;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #2c3650;\n"
"    }\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.btn_continuar, 3, 2, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(License_Viewer)

        QMetaObject.connectSlotsByName(License_Viewer)
    # setupUi

    def retranslateUi(self, License_Viewer):
        License_Viewer.setWindowTitle(QCoreApplication.translate("License_Viewer", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("License_Viewer", u"Aviso!!!!!!", None))
        self.label_aviso.setText("")
        self.label.setText(QCoreApplication.translate("License_Viewer", u"Chave de Autentica\u00e7\u00e3o", None))
        self.btn_autenticar.setText(QCoreApplication.translate("License_Viewer", u"Autenticar Licen\u00e7a", None))
        self.btn_continuar.setText(QCoreApplication.translate("License_Viewer", u"Continuar", None))
    # retranslateUi

