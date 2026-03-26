import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox, QHeaderView)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from PySide6.QtCore import QTimer, QTime
from PySide6 import QtWidgets
from datetime import datetime
from escpos.printer import Usb
import win32print
import win32api
import subprocess
import locale
import usb.core
import usb.util
import random
import os
import sys
import ctypes
import mysql.connector
import bdestoque
import configparser
import matplotlib.pyplot as plt
winspool = ctypes.WinDLL('winspool.drv')
from ui_form import Ui_W_W_AUTO_COM_PDV  # Certifique-se de que você está importando corretamente a classe Ui_W_W_AUTO_COM_PDV
from Resource_rc import *

class W_W_AUTO_COM_PDV(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_W_W_AUTO_COM_PDV()
        self.ui.setupUi(self)

#####################################################################################################

#####################################################################################################







        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = W_W_AUTO_COM_PDV()
    widget.show()
    sys.exit(app.exec())
