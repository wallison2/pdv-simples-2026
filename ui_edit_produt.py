# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_produt.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Edicao_Produto(object):
    def setupUi(self, Edicao_Produto):
        if not Edicao_Produto.objectName():
            Edicao_Produto.setObjectName(u"Edicao_Produto")
        Edicao_Produto.resize(620, 690)
        Edicao_Produto.setMinimumSize(QSize(620, 690))
        Edicao_Produto.setMaximumSize(QSize(620, 690))
        Edicao_Produto.setStyleSheet(u"background: rgba(0,191,255,0.6);")
        self.gridLayout = QGridLayout(Edicao_Produto)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(Edicao_Produto)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background: rgba(0,191,255,0.6);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_edit_nome_produt = QLineEdit(self.frame)
        self.txt_edit_nome_produt.setObjectName(u"txt_edit_nome_produt")
        self.txt_edit_nome_produt.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
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

        self.gridLayout_2.addWidget(self.txt_edit_nome_produt, 6, 0, 1, 2)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.label_6, 15, 0, 1, 2)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.label_17, 3, 0, 1, 2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.label_5, 13, 0, 1, 2)

        self.txt_edit_valor_compra_produt = QLineEdit(self.frame)
        self.txt_edit_valor_compra_produt.setObjectName(u"txt_edit_valor_compra_produt")
        self.txt_edit_valor_compra_produt.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
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

        self.gridLayout_2.addWidget(self.txt_edit_valor_compra_produt, 14, 0, 1, 2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.label_3, 7, 0, 1, 2)

        self.txt_edit_descricao_produt = QLineEdit(self.frame)
        self.txt_edit_descricao_produt.setObjectName(u"txt_edit_descricao_produt")
        self.txt_edit_descricao_produt.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
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

        self.gridLayout_2.addWidget(self.txt_edit_descricao_produt, 8, 0, 1, 2)

        self.comboBox_novo_tipo_produto = QComboBox(self.frame)
        self.comboBox_novo_tipo_produto.addItem("")
        self.comboBox_novo_tipo_produto.addItem("")
        self.comboBox_novo_tipo_produto.setObjectName(u"comboBox_novo_tipo_produto")
        self.comboBox_novo_tipo_produto.setStyleSheet(u"QComboBox {\n"
"    background-color: rgb(80, 81, 82);\n"
"    border: 2px solid #394568;\n"
"    border-radius: 10px;\n"
"    font: 700 10pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);  /* Cor do texto na caixa do ComboBox */\n"
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
"    color: rgb(255, 255, 255);  /* Cor do texto dos itens da lista */\n"
"    background-color: rgb(80, 81, 82);  /* Cor de fundo do menu suspenso */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(path/to/your/icon.png);  /* Se voc\u00ea quiser adicionar um \u00edcone de seta */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.comboBox_novo_tipo_produto, 12, 0, 1, 2)

        self.txt_edit_qtde_produt = QLineEdit(self.frame)
        self.txt_edit_qtde_produt.setObjectName(u"txt_edit_qtde_produt")
        self.txt_edit_qtde_produt.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
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

        self.gridLayout_2.addWidget(self.txt_edit_qtde_produt, 10, 0, 1, 2)

        self.txt_edit_valor_venda_produt = QLineEdit(self.frame)
        self.txt_edit_valor_venda_produt.setObjectName(u"txt_edit_valor_venda_produt")
        self.txt_edit_valor_venda_produt.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
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

        self.gridLayout_2.addWidget(self.txt_edit_valor_venda_produt, 16, 0, 1, 2)

        self.btn_sair_sem_salvar_edicao_produto = QPushButton(self.frame)
        self.btn_sair_sem_salvar_edicao_produto.setObjectName(u"btn_sair_sem_salvar_edicao_produto")
        self.btn_sair_sem_salvar_edicao_produto.setMinimumSize(QSize(140, 30))
        self.btn_sair_sem_salvar_edicao_produto.setMaximumSize(QSize(140, 30))
        self.btn_sair_sem_salvar_edicao_produto.setStyleSheet(u"    QPushButton {\n"
"        background-color: #394568;\n"
"        border: 2px solid #394568;\n"
"        border-radius: 12px;\n"
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

        self.gridLayout_2.addWidget(self.btn_sair_sem_salvar_edicao_produto, 17, 1, 1, 1)

        self.btn_salvar_edicao_produto = QPushButton(self.frame)
        self.btn_salvar_edicao_produto.setObjectName(u"btn_salvar_edicao_produto")
        self.btn_salvar_edicao_produto.setMinimumSize(QSize(140, 30))
        self.btn_salvar_edicao_produto.setMaximumSize(QSize(140, 30))
        self.btn_salvar_edicao_produto.setStyleSheet(u"    QPushButton {\n"
"        background-color: #394568;\n"
"        border: 2px solid #394568;\n"
"        border-radius: 12px;\n"
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

        self.gridLayout_2.addWidget(self.btn_salvar_edicao_produto, 17, 0, 1, 1)

        self.txt_edit_codigo_barras_produt = QLineEdit(self.frame)
        self.txt_edit_codigo_barras_produt.setObjectName(u"txt_edit_codigo_barras_produt")
        self.txt_edit_codigo_barras_produt.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
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

        self.gridLayout_2.addWidget(self.txt_edit_codigo_barras_produt, 4, 0, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(287, 27))
        self.label_15.setStyleSheet(u"background: transparent;\n"
"font: bold 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.label_4, 9, 0, 1, 2)

        self.txt_edit_codigo_produt = QLineEdit(self.frame)
        self.txt_edit_codigo_produt.setObjectName(u"txt_edit_codigo_produt")
        self.txt_edit_codigo_produt.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
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

        self.gridLayout_2.addWidget(self.txt_edit_codigo_produt, 2, 0, 1, 2)

        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.label_19, 11, 0, 1, 2)


        self.gridLayout_4.addWidget(self.frame, 2, 2, 1, 1)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background: rgba(0,191,255,0.6);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"background: transparent;\n"
"font: bold 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_codigo_anterior_produto = QLabel(self.frame_2)
        self.label_codigo_anterior_produto.setObjectName(u"label_codigo_anterior_produto")
        self.label_codigo_anterior_produto.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_codigo_anterior_produto, 2, 0, 1, 1)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.label_16, 3, 0, 1, 1)

        self.label_codigo_barras_anterior_produto = QLabel(self.frame_2)
        self.label_codigo_barras_anterior_produto.setObjectName(u"label_codigo_barras_anterior_produto")
        self.label_codigo_barras_anterior_produto.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_codigo_barras_anterior_produto, 4, 0, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)

        self.label_nome_anterior_produto = QLabel(self.frame_2)
        self.label_nome_anterior_produto.setObjectName(u"label_nome_anterior_produto")
        self.label_nome_anterior_produto.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_nome_anterior_produto, 6, 0, 1, 1)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.label_10, 7, 0, 1, 1)

        self.label_descricao_anterior_produto = QLabel(self.frame_2)
        self.label_descricao_anterior_produto.setObjectName(u"label_descricao_anterior_produto")
        self.label_descricao_anterior_produto.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_descricao_anterior_produto, 8, 0, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.label_11, 9, 0, 1, 1)

        self.label_qtde_anterior_produto = QLabel(self.frame_2)
        self.label_qtde_anterior_produto.setObjectName(u"label_qtde_anterior_produto")
        self.label_qtde_anterior_produto.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_qtde_anterior_produto, 10, 0, 1, 1)

        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.label_18, 11, 0, 1, 1)

        self.label_tipo_anterior_produto = QLabel(self.frame_2)
        self.label_tipo_anterior_produto.setObjectName(u"label_tipo_anterior_produto")
        self.label_tipo_anterior_produto.setMinimumSize(QSize(26, 0))
        self.label_tipo_anterior_produto.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_tipo_anterior_produto, 12, 0, 1, 1)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.label_12, 13, 0, 1, 1)

        self.label_valor_compra_anterior_produto = QLabel(self.frame_2)
        self.label_valor_compra_anterior_produto.setObjectName(u"label_valor_compra_anterior_produto")
        self.label_valor_compra_anterior_produto.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_valor_compra_anterior_produto, 14, 0, 1, 1)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background: transparent;\n"
"font: bold 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.label_13, 15, 0, 1, 1)

        self.label_valor_venda_anterior_produto = QLabel(self.frame_2)
        self.label_valor_venda_anterior_produto.setObjectName(u"label_valor_venda_anterior_produto")
        self.label_valor_venda_anterior_produto.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_valor_venda_anterior_produto, 16, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 2, 1, 1, 1)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(580, 30))
        self.label_7.setStyleSheet(u"background: transparent;\n"
"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_7, 1, 1, 1, 2)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)


        self.retranslateUi(Edicao_Produto)

        QMetaObject.connectSlotsByName(Edicao_Produto)
    # setupUi

    def retranslateUi(self, Edicao_Produto):
        Edicao_Produto.setWindowTitle(QCoreApplication.translate("Edicao_Produto", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("Edicao_Produto", u"Editar Valor da Venda do Produto", None))
        self.label_17.setText(QCoreApplication.translate("Edicao_Produto", u"Editar C\u00f3digo de Barras do Produto", None))
        self.label_5.setText(QCoreApplication.translate("Edicao_Produto", u"Editar Valor da Compra do Produto", None))
        self.label_2.setText(QCoreApplication.translate("Edicao_Produto", u"Editar Nome do Produto", None))
        self.label_3.setText(QCoreApplication.translate("Edicao_Produto", u"Editar Descri\u00e7\u00e3o do Produto", None))
        self.comboBox_novo_tipo_produto.setItemText(0, QCoreApplication.translate("Edicao_Produto", u"UNI", None))
        self.comboBox_novo_tipo_produto.setItemText(1, QCoreApplication.translate("Edicao_Produto", u"PCTO", None))

        self.btn_sair_sem_salvar_edicao_produto.setText(QCoreApplication.translate("Edicao_Produto", u"Sair Sem Salvar", None))
        self.btn_salvar_edicao_produto.setText(QCoreApplication.translate("Edicao_Produto", u"Salvar Edi\u00e7\u00e3o", None))
        self.label.setText(QCoreApplication.translate("Edicao_Produto", u"Editar C\u00f3digo do Produto", None))
        self.label_15.setText(QCoreApplication.translate("Edicao_Produto", u"Valores Editados", None))
        self.label_4.setText(QCoreApplication.translate("Edicao_Produto", u"Editar Quantidade do Produto", None))
        self.label_19.setText(QCoreApplication.translate("Edicao_Produto", u"Editar Tipo do Produto Uni/Pcto", None))
        self.label_14.setText(QCoreApplication.translate("Edicao_Produto", u"Valores Salvos", None))
        self.label_8.setText(QCoreApplication.translate("Edicao_Produto", u"C\u00f3digo Produto", None))
        self.label_codigo_anterior_produto.setText("")
        self.label_16.setText(QCoreApplication.translate("Edicao_Produto", u"C\u00f3digo de Barras", None))
        self.label_codigo_barras_anterior_produto.setText("")
        self.label_9.setText(QCoreApplication.translate("Edicao_Produto", u"Nome do Produto", None))
        self.label_nome_anterior_produto.setText("")
        self.label_10.setText(QCoreApplication.translate("Edicao_Produto", u"Descri\u00e7\u00e3o do Produto", None))
        self.label_descricao_anterior_produto.setText("")
        self.label_11.setText(QCoreApplication.translate("Edicao_Produto", u"Quantidade do Produto", None))
        self.label_qtde_anterior_produto.setText("")
        self.label_18.setText(QCoreApplication.translate("Edicao_Produto", u"Tipo do Produto Uni/Pcto", None))
        self.label_tipo_anterior_produto.setText("")
        self.label_12.setText(QCoreApplication.translate("Edicao_Produto", u"Valor da Compra do Produto", None))
        self.label_valor_compra_anterior_produto.setText("")
        self.label_13.setText(QCoreApplication.translate("Edicao_Produto", u"Valor da Venda do Produto", None))
        self.label_valor_venda_anterior_produto.setText("")
        self.label_7.setText(QCoreApplication.translate("Edicao_Produto", u"Edi\u00e7\u00e3o de Produtos", None))
    # retranslateUi

