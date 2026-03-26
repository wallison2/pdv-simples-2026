# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuracoes.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QToolBox, QToolButton, QVBoxLayout,
    QWidget)
import Resource_rc

class Ui_Configuracoes(object):
    def setupUi(self, Configuracoes):
        if not Configuracoes.objectName():
            Configuracoes.setObjectName(u"Configuracoes")
        Configuracoes.resize(695, 665)
        Configuracoes.setMinimumSize(QSize(695, 665))
        Configuracoes.setMaximumSize(QSize(695, 665))
        icon = QIcon()
        icon.addFile(u":/new/img/img (27).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Configuracoes.setWindowIcon(icon)
        Configuracoes.setStyleSheet(u"background-color: rgb(15, 195, 254);")
        self.gridLayout = QGridLayout(Configuracoes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Configuracoes)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.toolBox_config = QToolBox(self.frame)
        self.toolBox_config.setObjectName(u"toolBox_config")
        self.toolBox_config.setStyleSheet(u"QToolBox::tab {\n"
"    background: #DCDCDC;\n"
"    border: 2px solid #888;\n"
"    padding: 2px 6px; /* Top/Bottom: 4px | Left/Right: 8px */\n"
"    font: bold 10pt \"Segoe UI\";\n"
"    color: #333;\n"
"    border-radius: 10px;\n"
"    min-height: 30px;  /* Altura m\u00ednima ajustada */\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"    background: #A9D0F5;\n"
"    color: #000;\n"
"    font: bold 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"    background: #BDBDBD;\n"
"}\n"
"")
        self.page_config_empresa = QWidget()
        self.page_config_empresa.setObjectName(u"page_config_empresa")
        self.page_config_empresa.setGeometry(QRect(0, 0, 651, 435))
        self.gridLayout_2 = QGridLayout(self.page_config_empresa)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_13 = QFrame(self.page_config_empresa)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(650, 430))
        self.frame_13.setStyleSheet(u"QFrame {\n"
"    background-color: transparent;\n"
"    border: 2px solid #333333;\n"
"    border-radius: 5px;\n"
"   border-radius: 8px; /* Ajuste o valor para controlar a curvatura das bordas */\n"
"}\n"
"\n"
"QLabel, QLineEdit, QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_13)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_52 = QLabel(self.frame_13)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_33.addWidget(self.label_52)

        self.txt_info_empresa_endereco = QLineEdit(self.frame_13)
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


        self.gridLayout_9.addLayout(self.horizontalLayout_33, 5, 0, 1, 1)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_53 = QLabel(self.frame_13)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_34.addWidget(self.label_53)

        self.txt_info_empresa_cnpj = QLineEdit(self.frame_13)
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

        self.label_54 = QLabel(self.frame_13)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_34.addWidget(self.label_54)

        self.txt_info_empresa_ie = QLineEdit(self.frame_13)
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


        self.gridLayout_9.addLayout(self.horizontalLayout_34, 2, 0, 1, 1)

        self.label_40 = QLabel(self.frame_13)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(16777215, 20))
        self.label_40.setStyleSheet(u"background: transparent;\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.label_40, 0, 0, 1, 1)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_55 = QLabel(self.frame_13)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_35.addWidget(self.label_55)

        self.txt_info_empresa_telefone = QLineEdit(self.frame_13)
        self.txt_info_empresa_telefone.setObjectName(u"txt_info_empresa_telefone")
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

        self.horizontalLayout_35.addWidget(self.txt_info_empresa_telefone)


        self.gridLayout_9.addLayout(self.horizontalLayout_35, 4, 0, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_13)

        self.btn_salvar_info_empresa = QPushButton(self.frame_13)
        self.btn_salvar_info_empresa.setObjectName(u"btn_salvar_info_empresa")
        self.btn_salvar_info_empresa.setMaximumSize(QSize(93, 40))
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
        icon1 = QIcon()
        icon1.addFile(u":/new/img/0 (81).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_salvar_info_empresa.setIcon(icon1)

        self.horizontalLayout_27.addWidget(self.btn_salvar_info_empresa)

        self.btn_delete_info_empresa = QPushButton(self.frame_13)
        self.btn_delete_info_empresa.setObjectName(u"btn_delete_info_empresa")
        self.btn_delete_info_empresa.setMaximumSize(QSize(100, 30))
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
        icon2 = QIcon()
        icon2.addFile(u":/new/img/0 (35).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete_info_empresa.setIcon(icon2)

        self.horizontalLayout_27.addWidget(self.btn_delete_info_empresa)

        self.btn_carrega_dados_empresa = QPushButton(self.frame_13)
        self.btn_carrega_dados_empresa.setObjectName(u"btn_carrega_dados_empresa")
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
        icon3 = QIcon()
        icon3.addFile(u":/new/img/0 (21).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_carrega_dados_empresa.setIcon(icon3)

        self.horizontalLayout_27.addWidget(self.btn_carrega_dados_empresa)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_14)


        self.gridLayout_9.addLayout(self.horizontalLayout_27, 10, 0, 1, 1)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_56 = QLabel(self.frame_13)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(177, 67))
        self.label_56.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_36.addWidget(self.label_56)

        self.plainTextEdit_info_empresa_rodape_cupom = QPlainTextEdit(self.frame_13)
        self.plainTextEdit_info_empresa_rodape_cupom.setObjectName(u"plainTextEdit_info_empresa_rodape_cupom")
        self.plainTextEdit_info_empresa_rodape_cupom.setMaximumSize(QSize(16777215, 50))
        self.plainTextEdit_info_empresa_rodape_cupom.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_36.addWidget(self.plainTextEdit_info_empresa_rodape_cupom)


        self.gridLayout_9.addLayout(self.horizontalLayout_36, 7, 0, 1, 1)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_57 = QLabel(self.frame_13)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_37.addWidget(self.label_57)

        self.txt_info_empresa_email = QLineEdit(self.frame_13)
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


        self.gridLayout_9.addLayout(self.horizontalLayout_37, 6, 0, 1, 1)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_58 = QLabel(self.frame_13)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_38.addWidget(self.label_58)

        self.txt_info_empresa_cidade = QLineEdit(self.frame_13)
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

        self.horizontalLayout_38.addWidget(self.txt_info_empresa_cidade)


        self.gridLayout_9.addLayout(self.horizontalLayout_38, 3, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout_8.addWidget(self.label_4)

        self.cb_segment = QComboBox(self.frame_13)
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
        self.cb_segment.setEditable(True)

        self.verticalLayout_8.addWidget(self.cb_segment)


        self.horizontalLayout_14.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.frame_13)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.label_5)

        self.cb_tipo_prod_serv = QComboBox(self.frame_13)
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
        self.cb_tipo_prod_serv.setEditable(True)

        self.verticalLayout_7.addWidget(self.cb_tipo_prod_serv)


        self.horizontalLayout_14.addLayout(self.verticalLayout_7)


        self.gridLayout_9.addLayout(self.horizontalLayout_14, 9, 0, 1, 1)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_51 = QLabel(self.frame_13)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_32.addWidget(self.label_51)

        self.txt_info_empresa_razao_social = QLineEdit(self.frame_13)
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


        self.gridLayout_9.addLayout(self.horizontalLayout_32, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_13, 0, 0, 1, 1)

        self.toolBox_config.addItem(self.page_config_empresa, u"Configura\u00e7\u00f5es da Empresa  ")
        self.page_up_logo = QWidget()
        self.page_up_logo.setObjectName(u"page_up_logo")
        self.page_up_logo.setGeometry(QRect(0, 0, 651, 435))
        self.gridLayout_3 = QGridLayout(self.page_up_logo)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_12 = QFrame(self.page_up_logo)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(558, 48))
        self.frame_12.setStyleSheet(u"QFrame {\n"
"    background-color: transparent;\n"
"    border: 2px solid #333333;\n"
"    border-radius: 5px;\n"
"   border-radius: 8px; /* Ajuste o valor para controlar a curvatura das bordas */\n"
"}\n"
"\n"
"QLabel, QLineEdit, QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_12)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(232, 22))
        self.label_12.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_9.addWidget(self.label_12)

        self.txt_caminho_logo_empresa = QLineEdit(self.frame_12)
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

        self.toolButton_logo_caminho = QToolButton(self.frame_12)
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

        self.btn_salvar_logo_empresa = QPushButton(self.frame_12)
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


        self.gridLayout_16.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_12, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.toolBox_config.addItem(self.page_up_logo, u"Carregar Logo")
        self.page_acesso_remoto = QWidget()
        self.page_acesso_remoto.setObjectName(u"page_acesso_remoto")
        self.page_acesso_remoto.setGeometry(QRect(0, 0, 651, 435))
        self.gridLayout_4 = QGridLayout(self.page_acesso_remoto)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_16 = QFrame(self.page_acesso_remoto)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(535, 180))
        self.frame_16.setStyleSheet(u"QFrame {\n"
"    background-color: transparent;\n"
"    border: 2px solid #333333;\n"
"    border-radius: 5px;\n"
"   border-radius: 8px; /* Ajuste o valor para controlar a curvatura das bordas */\n"
"}\n"
"\n"
"QLabel, QLineEdit, QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_16)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_14 = QLabel(self.frame_16)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 20))
        self.label_14.setStyleSheet(u"background: transparent;\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_21.addWidget(self.label_14, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.radioButton_server = QRadioButton(self.frame_16)
        self.radioButton_server.setObjectName(u"radioButton_server")
        self.radioButton_server.setStyleSheet(u"QRadioButton {\n"
"	background: transparent;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.radioButton_server)

        self.txt_ip_servidor = QLineEdit(self.frame_16)
        self.txt_ip_servidor.setObjectName(u"txt_ip_servidor")
        self.txt_ip_servidor.setMinimumSize(QSize(220, 0))
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

        self.label_15 = QLabel(self.frame_16)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.label_15)

        self.comboBox_porta_servidor = QComboBox(self.frame_16)
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

        self.btn_salvar_server = QPushButton(self.frame_16)
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


        self.gridLayout_21.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)

        self.label_status_server = QLabel(self.frame_16)
        self.label_status_server.setObjectName(u"label_status_server")
        self.label_status_server.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_status_server.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_21.addWidget(self.label_status_server, 2, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.radioButton_client = QRadioButton(self.frame_16)
        self.radioButton_client.setObjectName(u"radioButton_client")
        self.radioButton_client.setStyleSheet(u"QRadioButton {\n"
"	background: transparent;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.radioButton_client)

        self.txt_ip_client = QLineEdit(self.frame_16)
        self.txt_ip_client.setObjectName(u"txt_ip_client")
        self.txt_ip_client.setMinimumSize(QSize(220, 0))
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

        self.label_16 = QLabel(self.frame_16)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_15.addWidget(self.label_16)

        self.txt_porta_client = QLineEdit(self.frame_16)
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

        self.btn_salvar_client = QPushButton(self.frame_16)
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


        self.gridLayout_21.addLayout(self.horizontalLayout_15, 3, 0, 1, 1)

        self.label_status_client = QLabel(self.frame_16)
        self.label_status_client.setObjectName(u"label_status_client")
        self.label_status_client.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_status_client.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_21.addWidget(self.label_status_client, 4, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_16, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.toolBox_config.addItem(self.page_acesso_remoto, u"Acesso Remoto")
        self.page_usuarios = QWidget()
        self.page_usuarios.setObjectName(u"page_usuarios")
        self.gridLayout_5 = QGridLayout(self.page_usuarios)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_9 = QFrame(self.page_usuarios)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(480, 145))
        self.frame_9.setStyleSheet(u"QFrame {\n"
"    background-color: transparent;\n"
"    border: 2px solid #333333;\n"
"    border-radius: 5px;\n"
"   border-radius: 8px; /* Ajuste o valor para controlar a curvatura das bordas */\n"
"}\n"
"\n"
"QLabel, QLineEdit, QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_9)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setStyleSheet(u"background: transparent;\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_20.addWidget(self.label_7, 0, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.label_18)

        self.txt_new_nome = QLineEdit(self.frame_9)
        self.txt_new_nome.setObjectName(u"txt_new_nome")
        self.txt_new_nome.setMinimumSize(QSize(200, 25))
        self.txt_new_nome.setMaximumSize(QSize(200, 25))
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

        self.verticalLayout_2.addWidget(self.txt_new_nome)


        self.gridLayout_20.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_21 = QLabel(self.frame_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.label_21)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.txt_new_password = QLineEdit(self.frame_9)
        self.txt_new_password.setObjectName(u"txt_new_password")
        self.txt_new_password.setMinimumSize(QSize(200, 25))
        self.txt_new_password.setMaximumSize(QSize(200, 25))
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

        self.checkBox_show_pass = QCheckBox(self.frame_9)
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


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)


        self.gridLayout_20.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_22.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_22)

        self.comboBox_new_privilegio = QComboBox(self.frame_9)
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

        self.horizontalLayout_3.addWidget(self.comboBox_new_privilegio)

        self.btn_salvar_new_user = QPushButton(self.frame_9)
        self.btn_salvar_new_user.setObjectName(u"btn_salvar_new_user")
        self.btn_salvar_new_user.setMinimumSize(QSize(75, 25))
        self.btn_salvar_new_user.setMaximumSize(QSize(75, 25))
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


        self.gridLayout_20.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)


        self.gridLayout_5.addWidget(self.frame_9, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.toolBox_config.addItem(self.page_usuarios, u"Usu\u00e1rios")
        self.page_config_cupom_fiscal = QWidget()
        self.page_config_cupom_fiscal.setObjectName(u"page_config_cupom_fiscal")
        self.gridLayout_7 = QGridLayout(self.page_config_cupom_fiscal)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_14 = QFrame(self.page_config_cupom_fiscal)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(350, 115))
        self.frame_14.setStyleSheet(u"QFrame {\n"
"    background-color: transparent;\n"
"    border: 2px solid #333333;\n"
"    border-radius: 5px;\n"
"   border-radius: 8px; /* Ajuste o valor para controlar a curvatura das bordas */\n"
"}\n"
"\n"
"QLabel, QLineEdit, QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_14)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(155, 30))
        self.label_8.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.comboBox_fonte_cupom = QComboBox(self.frame_14)
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

        self.horizontalLayout_8.addWidget(self.comboBox_fonte_cupom)

        self.btn_salvar_tipo_fonte_cupom = QPushButton(self.frame_14)
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


        self.gridLayout_6.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.frame_14)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(155, 30))
        self.label_2.setStyleSheet(u"background: transparent;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.comboBox_tipo_cupom = QComboBox(self.frame_14)
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

        self.horizontalLayout_7.addWidget(self.comboBox_tipo_cupom)

        self.btn_salvar_tipo_cupom = QPushButton(self.frame_14)
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


        self.gridLayout_6.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.label_10 = QLabel(self.frame_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(333, 20))
        self.label_10.setMaximumSize(QSize(455, 20))
        self.label_10.setStyleSheet(u"background: transparent;\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_10, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_14, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.toolBox_config.addItem(self.page_config_cupom_fiscal, u"Configura\u00e7\u00f5es do Cupom Fiscal")

        self.gridLayout_8.addWidget(self.toolBox_config, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.label = QLabel(Configuracoes)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: transparent;\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.retranslateUi(Configuracoes)

        self.toolBox_config.setCurrentIndex(0)
        self.toolBox_config.layout().setSpacing(6)


        QMetaObject.connectSlotsByName(Configuracoes)
    # setupUi

    def retranslateUi(self, Configuracoes):
        Configuracoes.setWindowTitle(QCoreApplication.translate("Configuracoes", u"Configura\u00e7\u00f5es", None))
        self.label_52.setText(QCoreApplication.translate("Configuracoes", u"Endere\u00e7o:", None))
        self.label_53.setText(QCoreApplication.translate("Configuracoes", u"CNPJ:", None))
        self.label_54.setText(QCoreApplication.translate("Configuracoes", u"IE:", None))
        self.label_40.setText(QCoreApplication.translate("Configuracoes", u"Informa\u00e7\u00f5es da Empresa", None))
        self.label_55.setText(QCoreApplication.translate("Configuracoes", u"Telefone:", None))
        self.btn_salvar_info_empresa.setText(QCoreApplication.translate("Configuracoes", u"Salvar", None))
        self.btn_delete_info_empresa.setText(QCoreApplication.translate("Configuracoes", u"Deletar", None))
        self.btn_carrega_dados_empresa.setText(QCoreApplication.translate("Configuracoes", u"Exibir Dados", None))
        self.label_56.setText(QCoreApplication.translate("Configuracoes", u"Rodape Cupom Fiscal:", None))
        self.label_57.setText(QCoreApplication.translate("Configuracoes", u"Email:", None))
        self.label_58.setText(QCoreApplication.translate("Configuracoes", u"Cidade:", None))
        self.label_4.setText(QCoreApplication.translate("Configuracoes", u"Empresa do Segmento", None))
        self.cb_segment.setItemText(0, QCoreApplication.translate("Configuracoes", u"Alimenta\u00e7\u00e3o", None))
        self.cb_segment.setItemText(1, QCoreApplication.translate("Configuracoes", u"Beleza e Est\u00e9tica", None))
        self.cb_segment.setItemText(2, QCoreApplication.translate("Configuracoes", u"Higiene pessoal", None))
        self.cb_segment.setItemText(3, QCoreApplication.translate("Configuracoes", u"Materias para Constru\u00e7\u00e3o Civil", None))
        self.cb_segment.setItemText(4, QCoreApplication.translate("Configuracoes", u"Materiais de Limpeza", None))
        self.cb_segment.setItemText(5, QCoreApplication.translate("Configuracoes", u"Moda e Vestu\u00e1rio", None))
        self.cb_segment.setItemText(6, QCoreApplication.translate("Configuracoes", u"Lar e Decora\u00e7\u00e3o", None))
        self.cb_segment.setItemText(7, QCoreApplication.translate("Configuracoes", u"Tecnologia e Inform\u00e1tica", None))
        self.cb_segment.setItemText(8, QCoreApplication.translate("Configuracoes", u"Manuten\u00e7\u00e3o", None))

        self.cb_segment.setCurrentText(QCoreApplication.translate("Configuracoes", u"Alimenta\u00e7\u00e3o", None))
        self.label_5.setText(QCoreApplication.translate("Configuracoes", u"Venda especializada:", None))
        self.cb_tipo_prod_serv.setItemText(0, QCoreApplication.translate("Configuracoes", u"Alimentos Congelados", None))
        self.cb_tipo_prod_serv.setItemText(1, QCoreApplication.translate("Configuracoes", u"Alimentos N\u00e3o Perec\u00edveis/Enlatados", None))
        self.cb_tipo_prod_serv.setItemText(2, QCoreApplication.translate("Configuracoes", u"Alimentos Perec\u00edveis/Embalados", None))
        self.cb_tipo_prod_serv.setItemText(3, QCoreApplication.translate("Configuracoes", u"Bebidas", None))
        self.cb_tipo_prod_serv.setItemText(4, QCoreApplication.translate("Configuracoes", u"Ferragens E Materiais De Constru\u00e7\u00e3o", None))
        self.cb_tipo_prod_serv.setItemText(5, QCoreApplication.translate("Configuracoes", u"Hortifr\u00fati E Carnes", None))
        self.cb_tipo_prod_serv.setItemText(6, QCoreApplication.translate("Configuracoes", u"Pe\u00e7as de Motos e Carros", None))
        self.cb_tipo_prod_serv.setItemText(7, QCoreApplication.translate("Configuracoes", u"Produtos De Higiene Pessoal", None))
        self.cb_tipo_prod_serv.setItemText(8, QCoreApplication.translate("Configuracoes", u"Produtos De Limpeza", None))
        self.cb_tipo_prod_serv.setItemText(9, QCoreApplication.translate("Configuracoes", u"Produtos Para Pets", None))
        self.cb_tipo_prod_serv.setItemText(10, QCoreApplication.translate("Configuracoes", u"Roupas, Cal\u00e7ados E Acess\u00f3rios", None))
        self.cb_tipo_prod_serv.setItemText(11, QCoreApplication.translate("Configuracoes", u"Sal\u00e3o De Beleza, Est\u00e9tica E Spa", None))
        self.cb_tipo_prod_serv.setItemText(12, QCoreApplication.translate("Configuracoes", u"Sv\u00e7/Manuten\u00e7\u00e3o Celular E Tablet", None))
        self.cb_tipo_prod_serv.setItemText(13, QCoreApplication.translate("Configuracoes", u"Sv\u00e7/Manuten\u00e7\u00e3o de Ar Cond. e Vent", None))
        self.cb_tipo_prod_serv.setItemText(14, QCoreApplication.translate("Configuracoes", u"Sv\u00e7/Mec\u00e2nico de Carro", None))
        self.cb_tipo_prod_serv.setItemText(15, QCoreApplication.translate("Configuracoes", u"Sv\u00e7/Mec\u00e2nico de Moto", None))
        self.cb_tipo_prod_serv.setItemText(16, QCoreApplication.translate("Configuracoes", u"Vidra\u00e7aria, Marmoraria E Carpintaria", None))
        self.cb_tipo_prod_serv.setItemText(17, QCoreApplication.translate("Configuracoes", u"Outros", None))

        self.cb_tipo_prod_serv.setCurrentText(QCoreApplication.translate("Configuracoes", u"Alimentos Congelados", None))
        self.label_51.setText(QCoreApplication.translate("Configuracoes", u"Raz\u00e3o Social:", None))
        self.toolBox_config.setItemText(self.toolBox_config.indexOf(self.page_config_empresa), QCoreApplication.translate("Configuracoes", u"Configura\u00e7\u00f5es da Empresa  ", None))
        self.label_12.setText(QCoreApplication.translate("Configuracoes", u"Carregar Logo da Empresa", None))
        self.toolButton_logo_caminho.setText(QCoreApplication.translate("Configuracoes", u"...", None))
        self.btn_salvar_logo_empresa.setText(QCoreApplication.translate("Configuracoes", u"OK", None))
        self.toolBox_config.setItemText(self.toolBox_config.indexOf(self.page_up_logo), QCoreApplication.translate("Configuracoes", u"Carregar Logo", None))
        self.label_14.setText(QCoreApplication.translate("Configuracoes", u"Acesso Remoto", None))
        self.radioButton_server.setText(QCoreApplication.translate("Configuracoes", u"Server", None))
        self.label_15.setText(QCoreApplication.translate("Configuracoes", u"Port", None))
        self.comboBox_porta_servidor.setItemText(0, QCoreApplication.translate("Configuracoes", u"5000", None))
        self.comboBox_porta_servidor.setItemText(1, QCoreApplication.translate("Configuracoes", u"6000", None))
        self.comboBox_porta_servidor.setItemText(2, QCoreApplication.translate("Configuracoes", u"6060", None))
        self.comboBox_porta_servidor.setItemText(3, QCoreApplication.translate("Configuracoes", u"7000", None))
        self.comboBox_porta_servidor.setItemText(4, QCoreApplication.translate("Configuracoes", u"7070", None))
        self.comboBox_porta_servidor.setItemText(5, QCoreApplication.translate("Configuracoes", u"8000", None))
        self.comboBox_porta_servidor.setItemText(6, QCoreApplication.translate("Configuracoes", u"8080", None))

        self.btn_salvar_server.setText(QCoreApplication.translate("Configuracoes", u"OK", None))
        self.label_status_server.setText("")
        self.radioButton_client.setText(QCoreApplication.translate("Configuracoes", u"Client", None))
        self.label_16.setText(QCoreApplication.translate("Configuracoes", u"Port", None))
        self.btn_salvar_client.setText(QCoreApplication.translate("Configuracoes", u"OK", None))
        self.label_status_client.setText("")
        self.toolBox_config.setItemText(self.toolBox_config.indexOf(self.page_acesso_remoto), QCoreApplication.translate("Configuracoes", u"Acesso Remoto", None))
        self.label_7.setText(QCoreApplication.translate("Configuracoes", u"Adicionar Usu\u00e1rios", None))
        self.label_18.setText(QCoreApplication.translate("Configuracoes", u"Nome do novo usu\u00e1rio:", None))
        self.label_21.setText(QCoreApplication.translate("Configuracoes", u"Password:", None))
        self.checkBox_show_pass.setText("")
        self.label_22.setText(QCoreApplication.translate("Configuracoes", u"Privil\u00e9gio:", None))
        self.comboBox_new_privilegio.setItemText(0, QCoreApplication.translate("Configuracoes", u"Comum", None))
        self.comboBox_new_privilegio.setItemText(1, QCoreApplication.translate("Configuracoes", u"Gerente", None))
        self.comboBox_new_privilegio.setItemText(2, QCoreApplication.translate("Configuracoes", u"Administrador do Sistema", None))

        self.btn_salvar_new_user.setText(QCoreApplication.translate("Configuracoes", u"OK", None))
        self.toolBox_config.setItemText(self.toolBox_config.indexOf(self.page_usuarios), QCoreApplication.translate("Configuracoes", u"Usu\u00e1rios", None))
        self.label_8.setText(QCoreApplication.translate("Configuracoes", u"Fonte do Cupom", None))
        self.comboBox_fonte_cupom.setItemText(0, QCoreApplication.translate("Configuracoes", u"10", None))
        self.comboBox_fonte_cupom.setItemText(1, QCoreApplication.translate("Configuracoes", u"12", None))
        self.comboBox_fonte_cupom.setItemText(2, QCoreApplication.translate("Configuracoes", u"14", None))
        self.comboBox_fonte_cupom.setItemText(3, QCoreApplication.translate("Configuracoes", u"16", None))
        self.comboBox_fonte_cupom.setItemText(4, QCoreApplication.translate("Configuracoes", u"18", None))
        self.comboBox_fonte_cupom.setItemText(5, QCoreApplication.translate("Configuracoes", u"20", None))
        self.comboBox_fonte_cupom.setItemText(6, QCoreApplication.translate("Configuracoes", u"22", None))
        self.comboBox_fonte_cupom.setItemText(7, QCoreApplication.translate("Configuracoes", u"24", None))
        self.comboBox_fonte_cupom.setItemText(8, QCoreApplication.translate("Configuracoes", u"26", None))
        self.comboBox_fonte_cupom.setItemText(9, QCoreApplication.translate("Configuracoes", u"28", None))

        self.btn_salvar_tipo_fonte_cupom.setText(QCoreApplication.translate("Configuracoes", u"Salvar", None))
        self.label_2.setText(QCoreApplication.translate("Configuracoes", u"Tipo de  Cupom", None))
        self.comboBox_tipo_cupom.setItemText(0, QCoreApplication.translate("Configuracoes", u"80mm", None))
        self.comboBox_tipo_cupom.setItemText(1, QCoreApplication.translate("Configuracoes", u"58mm", None))

        self.btn_salvar_tipo_cupom.setText(QCoreApplication.translate("Configuracoes", u"Salvar", None))
        self.label_10.setText(QCoreApplication.translate("Configuracoes", u"Configura\u00e7\u00f5es do Cupom", None))
        self.toolBox_config.setItemText(self.toolBox_config.indexOf(self.page_config_cupom_fiscal), QCoreApplication.translate("Configuracoes", u"Configura\u00e7\u00f5es do Cupom Fiscal", None))
        self.label.setText(QCoreApplication.translate("Configuracoes", u"Configura\u00e7\u00f5es", None))
    # retranslateUi

