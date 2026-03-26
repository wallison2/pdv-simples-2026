import sys
import os
from cx_Freeze import setup, Executable

# Configuração das opções de build
build_exe_options = {
    "packages": [
        "sys", "PySide6", "datetime", "escpos", "subprocess",
        "tempfile", "win32print", "reportlab", "usb.util", 
        "os", "ctypes", "sqlite3", "time", "matplotlib.pyplot",
        "locale", "pandas", "openpyxl", "xml.etree.ElementTree",
        "random", "flask", "flask_basicauth", "hashlib"
    ],
    "include_files": [
        "bd/",  # Inclua a pasta do banco de dados
        "ui_login.py", "ui_form.py", "ui_Saida.py", 
        "ui_forma_pagamento.py", "Resource_rc.py", 
        "bdestoque.py", "bduser.py", "controle_financeiro.py"
    ],

}

# Configuração do executável
executables = [Executable("main.py", base=None)]

# Configuração do setup
setup(
    name="PDV-SIMPLES",
    version="1.0",
    description="Descrição do seu aplicativo: Sem impressão de cupom fiscal, com controle de estoque e uma janela de financeira básica",
    options={"build_exe": build_exe_options},
    executables=executables
)
