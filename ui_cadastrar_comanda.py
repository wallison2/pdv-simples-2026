# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastrar_comanda.ui'
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
    QLineEdit, QListView, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Cadastrar_Comanda(object):
    def setupUi(self, Cadastrar_Comanda):
        if not Cadastrar_Comanda.objectName():
            Cadastrar_Comanda.setObjectName(u"Cadastrar_Comanda")
        Cadastrar_Comanda.resize(380, 290)
        Cadastrar_Comanda.setMinimumSize(QSize(380, 290))
        Cadastrar_Comanda.setMaximumSize(QSize(380, 290))
        Cadastrar_Comanda.setStyleSheet(u"background: rgba(0,191,255,0.6);\n"
"")
        self.gridLayout_2 = QGridLayout(Cadastrar_Comanda)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Cadastrar_Comanda)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(39, 16777215))
        self.label_2.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.txt_codigo_comanda_cadastrar = QLineEdit(self.frame)
        self.txt_codigo_comanda_cadastrar.setObjectName(u"txt_codigo_comanda_cadastrar")
        self.txt_codigo_comanda_cadastrar.setStyleSheet(u"QLineEdit {\n"
"   \n"
"	background-color: rgb(255, 255, 127);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: rgb(127, 191, 255); /* Cor quando selecionado/focado */\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 10px \"Segoe UI\";\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.txt_codigo_comanda_cadastrar, 3, 0, 1, 2)

        self.radioButton_comanda = QRadioButton(self.frame)
        self.radioButton_comanda.setObjectName(u"radioButton_comanda")
        self.radioButton_comanda.setStyleSheet(u"QRadioButton {\n"
"    background: transparent;\n"
"    font: 700 10pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #32CD32;         /* verde lim\u00e3o */\n"
"    border: 2px solid #228B22;         /* verde escuro */\n"
"    border-radius: 8px;                /* borda arredondada */\n"
"}\n"
"")

        self.gridLayout.addWidget(self.radioButton_comanda, 2, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: transparent;\n"
"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.listView_listar_comanda = QListView(self.frame)
        self.listView_listar_comanda.setObjectName(u"listView_listar_comanda")

        self.gridLayout.addWidget(self.listView_listar_comanda, 5, 0, 1, 3)

        self.btn_excluir_cadastrar = QPushButton(self.frame)
        self.btn_excluir_cadastrar.setObjectName(u"btn_excluir_cadastrar")
        self.btn_excluir_cadastrar.setStyleSheet(u"\n"
"    QPushButton {\n"
"	background-color: rgb(255, 0, 0);\n"
"        border: 2px solid #394568;\n"
"        border-radius: 8px;\n"
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

        self.gridLayout.addWidget(self.btn_excluir_cadastrar, 3, 2, 1, 1)

        self.btn_salvar_cadastrar = QPushButton(self.frame)
        self.btn_salvar_cadastrar.setObjectName(u"btn_salvar_cadastrar")
        self.btn_salvar_cadastrar.setStyleSheet(u"\n"
"    QPushButton {\n"
"        background-color: #394568;\n"
"        border: 2px solid #394568;\n"
"        border-radius: 8px;\n"
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

        self.gridLayout.addWidget(self.btn_salvar_cadastrar, 2, 2, 1, 1)

        self.btn_ad_exemplos = QPushButton(self.frame)
        self.btn_ad_exemplos.setObjectName(u"btn_ad_exemplos")
        self.btn_ad_exemplos.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(255, 255, 0);  /* Amarelo */\n"
"    border: 2px solid #394568;\n"
"    border-radius: 8px;\n"
"    font: 700 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);  \n"
"    }\n"
"    QPushButton:hover {\n"
"	   background-color: #ffff00;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #2c3650;\n"
"    }\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_ad_exemplos, 4, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Cadastrar_Comanda)

        QMetaObject.connectSlotsByName(Cadastrar_Comanda)
    # setupUi

    def retranslateUi(self, Cadastrar_Comanda):
        Cadastrar_Comanda.setWindowTitle(QCoreApplication.translate("Cadastrar_Comanda", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Cadastrar_Comanda", u"Tipo:", None))
        self.txt_codigo_comanda_cadastrar.setPlaceholderText(QCoreApplication.translate("Cadastrar_Comanda", u"C\u00f3digo de identifica\u00e7\u00e3o", None))
        self.radioButton_comanda.setText(QCoreApplication.translate("Cadastrar_Comanda", u"Comanda", None))
        self.label.setText(QCoreApplication.translate("Cadastrar_Comanda", u"Cadastrar Mesas/Comandas", None))
        self.btn_excluir_cadastrar.setText(QCoreApplication.translate("Cadastrar_Comanda", u"Excluir", None))
        self.btn_salvar_cadastrar.setText(QCoreApplication.translate("Cadastrar_Comanda", u"Salvar", None))
        self.btn_ad_exemplos.setText(QCoreApplication.translate("Cadastrar_Comanda", u"ad_exemplos", None))
    # retranslateUi

