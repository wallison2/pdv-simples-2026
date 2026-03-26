# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comandas.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListView, QPushButton, QSizePolicy, QSplitter,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(660, 409)
        Form.setMaximumSize(QSize(660, 16777215))
        Form.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.label_3 = QLabel(self.splitter)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.splitter.addWidget(self.label_3)
        self.lineEdit = QLineEdit(self.splitter)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
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
        self.splitter.addWidget(self.lineEdit)

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)

        self.splitter_3 = QSplitter(self.groupBox)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Vertical)
        self.label_4 = QLabel(self.splitter_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.splitter_3.addWidget(self.label_4)
        self.lineEdit_3 = QLineEdit(self.splitter_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
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
        self.splitter_3.addWidget(self.lineEdit_3)

        self.gridLayout_2.addWidget(self.splitter_3, 0, 1, 1, 1)

        self.splitter_2 = QSplitter(self.groupBox)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.label_5 = QLabel(self.splitter_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.splitter_2.addWidget(self.label_5)
        self.lineEdit_2 = QLineEdit(self.splitter_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
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
        self.splitter_2.addWidget(self.lineEdit_2)

        self.gridLayout_2.addWidget(self.splitter_2, 1, 0, 1, 1)

        self.splitter_4 = QSplitter(self.groupBox)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Orientation.Vertical)
        self.label_6 = QLabel(self.splitter_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.splitter_4.addWidget(self.label_6)
        self.lineEdit_4 = QLineEdit(self.splitter_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
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
        self.splitter_4.addWidget(self.lineEdit_4)

        self.gridLayout_2.addWidget(self.splitter_4, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(120, 16777215))
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(90, 0))
        self.pushButton.setStyleSheet(u"\n"
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

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(90, 0))
        self.pushButton_2.setStyleSheet(u"\n"
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

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(90, 0))
        self.pushButton_3.setStyleSheet(u"\n"
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

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.pushButton_3)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)

        self.listView = QListView(self.frame)
        self.listView.setObjectName(u"listView")

        self.gridLayout_3.addWidget(self.listView, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Mesa/Comanda", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Mesa/Comanda", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Quantidade", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Digiter o Codigo do Produto", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Nome Produto", None))
        self.groupBox_2.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Adicionar Item", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Lan\u00e7ar M/C", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Excluir Itens", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Lista das comandas", None))
    # retranslateUi


