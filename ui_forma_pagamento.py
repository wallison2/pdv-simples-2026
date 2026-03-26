# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forma_pagamento.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form_Pgto(object):
    def setupUi(self, Form_Pgto):
        if not Form_Pgto.objectName():
            Form_Pgto.setObjectName(u"Form_Pgto")
        Form_Pgto.resize(692, 454)
        Form_Pgto.setMaximumSize(QSize(692, 454))
        Form_Pgto.setStyleSheet(u"background: rgba(0,191,255,0.6);")
        self.gridLayout_2 = QGridLayout(Form_Pgto)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(Form_Pgto)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background: transparent;\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)

        self.frame = QFrame(Form_Pgto)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setStyleSheet(u"background: transparent;\n"
"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.labell_valor_venda = QLabel(self.frame)
        self.labell_valor_venda.setObjectName(u"labell_valor_venda")
        self.labell_valor_venda.setMinimumSize(QSize(0, 160))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(50)
        font1.setBold(True)
        font1.setItalic(False)
        self.labell_valor_venda.setFont(font1)
        self.labell_valor_venda.setStyleSheet(u"background: transparent;\n"
"font: 700 50pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"\n"
"\n"
"")
        self.labell_valor_venda.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.labell_valor_venda)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 2, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setStyleSheet(u"background: transparent;\n"
"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.comboBox_forma_pgto = QComboBox(self.frame)
        self.comboBox_forma_pgto.addItem(u"Dinheiro")
        self.comboBox_forma_pgto.addItem("")
        self.comboBox_forma_pgto.addItem("")
        self.comboBox_forma_pgto.addItem("")
        self.comboBox_forma_pgto.setObjectName(u"comboBox_forma_pgto")
        self.comboBox_forma_pgto.setMinimumSize(QSize(270, 70))
        self.comboBox_forma_pgto.setMaximumSize(QSize(270, 70))
        self.comboBox_forma_pgto.setStyleSheet(u"QComboBox {\n"
"		background-color: rgb(80, 81, 82);\n"
"        border: 2px solid #394568;\n"
"        border-radius: 10px;\n"
"        font: 700 14pt \"Segoe UI\";\n"
"		color: rgb(255, 255, 255);\n"
"    }\n"
"     QComboBox:hover {\n"
"        \n"
"	background-color: rgb(75, 85, 83);\n"
"\n"
"    }\n"
"     QComboBox:pressed {\n"
"        background-color: #2c3650;\n"
"    }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"    /* Propriedades de estilo para o menu suspenso */\n"
"}\n"
"")
        self.comboBox_forma_pgto.setEditable(True)

        self.verticalLayout.addWidget(self.comboBox_forma_pgto)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background: transparent;\n"
"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_troco_finalizar = QLabel(self.frame)
        self.label_troco_finalizar.setObjectName(u"label_troco_finalizar")
        self.label_troco_finalizar.setStyleSheet(u"background: transparent;\n"
"font: 700 50pt \"Segoe UI\";\n"
"color: rgb(255, 0, 0);\n"
"\n"
"\n"
"")
        self.label_troco_finalizar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_troco_finalizar)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 2, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setStyleSheet(u"background: transparent;\n"
"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.txt_dinheiro_finaliza = QLineEdit(self.frame)
        self.txt_dinheiro_finaliza.setObjectName(u"txt_dinheiro_finaliza")
        self.txt_dinheiro_finaliza.setMinimumSize(QSize(290, 50))
        self.txt_dinheiro_finaliza.setMaximumSize(QSize(290, 60))
        self.txt_dinheiro_finaliza.setStyleSheet(u"QLineEdit {\n"
"   \n"
"	background-color: rgb(255, 255, 255);\n"
"    font: bold 24pt \"Segoe UI\";\n"
"    border-radius: 10px;\n"
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
"    border-radius: 10px;\n"
"}")
        self.txt_dinheiro_finaliza.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.txt_dinheiro_finaliza)


        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 2)

        self.btn_finalizar_venda = QPushButton(Form_Pgto)
        self.btn_finalizar_venda.setObjectName(u"btn_finalizar_venda")
        self.btn_finalizar_venda.setMinimumSize(QSize(0, 45))
        self.btn_finalizar_venda.setStyleSheet(u"\n"
"    QPushButton {\n"
"        background-color: #394568;\n"
"        border: 2px solid #394568;\n"
"        border-radius: 10px;\n"
"        font: 700 14pt \"Segoe UI\";\n"
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

        self.gridLayout_2.addWidget(self.btn_finalizar_venda, 2, 0, 1, 1)

        self.btn_cancelar_venda_final = QPushButton(Form_Pgto)
        self.btn_cancelar_venda_final.setObjectName(u"btn_cancelar_venda_final")
        self.btn_cancelar_venda_final.setMinimumSize(QSize(0, 45))
        self.btn_cancelar_venda_final.setStyleSheet(u"\n"
"    QPushButton {\n"
"        background-color: #394568;\n"
"        border: 2px solid #394568;\n"
"        border-radius: 10px;\n"
"        font: 700 14pt \"Segoe UI\";\n"
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

        self.gridLayout_2.addWidget(self.btn_cancelar_venda_final, 2, 1, 1, 1)

        QWidget.setTabOrder(self.txt_dinheiro_finaliza, self.comboBox_forma_pgto)
        QWidget.setTabOrder(self.comboBox_forma_pgto, self.btn_finalizar_venda)
        QWidget.setTabOrder(self.btn_finalizar_venda, self.btn_cancelar_venda_final)

        self.retranslateUi(Form_Pgto)
        self.btn_cancelar_venda_final.clicked.connect(Form_Pgto.close)

        QMetaObject.connectSlotsByName(Form_Pgto)
    # setupUi

    def retranslateUi(self, Form_Pgto):
        Form_Pgto.setWindowTitle(QCoreApplication.translate("Form_Pgto", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form_Pgto", u"Finalizar Venda", None))
        self.label_2.setText(QCoreApplication.translate("Form_Pgto", u"Valor a Pagar", None))
        self.labell_valor_venda.setText("")
        self.label_3.setText(QCoreApplication.translate("Form_Pgto", u"Alterar Formas de Pgto \"F5\"", None))
        self.comboBox_forma_pgto.setItemText(1, QCoreApplication.translate("Form_Pgto", u"Cart\u00e3o de Cr\u00e9dito", None))
        self.comboBox_forma_pgto.setItemText(2, QCoreApplication.translate("Form_Pgto", u"Cart\u00e3o de D\u00e9bito", None))
        self.comboBox_forma_pgto.setItemText(3, QCoreApplication.translate("Form_Pgto", u"Pix", None))

        self.comboBox_forma_pgto.setCurrentText(QCoreApplication.translate("Form_Pgto", u"Dinheiro", None))
        self.comboBox_forma_pgto.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("Form_Pgto", u"Troco", None))
        self.label_troco_finalizar.setText("")
        self.label.setText(QCoreApplication.translate("Form_Pgto", u"Dinheiro R$", None))
        self.txt_dinheiro_finaliza.setInputMask("")
        self.txt_dinheiro_finaliza.setText("")
        self.txt_dinheiro_finaliza.setPlaceholderText("")
        self.btn_finalizar_venda.setText(QCoreApplication.translate("Form_Pgto", u"Finalizar Venda/F2", None))
#if QT_CONFIG(shortcut)
        self.btn_finalizar_venda.setShortcut(QCoreApplication.translate("Form_Pgto", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_cancelar_venda_final.setText(QCoreApplication.translate("Form_Pgto", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.btn_cancelar_venda_final.setShortcut(QCoreApplication.translate("Form_Pgto", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

