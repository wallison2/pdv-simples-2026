# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSplitter, QTabWidget,
    QTableView, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)
import Resource_rc

class Ui_W_W_AUTO_COM_PDV(object):
    def setupUi(self, W_W_AUTO_COM_PDV):
        if not W_W_AUTO_COM_PDV.objectName():
            W_W_AUTO_COM_PDV.setObjectName(u"W_W_AUTO_COM_PDV")
        W_W_AUTO_COM_PDV.setEnabled(True)
        W_W_AUTO_COM_PDV.resize(993, 744)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(W_W_AUTO_COM_PDV.sizePolicy().hasHeightForWidth())
        W_W_AUTO_COM_PDV.setSizePolicy(sizePolicy)
        W_W_AUTO_COM_PDV.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/new/img/img (85).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        W_W_AUTO_COM_PDV.setWindowIcon(icon)
        W_W_AUTO_COM_PDV.setStyleSheet(u"background: rgba(0,191,255,0.6);\n"
"")
        W_W_AUTO_COM_PDV.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        W_W_AUTO_COM_PDV.setDockOptions(QMainWindow.DockOption.AllowNestedDocks|QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks|QMainWindow.DockOption.ForceTabbedDocks|QMainWindow.DockOption.GroupedDragging|QMainWindow.DockOption.VerticalTabs)
        self.actionTrocar_User = QAction(W_W_AUTO_COM_PDV)
        self.actionTrocar_User.setObjectName(u"actionTrocar_User")
        self.centralwidget1518 = QWidget(W_W_AUTO_COM_PDV)
        self.centralwidget1518.setObjectName(u"centralwidget1518")
        self.gridLayout_8 = QGridLayout(self.centralwidget1518)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tabPrincipal = QTabWidget(self.centralwidget1518)
        self.tabPrincipal.setObjectName(u"tabPrincipal")
        self.tabPrincipal.setEnabled(True)
        self.tabPrincipal.setMinimumSize(QSize(40, 30))
        font = QFont()
        font.setFamilies([u"Segoe MDL2 Assets"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.tabPrincipal.setFont(font)
        self.tabPrincipal.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.tabPrincipal.setStyleSheet(u"QTabBar::tab {\n"
"background-color: rgb(80, 81, 82);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 10pt \"Arial\";\n"
"border: 3px solid #555555;\n"
" border-radius: 10px;\n"
" min-width: 80px;\n"
" padding: -5px;\n"
"                         }\n"
"\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(100, 149, 237);\n"
"	border-color: rgb(80, 81, 82);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"                         \n"
"")
        self.tabPrincipal.setTabPosition(QTabWidget.TabPosition.North)
        self.tabPrincipal.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabPrincipal.setIconSize(QSize(40, 30))
        self.tabPrincipal.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabPrincipal.setUsesScrollButtons(True)
        self.tabPrincipal.setDocumentMode(False)
        self.tabPrincipal.setTabsClosable(False)
        self.tabPrincipal.setMovable(False)
        self.tabPrincipal.setTabBarAutoHide(False)
        self.widget00 = QWidget()
        self.widget00.setObjectName(u"widget00")
        self.gridLayout_5 = QGridLayout(self.widget00)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.widget00)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/new/img/img (108).png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        icon1 = QIcon()
        icon1.addFile(u":/new/img/img (55).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabPrincipal.addTab(self.widget00, icon1, "")
        self.widget_1 = QWidget()
        self.widget_1.setObjectName(u"widget_1")
        sizePolicy.setHeightForWidth(self.widget_1.sizePolicy().hasHeightForWidth())
        self.widget_1.setSizePolicy(sizePolicy)
        self.gridLayout_7 = QGridLayout(self.widget_1)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame = QFrame(self.widget_1)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_26 = QGridLayout(self.frame)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.txt_cod_pdv = QLineEdit(self.frame)
        self.txt_cod_pdv.setObjectName(u"txt_cod_pdv")
        self.txt_cod_pdv.setMinimumSize(QSize(0, 50))
        self.txt_cod_pdv.setStyleSheet(u"QLineEdit {\n"
"   \n"
"	background-color: rgb(255, 255, 127);\n"
"    font: bold 20pt \"Segoe UI\";\n"
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
        self.txt_cod_pdv.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.txt_cod_pdv.setDragEnabled(False)
        self.txt_cod_pdv.setReadOnly(False)
        self.txt_cod_pdv.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.txt_cod_pdv.setClearButtonEnabled(True)

        self.gridLayout_26.addWidget(self.txt_cod_pdv, 0, 0, 1, 2)

        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(270, 52))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_17)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_20 = QLabel(self.frame_17)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setMaximumSize(QSize(145, 16777215))
        self.label_20.setStyleSheet(u"background: transparent;\n"
"font: 700 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_12.addWidget(self.label_20, 0, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.btn_mais_qtde = QPushButton(self.frame_17)
        self.btn_mais_qtde.setObjectName(u"btn_mais_qtde")
        self.btn_mais_qtde.setMaximumSize(QSize(22, 20))
        self.btn_mais_qtde.setStyleSheet(u"\n"
"    QPushButton {\n"
"        background-color: #394568;\n"
"        border: 2px solid #394568;\n"
"        border-radius: 8px;\n"
"        font: 700 20pt \"Segoe UI\";\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/new/img/img (133).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_mais_qtde.setIcon(icon2)

        self.horizontalLayout_22.addWidget(self.btn_mais_qtde)

        self.txt_qtde = QLineEdit(self.frame_17)
        self.txt_qtde.setObjectName(u"txt_qtde")
        self.txt_qtde.setMinimumSize(QSize(50, 30))
        self.txt_qtde.setMaximumSize(QSize(50, 30))
        self.txt_qtde.setStyleSheet(u"QLineEdit {\n"
"   \n"
"	background-color: rgb(255, 255, 127);\n"
"    font: bold 18pt \"Segoe UI\";\n"
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
        self.txt_qtde.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_22.addWidget(self.txt_qtde)

        self.btn_menos_qtde = QPushButton(self.frame_17)
        self.btn_menos_qtde.setObjectName(u"btn_menos_qtde")
        self.btn_menos_qtde.setMaximumSize(QSize(22, 20))
        self.btn_menos_qtde.setStyleSheet(u"\n"
"    QPushButton {\n"
"        background-color: #394568;\n"
"        border: 2px solid #394568;\n"
"        border-radius: 8px;\n"
"        font: 700 20pt \"Segoe UI\";\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/new/img/img (132).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menos_qtde.setIcon(icon3)

        self.horizontalLayout_22.addWidget(self.btn_menos_qtde)


        self.gridLayout_12.addLayout(self.horizontalLayout_22, 0, 1, 1, 1)


        self.gridLayout_26.addWidget(self.frame_17, 0, 2, 1, 1)

        self.tableView_pdv = QTableView(self.frame)
        self.tableView_pdv.setObjectName(u"tableView_pdv")
        self.tableView_pdv.setStyleSheet(u"")

        self.gridLayout_26.addWidget(self.tableView_pdv, 1, 0, 3, 1)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(280, 16777215))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_7)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_logo_empresa = QLabel(self.frame_7)
        self.label_logo_empresa.setObjectName(u"label_logo_empresa")
        self.label_logo_empresa.setStyleSheet(u"")
        self.label_logo_empresa.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_logo_empresa)


        self.gridLayout_25.addLayout(self.horizontalLayout_23, 0, 0, 1, 1)

        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 0))
        self.label_13.setMaximumSize(QSize(16777215, 35))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background: transparent;\n"
"font: 700 22pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_25.addWidget(self.label_13, 1, 0, 1, 1)

        self.txt_valor_total_pdv = QLineEdit(self.frame_7)
        self.txt_valor_total_pdv.setObjectName(u"txt_valor_total_pdv")
        self.txt_valor_total_pdv.setMinimumSize(QSize(260, 120))
        self.txt_valor_total_pdv.setMaximumSize(QSize(16777215, 120))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(30)
        font2.setBold(True)
        font2.setItalic(False)
        self.txt_valor_total_pdv.setFont(font2)
        self.txt_valor_total_pdv.setStyleSheet(u"\n"
"QLineEdit {\n"
"   \n"
"	background-color: rgb(255, 255, 255);\n"
"    font: bold 30pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
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
        self.txt_valor_total_pdv.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_25.addWidget(self.txt_valor_total_pdv, 2, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_7, 1, 1, 1, 2)

        self.frame_15 = QFrame(self.frame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 0))
        self.frame_15.setMaximumSize(QSize(280, 230))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_15)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_open_finalizar_venda = QPushButton(self.frame_15)
        self.btn_open_finalizar_venda.setObjectName(u"btn_open_finalizar_venda")
        self.btn_open_finalizar_venda.setMaximumSize(QSize(125, 25))
        self.btn_open_finalizar_venda.setStyleSheet(u"\n"
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
        self.btn_open_finalizar_venda.setIconSize(QSize(20, 20))

        self.horizontalLayout_16.addWidget(self.btn_open_finalizar_venda)

        self.btn_open_cancelar_venda = QPushButton(self.frame_15)
        self.btn_open_cancelar_venda.setObjectName(u"btn_open_cancelar_venda")
        self.btn_open_cancelar_venda.setMaximumSize(QSize(125, 25))
        self.btn_open_cancelar_venda.setStyleSheet(u"\n"
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
        self.btn_open_cancelar_venda.setIconSize(QSize(20, 20))

        self.horizontalLayout_16.addWidget(self.btn_open_cancelar_venda)


        self.gridLayout_2.addLayout(self.horizontalLayout_16, 9, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.btn_abrir_caixa = QPushButton(self.frame_15)
        self.btn_abrir_caixa.setObjectName(u"btn_abrir_caixa")
        self.btn_abrir_caixa.setMaximumSize(QSize(125, 25))
        self.btn_abrir_caixa.setStyleSheet(u"\n"
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

        self.horizontalLayout_21.addWidget(self.btn_abrir_caixa)

        self.btn_fechar_caixa = QPushButton(self.frame_15)
        self.btn_fechar_caixa.setObjectName(u"btn_fechar_caixa")
        self.btn_fechar_caixa.setMaximumSize(QSize(125, 25))
        self.btn_fechar_caixa.setStyleSheet(u"\n"
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

        self.horizontalLayout_21.addWidget(self.btn_fechar_caixa)


        self.gridLayout_2.addLayout(self.horizontalLayout_21, 5, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_nfe = QPushButton(self.frame_15)
        self.btn_nfe.setObjectName(u"btn_nfe")
        self.btn_nfe.setMinimumSize(QSize(0, 22))
        self.btn_nfe.setMaximumSize(QSize(16777215, 25))
        self.btn_nfe.setStyleSheet(u"\n"
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

        self.horizontalLayout_18.addWidget(self.btn_nfe)

        self.btn_valor_avuso = QPushButton(self.frame_15)
        self.btn_valor_avuso.setObjectName(u"btn_valor_avuso")
        self.btn_valor_avuso.setMaximumSize(QSize(125, 25))
        self.btn_valor_avuso.setStyleSheet(u"\n"
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

        self.horizontalLayout_18.addWidget(self.btn_valor_avuso)


        self.gridLayout_2.addLayout(self.horizontalLayout_18, 8, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.btn_open_saida = QPushButton(self.frame_15)
        self.btn_open_saida.setObjectName(u"btn_open_saida")
        self.btn_open_saida.setMaximumSize(QSize(125, 25))
        self.btn_open_saida.setStyleSheet(u"\n"
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

        self.horizontalLayout_17.addWidget(self.btn_open_saida)

        self.btn_multiplicar_pdv = QPushButton(self.frame_15)
        self.btn_multiplicar_pdv.setObjectName(u"btn_multiplicar_pdv")
        self.btn_multiplicar_pdv.setMaximumSize(QSize(125, 25))
        self.btn_multiplicar_pdv.setStyleSheet(u"\n"
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
        self.btn_multiplicar_pdv.setIconSize(QSize(20, 20))

        self.horizontalLayout_17.addWidget(self.btn_multiplicar_pdv)


        self.gridLayout_2.addLayout(self.horizontalLayout_17, 6, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.btn_open_excluir_item = QPushButton(self.frame_15)
        self.btn_open_excluir_item.setObjectName(u"btn_open_excluir_item")
        self.btn_open_excluir_item.setMaximumSize(QSize(125, 25))
        self.btn_open_excluir_item.setStyleSheet(u"\n"
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
        self.btn_open_excluir_item.setIconSize(QSize(20, 20))

        self.horizontalLayout_19.addWidget(self.btn_open_excluir_item)

        self.btn_calc_pdv = QPushButton(self.frame_15)
        self.btn_calc_pdv.setObjectName(u"btn_calc_pdv")
        self.btn_calc_pdv.setMaximumSize(QSize(125, 25))
        self.btn_calc_pdv.setStyleSheet(u"\n"
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
        self.btn_calc_pdv.setIconSize(QSize(20, 20))

        self.horizontalLayout_19.addWidget(self.btn_calc_pdv)


        self.gridLayout_2.addLayout(self.horizontalLayout_19, 7, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_15, 2, 1, 1, 2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 80))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_2)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(38, 16777215))
        self.label_11.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_20.addWidget(self.label_11)

        self.label_hora = QLabel(self.frame_2)
        self.label_hora.setObjectName(u"label_hora")
        self.label_hora.setStyleSheet(u"background: transparent;\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_hora.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_hora)


        self.gridLayout_18.addLayout(self.horizontalLayout_20, 0, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_2.addWidget(self.label_24)

        self.label_data = QLabel(self.frame_2)
        self.label_data.setObjectName(u"label_data")
        self.label_data.setStyleSheet(u"background: transparent;\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_data.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_data)


        self.gridLayout_18.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)

        self.label_print_default = QLabel(self.frame_2)
        self.label_print_default.setObjectName(u"label_print_default")
        self.label_print_default.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_18.addWidget(self.label_print_default, 2, 0, 1, 3)

        self.label_dias_restantes = QLabel(self.frame_2)
        self.label_dias_restantes.setObjectName(u"label_dias_restantes")
        self.label_dias_restantes.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_18.addWidget(self.label_dias_restantes, 1, 2, 1, 1)

        self.label_operador = QLabel(self.frame_2)
        self.label_operador.setObjectName(u"label_operador")
        self.label_operador.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_operador.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_18.addWidget(self.label_operador, 1, 0, 1, 2)


        self.gridLayout_26.addWidget(self.frame_2, 3, 1, 1, 2)


        self.gridLayout_7.addWidget(self.frame, 0, 0, 1, 1)

        icon4 = QIcon()
        icon4.addFile(u":/new/img/img (86).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabPrincipal.addTab(self.widget_1, icon4, "")
        self.widget_4 = QWidget()
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_13 = QGridLayout(self.widget_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_5 = QFrame(self.widget_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background: transparent;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_5)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 25))
        self.label_6.setStyleSheet(u"background: transparent;\n"
"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 150))
        self.frame_3.setStyleSheet(u"/* Estilo do QFrame com bordas redondas */\n"
"QFrame {\n"
"    border-radius: 8px; /* Ajuste o valor para controlar a curvatura das bordas */\n"
"   /* background-color: rgb(87, 133, 206); /* Cor de fundo do QFrame */\n"
"    border: 1px solid #B0E0E6; /* Cor da borda e largura da borda */\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.splitter_3 = QSplitter(self.frame_3)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.comboBox_tipo_produto = QComboBox(self.splitter_3)
        self.comboBox_tipo_produto.setObjectName(u"comboBox_tipo_produto")
        self.comboBox_tipo_produto.setMaximumSize(QSize(265, 25))
        self.comboBox_tipo_produto.setStyleSheet(u"QComboBox {\n"
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
"")
        self.comboBox_tipo_produto.setDuplicatesEnabled(False)
        self.splitter_3.addWidget(self.comboBox_tipo_produto)
        self.txt_pesquisa_prod = QLineEdit(self.splitter_3)
        self.txt_pesquisa_prod.setObjectName(u"txt_pesquisa_prod")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        self.txt_pesquisa_prod.setFont(font3)
        self.txt_pesquisa_prod.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: bold 12pt \"Segoe UI\";\n"
"border-radius:5px\n"
"")
        self.splitter_3.addWidget(self.txt_pesquisa_prod)

        self.gridLayout_6.addWidget(self.splitter_3, 2, 0, 1, 1)

        self.splitter_2 = QSplitter(self.frame_3)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.txt_codigo_prod = QLineEdit(self.splitter_2)
        self.txt_codigo_prod.setObjectName(u"txt_codigo_prod")
        self.txt_codigo_prod.setMaximumSize(QSize(425, 30))
        self.txt_codigo_prod.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 8px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.txt_codigo_prod.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter_2.addWidget(self.txt_codigo_prod)
        self.txt_nome_prod = QLineEdit(self.splitter_2)
        self.txt_nome_prod.setObjectName(u"txt_nome_prod")
        self.txt_nome_prod.setMaximumSize(QSize(16777215, 30))
        self.txt_nome_prod.setFont(font3)
        self.txt_nome_prod.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 8px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.txt_nome_prod.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter_2.addWidget(self.txt_nome_prod)
        self.txt_des_prod = QLineEdit(self.splitter_2)
        self.txt_des_prod.setObjectName(u"txt_des_prod")
        self.txt_des_prod.setMaximumSize(QSize(16777215, 30))
        self.txt_des_prod.setFont(font3)
        self.txt_des_prod.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 8px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.txt_des_prod.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter_2.addWidget(self.txt_des_prod)

        self.gridLayout_6.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.splitter = QSplitter(self.frame_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.txt_valor_prod = QLineEdit(self.splitter)
        self.txt_valor_prod.setObjectName(u"txt_valor_prod")
        self.txt_valor_prod.setMaximumSize(QSize(16777215, 30))
        self.txt_valor_prod.setFont(font3)
        self.txt_valor_prod.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 8px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.txt_valor_prod.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.txt_valor_prod)
        self.txt_qtd_prod = QLineEdit(self.splitter)
        self.txt_qtd_prod.setObjectName(u"txt_qtd_prod")
        self.txt_qtd_prod.setMaximumSize(QSize(16777215, 30))
        self.txt_qtd_prod.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 8px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.txt_qtd_prod.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.txt_qtd_prod)
        self.comboBox_uni_pcto = QComboBox(self.splitter)
        self.comboBox_uni_pcto.addItem("")
        self.comboBox_uni_pcto.addItem("")
        self.comboBox_uni_pcto.addItem("")
        self.comboBox_uni_pcto.addItem("")
        self.comboBox_uni_pcto.addItem("")
        self.comboBox_uni_pcto.setObjectName(u"comboBox_uni_pcto")
        self.comboBox_uni_pcto.setStyleSheet(u"QComboBox {\n"
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
"")
        self.splitter.addWidget(self.comboBox_uni_pcto)
        self.txt_valor_compra = QLineEdit(self.splitter)
        self.txt_valor_compra.setObjectName(u"txt_valor_compra")
        self.txt_valor_compra.setMaximumSize(QSize(16777215, 30))
        self.txt_valor_compra.setFont(font3)
        self.txt_valor_compra.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"    color: rgb(0, 0, 0); /* Define a cor da fonte como preta */\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 8px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.txt_valor_compra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.txt_valor_compra)

        self.gridLayout_6.addWidget(self.splitter, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.frame_22 = QFrame(self.frame_5)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"/* Estilo do QFrame com bordas redondas */\n"
"QFrame {\n"
"    border-radius: 8px; /* Ajuste o valor para controlar a curvatura das bordas */\n"
"   /* background-color: rgb(87, 133, 206); /* Cor de fundo do QFrame */\n"
"    border: 1px solid #B0E0E6; /* Cor da borda e largura da borda */\n"
"}\n"
"")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_22)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_excluir_prod = QPushButton(self.frame_22)
        self.btn_excluir_prod.setObjectName(u"btn_excluir_prod")
        self.btn_excluir_prod.setMinimumSize(QSize(90, 30))
        self.btn_excluir_prod.setMaximumSize(QSize(90, 30))
        self.btn_excluir_prod.setStyleSheet(u"    QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.btn_excluir_prod, 3, 0, 1, 1)

        self.radioButton_excluir_todos = QRadioButton(self.frame_22)
        self.radioButton_excluir_todos.setObjectName(u"radioButton_excluir_todos")
        self.radioButton_excluir_todos.setStyleSheet(u"QRadioButton {\n"
"	background: transparent;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.radioButton_excluir_todos, 4, 0, 1, 1)

        self.btn_editar_produtos = QPushButton(self.frame_22)
        self.btn_editar_produtos.setObjectName(u"btn_editar_produtos")
        self.btn_editar_produtos.setMinimumSize(QSize(90, 30))
        self.btn_editar_produtos.setMaximumSize(QSize(90, 30))
        self.btn_editar_produtos.setStyleSheet(u"    QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.btn_editar_produtos, 2, 0, 1, 1)

        self.btn_cadastrar_prod = QPushButton(self.frame_22)
        self.btn_cadastrar_prod.setObjectName(u"btn_cadastrar_prod")
        self.btn_cadastrar_prod.setMinimumSize(QSize(90, 30))
        self.btn_cadastrar_prod.setMaximumSize(QSize(90, 30))
        self.btn_cadastrar_prod.setStyleSheet(u"    QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.btn_cadastrar_prod, 0, 0, 1, 1)

        self.btn_atualizar_estoque = QPushButton(self.frame_22)
        self.btn_atualizar_estoque.setObjectName(u"btn_atualizar_estoque")
        self.btn_atualizar_estoque.setMinimumSize(QSize(90, 30))
        self.btn_atualizar_estoque.setMaximumSize(QSize(90, 30))
        self.btn_atualizar_estoque.setStyleSheet(u"    QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.btn_atualizar_estoque, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_22)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.tableView_estoque = QTableView(self.frame_5)
        self.tableView_estoque.setObjectName(u"tableView_estoque")

        self.verticalLayout_5.addWidget(self.tableView_estoque)


        self.gridLayout_19.addLayout(self.verticalLayout_5, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_5, 0, 0, 1, 1)

        icon5 = QIcon()
        icon5.addFile(u":/new/img/img (43).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabPrincipal.addTab(self.widget_4, icon5, "")
        self.widget_5 = QWidget()
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_28 = QGridLayout(self.widget_5)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.frame_6 = QFrame(self.widget_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_6)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.tabWidget = QTabWidget(self.frame_6)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabBar::tab {\n"
"background-color: rgb(80, 81, 82);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Arial\";\n"
" border-radius: 4px;\n"
" min-width: 100px;\n"
" padding: 1px;\n"
"                         }\n"
"\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(100, 149, 237);\n"
"	border-color: rgb(80, 81, 82);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"                         ")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_15 = QGridLayout(self.tab)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 25))
        self.label_9.setMaximumSize(QSize(16777215, 25))
        self.label_9.setStyleSheet(u"background: transparent;\n"
"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_15.addWidget(self.label_9, 0, 0, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.frame_9 = QFrame(self.tab)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(850, 120))
        self.frame_9.setMaximumSize(QSize(850, 120))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_9)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.groupBox_7 = QGroupBox(self.frame_9)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMaximumSize(QSize(260, 60))
        self.groupBox_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.checkBox_saidas = QCheckBox(self.groupBox_7)
        self.checkBox_saidas.setObjectName(u"checkBox_saidas")
        self.checkBox_saidas.setGeometry(QRect(90, 31, 58, 17))
        self.checkBox_saidas.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Segoe UI\";")
        self.checkBox_entradas = QCheckBox(self.groupBox_7)
        self.checkBox_entradas.setObjectName(u"checkBox_entradas")
        self.checkBox_entradas.setGeometry(QRect(12, 31, 72, 17))
        self.checkBox_entradas.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Segoe UI\";")
        self.radioButton_tudo = QRadioButton(self.groupBox_7)
        self.radioButton_tudo.setObjectName(u"radioButton_tudo")
        self.radioButton_tudo.setGeometry(QRect(154, 31, 94, 17))
        self.radioButton_tudo.setMaximumSize(QSize(110, 16777215))
        self.radioButton_tudo.setStyleSheet(u"QRadioButton {\n"
"	background: transparent;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_24.addWidget(self.groupBox_7, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.frame_9)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(175, 107))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_4)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.btn_atualizar_receitas = QPushButton(self.frame_4)
        self.btn_atualizar_receitas.setObjectName(u"btn_atualizar_receitas")
        self.btn_atualizar_receitas.setStyleSheet(u"    QPushButton {\n"
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

        self.gridLayout_14.addWidget(self.btn_atualizar_receitas, 0, 0, 1, 1)

        self.btn_relatorio_geral = QPushButton(self.frame_4)
        self.btn_relatorio_geral.setObjectName(u"btn_relatorio_geral")
        self.btn_relatorio_geral.setStyleSheet(u"    QPushButton {\n"
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

        self.gridLayout_14.addWidget(self.btn_relatorio_geral, 1, 0, 1, 1)

        self.btn_clear_all = QPushButton(self.frame_4)
        self.btn_clear_all.setObjectName(u"btn_clear_all")
        self.btn_clear_all.setStyleSheet(u"    QPushButton {\n"
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

        self.gridLayout_14.addWidget(self.btn_clear_all, 2, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_4, 0, 2, 1, 1)

        self.groupBox_8 = QGroupBox(self.frame_9)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMaximumSize(QSize(390, 60))
        self.groupBox_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.gridLayout_22 = QGridLayout(self.groupBox_8)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.radioButton_c_credito = QRadioButton(self.groupBox_8)
        self.radioButton_c_credito.setObjectName(u"radioButton_c_credito")
        self.radioButton_c_credito.setMaximumSize(QSize(135, 23))
        self.radioButton_c_credito.setStyleSheet(u"QRadioButton {\n"
"	background: transparent;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_22.addWidget(self.radioButton_c_credito, 0, 0, 1, 1)

        self.radioButton_c_debito = QRadioButton(self.groupBox_8)
        self.radioButton_c_debito.setObjectName(u"radioButton_c_debito")
        self.radioButton_c_debito.setMaximumSize(QSize(131, 23))
        self.radioButton_c_debito.setStyleSheet(u"QRadioButton {\n"
"	background: transparent;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_22.addWidget(self.radioButton_c_debito, 0, 1, 1, 1)

        self.radioButton_dinheiro = QRadioButton(self.groupBox_8)
        self.radioButton_dinheiro.setObjectName(u"radioButton_dinheiro")
        self.radioButton_dinheiro.setMaximumSize(QSize(90, 23))
        self.radioButton_dinheiro.setStyleSheet(u"QRadioButton {\n"
"	background: transparent;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_22.addWidget(self.radioButton_dinheiro, 0, 2, 1, 1)

        self.radioButton_pix = QRadioButton(self.groupBox_8)
        self.radioButton_pix.setObjectName(u"radioButton_pix")
        self.radioButton_pix.setMaximumSize(QSize(50, 16777215))
        self.radioButton_pix.setStyleSheet(u"QRadioButton {\n"
"	background: transparent;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_22.addWidget(self.radioButton_pix, 0, 3, 1, 1)


        self.gridLayout_24.addWidget(self.groupBox_8, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_9, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.tableWidget_relatorio_entradas = QTableWidget(self.tab)
        if (self.tableWidget_relatorio_entradas.columnCount() < 5):
            self.tableWidget_relatorio_entradas.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_relatorio_entradas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_relatorio_entradas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_relatorio_entradas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_relatorio_entradas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_relatorio_entradas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_relatorio_entradas.setObjectName(u"tableWidget_relatorio_entradas")
        font4 = QFont()
        font4.setPointSize(9)
        self.tableWidget_relatorio_entradas.setFont(font4)

        self.gridLayout_15.addWidget(self.tableWidget_relatorio_entradas, 2, 0, 1, 3)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_27.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.frame_6, 0, 0, 1, 1)

        icon6 = QIcon()
        icon6.addFile(u":/new/img/img (51).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabPrincipal.addTab(self.widget_5, icon6, "")
        self.widget_6 = QWidget()
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setEnabled(True)
        self.gridLayout_11 = QGridLayout(self.widget_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.scrollArea = QScrollArea(self.widget_6)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 953, 642))
        self.gridLayout_20 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_8)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.groupBox_2 = QGroupBox(self.frame_8)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(340, 90))
        self.groupBox_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.gridLayout_23 = QGridLayout(self.groupBox_2)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.txt_caminho_logo_empresa = QLineEdit(self.groupBox_2)
        self.txt_caminho_logo_empresa.setObjectName(u"txt_caminho_logo_empresa")
        self.txt_caminho_logo_empresa.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 12px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.txt_caminho_logo_empresa)

        self.toolButton_logo_caminho = QToolButton(self.groupBox_2)
        self.toolButton_logo_caminho.setObjectName(u"toolButton_logo_caminho")
        self.toolButton_logo_caminho.setStyleSheet(u"    QToolButton {\n"
"        background-color: #394568;\n"
"        border: 2px solid #394568;\n"
"        border-radius: 10px;\n"
"        font: 700 10pt \"Segoe UI\";\n"
"		color: rgb(255, 255, 255);\n"
"    }\n"
"    QToolButton:hover {\n"
"        background-color: #44537c;\n"
"    }\n"
"    QToolButton:pressed {\n"
"        background-color: #2c3650;\n"
"    }\n"
"\n"
"")

        self.horizontalLayout_9.addWidget(self.toolButton_logo_caminho)

        self.btn_salvar_logo_empresa = QPushButton(self.groupBox_2)
        self.btn_salvar_logo_empresa.setObjectName(u"btn_salvar_logo_empresa")
        self.btn_salvar_logo_empresa.setMinimumSize(QSize(50, 0))
        self.btn_salvar_logo_empresa.setMaximumSize(QSize(50, 16777215))
        self.btn_salvar_logo_empresa.setStyleSheet(u"    QPushButton {\n"
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

        self.horizontalLayout_9.addWidget(self.btn_salvar_logo_empresa)


        self.gridLayout_23.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)


        self.gridLayout_30.addWidget(self.groupBox_2, 2, 2, 1, 1)

        self.groupBox_5 = QGroupBox(self.frame_8)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(340, 120))
        self.groupBox_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.gridLayout_17 = QGridLayout(self.groupBox_5)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(155, 30))
        self.label_2.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.comboBox_tipo_cupom = QComboBox(self.groupBox_5)
        self.comboBox_tipo_cupom.addItem("")
        self.comboBox_tipo_cupom.addItem("")
        self.comboBox_tipo_cupom.setObjectName(u"comboBox_tipo_cupom")
        self.comboBox_tipo_cupom.setMinimumSize(QSize(130, 0))
        self.comboBox_tipo_cupom.setMaximumSize(QSize(130, 25))
        self.comboBox_tipo_cupom.setStyleSheet(u"QComboBox {\n"
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
"")

        self.horizontalLayout_7.addWidget(self.comboBox_tipo_cupom)

        self.btn_salvar_tipo_cupom = QPushButton(self.groupBox_5)
        self.btn_salvar_tipo_cupom.setObjectName(u"btn_salvar_tipo_cupom")
        self.btn_salvar_tipo_cupom.setMinimumSize(QSize(65, 25))
        self.btn_salvar_tipo_cupom.setMaximumSize(QSize(65, 25))
        self.btn_salvar_tipo_cupom.setStyleSheet(u"    QPushButton {\n"
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

        self.horizontalLayout_7.addWidget(self.btn_salvar_tipo_cupom)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.gridLayout_17.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(155, 30))
        self.label_8.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.comboBox_fonte_cupom = QComboBox(self.groupBox_5)
        self.comboBox_fonte_cupom.addItem("")
        self.comboBox_fonte_cupom.addItem("")
        self.comboBox_fonte_cupom.addItem("")
        self.comboBox_fonte_cupom.addItem("")
        self.comboBox_fonte_cupom.addItem("")
        self.comboBox_fonte_cupom.addItem("")
        self.comboBox_fonte_cupom.addItem("")
        self.comboBox_fonte_cupom.addItem("")
        self.comboBox_fonte_cupom.addItem("")
        self.comboBox_fonte_cupom.addItem("")
        self.comboBox_fonte_cupom.setObjectName(u"comboBox_fonte_cupom")
        self.comboBox_fonte_cupom.setMinimumSize(QSize(80, 0))
        self.comboBox_fonte_cupom.setMaximumSize(QSize(80, 25))
        self.comboBox_fonte_cupom.setStyleSheet(u"QComboBox {\n"
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
"")

        self.horizontalLayout_8.addWidget(self.comboBox_fonte_cupom)

        self.btn_salvar_tipo_fonte_cupom = QPushButton(self.groupBox_5)
        self.btn_salvar_tipo_fonte_cupom.setObjectName(u"btn_salvar_tipo_fonte_cupom")
        self.btn_salvar_tipo_fonte_cupom.setMinimumSize(QSize(65, 25))
        self.btn_salvar_tipo_fonte_cupom.setMaximumSize(QSize(25, 30))
        self.btn_salvar_tipo_fonte_cupom.setStyleSheet(u"    QPushButton {\n"
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

        self.horizontalLayout_8.addWidget(self.btn_salvar_tipo_fonte_cupom)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.gridLayout_17.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)


        self.gridLayout_30.addWidget(self.groupBox_5, 1, 2, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame_8)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(590, 125))
        self.groupBox_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.radioButton_server = QRadioButton(self.groupBox_3)
        self.radioButton_server.setObjectName(u"radioButton_server")
        self.radioButton_server.setStyleSheet(u"QRadioButton {\n"
"	background: transparent;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.radioButton_server)

        self.txt_ip_servidor = QLineEdit(self.groupBox_3)
        self.txt_ip_servidor.setObjectName(u"txt_ip_servidor")
        self.txt_ip_servidor.setMinimumSize(QSize(272, 0))
        self.txt_ip_servidor.setMaximumSize(QSize(220, 16777215))
        self.txt_ip_servidor.setStyleSheet(u"QLineEdit {\n"
"   \n"
"	background-color: rgb(255, 255, 255);\n"
"    font: bold 10pt \"Segoe UI\";\n"
"    border-radius: 5px;\n"
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
"    border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.txt_ip_servidor)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_13)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.label_15)

        self.comboBox_porta_servidor = QComboBox(self.groupBox_3)
        self.comboBox_porta_servidor.addItem("")
        self.comboBox_porta_servidor.addItem("")
        self.comboBox_porta_servidor.addItem("")
        self.comboBox_porta_servidor.addItem("")
        self.comboBox_porta_servidor.addItem("")
        self.comboBox_porta_servidor.addItem("")
        self.comboBox_porta_servidor.addItem("")
        self.comboBox_porta_servidor.setObjectName(u"comboBox_porta_servidor")
        self.comboBox_porta_servidor.setMinimumSize(QSize(95, 25))
        self.comboBox_porta_servidor.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout_11.addWidget(self.comboBox_porta_servidor)

        self.btn_salvar_server = QPushButton(self.groupBox_3)
        self.btn_salvar_server.setObjectName(u"btn_salvar_server")
        self.btn_salvar_server.setMinimumSize(QSize(50, 25))
        self.btn_salvar_server.setMaximumSize(QSize(50, 25))
        self.btn_salvar_server.setStyleSheet(u"    QPushButton {\n"
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

        self.horizontalLayout_11.addWidget(self.btn_salvar_server)


        self.gridLayout.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.radioButton_client = QRadioButton(self.groupBox_3)
        self.radioButton_client.setObjectName(u"radioButton_client")
        self.radioButton_client.setStyleSheet(u"QRadioButton {\n"
"	background: transparent;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.radioButton_client)

        self.txt_ip_client = QLineEdit(self.groupBox_3)
        self.txt_ip_client.setObjectName(u"txt_ip_client")
        self.txt_ip_client.setMinimumSize(QSize(272, 0))
        self.txt_ip_client.setMaximumSize(QSize(220, 16777215))
        self.txt_ip_client.setStyleSheet(u"QLineEdit {\n"
"   \n"
"	background-color: rgb(255, 255, 255);\n"
"    font: bold 10pt \"Segoe UI\";\n"
"    border-radius: 5px;\n"
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
"    border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.txt_ip_client)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_12)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_15.addWidget(self.label_16)

        self.txt_porta_client = QLineEdit(self.groupBox_3)
        self.txt_porta_client.setObjectName(u"txt_porta_client")
        self.txt_porta_client.setMinimumSize(QSize(95, 0))
        self.txt_porta_client.setMaximumSize(QSize(95, 25))
        self.txt_porta_client.setStyleSheet(u"QLineEdit {\n"
"   \n"
"	background-color: rgb(255, 255, 255);\n"
"    font: bold 10pt \"Segoe UI\";\n"
"    border-radius: 5px;\n"
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
"    border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.txt_porta_client)

        self.btn_salvar_client = QPushButton(self.groupBox_3)
        self.btn_salvar_client.setObjectName(u"btn_salvar_client")
        self.btn_salvar_client.setMinimumSize(QSize(50, 25))
        self.btn_salvar_client.setMaximumSize(QSize(50, 25))
        self.btn_salvar_client.setStyleSheet(u"    QPushButton {\n"
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

        self.horizontalLayout_15.addWidget(self.btn_salvar_client)


        self.gridLayout.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)

        self.label_status_server = QLabel(self.groupBox_3)
        self.label_status_server.setObjectName(u"label_status_server")
        self.label_status_server.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.label_status_server.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_status_server, 2, 0, 1, 1)


        self.gridLayout_30.addWidget(self.groupBox_3, 3, 0, 1, 1)

        self.groupBox = QGroupBox(self.frame_8)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(590, 375))
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.gridLayout_9 = QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_51 = QLabel(self.groupBox)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_32.addWidget(self.label_51)

        self.txt_info_empresa_razao_social = QLineEdit(self.groupBox)
        self.txt_info_empresa_razao_social.setObjectName(u"txt_info_empresa_razao_social")
        self.txt_info_empresa_razao_social.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 12px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_32.addWidget(self.txt_info_empresa_razao_social)


        self.gridLayout_9.addLayout(self.horizontalLayout_32, 0, 0, 1, 2)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_53 = QLabel(self.groupBox)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_34.addWidget(self.label_53)

        self.txt_info_empresa_cnpj = QLineEdit(self.groupBox)
        self.txt_info_empresa_cnpj.setObjectName(u"txt_info_empresa_cnpj")
        self.txt_info_empresa_cnpj.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 12px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_34.addWidget(self.txt_info_empresa_cnpj)

        self.label_54 = QLabel(self.groupBox)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_34.addWidget(self.label_54)

        self.txt_info_empresa_ie = QLineEdit(self.groupBox)
        self.txt_info_empresa_ie.setObjectName(u"txt_info_empresa_ie")
        self.txt_info_empresa_ie.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 12px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_34.addWidget(self.txt_info_empresa_ie)


        self.gridLayout_9.addLayout(self.horizontalLayout_34, 1, 0, 1, 2)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_55 = QLabel(self.groupBox)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_26.addWidget(self.label_55)

        self.txt_info_empresa_telefone = QLineEdit(self.groupBox)
        self.txt_info_empresa_telefone.setObjectName(u"txt_info_empresa_telefone")
        self.txt_info_empresa_telefone.setMaximumSize(QSize(140, 16777215))
        self.txt_info_empresa_telefone.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 12px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_26.addWidget(self.txt_info_empresa_telefone)

        self.label_58 = QLabel(self.groupBox)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_26.addWidget(self.label_58)

        self.txt_info_empresa_cidade = QLineEdit(self.groupBox)
        self.txt_info_empresa_cidade.setObjectName(u"txt_info_empresa_cidade")
        self.txt_info_empresa_cidade.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 12px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_26.addWidget(self.txt_info_empresa_cidade)


        self.gridLayout_9.addLayout(self.horizontalLayout_26, 2, 0, 1, 2)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_52 = QLabel(self.groupBox)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_33.addWidget(self.label_52)

        self.txt_info_empresa_endereco = QLineEdit(self.groupBox)
        self.txt_info_empresa_endereco.setObjectName(u"txt_info_empresa_endereco")
        self.txt_info_empresa_endereco.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 12px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_33.addWidget(self.txt_info_empresa_endereco)


        self.gridLayout_9.addLayout(self.horizontalLayout_33, 3, 0, 1, 2)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_57 = QLabel(self.groupBox)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_37.addWidget(self.label_57)

        self.txt_info_empresa_email = QLineEdit(self.groupBox)
        self.txt_info_empresa_email.setObjectName(u"txt_info_empresa_email")
        self.txt_info_empresa_email.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 12px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_37.addWidget(self.txt_info_empresa_email)


        self.gridLayout_9.addLayout(self.horizontalLayout_37, 4, 0, 1, 2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout_8.addWidget(self.label_4)

        self.cb_segment = QComboBox(self.groupBox)
        self.cb_segment.addItem("")
        self.cb_segment.addItem("")
        self.cb_segment.addItem("")
        self.cb_segment.addItem("")
        self.cb_segment.addItem("")
        self.cb_segment.addItem("")
        self.cb_segment.addItem("")
        self.cb_segment.addItem("")
        self.cb_segment.addItem("")
        self.cb_segment.setObjectName(u"cb_segment")
        self.cb_segment.setMinimumSize(QSize(0, 25))
        self.cb_segment.setMaximumSize(QSize(250, 25))
        self.cb_segment.setStyleSheet(u"QComboBox {\n"
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
"")
        self.cb_segment.setEditable(True)

        self.verticalLayout_8.addWidget(self.cb_segment)


        self.gridLayout_9.addLayout(self.verticalLayout_8, 5, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.label_5)

        self.cb_tipo_prod_serv = QComboBox(self.groupBox)
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.addItem("")
        self.cb_tipo_prod_serv.setObjectName(u"cb_tipo_prod_serv")
        self.cb_tipo_prod_serv.setMinimumSize(QSize(0, 25))
        self.cb_tipo_prod_serv.setMaximumSize(QSize(300, 25))
        self.cb_tipo_prod_serv.setStyleSheet(u"QComboBox {\n"
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
"")
        self.cb_tipo_prod_serv.setEditable(True)

        self.verticalLayout_7.addWidget(self.cb_tipo_prod_serv)


        self.gridLayout_9.addLayout(self.verticalLayout_7, 6, 0, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_13)

        self.btn_salvar_info_empresa = QPushButton(self.groupBox)
        self.btn_salvar_info_empresa.setObjectName(u"btn_salvar_info_empresa")
        self.btn_salvar_info_empresa.setMaximumSize(QSize(93, 25))
        self.btn_salvar_info_empresa.setStyleSheet(u"    QPushButton {\n"
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
        icon7 = QIcon()
        icon7.addFile(u":/new/img/0 (81).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_salvar_info_empresa.setIcon(icon7)

        self.horizontalLayout_27.addWidget(self.btn_salvar_info_empresa)

        self.btn_delete_info_empresa = QPushButton(self.groupBox)
        self.btn_delete_info_empresa.setObjectName(u"btn_delete_info_empresa")
        self.btn_delete_info_empresa.setMaximumSize(QSize(100, 25))
        self.btn_delete_info_empresa.setStyleSheet(u"    QPushButton {\n"
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
        icon8 = QIcon()
        icon8.addFile(u":/new/img/0 (35).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete_info_empresa.setIcon(icon8)

        self.horizontalLayout_27.addWidget(self.btn_delete_info_empresa)

        self.btn_carrega_dados_empresa = QPushButton(self.groupBox)
        self.btn_carrega_dados_empresa.setObjectName(u"btn_carrega_dados_empresa")
        self.btn_carrega_dados_empresa.setMaximumSize(QSize(16777215, 25))
        self.btn_carrega_dados_empresa.setStyleSheet(u"    QPushButton {\n"
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
        icon9 = QIcon()
        icon9.addFile(u":/new/img/0 (21).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_carrega_dados_empresa.setIcon(icon9)

        self.horizontalLayout_27.addWidget(self.btn_carrega_dados_empresa)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_14)


        self.gridLayout_9.addLayout(self.horizontalLayout_27, 7, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_4 = QGridLayout(self.groupBox_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.plainTextEdit_info_empresa_rodape_cupom = QPlainTextEdit(self.groupBox_6)
        self.plainTextEdit_info_empresa_rodape_cupom.setObjectName(u"plainTextEdit_info_empresa_rodape_cupom")
        self.plainTextEdit_info_empresa_rodape_cupom.setMinimumSize(QSize(0, 75))
        self.plainTextEdit_info_empresa_rodape_cupom.setMaximumSize(QSize(16777215, 100))
        self.plainTextEdit_info_empresa_rodape_cupom.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(255, 255, 127);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px; /* Define um raio de borda de 5 pixels */\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: #ffffff;\n"
"    font: bold 12px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.plainTextEdit_info_empresa_rodape_cupom, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_6, 5, 1, 3, 1)


        self.gridLayout_30.addWidget(self.groupBox, 0, 0, 3, 2)

        self.groupBox_4 = QGroupBox(self.frame_8)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(340, 138))
        self.groupBox_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.gridLayout_10 = QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(93, 16777215))
        self.label_18.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_25.addWidget(self.label_18)

        self.txt_new_nome = QLineEdit(self.groupBox_4)
        self.txt_new_nome.setObjectName(u"txt_new_nome")
        self.txt_new_nome.setMinimumSize(QSize(200, 25))
        self.txt_new_nome.setStyleSheet(u"QLineEdit {\n"
"   \n"
"	background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px;\n"
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
"    font: bold 12px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_25.addWidget(self.txt_new_nome)


        self.gridLayout_10.addLayout(self.horizontalLayout_25, 0, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_21 = QLabel(self.groupBox_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_24.addWidget(self.label_21)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.txt_new_password = QLineEdit(self.groupBox_4)
        self.txt_new_password.setObjectName(u"txt_new_password")
        self.txt_new_password.setMinimumSize(QSize(200, 25))
        self.txt_new_password.setStyleSheet(u"QLineEdit {\n"
"   \n"
"	background-color: rgb(255, 255, 255);\n"
"    font: bold 12pt \"Segoe UI\";\n"
"    border-radius: 5px;\n"
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
"    font: bold 12px \"Segoe UI\";\n"
"    border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.txt_new_password)

        self.checkBox_show_pass = QCheckBox(self.groupBox_4)
        self.checkBox_show_pass.setObjectName(u"checkBox_show_pass")
        self.checkBox_show_pass.setMaximumSize(QSize(25, 19))
        self.checkBox_show_pass.setStyleSheet(u"QCheckBox {\n"
"  font-size: 16px;\n"
" \n"
"	color: rgb(0, 0, 0);\n"
" }\n"
" QCheckBox::indicator {\n"
" width: 15px;\n"
" height: 15px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	background-color: rgb(80, 81, 82);\n"
" border: 2px solid #000000;\n"
" }\n"
" QCheckBox::indicator:unchecked {\n"
"	background-color: #00aa00;\n"
" border: 2px solid ;\n"
"}")

        self.horizontalLayout_10.addWidget(self.checkBox_show_pass)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_10)


        self.gridLayout_10.addLayout(self.horizontalLayout_24, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_22 = QLabel(self.groupBox_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_22.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_22)

        self.comboBox_new_privilegio = QComboBox(self.groupBox_4)
        self.comboBox_new_privilegio.addItem("")
        self.comboBox_new_privilegio.addItem("")
        self.comboBox_new_privilegio.addItem("")
        self.comboBox_new_privilegio.setObjectName(u"comboBox_new_privilegio")
        self.comboBox_new_privilegio.setMinimumSize(QSize(175, 25))
        self.comboBox_new_privilegio.setMaximumSize(QSize(195, 25))
        self.comboBox_new_privilegio.setStyleSheet(u"QComboBox {\n"
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
"\n"
"")

        self.horizontalLayout_3.addWidget(self.comboBox_new_privilegio)

        self.btn_salvar_new_user = QPushButton(self.groupBox_4)
        self.btn_salvar_new_user.setObjectName(u"btn_salvar_new_user")
        self.btn_salvar_new_user.setMinimumSize(QSize(60, 25))
        self.btn_salvar_new_user.setMaximumSize(QSize(60, 25))
        self.btn_salvar_new_user.setStyleSheet(u"    QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.btn_salvar_new_user)


        self.gridLayout_10.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)


        self.gridLayout_30.addWidget(self.groupBox_4, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_30.addItem(self.verticalSpacer, 4, 0, 2, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 408, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_30.addItem(self.verticalSpacer_2, 5, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.groupBox_9 = QGroupBox(self.frame_8)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.gridLayout_16 = QGridLayout(self.groupBox_9)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_digite = QLabel(self.groupBox_9)
        self.label_digite.setObjectName(u"label_digite")
        self.label_digite.setMaximumSize(QSize(101, 16))

        self.gridLayout_16.addWidget(self.label_digite, 0, 0, 1, 1)

        self.txt_licenca = QLineEdit(self.groupBox_9)
        self.txt_licenca.setObjectName(u"txt_licenca")
        self.txt_licenca.setMinimumSize(QSize(0, 25))
        self.txt_licenca.setStyleSheet(u"QLineEdit {\n"
"   \n"
"	background-color: rgb(255, 255, 127);\n"
"    font: bold 10pt \"Segoe UI\";\n"
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
        self.txt_licenca.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.txt_licenca.setClearButtonEnabled(True)

        self.gridLayout_16.addWidget(self.txt_licenca, 1, 0, 1, 2)

        self.label_dias_expira = QLabel(self.groupBox_9)
        self.label_dias_expira.setObjectName(u"label_dias_expira")

        self.gridLayout_16.addWidget(self.label_dias_expira, 2, 0, 1, 1)

        self.btn_liberar_licenca = QPushButton(self.groupBox_9)
        self.btn_liberar_licenca.setObjectName(u"btn_liberar_licenca")
        self.btn_liberar_licenca.setMaximumSize(QSize(86, 24))
        self.btn_liberar_licenca.setStyleSheet(u"    QPushButton {\n"
"	background-color: rgb(0, 255, 127);\n"
"        border: 2px solid #394568;\n"
"        border-radius: 10px;\n"
"        font: 700 10pt \"Segoe UI\";\n"
"		color: rgb(0, 0, 0);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #44537c;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #2c3650;\n"
"    }\n"
"\n"
"")

        self.gridLayout_16.addWidget(self.btn_liberar_licenca, 2, 1, 1, 1)


        self.gridLayout_30.addWidget(self.groupBox_9, 3, 2, 1, 1)


        self.gridLayout_20.addWidget(self.frame_8, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_11.addWidget(self.scrollArea, 0, 0, 1, 1)

        icon10 = QIcon()
        icon10.addFile(u":/new/img/img (27).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabPrincipal.addTab(self.widget_6, icon10, "")

        self.gridLayout_8.addWidget(self.tabPrincipal, 0, 0, 1, 1)

        W_W_AUTO_COM_PDV.setCentralWidget(self.centralwidget1518)
        self.menu_janela = QMenuBar(W_W_AUTO_COM_PDV)
        self.menu_janela.setObjectName(u"menu_janela")
        self.menu_janela.setGeometry(QRect(0, 0, 993, 22))
        font5 = QFont()
        font5.setPointSize(10)
        self.menu_janela.setFont(font5)
        W_W_AUTO_COM_PDV.setMenuBar(self.menu_janela)
        QWidget.setTabOrder(self.txt_codigo_prod, self.txt_nome_prod)
        QWidget.setTabOrder(self.txt_nome_prod, self.txt_des_prod)
        QWidget.setTabOrder(self.txt_des_prod, self.txt_valor_prod)
        QWidget.setTabOrder(self.txt_valor_prod, self.txt_qtd_prod)
        QWidget.setTabOrder(self.txt_qtd_prod, self.comboBox_uni_pcto)
        QWidget.setTabOrder(self.comboBox_uni_pcto, self.txt_valor_compra)
        QWidget.setTabOrder(self.txt_valor_compra, self.comboBox_tipo_produto)
        QWidget.setTabOrder(self.comboBox_tipo_produto, self.txt_pesquisa_prod)
        QWidget.setTabOrder(self.txt_pesquisa_prod, self.btn_cadastrar_prod)
        QWidget.setTabOrder(self.btn_cadastrar_prod, self.btn_atualizar_estoque)
        QWidget.setTabOrder(self.btn_atualizar_estoque, self.btn_editar_produtos)
        QWidget.setTabOrder(self.btn_editar_produtos, self.btn_excluir_prod)
        QWidget.setTabOrder(self.btn_excluir_prod, self.radioButton_excluir_todos)
        QWidget.setTabOrder(self.radioButton_excluir_todos, self.radioButton_dinheiro)
        QWidget.setTabOrder(self.radioButton_dinheiro, self.radioButton_pix)
        QWidget.setTabOrder(self.radioButton_pix, self.btn_atualizar_receitas)
        QWidget.setTabOrder(self.btn_atualizar_receitas, self.cb_segment)
        QWidget.setTabOrder(self.cb_segment, self.cb_tipo_prod_serv)
        QWidget.setTabOrder(self.cb_tipo_prod_serv, self.txt_valor_total_pdv)
        QWidget.setTabOrder(self.txt_valor_total_pdv, self.tabPrincipal)
        QWidget.setTabOrder(self.tabPrincipal, self.tableView_estoque)
        QWidget.setTabOrder(self.tableView_estoque, self.tableView_pdv)
        QWidget.setTabOrder(self.tableView_pdv, self.radioButton_c_credito)
        QWidget.setTabOrder(self.radioButton_c_credito, self.radioButton_tudo)
        QWidget.setTabOrder(self.radioButton_tudo, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.radioButton_c_debito)
        QWidget.setTabOrder(self.radioButton_c_debito, self.txt_info_empresa_telefone)
        QWidget.setTabOrder(self.txt_info_empresa_telefone, self.btn_clear_all)
        QWidget.setTabOrder(self.btn_clear_all, self.txt_caminho_logo_empresa)
        QWidget.setTabOrder(self.txt_caminho_logo_empresa, self.toolButton_logo_caminho)
        QWidget.setTabOrder(self.toolButton_logo_caminho, self.btn_salvar_logo_empresa)
        QWidget.setTabOrder(self.btn_salvar_logo_empresa, self.txt_new_nome)
        QWidget.setTabOrder(self.txt_new_nome, self.txt_new_password)
        QWidget.setTabOrder(self.txt_new_password, self.checkBox_show_pass)
        QWidget.setTabOrder(self.checkBox_show_pass, self.comboBox_new_privilegio)
        QWidget.setTabOrder(self.comboBox_new_privilegio, self.btn_nfe)
        QWidget.setTabOrder(self.btn_nfe, self.btn_abrir_caixa)
        QWidget.setTabOrder(self.btn_abrir_caixa, self.btn_fechar_caixa)
        QWidget.setTabOrder(self.btn_fechar_caixa, self.btn_open_saida)
        QWidget.setTabOrder(self.btn_open_saida, self.btn_multiplicar_pdv)
        QWidget.setTabOrder(self.btn_multiplicar_pdv, self.btn_open_excluir_item)
        QWidget.setTabOrder(self.btn_open_excluir_item, self.btn_calc_pdv)
        QWidget.setTabOrder(self.btn_calc_pdv, self.btn_open_finalizar_venda)
        QWidget.setTabOrder(self.btn_open_finalizar_venda, self.btn_open_cancelar_venda)
        QWidget.setTabOrder(self.btn_open_cancelar_venda, self.txt_info_empresa_razao_social)
        QWidget.setTabOrder(self.txt_info_empresa_razao_social, self.txt_info_empresa_ie)
        QWidget.setTabOrder(self.txt_info_empresa_ie, self.txt_info_empresa_endereco)
        QWidget.setTabOrder(self.txt_info_empresa_endereco, self.txt_info_empresa_cidade)
        QWidget.setTabOrder(self.txt_info_empresa_cidade, self.btn_delete_info_empresa)
        QWidget.setTabOrder(self.btn_delete_info_empresa, self.txt_cod_pdv)
        QWidget.setTabOrder(self.txt_cod_pdv, self.txt_info_empresa_cnpj)
        QWidget.setTabOrder(self.txt_info_empresa_cnpj, self.txt_info_empresa_email)
        QWidget.setTabOrder(self.txt_info_empresa_email, self.btn_salvar_info_empresa)
        QWidget.setTabOrder(self.btn_salvar_info_empresa, self.btn_carrega_dados_empresa)
        QWidget.setTabOrder(self.btn_carrega_dados_empresa, self.plainTextEdit_info_empresa_rodape_cupom)
        QWidget.setTabOrder(self.plainTextEdit_info_empresa_rodape_cupom, self.comboBox_fonte_cupom)
        QWidget.setTabOrder(self.comboBox_fonte_cupom, self.btn_salvar_tipo_fonte_cupom)
        QWidget.setTabOrder(self.btn_salvar_tipo_fonte_cupom, self.comboBox_tipo_cupom)
        QWidget.setTabOrder(self.comboBox_tipo_cupom, self.btn_salvar_tipo_cupom)
        QWidget.setTabOrder(self.btn_salvar_tipo_cupom, self.radioButton_server)
        QWidget.setTabOrder(self.radioButton_server, self.txt_ip_servidor)
        QWidget.setTabOrder(self.txt_ip_servidor, self.comboBox_porta_servidor)
        QWidget.setTabOrder(self.comboBox_porta_servidor, self.btn_salvar_server)
        QWidget.setTabOrder(self.btn_salvar_server, self.radioButton_client)
        QWidget.setTabOrder(self.radioButton_client, self.txt_ip_client)
        QWidget.setTabOrder(self.txt_ip_client, self.txt_porta_client)
        QWidget.setTabOrder(self.txt_porta_client, self.btn_salvar_client)
        QWidget.setTabOrder(self.btn_salvar_client, self.btn_salvar_new_user)
        QWidget.setTabOrder(self.btn_salvar_new_user, self.btn_mais_qtde)
        QWidget.setTabOrder(self.btn_mais_qtde, self.txt_qtde)
        QWidget.setTabOrder(self.txt_qtde, self.btn_menos_qtde)
        QWidget.setTabOrder(self.btn_menos_qtde, self.btn_valor_avuso)
        QWidget.setTabOrder(self.btn_valor_avuso, self.checkBox_saidas)
        QWidget.setTabOrder(self.checkBox_saidas, self.checkBox_entradas)
        QWidget.setTabOrder(self.checkBox_entradas, self.btn_relatorio_geral)
        QWidget.setTabOrder(self.btn_relatorio_geral, self.tableWidget_relatorio_entradas)
        QWidget.setTabOrder(self.tableWidget_relatorio_entradas, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.txt_licenca)
        QWidget.setTabOrder(self.txt_licenca, self.btn_liberar_licenca)

        self.retranslateUi(W_W_AUTO_COM_PDV)

        self.tabPrincipal.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(W_W_AUTO_COM_PDV)
    # setupUi

    def retranslateUi(self, W_W_AUTO_COM_PDV):
        W_W_AUTO_COM_PDV.setWindowTitle(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"W&W Softwares", None))
        self.actionTrocar_User.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Trocar User", None))
        self.label.setText("")
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.widget00), QCoreApplication.translate("W_W_AUTO_COM_PDV", u"HOME", None))
        self.txt_cod_pdv.setPlaceholderText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"C\u00f3digo", None))
        self.label_20.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Qtde Un:", None))
        self.btn_mais_qtde.setText("")
        self.btn_menos_qtde.setText("")
        self.label_logo_empresa.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Logo empressa ", None))
        self.label_13.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Valor Total:", None))
#if QT_CONFIG(whatsthis)
        self.btn_open_finalizar_venda.setWhatsThis(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"<html><head/><body><p><img src=\":/new/img/img/COMFIRMAR.png\" /></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_open_finalizar_venda.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Finalizar Venda/F2", None))
#if QT_CONFIG(shortcut)
        self.btn_open_finalizar_venda.setShortcut(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_open_cancelar_venda.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Cancelar Venda/F3", None))
#if QT_CONFIG(shortcut)
        self.btn_open_cancelar_venda.setShortcut(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"F3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_abrir_caixa.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Abrir Caixa", None))
        self.btn_fechar_caixa.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Fechar Caixa", None))
        self.btn_nfe.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Pasta NFC-e", None))
        self.btn_valor_avuso.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Valor Avulso/F6", None))
        self.btn_open_saida.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Saidas/F4", None))
#if QT_CONFIG(shortcut)
        self.btn_open_saida.setShortcut(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"F4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_multiplicar_pdv.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Alterar Qtde/F5", None))
        self.btn_open_excluir_item.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Excluir Item/Del", None))
        self.btn_calc_pdv.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Calculadora", None))
        self.label_11.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Hora: ", None))
        self.label_hora.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"00:00:00", None))
        self.label_24.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Data: ", None))
        self.label_data.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"00/00/0000", None))
        self.label_print_default.setText("")
        self.label_dias_restantes.setText("")
        self.label_operador.setText("")
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.widget_1), QCoreApplication.translate("W_W_AUTO_COM_PDV", u"PDV", None))
        self.label_6.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Cadastrar Produtos", None))
        self.comboBox_tipo_produto.setCurrentText("")
        self.comboBox_tipo_produto.setPlaceholderText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Tipo de Produto", None))
#if QT_CONFIG(tooltip)
        self.txt_pesquisa_prod.setToolTip(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Adicione % + Texto da Pesquisa + % para Refinar a Pesquisa", None))
#endif // QT_CONFIG(tooltip)
        self.txt_pesquisa_prod.setText("")
        self.txt_pesquisa_prod.setPlaceholderText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Refinar Pesquisa", None))
        self.txt_codigo_prod.setPlaceholderText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Codigo de Barras", None))
#if QT_CONFIG(tooltip)
        self.txt_nome_prod.setToolTip(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Crie Um Nome com no Maximo 20 Letras", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.txt_nome_prod.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.txt_nome_prod.setPlaceholderText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Nome do Produto", None))
#if QT_CONFIG(tooltip)
        self.txt_des_prod.setToolTip(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Crie Uma Descri\u00e7\u00e3o com no Maximo 20 Letras", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.txt_des_prod.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.txt_des_prod.setPlaceholderText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Descri\u00e7\u00e3o do Produto", None))
        self.txt_valor_prod.setInputMask("")
        self.txt_valor_prod.setPlaceholderText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Valor da Venda", None))
        self.txt_qtd_prod.setPlaceholderText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Qtde de Produtos", None))
        self.comboBox_uni_pcto.setItemText(0, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"UNI", None))
        self.comboBox_uni_pcto.setItemText(1, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"PCTO", None))
        self.comboBox_uni_pcto.setItemText(2, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"KG", None))
        self.comboBox_uni_pcto.setItemText(3, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"DUZIA", None))
        self.comboBox_uni_pcto.setItemText(4, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"MEIA DUZIA", None))

        self.txt_valor_compra.setInputMask("")
        self.txt_valor_compra.setPlaceholderText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Valor da Compra", None))
        self.btn_excluir_prod.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Excluir", None))
        self.radioButton_excluir_todos.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Tudo", None))
        self.btn_editar_produtos.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Editar", None))
        self.btn_cadastrar_prod.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Cadrastrar", None))
        self.btn_atualizar_estoque.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Atualizar", None))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.widget_4), QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Estoque", None))
        self.label_9.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Receitas Entradas/Saidas", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Filtra por:", None))
        self.checkBox_saidas.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Saida", None))
        self.checkBox_entradas.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Entrada", None))
        self.radioButton_tudo.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Exibir Tudo", None))
        self.btn_atualizar_receitas.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Atualizar", None))
        self.btn_relatorio_geral.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Gerar Relat\u00f3rio Geral", None))
        self.btn_clear_all.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Clear All", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Tipo de Opera\u00e7\u00e3o:", None))
        self.radioButton_c_credito.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Cart\u00e3o Cr\u00e9dito", None))
        self.radioButton_c_debito.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Cart\u00e3o D\u00e9bito", None))
        self.radioButton_dinheiro.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Dinheiro", None))
        self.radioButton_pix.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Pix", None))
        ___qtablewidgetitem = self.tableWidget_relatorio_entradas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Tipo de Receita", None));
        ___qtablewidgetitem1 = self.tableWidget_relatorio_entradas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Forma de Pagamento", None));
        ___qtablewidgetitem2 = self.tableWidget_relatorio_entradas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Valor Recebido", None));
        ___qtablewidgetitem3 = self.tableWidget_relatorio_entradas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Data-Hora", None));
        ___qtablewidgetitem4 = self.tableWidget_relatorio_entradas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Descri\u00e7\u00e3o", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Relat\u00f3rios", None))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.widget_5), QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Financeiro", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Carregar Logo da Empresa", None))
        self.toolButton_logo_caminho.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"...", None))
        self.btn_salvar_logo_empresa.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"OK", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Configura\u00e7\u00f5es do Cupom", None))
        self.label_2.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Tipo de  Cupom", None))
        self.comboBox_tipo_cupom.setItemText(0, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"80mm", None))
        self.comboBox_tipo_cupom.setItemText(1, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"58mm", None))

        self.btn_salvar_tipo_cupom.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Salvar", None))
        self.label_8.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Fonte do Cupom", None))
        self.comboBox_fonte_cupom.setItemText(0, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"10", None))
        self.comboBox_fonte_cupom.setItemText(1, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"12", None))
        self.comboBox_fonte_cupom.setItemText(2, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"14", None))
        self.comboBox_fonte_cupom.setItemText(3, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"16", None))
        self.comboBox_fonte_cupom.setItemText(4, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"18", None))
        self.comboBox_fonte_cupom.setItemText(5, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"20", None))
        self.comboBox_fonte_cupom.setItemText(6, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"22", None))
        self.comboBox_fonte_cupom.setItemText(7, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"24", None))
        self.comboBox_fonte_cupom.setItemText(8, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"26", None))
        self.comboBox_fonte_cupom.setItemText(9, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"28", None))

        self.btn_salvar_tipo_fonte_cupom.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Salvar", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Acesso Remoto", None))
        self.radioButton_server.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Server", None))
        self.label_15.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Port", None))
        self.comboBox_porta_servidor.setItemText(0, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"5000", None))
        self.comboBox_porta_servidor.setItemText(1, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"6000", None))
        self.comboBox_porta_servidor.setItemText(2, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"6060", None))
        self.comboBox_porta_servidor.setItemText(3, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"7000", None))
        self.comboBox_porta_servidor.setItemText(4, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"7070", None))
        self.comboBox_porta_servidor.setItemText(5, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"8000", None))
        self.comboBox_porta_servidor.setItemText(6, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"8080", None))

        self.btn_salvar_server.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"OK", None))
        self.radioButton_client.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Client", None))
        self.label_16.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Port", None))
        self.btn_salvar_client.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"OK", None))
        self.label_status_server.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Informa\u00e7\u00f5es da Empresa", None))
        self.label_51.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Raz\u00e3o Social:", None))
        self.label_53.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"CNPJ:", None))
        self.label_54.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"IE:", None))
        self.label_55.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Telefone:", None))
        self.label_58.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Cidade:", None))
        self.label_52.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Endere\u00e7o:", None))
        self.label_57.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Email:", None))
        self.label_4.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Empresa do Segmento", None))
        self.cb_segment.setItemText(0, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Alimenta\u00e7\u00e3o", None))
        self.cb_segment.setItemText(1, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Beleza e Est\u00e9tica", None))
        self.cb_segment.setItemText(2, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Higiene pessoal", None))
        self.cb_segment.setItemText(3, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Materias para Constru\u00e7\u00e3o Civil", None))
        self.cb_segment.setItemText(4, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Materiais de Limpeza", None))
        self.cb_segment.setItemText(5, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Moda e Vestu\u00e1rio", None))
        self.cb_segment.setItemText(6, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Lar e Decora\u00e7\u00e3o", None))
        self.cb_segment.setItemText(7, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Tecnologia e Inform\u00e1tica", None))
        self.cb_segment.setItemText(8, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Manuten\u00e7\u00e3o", None))

        self.cb_segment.setCurrentText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Alimenta\u00e7\u00e3o", None))
        self.label_5.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Venda especializada:", None))
        self.cb_tipo_prod_serv.setItemText(0, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Alimentos Congelados", None))
        self.cb_tipo_prod_serv.setItemText(1, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Alimentos N\u00e3o Perec\u00edveis/Enlatados", None))
        self.cb_tipo_prod_serv.setItemText(2, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Alimentos Perec\u00edveis/Embalados", None))
        self.cb_tipo_prod_serv.setItemText(3, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Bebidas", None))
        self.cb_tipo_prod_serv.setItemText(4, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Ferragens E Materiais De Constru\u00e7\u00e3o", None))
        self.cb_tipo_prod_serv.setItemText(5, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Hortifr\u00fati E Carnes", None))
        self.cb_tipo_prod_serv.setItemText(6, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Pe\u00e7as de Motos e Carros", None))
        self.cb_tipo_prod_serv.setItemText(7, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Produtos De Higiene Pessoal", None))
        self.cb_tipo_prod_serv.setItemText(8, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Produtos De Limpeza", None))
        self.cb_tipo_prod_serv.setItemText(9, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Produtos Para Pets", None))
        self.cb_tipo_prod_serv.setItemText(10, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Roupas, Cal\u00e7ados E Acess\u00f3rios", None))
        self.cb_tipo_prod_serv.setItemText(11, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Sal\u00e3o De Beleza, Est\u00e9tica E Spa", None))
        self.cb_tipo_prod_serv.setItemText(12, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Sv\u00e7/Manuten\u00e7\u00e3o Celular E Tablet", None))
        self.cb_tipo_prod_serv.setItemText(13, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Sv\u00e7/Manuten\u00e7\u00e3o de Ar Cond. e Vent", None))
        self.cb_tipo_prod_serv.setItemText(14, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Sv\u00e7/Mec\u00e2nico de Carro", None))
        self.cb_tipo_prod_serv.setItemText(15, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Sv\u00e7/Mec\u00e2nico de Moto", None))
        self.cb_tipo_prod_serv.setItemText(16, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Vidra\u00e7aria, Marmoraria E Carpintaria", None))
        self.cb_tipo_prod_serv.setItemText(17, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Outros", None))

        self.cb_tipo_prod_serv.setCurrentText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Alimentos Congelados", None))
        self.btn_salvar_info_empresa.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Salvar", None))
        self.btn_delete_info_empresa.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Deletar", None))
        self.btn_carrega_dados_empresa.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Exibir Dados", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Rodape Cupom Fiscal:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Adicionar Usu\u00e1rios", None))
        self.label_18.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Novo usu\u00e1rio:", None))
        self.label_21.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Password:", None))
        self.checkBox_show_pass.setText("")
        self.label_22.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Privil\u00e9gio:", None))
        self.comboBox_new_privilegio.setItemText(0, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Comum", None))
        self.comboBox_new_privilegio.setItemText(1, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Gerente", None))
        self.comboBox_new_privilegio.setItemText(2, QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Administrador", None))

        self.btn_salvar_new_user.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"OK", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Licen\u00e7a", None))
        self.label_digite.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Digite a Licen\u00e7a:", None))
        self.label_dias_expira.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", None))
        self.btn_liberar_licenca.setText(QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Liberar", None))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.widget_6), QCoreApplication.translate("W_W_AUTO_COM_PDV", u"Configura\u00e7\u00f5es", None))
    # retranslateUi

