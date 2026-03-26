# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Saida.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import Resource_rc

class Ui_Saida(object):
    def setupUi(self, Saida):
        if not Saida.objectName():
            Saida.setObjectName(u"Saida")
        Saida.resize(410, 530)
        Saida.setMinimumSize(QSize(410, 530))
        Saida.setMaximumSize(QSize(410, 530))
        Saida.setStyleSheet(u"background: rgba(0,191,255,0.6);")
        self.gridLayout_2 = QGridLayout(Saida)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Saida)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background: rgba(0,191,255,0.6);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setStyleSheet(u"background: transparent;")
        self.label_2.setPixmap(QPixmap(u":/new/img/img (129).png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setStyleSheet(u"background: transparent;\n"
"font: 700 15pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(310, 30))
        self.label_3.setStyleSheet(u"background: transparent;\n"
"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.label_3)

        self.txt_valor_saida = QLineEdit(self.frame)
        self.txt_valor_saida.setObjectName(u"txt_valor_saida")
        self.txt_valor_saida.setStyleSheet(u"QLineEdit {\n"
"   \n"
"	background-color: rgb(255, 255, 127);\n"
"    font: bold 20pt \"Segoe UI\";\n"
"    border-radius: 6px;\n"
"	color: rgb(0, 0, 0);\n"
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

        self.verticalLayout_2.addWidget(self.txt_valor_saida)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(256, 30))
        self.label_4.setStyleSheet(u"background: transparent;\n"
"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout.addWidget(self.label_4)

        self.plainTextEdit_descricao_retirada = QPlainTextEdit(self.frame)
        self.plainTextEdit_descricao_retirada.setObjectName(u"plainTextEdit_descricao_retirada")
        self.plainTextEdit_descricao_retirada.setMinimumSize(QSize(0, 50))
        self.plainTextEdit_descricao_retirada.setMaximumSize(QSize(16777215, 50))
        self.plainTextEdit_descricao_retirada.setStyleSheet(u"QPlainTextEdit {\n"
"   \n"
"	background-color: rgb(255, 255, 127);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    background-color: rgb(127, 191, 255); /* Cor quando selecionado/focado */\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 10px \"Segoe UI\";\n"
"    border-radius: 6px;\n"
"}")

        self.verticalLayout.addWidget(self.plainTextEdit_descricao_retirada)


        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background: transparent;\n"
"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_3.addWidget(self.label_5)

        self.comboBox_descricao_saidas = QComboBox(self.frame)
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.addItem("")
        self.comboBox_descricao_saidas.setObjectName(u"comboBox_descricao_saidas")
        self.comboBox_descricao_saidas.setMinimumSize(QSize(0, 40))
        self.comboBox_descricao_saidas.setMaximumSize(QSize(430, 40))
        self.comboBox_descricao_saidas.setStyleSheet(u"QComboBox {\n"
"		background-color: rgb(80, 81, 82);\n"
"        border: 2px solid #394568;\n"
"        border-radius: 10px;\n"
"        font: 700 10pt \"Segoe UI\";\n"
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

        self.verticalLayout_3.addWidget(self.comboBox_descricao_saidas)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background: transparent;\n"
"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.label_6)

        self.comboBox_forma_pgto_saida = QComboBox(self.frame)
        self.comboBox_forma_pgto_saida.addItem("")
        self.comboBox_forma_pgto_saida.addItem("")
        self.comboBox_forma_pgto_saida.addItem("")
        self.comboBox_forma_pgto_saida.addItem("")
        self.comboBox_forma_pgto_saida.setObjectName(u"comboBox_forma_pgto_saida")
        self.comboBox_forma_pgto_saida.setMinimumSize(QSize(0, 40))
        self.comboBox_forma_pgto_saida.setMaximumSize(QSize(430, 40))
        self.comboBox_forma_pgto_saida.setStyleSheet(u"QComboBox {\n"
"		background-color: rgb(80, 81, 82);\n"
"        border: 2px solid #394568;\n"
"        border-radius: 10px;\n"
"        font: 700 10pt \"Segoe UI\";\n"
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

        self.verticalLayout_4.addWidget(self.comboBox_forma_pgto_saida)


        self.gridLayout.addLayout(self.verticalLayout_4, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_salvar_saida = QPushButton(self.frame)
        self.btn_salvar_saida.setObjectName(u"btn_salvar_saida")
        self.btn_salvar_saida.setMinimumSize(QSize(120, 30))
        self.btn_salvar_saida.setMaximumSize(QSize(120, 30))
        self.btn_salvar_saida.setStyleSheet(u"\n"
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

        self.horizontalLayout_2.addWidget(self.btn_salvar_saida)

        self.btn_saidas_sair = QPushButton(self.frame)
        self.btn_saidas_sair.setObjectName(u"btn_saidas_sair")
        self.btn_saidas_sair.setMinimumSize(QSize(90, 30))
        self.btn_saidas_sair.setMaximumSize(QSize(90, 30))
        self.btn_saidas_sair.setStyleSheet(u"\n"
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

        self.horizontalLayout_2.addWidget(self.btn_saidas_sair)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Saida)
        self.btn_saidas_sair.clicked.connect(Saida.close)

        QMetaObject.connectSlotsByName(Saida)
    # setupUi

    def retranslateUi(self, Saida):
        Saida.setWindowTitle(QCoreApplication.translate("Saida", u"Form", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("Saida", u"Saidas - Sangrias", None))
        self.label_3.setText(QCoreApplication.translate("Saida", u"Valor", None))
        self.txt_valor_saida.setPlaceholderText(QCoreApplication.translate("Saida", u"Valor R$", None))
        self.label_4.setText(QCoreApplication.translate("Saida", u"Descri\u00e7\u00e3o da Retirada", None))
        self.label_5.setText(QCoreApplication.translate("Saida", u"Tipo de Despesa", None))
        self.comboBox_descricao_saidas.setItemText(0, QCoreApplication.translate("Saida", u"Sa\u00edda em Dinheiro", None))
        self.comboBox_descricao_saidas.setItemText(1, QCoreApplication.translate("Saida", u"Cancelamento de Venda", None))
        self.comboBox_descricao_saidas.setItemText(2, QCoreApplication.translate("Saida", u"Devolu\u00e7\u00e3o de Produto", None))
        self.comboBox_descricao_saidas.setItemText(3, QCoreApplication.translate("Saida", u"Venda de Produto", None))
        self.comboBox_descricao_saidas.setItemText(4, QCoreApplication.translate("Saida", u"Retirada para Troco", None))
        self.comboBox_descricao_saidas.setItemText(5, QCoreApplication.translate("Saida", u"Sa\u00edda via Pix", None))
        self.comboBox_descricao_saidas.setItemText(6, QCoreApplication.translate("Saida", u"Retirada para Despesas Operacionais", None))
        self.comboBox_descricao_saidas.setItemText(7, QCoreApplication.translate("Saida", u"Retirada para Pagamento de Fornecedores", None))
        self.comboBox_descricao_saidas.setItemText(8, QCoreApplication.translate("Saida", u"Retirada para Pagamento de Contas", None))
        self.comboBox_descricao_saidas.setItemText(9, QCoreApplication.translate("Saida", u"Retirada para Fundo de Caixa", None))
        self.comboBox_descricao_saidas.setItemText(10, QCoreApplication.translate("Saida", u"Sa\u00edda em Cart\u00e3o de Cr\u00e9dito", None))
        self.comboBox_descricao_saidas.setItemText(11, QCoreApplication.translate("Saida", u"Sa\u00edda em Cart\u00e3o de D\u00e9bito", None))
        self.comboBox_descricao_saidas.setItemText(12, QCoreApplication.translate("Saida", u"Sa\u00edda para Dep\u00f3sito Banc\u00e1rio", None))
        self.comboBox_descricao_saidas.setItemText(13, QCoreApplication.translate("Saida", u"Sa\u00edda para Transfer\u00eancia Eletr\u00f4nica", None))
        self.comboBox_descricao_saidas.setItemText(14, QCoreApplication.translate("Saida", u"Sa\u00edda para Pagamento de Sal\u00e1rios", None))
        self.comboBox_descricao_saidas.setItemText(15, QCoreApplication.translate("Saida", u"Sa\u00edda para Pagamento de Impostos", None))
        self.comboBox_descricao_saidas.setItemText(16, QCoreApplication.translate("Saida", u"Retirada para Investimentos", None))
        self.comboBox_descricao_saidas.setItemText(17, QCoreApplication.translate("Saida", u"Retirada para Capital de Giro", None))
        self.comboBox_descricao_saidas.setItemText(18, QCoreApplication.translate("Saida", u"Sa\u00edda para Compra de Ativos", None))
        self.comboBox_descricao_saidas.setItemText(19, QCoreApplication.translate("Saida", u"Outras Sa\u00eddas ou Sangrias", None))

        self.label_6.setText(QCoreApplication.translate("Saida", u"Forma de Pgto", None))
        self.comboBox_forma_pgto_saida.setItemText(0, QCoreApplication.translate("Saida", u"Dinheiro", None))
        self.comboBox_forma_pgto_saida.setItemText(1, QCoreApplication.translate("Saida", u"Cart\u00e3o de Cr\u00e9dito", None))
        self.comboBox_forma_pgto_saida.setItemText(2, QCoreApplication.translate("Saida", u"Cart\u00e3o de D\u00e9bito", None))
        self.comboBox_forma_pgto_saida.setItemText(3, QCoreApplication.translate("Saida", u"Pix", None))

        self.btn_salvar_saida.setText(QCoreApplication.translate("Saida", u"Salvar Saida", None))
        self.btn_saidas_sair.setText(QCoreApplication.translate("Saida", u"Sair", None))
#if QT_CONFIG(shortcut)
        self.btn_saidas_sair.setShortcut(QCoreApplication.translate("Saida", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

