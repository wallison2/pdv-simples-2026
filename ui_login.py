# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import Resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(270, 180)
        Dialog.setMinimumSize(QSize(270, 180))
        Dialog.setMaximumSize(QSize(270, 180))
        icon = QIcon()
        icon.addFile(u":/new/img/img (66).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background: rgba(0,191,255,0.6);")
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background: rgba(0,191,255,0.6);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox_login = QComboBox(self.frame)
        self.comboBox_login.setObjectName(u"comboBox_login")
        self.comboBox_login.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.comboBox_login.setFont(font)
        self.comboBox_login.setStyleSheet(u"QComboBox {\n"
"    background-color: rgb(80, 81, 82);\n"
"    border: 2px solid #394568;\n"
"    border-radius: 10px;\n"
"    font: 700 10pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgb(75, 85, 83);\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: #2c3650;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(80, 81, 82);  /* cor de fundo da lista */\n"
"    color: rgb(255, 255, 255);          /* cor do texto das op\u00e7\u00f5es */\n"
"}\n"
"")
        self.comboBox_login.setEditable(False)

        self.horizontalLayout_4.addWidget(self.comboBox_login)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setMaximumSize(QSize(220, 25))
        self.txt_password.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 127);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"  	color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: rgb(191, 191, 191); /* Cor quando selecionado/focado */\n"
"    color: rgb(0, 0, 0); /* Mant\u00e9m a fonte preta ao focar */\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255); /* Ajuste a cor da fonte para branco para contraste */\n"
"    font: bold 8px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_password.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.txt_password.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.txt_password)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_bar = QLabel(self.frame)
        self.label_bar.setObjectName(u"label_bar")
        self.label_bar.setMinimumSize(QSize(0, 20))
        self.label_bar.setMaximumSize(QSize(16777215, 20))
        self.label_bar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_bar.setStyleSheet(u"background: transparent;\n"
"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_bar.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_bar)

        self.btn_entrar = QPushButton(self.frame)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setMinimumSize(QSize(100, 25))
        self.btn_entrar.setMaximumSize(QSize(100, 25))
        self.btn_entrar.setStyleSheet(u"\n"
"    QPushButton {\n"
"        background-color: #394568;\n"
"        border: 2px solid #394568;\n"
"        border-radius: 10px;\n"
"        font: 700 10pt \"Segoe UI\";\n"
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

        self.horizontalLayout.addWidget(self.btn_entrar)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)

        QWidget.setTabOrder(self.txt_password, self.btn_entrar)
        QWidget.setTabOrder(self.btn_entrar, self.comboBox_login)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Login", None))
        self.comboBox_login.setCurrentText("")
        self.comboBox_login.setPlaceholderText("")
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_bar.setText("")
        self.btn_entrar.setText(QCoreApplication.translate("Dialog", u"Entrar", None))
#if QT_CONFIG(shortcut)
        self.btn_entrar.setShortcut(QCoreApplication.translate("Dialog", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

