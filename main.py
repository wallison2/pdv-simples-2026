'''
                                Meu_Sistema/
                                │
                                ├── main.py                # Código principal
                                ├── api_server.py          # Contém as classes APIEstoque, APIUsuarios e APIFinanceiro
                                ├── bd/                    # Bancos de dados SQLite
                                │   ├── bdestoque.db
                                │   ├── bduser.db
                                │   └── transacoes_entrada_saida.db
                                └── requirements.txt       # Dependências do projeto


comando para converter oara um executável aonde aparece o cmd  ==> pyinstaller --onefile --icon="W_W-icone.ico" main.py

comando para converter oara um executável aonde nao aparece o cmd ==> pyinstaller --onefile --windowed --icon="W_W-icone.ico" main.py

Explicação:
--onefile: Cria um único arquivo executável.
--windowed (ou -w): Impede a abertura da janela de terminal (CMD) ao executar o executável.
--icon="W_W-icone.ico": Define o ícone do seu executável
'''

import sys
import os
import subprocess
import time
from PySide6.QtWidgets import QVBoxLayout, QWidget, QFileDialog
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, QMessageBox)
from PySide6.QtGui import QColor, QFont, QIcon, QShortcut, QAction
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QPoint, QEvent, QStringListModel
from PySide6.QtWidgets import QLabel, QToolBar, QHBoxLayout, QSizePolicy, QColorDialog, QMenuBar, QStatusBar

from PySide6.QtWidgets import QGraphicsScene, QGraphicsProxyWidget
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import QTimer, QTime
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QPushButton, QLineEdit
import re
from PySide6.QtGui import QPixmap
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import locale
import ctypes
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import messagebox

from openpyxl import Workbook
from openpyxl.styles import Font
import xml.etree.ElementTree as ET
from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth
from threading import Thread
from flask import Flask
from requests.exceptions import RequestException
import requests
import configparser

import signal
import uvicorn

from PIL import Image, ImageDraw, ImageFont
import win32print
import win32ui
import io
from PIL import ImageWin

##### AREA DE IMPORTAÇÃO DOS FORM´S DE (UI_LOGIN, Ui_W_W_AUTO_COM_PDV, UI_SAIDA)
from ui_login import Ui_Dialog # tela de login para acessa o programa
from ui_form import Ui_W_W_AUTO_COM_PDV  # Atento para importando corretamente a classe Ui_W_W_AUTO_COM_PDV
from ui_Saida import Ui_Saida # tela de saidas "SANGRIAS"
from ui_forma_pagamento import Ui_Form_Pgto # tela para finalizar venda com formas de pagamentos
from ui_edit_produt import Ui_Edicao_Produto # tela para edição de produto na aba de estoque
from ui_license_viewer import Ui_License_Viewer # tela de autenticação de licenca
from ui_configuracoes import Ui_Configuracoes # tela de configuracoes

import psutil
from Resource_rc import * # comando para converte o icones ==> pyside6-rcc Resource.qrc -o Resource_rc.py

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import threading
import socket
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

###### AREA DO BANCO DE DADOS (ESTOQUE, USUARIOS, E CONTROLE FINACEIRO)
from bdestoque import Banco_Estoque
from bduser import Banco_Users
from controle_financeiro import CONTROLE_FINANCEIRO


from PySide6.QtCore import QSettings

########################################
# ---------- Importa LicenseManager ----------

from license_manager import LicenseManager

from pathlib import Path

# instanciando com o novo arquivo .sd
lm = LicenseManager(
    secret=b"4fG7@!x9B2mQ#p1Lk6zY",
    preload_file="hmacs_preload.sd",  # <- aqui
    usadas_file="CV.sd"         # opcional, também pode mudar
)

#############################################################################################
CAMINHO_JSON = "config_fonte.json"
    
winspool = ctypes.WinDLL('winspool.drv')

# Variável para armazenar o caminho da imagem
logo_caminho = ""

# Definir a localidade para o Brasil (pt_BR.UTF-8)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

########## AREA DAS API'S (ESTOQUE, USUARIOS, E CONTROLE FINACEIRO)
from api_server import APIEstoque, APIUsuarios, APIFinanceiro

# Instanciando as classes
estoque_api = APIEstoque()
usuarios_api = APIUsuarios()
financeiro_api = APIFinanceiro()

class LicenseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ativação de Licença")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()
        self.label_info = QLabel("Digite sua chave de licença:")
        self.txt_licenca = QLineEdit()
        self.txt_licenca.setMaxLength(50)
        self.btn_liberar = QPushButton("Liberar Licença")
        self.label_dias_expira = QLabel("")
        layout.addWidget(self.label_info)
        layout.addWidget(self.txt_licenca)
        layout.addWidget(self.btn_liberar)
        layout.addWidget(self.label_dias_expira)
        self.setLayout(layout)

        self.btn_liberar.clicked.connect(self.liberar_licenca)
        self.licenca_ativa = False

    def verificar_licenca_inicio(self):
        ok, msg = lm.check_on_start()
        if not ok:
            # Licença não ativada ou expirada
            QMessageBox.warning(self, "Licença", f"{msg}\nDigite a chave para ativar.")
            return False  # licença não ativa
        else:
            # Licença ativa, mostra dias restantes
            dias = lm.dias_restantes()
            self.label_dias_expira.setText(f"Dias restantes: {dias}")
            estilo = "color: red; font-weight: bold;" if dias <= 5 else "color: black; font-weight: normal;"
            self.label_dias_expira.setStyleSheet(estilo)
            self.licenca_ativa = True
            return True  # licença ativa

    def liberar_licenca(self):
        chave_digitada = self.txt_licenca.text().strip().upper()
        if not chave_digitada:
            alerta = QMessageBox()
            alerta.setIcon(QMessageBox.Icon.Warning)
            alerta.setWindowTitle("Licença")
            alerta.setText("Digite a chave de licença.")
            alerta.exec()
            print("Digitada:", repr(chave_digitada))
            print("HMAC calculado:", lm._hmac_of(chave_digitada))

            return

            # 🔎 DEBUG AQUI
        print("Digitada:", repr(chave_digitada))
        print("HMAC calculado:", lm._hmac_of(chave_digitada))

        ok, retorno = lm.activate_key(chave_digitada)

        print("Resultado activate_key:", ok, retorno)

        if ok:
            # Atualiza a label de dias restantes antes de fechar
            self.licenca_ativa = True
            dias = lm.dias_restantes()
            self.label_dias_expira.setText(f"Dias restantes: {dias}")
            self.label_dias_expira.setStyleSheet(
                "background: transparent; font: 700 10pt 'Segoe UI'; font-weight: bold; color: red;" 
                if dias <= 5 else
                "background: transparent; font: 700 10pt 'Segoe UI'; font-weight: bold; color: rgb(255, 255, 255);"
            )
            if hasattr(self, "label_dias_restantes"):
                self.label_dias_restantes.setText(f"Dias restantes: {dias}")
                self.label_dias_restantes.setStyleSheet(self.label_dias_expira.styleSheet())

            # Mostra mensagem de sucesso
            info = QMessageBox()
            info.setIcon(QMessageBox.Icon.Information)
            info.setWindowTitle("Licença")
            info.setText(retorno)
            info.exec()

            # Só fecha o diálogo se quiser liberar o login
            self.accept()  # aqui fecha o diálogo depois de atualizar tudo

        else:
            alerta = QMessageBox()
            alerta.setIcon(QMessageBox.Icon.Warning)
            alerta.setWindowTitle("Licença")
            alerta.setText(retorno)
            alerta.exec()

# Class de login
class Login(QWidget, Ui_Dialog):
    
    def __init__(self):
        super().__init__()
        # Iniciar a interface de login depois de garantir que o servidor está rodando
        self.setupUi(self)
        self.setWindowTitle('Login')
        self.label_bar.setText("Aguardando login...")
        self.view_login_combobox()
        self.btn_entrar.clicked.connect(self.checklogin)

        self.tentativas = 0        
    
    def view_login_combobox(self):
        
        # Cria instância de Banco_Users e conecta ao banco
        self.banco_user = Banco_Users()
        self.banco_user.conectar_ao_sqlite()

        # Busca todos os usuários (retorna lista de tuplas)
        lista_usuarios = self.banco_user.listar_user()

        # Extrai apenas os nomes dos usuários (índice 1 da tupla)
        nomes = [usuario[1] for usuario in lista_usuarios] if lista_usuarios else []

        # Limpa o comboBox antes de preencher
        self.comboBox_login.clear()

        # Adiciona os nomes à comboBox
        self.comboBox_login.addItems(nomes)

        # Define o primeiro como padrão (opcional)
        if nomes:
            self.comboBox_login.setCurrentText(nomes[0])

    def checklogin(self):  # Verificação de login
        username = self.comboBox_login.currentText().strip().lower()
        password = self.txt_password.text()
        
        # Cria instância de Banco_Users e conecta ao banco
        self.banco_user = Banco_Users()
        self.banco_user.conectar_ao_sqlite()

        # Verifica usuário e senha
        user_info = self.banco_user.check_user(username, password)
        if user_info is not None:
            nome, stored_password, privilegio = user_info
            if stored_password == password and privilegio in ['Admin', 'Comum', 'Gerente']:
                # Acesso permitido
                self.atualizar_label_bar()
                time.sleep(0.2)
                self.close()
                self.open_segunda_tela(privilegio, nome)
                self.banco_user.close_connection()
            else:
                self.handle_login_error()
        else:
            self.handle_login_error()

    def handle_login_error(self):
        if self.tentativas < 3:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle("Erro ao Acessar")
            msg.setText(f'Dados Incorretos \n \n Tentativa: {self.tentativas + 1} de 3')
            msg.exec()
            self.tentativas += 1
            self.comboBox_login.setCurrentText("")
            self.txt_password.setText("")
        else:
            sys.exit(0)

    def open_segunda_tela(self, user_type, usuario_logado):
        """Abre a segunda tela com as informações do usuário logado."""
        self.windows2 = W_W_AUTO_COM_PDV(user_type, usuario_logado)
        self.windows2.show()
                    
    def atualizar_label_bar(self):
        texto = "Acesso Liberado!"
        self.comboBox_login.setCurrentText("")
        self.txt_password.setText("")
        self.label_bar.setText(texto)  # Atualiza a Label com o texto de sucesso
        self.label_bar.adjustSize()  # Ajusta o tamanho da Label para exibir todo o texto
        QApplication.processEvents()  # Atualiza a interface para exibir imediatamente a mensagem  

# Class de Janela Principal
class W_W_AUTO_COM_PDV(QMainWindow, Ui_W_W_AUTO_COM_PDV, Ui_Dialog, LicenseDialog): # class principal
    
    def __init__(self, user_type, usuario_logado, ip=None, porta=None):
        super(W_W_AUTO_COM_PDV, self).__init__()
        self.setupUi(self)
        #self.showMaximized()  # Maximiza a janela
        # ou 
        #self.setWindowState(Qt.WindowMaximized)
         
        # Atualiza label de dias restantes
        self.atualizar_dias_licenca()
                          
        # Remove os botões padrão da janela (min, max, fechar)
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint)
        
        self.offset = None  # posição inicial do clique
        self.configurar_menu_janela() # chama a funcao para criar botões padrão da janela (min, max, fechar) personalisados
       
        
        self.installEventFilter(self)  # Instalar o filtro de eventos na janela principal e se quiser capturar o ESC em qualquer parte da janela

###################################################################################     

   # 👇 Define os tamanhos dos botões ANTES de exibir a tela
        self.largura_botao = 100
        self.altura_botao = 60
         

###################################################################################    
        self.user_type = user_type
        self.usuario_logado = usuario_logado

        self.ip = ip or "0.0.0.0"  # Padrão se não for fornecido
        self.porta = porta or 5000   # Padrão se não for fornecido
        
        
        # Crie uma instância do banco de dados de estoque
        self.banco_estoque = Banco_Estoque()
        self.bancoCF = CONTROLE_FINANCEIRO()

        # Instancia o fluxo de caixa da class FuxoCaixa
        self.caixa_abrir = FluxoCaixa()
        
        # Variável de controle para evitar múltiplas mensagens
        self.msg_exibida_carreg_server_client = False  

########################          ####################################

#############################   Índices das guias com base no seu layout atual     ############################################################

                                        # HOME Numero da Guia "0"
                                        # PDV Numero da Guia "1"
                                        # COMANDA Numero da guia "2"
                                        # ESTOQUE Numero da Guia "3"
                                        # FINANCEIRO Numero da Guia "4"
                                        # CONFIGURAÇÕES Numero da Guia "5"

        tab_indices = {
            "Admin": [],
            "Comum": [3, 4, 5],  # Remover as guias Estoque e Financeiro e Configuração para o usuário Comum
            "Gerente": [5]     # Remover a guia Configuração para o usuário Gerente
        }

        if user_type in tab_indices:
            tabs_to_remove = tab_indices[user_type]
            for tab_index in reversed(tabs_to_remove):  # Remova as guias em ordem reversa para evitar problemas de índice
                self.tabPrincipal.removeTab(tab_index)

################################ usuario_logado  # Armazenar o nome do usuário autenticado #####################################################
        # usuario_logado  # Armazenar o nome do usuário autenticado
        self.label_operador.setText("Operador: " + usuario_logado)  # Usar o nome do usuario autenticado

######################################################################################################
        
        self.table_pdv()
        #self.exibir_table_estoque()
        self.exibir_table_relatorio_vendas()
        self.limpar_campos() 

        # Carrega a logo ao iniciar o programa
        self.carregar_logo_empresa()
        self.ip_maquina()
        self.iniciar_modo() ###############
        self.exibir_table_estoque()
        
        # Conectar o evento textChanged do txt_pesquisa_prod ao método buscar_prod_estoque
        self.txt_pesquisa_prod.textChanged.connect(self.buscar_prod_estoque)
        self.funcao_combobox_tipo_produtos()
        # Inicialize o layout vertical
        self.layout = QVBoxLayout()

        # Definir o campo txt_qtde como "1" após adicionar o produto
        self.txt_qtde.setText("1")
               
        self.cliente_counter = 1  # Inicialize o contador com o valor desejado
        
        # Lista para armazenar os códigos dos produtos
        self.codigos_produtos = []
####################################################################################################
    #''''''''''''''''HORA NA JANELA DEFINIDA'''''''''''''''#
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000) # atualiza a cada 1000 milissegundos (1 segundo)

#######################################################################################################
        # Configurar o QLineEdit para ocultar a senha por padrão
        self.txt_new_password.setEchoMode(QtWidgets.QLineEdit.Password)
#######################################################################################################
        # Timer para debounce
        self.timer_busca = QTimer()
        self.timer_busca.setInterval(100)  # 300 ms de atraso
        self.timer_busca.setSingleShot(True)
        self.timer_busca.timeout.connect(self.preencher_campos_produto)   

        # Conectar sinais
        self.conectar_sinais()

        self.venda_finalizada = False  # Defina o valor inicial apropriado
        # Lista para guardar os produtos adicionados
        self.produtos_adicionados = []
        self.num_itens_adicionados = 0
        self.produtos_temp = {}

############################## AREA DA IMPRESSORAS ###########################################################################

        self.ultimo_cupom = None  # Variável para armazenar o último cupom
        
        self.valor_venda = 0.0  # Inicializa como 0 ou "R$ 0,00"
        
        self.default_printer = self.verifica_impressora_padrao()

############################# area da empresa que adquiriu o sistema ###########################################################
        # btn_delete_info_empresa da empresa na janela infomaçoes da empresa        
        self.btn_delete_info_empresa.clicked.connect(self.deletar_dados_empresa)
        # btn_carrega_dados_empresa da empresa na janela infomaçoes da empresa        
        self.btn_carrega_dados_empresa.clicked.connect(self.carregar_dados_empresa)
        # btn_salvar_info_empresa da empresa na janela infomaçoes da empresa        
        self.btn_salvar_info_empresa.clicked.connect(self.salvar_dados_empresa)     
            
        # Conecte os botões às funções
        self.toolButton_logo_caminho.clicked.connect(self.abrir_selecionar_logo)
        self.btn_salvar_logo_empresa.clicked.connect(self.salvar_logo)

######################## AREA DO BOTOES DE FINALIZAR VENDA E GERAR COPIAR DE CUPOM #############################################
        self.btn_open_finalizar_venda.clicked.connect(self.Open_tela_finalizar_venda)
        self.btn_nfe.clicked.connect(self.abrir_pasta_nfe)
        self.btn_open_saida.clicked.connect(self.exit_sangria)
        
        self.btn_mais_qtde.clicked.connect(self.more_qtde)
        self.btn_menos_qtde.clicked.connect(self.less_qtde)
        self.txt_qtde.installEventFilter(self)


################################### AREA DO ESTOQUE BOTOES E LINES ############################################################

        self.btn_cadastrar_prod.clicked.connect(self.inserir_prod_estoque)
        self.btn_excluir_prod.clicked.connect(self.excluir_prod_estoque)
        self.btn_atualizar_estoque.clicked.connect(self.exibir_table_estoque)

        # Conecte o sinal do radioButton_excluir_todos à função
        self.radioButton_excluir_todos.toggled.connect(lambda checked: self.on_radioButton_excluir_todos_toggled(checked))
        self.btn_editar_produtos.clicked.connect(self.open_tela_edicao_produt)

##############################################################################################################################
        self.btn_multiplicar_pdv.clicked.connect(self.habilitar_edicao_spinBox)
        self.btn_open_cancelar_venda.clicked.connect(self.limpar_campos)
        self.btn_open_cancelar_venda.clicked.connect(self.nova_venda)
        self.btn_open_excluir_item.clicked.connect(self.excluir_item_selecionado)
        self.btn_calc_pdv.clicked.connect(self.abrir_calculadora)
        self.btn_salvar_new_user.clicked.connect(self.inserir_usuario_com_campos)
        self.checkBox_show_pass.clicked.connect(self.mostrar_senha) # função que mostra e oculta a senha de criação do usuario

####################################### BOTÕES DO FINANCEIRO ####################################################################   
        self.btn_relatorio_geral.clicked.connect(self.print_relatorio)
        self.btn_relatorio_geral.clicked.connect(self.gerar_relatorio_excel)
        self.btn_clear_all.clicked.connect(self.clear_bd_finaceiro)
        self.btn_atualizar_receitas.clicked.connect(self.exibir_table_relatorio_vendas)
        self.checkBox_entradas.stateChanged.connect(self.on_checkbox_entradas_changed)
        self.checkBox_saidas.stateChanged.connect(self.on_checkbox_saidas_changed)

        ###############################################
        # Conectar os sinais toggled dos QRadioButtons à função de filtragem e atualização da tabela
        self.radioButton_tudo.toggled.connect(self.filtrar_e_atualizar_tabela)
        self.radioButton_dinheiro.toggled.connect(self.filtrar_e_atualizar_tabela)
        self.radioButton_c_credito.toggled.connect(self.filtrar_e_atualizar_tabela)
        self.radioButton_c_debito.toggled.connect(self.filtrar_e_atualizar_tabela)
        self.radioButton_pix.toggled.connect(self.filtrar_e_atualizar_tabela)

        self.btn_editar_produtos.clicked.connect(self.open_tela_edicao_produt)
        
        self.btn_salvar_tipo_cupom.clicked.connect(self.salvar_tipo_cupom)
        self.btn_salvar_tipo_fonte_cupom.clicked.connect(self.salvar_fonte_cupom)

        self.btn_salvar_server.clicked.connect(self.salvar_opcao_select_server)
        self.btn_salvar_client.clicked.connect(self.salvar_opcao_select_client)

        # Conecta o botão ao método iniciar_dia
        self.btn_abrir_caixa.clicked.connect(self.abrir_caixa)
        self.btn_fechar_caixa.clicked.connect(self.fechar_caixa)
       
        self.btn_valor_avuso.clicked.connect(self.abrir_valor_avulso)
                
        self.btn_liberar_licenca.clicked.connect(self.btn_liberar_click)
        
################# MENUBAR #######################################################################################
    def configurar_menu_janela(self):
        """Cria a barra superior com botões e assinatura no rodapé"""

        # === BARRA SUPERIOR (Fechar, Maximizar, Minimizar) ===
        barra_superior = QWidget()
        layout_topo = QHBoxLayout(barra_superior)
        layout_topo.setContentsMargins(0, 0, 0, 0)
        layout_topo.setSpacing(0)

        # --- Barra de menu à direita ---
        self.menu_janela = QMenuBar()
        self.menu_janela.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.menu_janela.setStyleSheet("""
            QMenuBar {
                font-size: 8pt;
                font-weight: bold;
                spacing: 5px;
                padding: 1px;
            }
            QMenuBar::item {
                padding: 1px 6px;
            }
        """)

        # Botões de controle
        action_close = QAction("Fechar", self)
        action_close.triggered.connect(self.close_screen_main)
        self.menu_janela.addAction(action_close)

        self.action_max_restore = QAction("Maximizar", self)
        self.action_max_restore.triggered.connect(self.toggle_max_restore)
        self.menu_janela.addAction(self.action_max_restore)

        action_min = QAction("Minimizar", self)
        action_min.triggered.connect(self.showMinimized)
        self.menu_janela.addAction(action_min)

        layout_topo.addWidget(self.menu_janela, 1)

        # Monta a barra superior
        container = QWidget()
        layout_principal = QVBoxLayout(container)
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.setSpacing(0)
        layout_principal.addWidget(barra_superior)

        self.setMenuWidget(container)

        # === ASSINATURA NO RODAPÉ COM FUNDO TRANSPARENTE ===
        status_bar = QStatusBar()
        label_assinatura = QLabel("Desenvolvido por Wallison Nogueira © 2025")
        label_assinatura.setStyleSheet("""
            color: white;             
            background: transparent;  
            font-size: 8pt;
            font-style: italic;
            padding-right: 10px;
        """)
        status_bar.addPermanentWidget(label_assinatura)
        self.setStatusBar(status_bar)

        # Permite arrastar a janela pela barra
        self.menu_janela.installEventFilter(self)
        self.offset = None

    def eventFilter(self, obj, event):
        """Permite mover a janela clicando e arrastando a barra"""
        if obj == self.menu_janela:
            if event.type() == event.Type.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:
                action = self.menu_janela.actionAt(event.position().toPoint())
                if action is None:
                    self.offset = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
                else:
                    self.offset = None
                return False

            elif event.type() == event.Type.MouseMove and self.offset is not None:
                self.move(event.globalPosition().toPoint() - self.offset)
                return True

            elif event.type() == event.Type.MouseButtonRelease:
                self.offset = None
                return False

        if event.type() == event.Type.KeyPress:
            if event.key() == Qt.Key.Key_Escape:
                self.close_screen_main()
                return True

        return super().eventFilter(obj, event)

    def close_screen_main(self):
        """Confirma se o usuário quer sair ou trocar usuário"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setWindowIcon(QIcon(QIcon.fromTheme("dialog-question")))
        msg.setWindowTitle("Confirmação")
        msg.setText("O que deseja fazer?")

        # Botões
        btn_sair = msg.addButton("Sair", QMessageBox.ButtonRole.YesRole)
        btn_cancelar = msg.addButton("Cancelar", QMessageBox.ButtonRole.NoRole)
        msg.setDefaultButton(btn_cancelar)

        # Exibe o pop-up
        msg.exec()

        # Ação escolhida
        if msg.clickedButton() == btn_sair:
            try:
                self.stop_uvicorn()
            except:
                pass
            time.sleep(0.2)
            self.close()
                   
    def toggle_max_restore(self):
        """Alterna entre maximizar e restaurar a janela"""
        if self.isMaximized():
            self.showNormal()
            self.action_max_restore.setText("Maximizar")
        else:
            self.showMaximized()
            self.action_max_restore.setText("Restaurar")

######################## Area da License Manager ##################################
    def btn_liberar_click(self):
        
        chave_digitada = self.txt_licenca.text().strip().upper()

        if not chave_digitada:
            alerta = QMessageBox()
            alerta.setIcon(QMessageBox.Icon.Warning)
            alerta.setWindowTitle("Licença")
            alerta.setText("Digite a chave de licença.")
            alerta.exec()
            return

        ok, retorno = lm.activate_key(chave_digitada)

        if ok:
            # Atualiza a label de dias restantes
            self.licenca_ativa = True
            self.atualizar_dias_licenca()  # já vai mostrar os dias somados

            # Mostra mensagem de sucesso
            info = QMessageBox()
            info.setIcon(QMessageBox.Icon.Information)
            info.setWindowIcon(QIcon(QIcon.fromTheme("Information")))
            info.setWindowTitle("Licença")
            info.setText(retorno)
            info.exec()

            # NÃO chama self.accept() se estiver dentro da janela principal
            # self.accept()  # ❌ REMOVER

        else:
            alerta = QMessageBox()
            alerta.setIcon(QMessageBox.Icon.Warning)
            alerta.setWindowIcon(QIcon(QIcon.fromTheme("Warning")))  
            alerta.setWindowTitle("Licença")
            alerta.setText(retorno)
            alerta.exec()

    def atualizar_dias_licenca(self):
        """Atualiza a label de dias restantes da licença."""
        dias = lm.dias_restantes()  # novo método que calcula os dias restantes a partir da data de expiração
        self.label_dias_expira.setText(f"Dias restantes: {dias}")
        if hasattr(self, "label_dias_restantes"):
            self.label_dias_restantes.setText(f"Dias restantes: {dias}")

        # Estilo inicial (branco)
        estilo_base = "background: transparent; font: 700 10pt 'Segoe UI'; font-weight: bold;"

        if dias <= 5:
            # Quando faltar ≤5 dias, fica vermelho
            estilo = estilo_base + "color: red;"
        else:
            # Caso contrário, branco
            estilo = estilo_base + "color: rgb(255, 255, 255);"

        self.label_dias_expira.setStyleSheet(estilo)
        if hasattr(self, "label_dias_restantes"):
            self.label_dias_restantes.setStyleSheet(estilo)

####################################################################################################################

    def abrir_caixa(self): #Abre o diálogo para configurar o valor inicial do caixa.

        self.caixa_abrir.iniciar_dia()
        
    def fechar_caixa(self):

        self.caixa_abrir.fechar_caixa()#Abre o diálogo para configurar o valor Fechamento do caixa.

    def open_tela_edicao_produt(self):

        model = self.tableView_estoque.model()
        tabela_estoque_controller = self.banco_estoque
        http_estoque_main = self.http_estoque()  # Certifique-se de retornar os endpoints adequados

        self.windows_edit_produt = Tela_Edit_Produt(
            W_W_AUTO_COM_PDV=self, 
            modelo_estoque=model, 
            tabela_estoque_controller=tabela_estoque_controller, 
            http_estoque_main=http_estoque_main
        )
        
        self.windows_edit_produt.btn_salvar_edicao_produto.clicked.connect(self.exibir_table_estoque)
        #self.dados_produto_novos = self.windows_edit_produt.dados_produto
        self.windows_edit_produt.show()
        
    def formatar_valor_add_estoque(self, text):
        # Remover qualquer formatação existente
        text = text.replace(".", "").replace(",", "")

        # Inserir o ponto e a vírgula de acordo com a posição dos números
        if text:
            try:
                float_value = float(text)
                formatted_text = f"{float_value:,.2f}"
                return formatted_text
            except ValueError:
                return None
        return None
    
    def Open_tela_finalizar_venda(self):
        
        # Passa a janela principal para a tela de finalização
        self.windows_finalizar_venda = Tela_Finalizar_Vendas(self)

        # Configura valor total da venda
        self.windows_finalizar_venda.labell_valor_venda.setText(self.txt_valor_total_pdv.text())

        # Conectar botões
        self.windows_finalizar_venda.btn_finalizar_venda.clicked.connect(self.finalizar_venda)
        self.windows_finalizar_venda.btn_finalizar_venda.clicked.connect(self.nova_venda)
        self.windows_finalizar_venda.btn_finalizar_venda.clicked.connect(self.limpar_campos)

        # Conectar comboBox de forma de pagamento
        self.comboBox_forma_pgto_tela_finalizar_venda = self.windows_finalizar_venda.comboBox_forma_pgto

        # Verificar impressora padrão
        try:
            self.verifica_impressora_padrao = self.windows_finalizar_venda.verifica_impressora_padrao_tela_venda_finalizada()
        except AttributeError:
            print("A função 'verifica_impressora_padrao_tela_venda_finalizada' não existe.")
            self.verifica_impressora_padrao = None

        # Exibe a janela
        self.windows_finalizar_venda.show()

    def close_windows_finalizar_venda(self): # fechar a janela de finalizar venda
        # Fechar a janela de finalização de venda
        self.windows_finalizar_venda.close()

    def exit_sangria(self): # open tela de sangria
        # Obter o texto da label e atribuir a self.usuario_logado
        self.usuario_logado = self.label_operador.text()

        # Crie uma instância da classe Saida_Sangria passando o usuário logado
        self.janela_saida = Saida_Sangria(self.usuario_logado)

        self.janela_saida.btn_salvar_saida.clicked.connect(self.exibir_table_relatorio_vendas)
        self.janela_saida.btn_saidas_sair.clicked.connect(self.exibir_table_relatorio_vendas)
        self.janela_saida.show()
        
###################################### FUNÇÃO QUE CADASTRA NOVAS EMPRESAS CNPJ PARA USA O PROGRAMA #########################################
    
    def salvar_dados_empresa(self): #salva dados da empresa no banco .sd

        cidade_info = self.txt_info_empresa_cidade.text()
        cnpj_info = self.txt_info_empresa_cnpj.text()
        email_info = self.txt_info_empresa_email.text()
        endereco_info = self.txt_info_empresa_endereco.text()
        ie_info = self.txt_info_empresa_ie.text()
        razao_social_info = self.txt_info_empresa_razao_social.text()
        tel_info = self.txt_info_empresa_telefone.text()
        rodape_cupom_info = self.plainTextEdit_info_empresa_rodape_cupom.toPlainText()
    
        # Criar um dicionário com os dados coletados
        dados_empresa = {
            'Cidade': cidade_info,
            'CNPJ': cnpj_info,
            'E-mail': email_info,
            'Endereço': endereco_info,
            'IE': ie_info,
            'Razão Social': razao_social_info,
            'Telefone': tel_info,
            'Rodape_Cupom': rodape_cupom_info
        }

        # Salvar os dados em um arquivo .sd (formato de exemplo)
        with open('dados_empresa.sd', 'w') as file:
            for chave, valor in dados_empresa.items():
                file.write(f"{chave}: {valor}\n")
        
        # Exibir mensagem de sucesso
        QMessageBox.information(None, "Sucesso", "Seus dados foram salvos com sucesso!")

    def carregar_dados_empresa(self): # CARREGA OS DADOS SALVO .SD NA TELA 

        dados_empresa = {}
        try:
            with open('dados_empresa.sd', 'r') as file:
                for line in file:
                    if ':' in line:
                        chave, valor = line.strip().split(':', 1)  # Adicionamos "1" para dividir apenas na primeira ocorrência do caractere ':'
                        dados_empresa[chave.strip()] = valor.strip()

            # Exibir os dados nos campos da interface gráfica
            self.txt_info_empresa_cidade.setText(dados_empresa.get('Cidade', ''))
            self.txt_info_empresa_cnpj.setText(dados_empresa.get('CNPJ', ''))
            self.txt_info_empresa_email.setText(dados_empresa.get('E-mail', ''))
            self.txt_info_empresa_endereco.setText(dados_empresa.get('Endereço', ''))
            self.txt_info_empresa_ie.setText(dados_empresa.get('IE', ''))
            self.txt_info_empresa_razao_social.setText(dados_empresa.get('Razão Social', ''))
            self.txt_info_empresa_telefone.setText(dados_empresa.get('Telefone', ''))
            self.plainTextEdit_info_empresa_rodape_cupom.setPlainText(dados_empresa.get('Rodape_Cupom', ''))
        except FileNotFoundError:
            # Se o arquivo não existir, ou ocorrer algum erro, não fazer nada
            pass
    
    def deletar_dados_empresa(self): # Limpar os campos da interface que exibem os dados da empresa
         
        self.txt_info_empresa_cidade.clear()
        self.txt_info_empresa_cnpj.clear()
        self.txt_info_empresa_email.clear()
        self.txt_info_empresa_endereco.clear()
        self.txt_info_empresa_ie.clear()
        self.txt_info_empresa_razao_social.clear()
        self.txt_info_empresa_telefone.clear()
        self.plainTextEdit_info_empresa_rodape_cupom.setPlainText('')

        # Remover o arquivo 'dados_empresa.sd' caso ele exista
        if os.path.exists('dados_empresa.sd'):
            try:
                os.remove('dados_empresa.sd')
            except OSError as e:
                # Lidar com possíveis erros ao remover o arquivo
                print(f"Erro ao remover o arquivo: {e}")
    
    def abrir_selecionar_logo(self): # Função para abrir a janela de seleção de arquivo e carregar a imagem
        
        global logo_caminho
        # Abre a janela para escolher a imagem
        file_name, _ = QFileDialog.getOpenFileName(
            None, "Selecione a logo", "", "Imagens (*.png *.jpg *.jpeg)"
        )
        if file_name:
            # Exibe o caminho na caixa de texto
            self.txt_caminho_logo_empresa.setText(file_name)
            # Armazena o caminho da imagem
            logo_caminho = file_name
    
    def salvar_logo(self): # Função para salvar o caminho da logo e exibir no label_empressa

        if logo_caminho:
            # Salva o caminho da imagem para carregamento futuro (pode usar um arquivo .txt)
            with open("caminho_logo.txt", "w") as file:
                file.write(logo_caminho)
            # Exibe a imagem no label
            self.carregar_logo_empresa()
            # Exibe a mensagem de sucesso
            QMessageBox.information(None, "Sucesso", "Sua Logo Foi Carregada Com Sucesso!!!")
        else:
            QMessageBox.warning(None, "Nenhuma logo selecionada.")
                    
    def carregar_logo_empresa(self): # Função para carregar a logo no início do programa
        try:
            # Lê o caminho salvo da imagem
            with open("caminho_logo.txt", "r") as file:
                caminho_logo = file.read()
            # Carrega a imagem e ajusta o tamanho para 256x256
            pixmap = QPixmap(caminho_logo)
            pixmap = pixmap.scaled(256, 256, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # Exibe a imagem no label
            self.label_logo_empresa.setPixmap(pixmap)
        except FileNotFoundError:
            # Exibe uma mensagem se o arquivo não existir
            self.label_logo_empresa.clear()

######################################################################################################################

    
###################################### AREA DE ADD Novos USUARIOS ######################################################
    def inserir_usuario_com_campos(self):# FUNÇÃO QUE INSERIR NOVOS USUÁRIOS NO BANCO DE DADOS USER COM BASE QUE FOR FORNECIDO

        nome_usuario = self.txt_new_nome.text()
        password_usuario = self.txt_new_password.text()
        
        # Crie uma instância de Banco_Users e conecte ao SQLite
        self.banco_user = Banco_Users()
        conexao = self.banco_user.conectar_ao_sqlite()

        if conexao:
            cursor = conexao.cursor()
            try:
                # Mapear as opções da ComboBox para os privilégios correspondentes
                privilegio = ""
                if self.comboBox_new_privilegio.currentText() == "Administrador do Sistema":
                    privilegio = "Admin"
                elif self.comboBox_new_privilegio.currentText() == "Usuário Comum":
                    privilegio = "Comum"
                elif self.comboBox_new_privilegio.currentText() == "Gerente":
                    privilegio = "Gerente"
                else:
                    # Definir um valor padrão se a ComboBox não corresponder a nenhuma opção conhecida
                    privilegio = "Comum"

                cursor.execute("INSERT INTO usuarios (nome, password, privilegio) VALUES (?, ?, ?)", (nome_usuario, password_usuario, privilegio))

                conexao.commit()

                self.txt_new_nome.setText("")
                self.txt_new_password.setText("")
               
                # Exiba uma mensagem de sucesso
                msg = QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setText("Usuário inserido com sucesso.")
                msg.exec()

            except sqlite3.Error as err:
                conexao.rollback()

                self.txt_new_nome.setText("")
                self.txt_new_password.setText("")
            
                # Lida com exceções, como erro de conexão com o banco de dados
                msg = QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(f"Erro ao inserir o usuário: {err}")
                msg.exec()

            finally:
                cursor.close()
                conexao.close()
    
    def mostrar_senha(self): # FUNÇÃO QUE MOSTRAR A SENHA E OCULTA NA AREA DE CRIAR USUARIO 

        if self.checkBox_show_pass.isChecked():
            self.txt_new_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.txt_new_password.setEchoMode(QtWidgets.QLineEdit.Password)

#######################################################################################################

    def update_time(self): # ATUALIZA A HORA E DATA AUTOMATICAMENTE TANTO DO RODAPE QUANTO DA NFC-e

        current_time = QTime.currentTime()
        self.time_text = current_time.toString('hh:mm:ss')
        self.label_hora.setText(self.time_text)
        #''''''''''''''''DATA NA JANELA DEFINIDA'''''''''''''''# ↓↓↓↓↓
        data_atual = datetime.now()
        self.data_formatada = data_atual.strftime('%d/%m/%Y')
        self.label_data.setText(self.data_formatada)

##########################################################################################

    def abrir_calculadora(self): # FUNÇÃO QUE ABRI A CALCULADORA DO SISTEMA

        calculadora_path = "calc.exe"
        subprocess.Popen(calculadora_path)

############################# AREA DO PDV ###########################################
    def table_pdv(self):
        # Configurações da Tabela PDV
        modelo = QStandardItemModel()
        header_labels = [" ", "Código", "Descrição", "Qtde UN", "Valor Unit", "Valor Total"]
        modelo.setHorizontalHeaderLabels(header_labels)
        self.tableView_pdv.setModel(modelo)
        self.modelo = modelo

        # Configurações do cabeçalho
        header = self.tableView_pdv.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)

        # Ajuste automático das colunas ao conteúdo
        self.tableView_pdv.resizeColumnsToContents()  # Ajuste das colunas conforme o conteúdo

        # Definir tamanho específico para a coluna 0 (ícone/checkbox)
        self.tableView_pdv.setColumnWidth(0, 8)  # Ajuste o valor conforme a sua necessidade

        # Estilos adicionais para o cabeçalho e a tabela
        self.tableView_pdv.setStyleSheet(''' 
            QHeaderView::section {
                background-color:rgb(255, 255, 255); 
                color: #0000FF;
                border: 1px solidrgb(255, 255, 255);
                padding: 1px;
                border-radius: 3px;
                font-size: 14px;
                font-weight: bold;
                text-align: center;
            }
            QTableView {
                font-size: 14px;
                selection-background-color:rgb(255, 255, 255);
                selection-color: #000000;
            }
            QScrollBar:vertical {
                    background-color: rgb(135,206,250);
                }
                QScrollBar::handle:vertical {
                    background-color: rgb(57, 69, 104);
                }
                QScrollBar::add-line:vertical,
                QScrollBar::sub-line:vertical {
                    background: none;
                }
                QScrollBar::add-page:vertical,
                QScrollBar::sub-page:vertical {
                    background: none;
                }
                QScrollBar:horizontal {
                    background-color: rgb(135,206,250);
                }
                QScrollBar::handle:horizontal {
                    background-color: rgb(57, 69, 104);
                }
                QScrollBar::add-line:horizontal,
                QScrollBar::sub-line:horizontal {
                    background: none;
                }
                QScrollBar::add-page:horizontal,
                QScrollBar::sub-page:horizontal {
                    background: none;
                }
        ''')

        # Ocultar as linhas das colunas
        self.tableView_pdv.setShowGrid(False)

        # Ajuste automático das colunas e linhas
        self.tableView_pdv.resizeRowsToContents()

    def adicionar_item_na_tabela(self, cod_prod, nome_prod, qtde, vl_unitario, subtotal):
        # Garantir que cod_prod seja convertido para string (evitar problemas com overflow)
        cod_prod_str = str(cod_prod)

        # Criar o item checkbox
        checkbox_item = QStandardItem()
        checkbox_item.setCheckable(True)
        checkbox_item.setCheckState(Qt.CheckState.Unchecked)

        # Criar os itens para cada coluna e definir fonte e alinhamento
        item_codigo = QStandardItem(cod_prod_str)  # Usando a string convertida para cod_prod
        item_codigo.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        item_descricao = QStandardItem(nome_prod)
        item_descricao.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        
        item_qtde = QStandardItem(str(qtde))  # Garantir que a quantidade seja convertida para string
        item_qtde.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        item_vl_unitario = QStandardItem(f"R$ {vl_unitario:.2f}")  # Formatando o valor unitário para 2 casas decimais
        item_vl_unitario.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        item_subtotal = QStandardItem(f"R$ {subtotal:.2f}")  # Formatando o subtotal para 2 casas decimais
        item_subtotal.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        # Adicionando a nova linha à tabela
        nova_linha = [checkbox_item, item_codigo, item_descricao, item_qtde, item_vl_unitario, item_subtotal]
        self.modelo.appendRow(nova_linha)

        # Personalizar a aparência das células após adicionar o item
        self.personalizar_aparencia_tabela()

        # Ajustar o tamanho das colunas após adicionar a nova linha
        for column in range(self.modelo.columnCount()):
            self.tableView_pdv.resizeColumnToContents(column)

        # Definir o campo txt_qtde como "1" após adicionar o produto
        self.txt_qtde.setText("1")
        # Após adicionar o item, rolar até a última linha automaticamente
        ultima_linha = self.modelo.rowCount() - 1
        self.tableView_pdv.scrollTo(self.modelo.index(ultima_linha, 0))

    def personalizar_aparencia_tabela(self):

        for row in range(self.modelo.rowCount()):
            for col in range(self.modelo.columnCount()):
                item = self.modelo.item(row, col)
                # Personalize as células da tabela
                if row % 1 == 0:
                    item.setBackground(QColor(150, 149, 237, 0.2))
                    item.setForeground(QColor(255, 255, 255))  # Cor branca para o texto
                    font = QFont()
                    font.setBold(True)
                    font.setPointSize(14)  # Fonte de tamanho 14
                    item.setFont(font)
                else:
                    item.setBackground(QColor(173, 216, 230, 0.6))
                    item.setForeground(QColor(255, 255, 255))  # Cor branca para o texto
                    font = QFont()
                    font.setBold(True)
                    font.setPointSize(14)
                    item.setFont(font)

    def more_qtde(self): # adicionar MAIS 1 na txt_qtde
        try:
            valor = int(self.txt_qtde.text())
        except ValueError:
            valor = 0
        valor += 1
        self.txt_qtde.setText(str(valor))

    def less_qtde(self): # subtrair MENOS 1 na txt_qtde
        try:
            valor = int(self.txt_qtde.text())
        except ValueError:
            valor = 0
        if valor > 0:
            valor -= 1
        self.txt_qtde.setText(str(valor))

    def keyPressEvent(self, event):  # Função que ativa o evento da tecla F5 e F6
        # Verificar se a tecla F5 foi pressionada
        if event.key() == Qt.Key_F5:
            if self.txt_qtde.hasFocus():
                self.txt_cod_pdv.setFocus()
            else:
                self.txt_qtde.setFocus()
                # F6 -> abre janela de valor avulso
        elif event.key() == Qt.Key_F6:
            self.abrir_valor_avulso()

    def atualizar_valor_total_excluido(self):
        total = 0.0

        for row in range(self.modelo.rowCount()):
            try:
                subtotal_str = self.modelo.item(row, 5).text().replace("R$", "").replace(",", "")
                subtotal = float(subtotal_str)
                total += subtotal
            except ValueError:
                print(f"Erro ao converter o subtotal para a linha {row}")
                continue

        valor_total_str = locale.currency(total, grouping=True)
        self.txt_valor_total_pdv.setText(valor_total_str)

    def excluir_item_selecionado(self):
        rows_to_remove = []

        for row in range(self.modelo.rowCount() - 1, -1, -1):
            checkbox_item = self.modelo.item(row, 0)
            
            if checkbox_item and checkbox_item.checkState() == Qt.Checked:
                item_nome = self.modelo.item(row, 2).text()
                try:
                    item_qtde = int(self.modelo.item(row, 3).text())
                except ValueError:
                    print(f"Erro ao converter quantidade para o item {item_nome}")
                    continue

                item_vl_unitario = float(self.modelo.item(row, 4).text().replace('R$', '').replace(',', ''))
                self.produtos_adicionados = [
                    item for item in self.produtos_adicionados 
                    if item[0] != item_nome or item[1] != item_qtde or item[2] != item_vl_unitario
                ]
                
                rows_to_remove.append(row)

        for row in rows_to_remove:
            self.modelo.removeRow(row)
            self.num_itens_adicionados -= 1

        self.atualizar_valor_total_excluido()

    def adicionar_item_compra(self):
        if self.venda_finalizada:

            self.nova_venda()
        else:
            self.num_itens_adicionados += 1
            self.itens = (str(self.num_itens_adicionados))
            self.tableView_pdv.resizeColumnToContents(8)

    def nova_venda(self):
        self.venda_finalizada = False
        self.produtos_adicionados = []
        self.limpar_campos()

    def exibir_mensagem_aviso(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon(QMessageBox.standardIcon(QMessageBox.Warning)))
        msg.setWindowTitle("Aviso")
        msg.setText("Por favor, digite um valor válido.")
        msg.exec()

    def habilitar_edicao_spinBox(self):
        self.txt_qtde.setEnabled(True)
        self.txt_qtde.setFocus()

    def finalizar_venda(self):
        self.venda_finalizada = True
        self.num_itens_adicionados = 0
        self.produtos_adicionados = []
        self.coletar_dados_transacao_entradas()
        self.limpar_campos()
        self.txt_valor_total_pdv.setText("R$ 00.00")
        self.exibir_table_estoque()
        self.exibir_table_relatorio_vendas()

    def conectar_sinais(self):# Conectar o sinal textChanged para disparar o timer de debounce
        self.txt_cod_pdv.textChanged.connect(self.iniciar_busca_com_atraso)
        self.txt_qtde.textChanged.connect(self.atualizar_valor_total)

    def iniciar_busca_com_atraso(self):# Reinicia o timer para realizar a busca após atraso.
        self.timer_busca.start()

    def preencher_campos_produto(self):  # Obtém o código do produto do campo de entrada e remove espaços extras
        
        codigo_produto = self.txt_cod_pdv.text().strip()
        barras_prod = self.txt_cod_pdv.text().strip()


        # Valida se o campo contém um código válido
        if not codigo_produto or len(codigo_produto) == 0:
            return  # Retorna sem fazer nada se o campo estiver vazio ou inválido
        
        # Valida se o campo contém um código válido
        if not barras_prod or len(barras_prod) == 0:
            return  # Retorna sem fazer nada se o campo estiver vazio ou inválido
        
        
        _, _, http_buscar_produto_pdv, _, _, _, _ = self.http_estoque()

        try:
            # Define a URL com base no código ou código de barras
            if codigo_produto:
                url = f"{http_buscar_produto_pdv}?codigo={codigo_produto}"
            elif barras_prod:
                url = f"{http_buscar_produto_pdv}?barras={barras_prod}"
            else:
                raise ValueError("É necessário fornecer um código ou código de barras.")

            # Faz a requisição à API
            response = requests.get(url)
            response.raise_for_status()  # Gera uma exceção se houver erro HTTP
            data = response.json()
            
            # Acessa o dicionário 'produto' corretamente
            produto = data.get("produto")

            if not produto or not isinstance(produto, dict):
                self.exibir_mensagem("Produto não encontrado.", "Erro")
                return
            
            # Obtém os detalhes do produto
            codigo_prod = produto.get("codigo_produto")
            nome = produto.get("nome_produto")
            quantidade_estoque = produto.get("qtda_produto")
            valor_unitario = produto.get("valor_produto")

            # Valida os dados recebidos
            if None in (codigo_prod, nome, quantidade_estoque, valor_unitario):
                self.exibir_mensagem("Dados do produto inválidos.", "Aviso")
                return
            
            try:
                quantidade_selecionada = int(self.txt_qtde.text())
            except ValueError:
                quantidade_selecionada = 0  # ou 1, conforme a lógica do seu sistema

            if not quantidade_selecionada or quantidade_selecionada <= 0:
                self.exibir_mensagem("Selecione uma quantidade válida.", "Aviso")
                return

            # Calcula o subtotal e adiciona o produto à lista
            subtotal = valor_unitario * quantidade_selecionada
            self.produtos_adicionados.append((codigo_prod, nome, quantidade_selecionada, valor_unitario, subtotal))

            # Atualiza a interface com os novos dados
            self.adicionar_item_na_tabela(codigo_prod, nome, quantidade_selecionada, valor_unitario, subtotal)
            self.atualizar_valor_total()
            self.adicionar_item_compra()
            self.adicionar_produto_temp(codigo_prod, quantidade_selecionada)
            
            # Limpa o campo de entrada
            self.txt_cod_pdv.clear()
                   
        except requests.exceptions.RequestException as e:
            self.exibir_mensagem(f"Erro ao consultar a API: {e}", "Erro")
        except ValueError:
            self.exibir_mensagem("Erro ao processar os dados da API.", "Erro") 

    def exibir_mensagem(self, texto, titulo):
        """Exibe uma mensagem simples"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(titulo)
        msg.setText(texto)
        msg.exec()

    """" def atualizar_valor_total(self):  # Função que atualiza o valor total na treeView_pdv

        # Calcula o total somando os subtotais para cada produto
        total = sum(subtotal for _, _, _, _, subtotal in self.produtos_adicionados)

        # Formatar o total com separadores de milhares e duas casas decimais no estilo brasileiro
        valor_total_str = locale.currency(total, grouping=True)
        
        # Exibir o valor total formatado
        self.txt_valor_total_pdv.setText(valor_total_str)

        # Limpar o campo de código
        self.txt_cod_pdv.clear() """

    def calcular_valor_total(self, vl_unitario, qtde):  # Função que calcula o valor total (valor unitário * quantidade)

        try:
            vl_unitario = float(vl_unitario)
            qtde = int(qtde)
        except ValueError:
            return 0  # Retorna 0 para valores inválidos

        # Calcula o valor total
        valor_total = vl_unitario * qtde
        return valor_total 

    def atualizar_valor_total(self):
        
        total = 0.0
        for row in range(self.modelo.rowCount()):
            # Pega o valor da coluna 5 (subtotal) e remove "R$" e vírgula
            valor_item = self.modelo.item(row, 5).text().replace('R$', '').replace(',', '.')
            total += float(valor_item)
        
        # Formatar no padrão brasileiro
        self.txt_valor_total_pdv.setText(f"R$ {total:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

        # Limpar o campo de código
        self.txt_cod_pdv.clear()

    def limpar_campos(self): # FUNÇÃO QUE LIMPA DOS DADOS INSERIDOS NA NFC-e 
    
        self.table_pdv()
        self.txt_valor_total_pdv.setText("R$ 00,00")
        self.produtos_adicionados = []
        self.num_itens_adicionados = 0

    def upgrade_itens_estoque(self): # Atualiza a quantidade de produtos no estoque via API com base nas vendas temporárias. Reduz a quantidade vendida do estoque existente para cada produto.
        
        # Verifica se existem produtos temporários para atualizar
        if not self.produtos_temp:
            self.mostrar_mensagem("Nenhum produto para atualizar no estoque.")
            return

        # Verifica a configuração do HTTP
        if not self.http_estoque() or len(self.http_estoque()) != 7:
            self.mostrar_mensagem("Configuração inválida do HTTP. Verifique os parâmetros.")
            return

        # Definir o endpoint da API para buscar o produto
        _, _, http_buscar_produto_pdv, _, _, _, _ = self.http_estoque()
        http_buscar_produto_pdv = f"{http_buscar_produto_pdv}"

        # Criar um dicionário para armazenar temporariamente as quantidades de produtos
        produtos_estoque_atualizado = {}
        
        try:
            for codigo, quantidade_vendida in self.produtos_temp.items():
                # Consulta a API para obter os dados do produto
                url = f"{http_buscar_produto_pdv}?codigo={codigo}"
                response = requests.get(url)
                response.raise_for_status()  # Gera uma exceção para status HTTP de erro
                data = response.json()

                # Obtém a lista de produtos e verifica se ela contém pelo menos um item
                produto = data.get("produto", None)
                if not produto or not isinstance(produto, dict):
                    self.exibir_mensagem(f"Produto {codigo} não encontrado.", "Erro")
                    continue
                # produto já é um dicionário

                # Obtém os detalhes do produto
                codigo_prod = produto.get("codigo_produto")
                quantidade_estoque = produto.get("qtda_produto")

                if quantidade_estoque is None:
                    self.mostrar_mensagem(f"Quantidade do produto {codigo} não encontrada.")
                    continue

                # Subtrai a quantidade vendida do estoque atual
                nova_quantidade = quantidade_estoque - quantidade_vendida

                if nova_quantidade < 0:
                    self.mostrar_mensagem(f"Estoque insuficiente para o produto {codigo}. Venda não realizada.")
                    continue  # Não processa esse produto

                # Armazenar o código e nova quantidade em um dicionário temporário
                produtos_estoque_atualizado[codigo] = nova_quantidade

            # Definir o endpoint da API para atualizar o produto
            _, _, _, _, _, _, http_up_produt_quantidade = self.http_estoque()
            http_up_produt_quantidade = f"{http_up_produt_quantidade}"

            # Atualizar o estoque dos produtos
            for codigo, nova_quantidade in produtos_estoque_atualizado.items():
                # Coleta os dados de atualização (somente a quantidade)
                dados_atualizacao = {"codigo_produto": codigo, "nova_quantidade": nova_quantidade}

                # Envia os dados usando PATCH para atualização parcial
                response_update = requests.patch(http_up_produt_quantidade, json=dados_atualizacao)
                response_update.raise_for_status()

                # Verifica a resposta da API
                if response_update.status_code == 200:
                    # Exibe mensagem de sucesso
                    pass #self.mostrar_mensagem(f"Produto {codigo} atualizado com sucesso!")
                    # Verifica se a quantidade restante no estoque está baixa
                    if nova_quantidade == 1:
                        QMessageBox.information(
                            self,
                            "Aviso",
                            f"Só resta 1 unidade do produto {codigo} no estoque."
                        )
                    # print(f"Produto {codigo} atualizado com sucesso: {nova_quantidade} unidades restantes.")
                else:
                    self.mostrar_mensagem(f"Erro ao atualizar o produto {codigo}: {response_update.text}")

            # Limpar a lista de produtos temporários após atualizar o estoque
            self.produtos_temp.clear()
            self.exibir_table_estoque()

        except requests.exceptions.RequestException as e:
            self.mostrar_mensagem(f"Erro ao conectar com a API: {e}")
            print(f"Erro ao conectar com a API: {e}")
        except Exception as e:
            print(f"Erro ao atualizar o estoque: {e}")

    def adicionar_produto_temp(self, codigo, quantidade): #Adiciona temporariamente os produtos para que possam ser baixados assim que for finalizada a venda. Retorna o código e a nova quantidade.

        # Adiciona o produto temporariamente
        if codigo in self.produtos_temp:
            self.produtos_temp[codigo] += quantidade
        else:
            self.produtos_temp[codigo] = quantidade

        # Retorna o código e a nova quantidade do produto
        return codigo, self.produtos_temp[codigo]

    def abrir_valor_avulso(self): # abrir a janela para adicionar o valor avuso
        
        dialog = QDialog()
        dialog.setWindowTitle("Adicionar Valor Avulso")
        dialog.setWindowModality(Qt.ApplicationModal)

        layout = QVBoxLayout()
        label_instrucao = QLabel("Digite o valor avulso em R$:")
        layout.addWidget(label_instrucao)

        input_valor = QLineEdit()
        input_valor.setPlaceholderText("Exemplo: 15.00")
        input_valor.setAlignment(Qt.AlignCenter)
        layout.addWidget(input_valor)

        btn_confirmar = QPushButton("Confirmar")
        layout.addWidget(btn_confirmar)

        def confirmar_valor():
            try:
                valor_avulso = float(input_valor.text().replace(',', '.'))
                if valor_avulso <= 0:
                    raise ValueError("O valor deve ser maior que zero.")
                
                # Aqui você pode adicionar direto no carrinho/PDV
                self.adicionar_item_avulso(valor_avulso)

                QMessageBox.information(dialog, "Sucesso", f"Valor avulso adicionado: R$ {valor_avulso:.2f}")
                dialog.accept()
            except ValueError as e:
                QMessageBox.warning(dialog, "Erro", f"Valor inválido: {str(e)}")

        btn_confirmar.clicked.connect(confirmar_valor)
        dialog.setLayout(layout)
        dialog.exec()
            
    def adicionar_item_avulso(self, valor):  # Adiciona um valor avulso como item no carrinho do PDV.
        
        try:
            # Dados do item avulso
            codigo = "9999"
            descricao = "Valor Avulso"
            qtde = 1
            valor_unit = float(valor)
            subtotal = valor_unit * qtde

            # Criar itens da linha
            checkbox_item = QStandardItem()
            checkbox_item.setCheckable(True)
            checkbox_item.setCheckState(Qt.CheckState.Unchecked)

            item_codigo = QStandardItem(str(codigo))
            item_codigo.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_descricao = QStandardItem(descricao)
            item_descricao.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_qtde = QStandardItem(str(qtde))
            item_qtde.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_valor_unit = QStandardItem(f"R$ {valor_unit:.2f}")
            item_valor_unit.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_subtotal = QStandardItem(f"R$ {subtotal:.2f}")
            item_subtotal.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            # Adicionar linha na tabela
            nova_linha = [checkbox_item, item_codigo, item_descricao, item_qtde, item_valor_unit, item_subtotal]
            self.modelo.appendRow(nova_linha)

            # Ajustar aparência e tamanho das colunas
            if hasattr(self, "personalizar_aparencia_tabela"):
                self.personalizar_aparencia_tabela()
            for column in range(self.modelo.columnCount()):
                self.tableView_pdv.resizeColumnToContents(column)

            # Resetar quantidade e rolar até a última linha
            self.txt_qtde.setText("1")
            ultima_linha = self.modelo.rowCount() - 1
            self.tableView_pdv.scrollTo(self.modelo.index(ultima_linha, 0))

            # Atualizar valor total somando todas as linhas da tabela
            total = 0.0
            for row in range(self.modelo.rowCount()):
                valor_item = self.modelo.item(row, 5).text().replace('R$', '').replace(',', '.')
                total += float(valor_item)

            # Atualizar campo txt_valor_total_pdv
            self.txt_valor_total_pdv.setText(f"R$ {total:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

        except Exception as e:
            print(f"Erro ao adicionar valor avulso: {str(e)}")
            QMessageBox.warning(self, "Erro", f"Erro ao adicionar valor avulso: {str(e)}")
            
##################### AREA DA IMPRESSORAS ##############################################
    
    def verifica_impressora_padrao(self): # FAZ A VERIFICAÇÃO DA IMPRESSORA PADRÃO

        default_printer = win32print.GetDefaultPrinter()

        if default_printer:
            self.label_print_default.setText(f"Default printer: {default_printer}")
            return default_printer
        else:
            self.label_print_default.setText("No default printer found.")
            return None

############################################################################   

    def obter_dados_empresa_pdv(self): # FUNÇÃO PAR AOBTER OS DADOS DA EMPRESA PARA COLOCALAR NO NFC-e E SALVA-LOS EM 'dados_empresa.sd'
        dados_empresa_pdv = {}

        try:
            with open('dados_empresa.sd', 'r') as file:
                for line in file:
                    if ':' in line:
                        chave, valor = line.strip().split(':', 1)
                        dados_empresa_pdv[chave.strip()] = valor.strip()
        except FileNotFoundError:
            # Se o arquivo não existir, ou ocorrer algum erro, não fazer nada
            pass

        return dados_empresa_pdv

    def obter_dados_compra_pdv(self): # FUNÇÃO QUE OBTEM OS DADOS DA COMPRA DIRETO DA TELA DO PDV 
        
        dados_compra_pdv = []

        # Percorrer as linhas da treeView_pdv
        for row in range(self.modelo.rowCount()):
            codigo = self.modelo.index(row, 1).data()  # Coluna 1 contém o código
            descricao = self.modelo.index(row, 2).data()  # Coluna 2 contém a descrição
            qtde_str = self.modelo.index(row, 3).data()  # Coluna 3 contém a quantidade
            vl_unitario_str = self.modelo.index(row, 4).data()  # Coluna 4 contém o valor unitário

            # Verificar se qtde_str e vl_unitario_str estão preenchidos
            if qtde_str and vl_unitario_str:
                try:
                    # Remover "R$" e substituir vírgulas por pontos, além de remover espaços em branco
                    qtde = float(qtde_str.replace(",", ".").strip())
                    vl_unitario = float(vl_unitario_str.replace("R$", "").replace(",", ".").strip())
                except ValueError:
                    continue

                # Calcular o subtotal do produto
                subtotal_produto = self.calcular_valor_total(vl_unitario, qtde)

                # Criar o dicionário do produto
                produto = {
                    'Código': codigo,
                    'Descrição': descricao,
                    'Qtde UN': qtde,
                    'Vl Unit': vl_unitario,
                    'Vl Sub-Total': subtotal_produto,
                }

                # Adicionar o produto à lista de dados da compra
                dados_compra_pdv.append(produto)
            else:
                print(f"Valores faltando na linha {row}: Qtde={qtde_str}, Vl Unit={vl_unitario_str}")

        return dados_compra_pdv

    def abrir_pasta_nfe(self): # ABRIR A POSTA DE NFC-e 

        # Diretório onde o programa está instalado
        diretorio_instalacao = os.path.dirname(os.path.abspath(__file__))
        pasta_nfe = os.path.join(diretorio_instalacao, "NFe")

        try:
            # Verifique se a pasta "NFe" existe; se não, crie-a.
            if not os.path.exists(pasta_nfe):
                os.makedirs(pasta_nfe)

            # Obter a data e hora atual para criar o nome do arquivo
            agora = datetime.now()
            agora_data = agora.strftime("%Y-%m-%d")
            agora_hora = agora.strftime("%H-%M-%S")
            nome_arquivo = f"{agora_data}_{agora_hora}.txt"

            caminho_arquivo = os.path.join(pasta_nfe, nome_arquivo)

            # Verificar se a pasta "NFe" existe antes de tentar abri-la
            if os.path.exists(pasta_nfe):
                # Abrir a pasta "NFe" com o programa de gerenciamento de arquivos padrão do sistema
                os.startfile(pasta_nfe)
            else:
                print("A pasta NFe ainda não foi criada.")

        except Exception as e:
            print(f"Erro ao Abrir NFe: {str(e)}")

############################### AREA DO ESTOQUE ############################################################
        
    def exibir_table_estoque(self):

        time.sleep(1) # faz a pausa pra exibir o estoque para que a api possa carrega os dados

        http_estoque_exibir, _, _, _, _, _, _ = self.http_estoque()

        request_estoque = http_estoque_exibir
        try:
            # Fazer a requisição para a API do estoque
            response = requests.get(request_estoque)
            if response.status_code == 200:
                dados_estoque = response.json().get("estoque", [])
            else:
                raise Exception(f"Erro ao acessar API: {response.status_code}")

            # Modelo de exibição da tabela
            self.modelo_exibir_estoque = QStandardItemModel()
            header_labels_exibir_estoque = ['Check', 'Código', 'Código Barras', 'Nome', 'Descrição', 
                                        'Quantidade', 'Unidade', 'Valor da Compra', 'Valor da Venda']
            self.modelo_exibir_estoque.setHorizontalHeaderLabels(header_labels_exibir_estoque)
            self.tableView_estoque.setModel(self.modelo_exibir_estoque)
            self.modelo_exibir_estoque.removeRows(0, self.modelo_exibir_estoque.rowCount())
            self.modelo_exibir_estoque.setRowCount(len(dados_estoque))

            # Configuração do formato de moeda
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

            # Adicionando os dados na tabela
            for row, data_row in enumerate(dados_estoque):
                # Adiciona o checkbox na primeira coluna
                item_checkbox = QStandardItem()
                item_checkbox.setCheckable(True)
                item_checkbox.setCheckState(Qt.Unchecked)
                self.modelo_exibir_estoque.setItem(row, 0, item_checkbox)

                # Mapeia as chaves do dicionário para as colunas
                colunas = [
                    data_row.get("codigo_produto", ""),
                    data_row.get("barras_prod", ""),
                    data_row.get("nome_produto", ""),
                    data_row.get("descricao_produto", ""),
                    data_row.get("qtda_produto", ""),
                    data_row.get("uni_pcto_produto", ""),
                    data_row.get("valor_compra", ""),
                    data_row.get("valor_produto", "")
                ]

                for col, item_data in enumerate(colunas):
                    item = QStandardItem(str(item_data))

                    # Formatação monetária nas colunas de Valor da Compra e Valor do Produto
                    if col == 6:  # Índice para "Valor da Compra"
                        formatted_value = locale.currency(float(item_data), symbol=True, grouping=True)
                        item.setData(formatted_value, Qt.DisplayRole)
                    elif col == 7:  # Índice para "Valor do Produto"
                        formatted_value = locale.currency(float(item_data), symbol=True, grouping=True)
                        item.setData(formatted_value, Qt.DisplayRole)
                    else:
                        item.setData(str(item_data), Qt.DisplayRole)

                    self.modelo_exibir_estoque.setItem(row, col + 1, item)

                    # Formatação de estilo alternado para as linhas
                    if row % 2 == 0:
                        item.setBackground(QColor(150, 149, 237, 50))
                        item.setForeground(QColor(255, 255, 255))  # Cor branca para o texto
                        font = QFont()
                        font.setBold(True)
                        font.setPointSize(12)
                        item.setFont(font)
                    else:
                        item.setBackground(QColor(173, 216, 230, 150))
                        item.setForeground(QColor(255, 255, 255))  # Cor branca para o texto
                        font = QFont()
                        font.setBold(True)
                        font.setPointSize(12)
                        item.setFont(font) 

            # Configuração de estilo da tabela
            self.tableView_estoque.setShowGrid(False)
            self.tableView_estoque.setStyleSheet(''' 
                QHeaderView::section {
                    background-color: #ffffff; 
                    color: #0000FF;
                    border: 1px solid #cccccc;
                    padding: 1px;
                    border-radius: 3px;
                    font-size: 12px;
                    font-weight: bold;
                    text-align: center;
                }
                QTableView {
                    font-size: 12px;
                    selection-background-color: #d0e0f0;
                    selection-color: #000000;
                }
                QMenu {
                    background-color: rgb(000, 000, 000);
                    color: white;
                    font-size: 12px;
                }
                QScrollBar:vertical {
                    background-color: rgb(135,206,250);
                }
                QScrollBar::handle:vertical {
                    background-color: rgb(57, 69, 104);
                }
                QScrollBar::add-line:vertical,
                QScrollBar::sub-line:vertical {
                    background: none;
                }
                QScrollBar::add-page:vertical,
                QScrollBar::sub-page:vertical {
                    background: none;
                }
                QScrollBar:horizontal {
                    background-color: rgb(135,206,250);
                }
                QScrollBar::handle:horizontal {
                    background-color: rgb(57, 69, 104);
                }
                QScrollBar::add-line:horizontal,
                QScrollBar::sub-line:horizontal {
                    background: none;
                }
                QScrollBar::add-page:horizontal,
                QScrollBar::sub-page:horizontal {
                    background: none;
                }
            ''')

            self.tableView_estoque.resizeColumnsToContents()
            self.tableView_estoque.resizeRowsToContents()

        except Exception as e:
            pass
            
    def inserir_prod_estoque(self):  # Inserir produtos no estoque via API

        # Obtenha os valores dos campos da interface do usuário
        tipo_produto = self.comboBox_tipo_produto.currentText()  # Tipo de produto selecionado
        barras_prod = self.txt_codigo_prod.text()
        nome_produto = self.txt_nome_prod.text()
        descricao_produto = self.txt_des_prod.text()
        valor_compra = self.txt_valor_compra.text().replace(',', '').replace('.', '')  # Ajuste para valores
        qtda_produto = self.txt_qtd_prod.text()
        uni_pcto_produto = self.comboBox_uni_pcto.currentText()
        valor_produto = self.txt_valor_prod.text().replace(',', '').replace('.', '')  # Ajuste para valores

        # Dicionário de tipos de produtos e seus códigos
        tipos_produto = {
            "Alimentos de Cozinha, Cod - 400": "400",
            "Alimentos Não Perecíveis, Cod - 300": "300",
            "Alimentos Perecíveis, Cod - 270": "270",
            "Bebidas Alcoólicas, Cod - 150": "150",
            "Bebidas em Garrafa, Cod - 100": "100",
            "Bebidas em Lata, Cod - 200": "200",
            "Bebidas Energéticas, Cod - 160": "160",
            "Calçados, Cod - 310": "310",
            "Carnes e Aves, Cod - 800": "800",
            "Condimentos e Temperos, Cod - 170": "170",
            "Cosméticos, Cod - 320": "320",
            "Doces e Sobremesas, Cod - 210": "210",
            "Farinhas e Massas, Cod - 222": "222",
            "Frutas, Cod - 101": "101",
            "Grãos e Cereais, Cod - 120": "120",
            "Higiene Pessoal, Cod - 600": "600",
            "Laticínios, Cod - 700": "700",
            "Legumes e Verduras, Cod - 110": "110",
            "Outros, Cod - 290": "290",
            "Padaria e Confeitaria, Cod - 140": "140",
            "Papéis e Escritório, Cod - 260": "260",
            "Peixes e Frutos do Mar, Cod - 900": "900",
            "Pet Shop, Cod - 240": "240",
            "Produção Própria, Cod - 280": "280",
            "Produtos Congelados, Cod - 130": "130",
            "Produtos de Limpeza, Cod - 500": "500",
            "Produtos Naturais, Cod - 220": "220",
            "Snacks e Petiscos, Cod - 180": "180",
            "Sopas e Enlatados, Cod - 190": "190",
            "Suplementos Alimentares, Cod - 230": "230",
            "Utensílios de Cozinha, Cod - 250": "250",
            # ========================
            # Materiais de Construção
            # ========================
            "Cimento e Argamassa, Cod - 501": "501",
            "Areia e Brita, Cod - 502": "502",
            "Tijolos e Blocos, Cod - 503": "503",
            "Telhas e Coberturas, Cod - 504": "504",
            "Tintas e Corantes, Cod - 505": "505",
            "Ferragens e Parafusos, Cod - 506": "506",
            "Madeiras e Compensados, Cod - 507": "507",
            "Tubos e Conexões, Cod - 508": "508",
            "Elétrica e Iluminação, Cod - 509": "509",
            "Hidráulica, Cod - 510": "510",
            "Pisos e Revestimentos, Cod - 511": "511",
            "Portas e Janelas, Cod - 512": "512",
            "Ferramentas, Cod - 513": "513",
            "EPIs e Segurança, Cod - 514": "514",
            "Vedantes e Impermeabilizantes, Cod - 515": "515",
        }

        # Valida o tipo de produto
        tipo_codigo = tipos_produto.get(tipo_produto)
        if not tipo_codigo:
            self.mostrar_mensagem("Tipo de produto inválido.")
            return

        try:
            # Converte valores para o formato correto
            valor_compra = float(valor_compra) / 100
            valor_produto = float(valor_produto) / 100
            qtda_produto = int(qtda_produto)  # Certifique-se de que a quantidade é um número inteiro

            # Gera o código do produto
            sufixo_codigo = barras_prod[-3:] if len(barras_prod) >= 3 else barras_prod.zfill(3)
            codigo_produto = f"{tipo_codigo}{sufixo_codigo}"

            # Obtendo a URL de inserção de produto
            _, _, _, url_inserir_produto, _, _, _ = self.http_estoque()

            # Enviando os dados como parâmetros de consulta (query params)
            response = requests.post(
                url_inserir_produto,
                params={
                    "codigo_produto": codigo_produto,
                    "barras": barras_prod,
                    "nome": nome_produto,
                    "descricao": descricao_produto,
                    "quantidade": qtda_produto,
                    "unidade": uni_pcto_produto,
                    "valor_compra": valor_compra,
                    "valor_venda": valor_produto
                }
            )
            if response.status_code == 200:
                # Limpa os campos da interface
                self.txt_codigo_prod.clear()
                self.txt_nome_prod.clear()
                self.txt_des_prod.clear()
                self.comboBox_tipo_produto.setCurrentIndex(0)
                self.txt_valor_compra.clear()
                self.txt_qtd_prod.clear()
                self.comboBox_uni_pcto.setCurrentIndex(0)
                self.txt_valor_prod.clear()

                self.exibir_table_estoque()  # Atualiza a tabela de estoque
                self.mostrar_mensagem("Produto inserido com sucesso.")
            else:
                self.mostrar_mensagem(f"Erro ao inserir produto: {response.text}")

        except Exception as e:
            self.mostrar_mensagem(f"Erro ao adicionar produto: {e}")       

    def excluir_prod_estoque(self):  # Realiza a exclusão dos produtos marcados para exclusão
        model = self.tableView_estoque.model()

        if not model:
            self.mostrar_mensagem("Nenhum produto selecionado para exclusão")
            return

        ids_a_excluir = []

        # Obtém os IDs dos produtos marcados para exclusão
        for row in range(model.rowCount()):
            cell_item = model.item(row, 0)  # Coluna do checkbox
            if cell_item and cell_item.isCheckable() and cell_item.checkState() == Qt.Checked:
                id_item = model.item(row, 1).text()  # Coluna do ID do produto
                ids_a_excluir.append(id_item)

        if not ids_a_excluir:
            self.mostrar_mensagem("Nenhum produto marcado para exclusão")
            return

        # Mensagem de confirmação
        confirm_msg = QMessageBox()
        confirm_msg.setIcon(QMessageBox.Question)
        confirm_msg.setWindowTitle("Confirmação")
        confirm_msg.setText("Você realmente deseja excluir o(s) item(s) marcado(s) do estoque?")
        confirm_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        if confirm_msg.exec() == QMessageBox.Yes:
            # URL da API de exclusão do produto
            _, _, _, _, http_excluir_produto, _, _, = self.http_estoque()
            api_url = http_excluir_produto
            
            # ✅ Corrigido — enviar como dicionário JSON
            dados = {"ids_a_excluir": ids_a_excluir}

            try:
                response = requests.post(api_url, json=dados)
                if response.status_code == 200:
                    self.mostrar_mensagem("Produto(s) excluído(s) com sucesso.")
                    self.exibir_table_estoque()  # Atualiza a tabela após a exclusão
                else:
                    self.mostrar_mensagem(f"Erro ao excluir os produtos: {response.text}")
            except requests.exceptions.RequestException as e:
                self.mostrar_mensagem(f"Erro de conexão com a API: {e}")
                print(f"Erro de conexão com a API: {e}")
                
    def mostrar_mensagem(self, mensagem):
        # Exiba uma mensagem de sucesso
        msg = QMessageBox()
        msg.setWindowTitle("Aviso")
        msg.setText(mensagem)
        msg.exec()

    def marcar_todos_itens(self, marcar=True): # marca todos os itens da table do estoque para exclusão

        row_count = self.modelo_exibir_estoque.rowCount()
        for row in range(row_count):
            item = self.modelo_exibir_estoque.item(row, 0)  # Acessa a primeira coluna (caixa de seleção)
            if item is not None:
                item.setCheckState(Qt.Checked if marcar else Qt.Unchecked)

    def on_radioButton_excluir_todos_toggled(self, checked): # Função a ser conectada ao sinal do radioButton_excluir_todos
        self.marcar_todos_itens(marcar=checked)

    def buscar_prod_estoque(self, texto_pesquisa=None): # REALIZAR A BUSCA DO ESTOQUE
        
        try:
            texto_pesquisa = self.txt_pesquisa_prod.text().strip()

            if not texto_pesquisa:
                self.exibir_table_estoque()  # Exibe todos os produtos se não houver pesquisa
                return

            model = self.tableView_estoque.model()
            model.removeRows(0, model.rowCount())

            banco_estoque = Banco_Estoque()
            conexao = banco_estoque.conectar_ao_sqlite()
            produtos_encontrados = banco_estoque.buscar_produto(texto_pesquisa)

            if self.tableView_estoque.model() is None:
                modelo_exibir_estoque = QStandardItemModel()
                header_labels_exibir_estoque = ['Check', 'Código', 'Código Barras', 'Nome', 'Descrição', 'Quantidade', 'Valor da Compra', 'Valor da Venda']
                modelo_exibir_estoque.setHorizontalHeaderLabels(header_labels_exibir_estoque)
                self.tableView_estoque.setModel(modelo_exibir_estoque)

            modelo_exibir_estoque = self.tableView_estoque.model()
            modelo_exibir_estoque.removeRows(0, modelo_exibir_estoque.rowCount())

            modelo_exibir_estoque.setRowCount(len(produtos_encontrados))
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

            for row, data in enumerate(produtos_encontrados):
                item_radio_button = QStandardItem()
                item_radio_button.setCheckable(True)
                item_radio_button.setCheckState(Qt.Unchecked)
                modelo_exibir_estoque.setItem(row, 0, item_radio_button)

                for col, item_data in enumerate(data):
                    item = QStandardItem(str(item_data))
                    
                    if col == 6:  # Coluna de quantidade
                        quantidade = int(item_data)
                        if quantidade <= 0:
                            continue

                    if col == 7:  # Coluna de valor
                        formatted_value = locale.currency(float(item_data), grouping=True)
                        item.setData(formatted_value, Qt.DisplayRole)

                    modelo_exibir_estoque.setItem(row, col + 1, item)

                    # Personalize as células da tabela
                    if row % 2 == 0:
                        item.setBackground(QColor(150, 149, 237, 0.2))
                        item.setForeground(QColor(255, 255, 255))  # Cor branca para o texto
                        font = QFont()
                        font.setBold(True)
                        font.setPointSize(14)  # Fonte de tamanho 14
                        item.setFont(font)
                    else:
                        item.setBackground(QColor(173, 216, 230, 0.6))
                        item.setForeground(QColor(255, 255, 255))  # Cor branca para o texto
                        font = QFont()
                        font.setBold(True)
                        font.setPointSize(14)
                        item.setFont(font)

            # Personalize o cabeçalho e a tabela
            self.tableView_estoque.setShowGrid(False)
            self.tableView_estoque.setStyleSheet('''
                QHeaderView::section {
                    background-color: #ffffff; 
                    color: #0000FF;
                    border: 1px solid #cccccc;
                    padding: 1px;
                    border-radius: 5px;
                    font-size: 12px;
                    font-weight: bold;
                    text-align: center;
                }
                QTableView {
                    font-size: 12px;
                    selection-background-color: #d0e0f0;
                    selection-color: #000000;
                }
            ''')

            self.tableView_estoque.resizeColumnsToContents()
            self.tableView_estoque.resizeRowsToContents()

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao buscar produto(s) no banco de dados: {e}")
            msg.setStyleSheet("color: black;")
            msg.exec()
            print(e)

    def funcao_combobox_tipo_produtos(self):
        
        self.comboBox_tipo_produto.addItems([
            "Alimentos de Cozinha, Cod - 400",
            "Alimentos Não Perecíveis, Cod - 300",
            "Alimentos Perecíveis, Cod - 270",
            "Bebidas Alcoólicas, Cod - 150",
            "Bebidas em Garrafa, Cod - 100",
            "Bebidas em Lata, Cod - 200",
            "Bebidas Energéticas, Cod - 160",
            "Calçados, Cod - 310",
            "Carnes e Aves, Cod - 800",
            "Condimentos e Temperos, Cod - 170",
            "Cosméticos, Cod - 320",
            "Doces e Sobremesas, Cod - 210",
            "Farinhas e Massas, Cod - 222",
            "Frutas, Cod - 101",
            "Grãos e Cereais, Cod - 120",
            "Higiene Pessoal, Cod - 600",
            "Laticínios, Cod - 700",
            "Legumes e Verduras, Cod - 110",
            "Outros, Cod - 290",
            "Padaria e Confeitaria, Cod - 140",
            "Papéis e Escritório, Cod - 260",
            "Peixes e Frutos do Mar, Cod - 900",
            "Pet Shop, Cod - 240",
            "Produção Própria, Cod - 280",
            "Produtos Congelados, Cod - 130",
            "Produtos de Limpeza, Cod - 500",
            "Produtos Naturais, Cod - 220",
            "Snacks e Petiscos, Cod - 180",
            "Sopas e Enlatados, Cod - 190",
            "Suplementos Alimentares, Cod - 230",
            "Utensílios de Cozinha, Cod - 250",
            "Cimento e Argamassa, Cod - 501",
            "Areia e Brita, Cod - 502",
            "Tijolos e Blocos, Cod - 503",
            "Telhas e Coberturas, Cod - 504",
            "Tintas e Corantes, Cod - 505",
            "Ferragens e Parafusos, Cod - 506",
            "Madeiras e Compensados, Cod - 507",
            "Tubos e Conexões, Cod - 508",
            "Elétrica e Iluminação, Cod - 509",
            "Hidráulica, Cod - 510",
            "Pisos e Revestimentos, Cod - 511",
            "Portas e Janelas, Cod - 512",
            "Ferramentas, Cod - 513",
            "EPIs e Segurança, Cod - 514",
            "Vedantes e Impermeabilizantes, Cod - 515"
            ])

############################################### AREA DO FINANCEIRO #############################################################
    
    def clear_bd_finaceiro(self): # realizar a limpeza dos dados do banco transações de entradas e saidas

        try:
            # Confirmar exclusão
            confirm_msg = QMessageBox()
            confirm_msg.setIcon(QMessageBox.Icon.Question)
            confirm_msg.setWindowTitle("Confirmação")
            confirm_msg.setText("Você realmente deseja excluir todos os dados financeiros?")
            confirm_msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            confirm_msg.setDefaultButton(QMessageBox.StandardButton.No)
            confirm_msg.button(QMessageBox.StandardButton.Yes).setText("Sim")
            confirm_msg.button(QMessageBox.StandardButton.No).setText("Não")
            confirm_msg.setStyleSheet("color: black;")
            response = confirm_msg.exec()

            if response == QMessageBox.No:
                return

            # Limpar os dados do banco financeiro
            banco_cf = CONTROLE_FINANCEIRO()
            banco_cf.conectar_ao_sqlite()
            banco_cf.limpar_tabelas()

            # realiza a atualiza da tabela apos excluir tudo
            self.exibir_table_relatorio_vendas()

            # Exibir mensagem de sucesso
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("Aviso")
            msg.setText("Sucesso: Todos os dados financeiros foram excluídos com sucesso!")
            msg.setStyleSheet("color: black;")
            msg.exec()

        except Exception as e:
            # Lidar com exceções
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao excluir os dados financeiros: {e}")
            msg.setStyleSheet("color: black;")
            msg.exec()
        
    def coletar_dados_transacao_entradas(self):
        
        try:
            # Pegar o valor total diretamente do campo de texto do PDV
            valor_recebido_pdv_str = self.txt_valor_total_pdv.text()  # Ex.: "R$ 123,45"
            valor_formato_pdv = float(valor_recebido_pdv_str.replace("R$ ", "").replace(".", "").replace(",", "."))

        except (ValueError, AttributeError):
            print("Erro: valor total inválido ou campo não encontrado")
            return False

        # Pegar a forma de pagamento diretamente do comboBox da tela de finalização
        try:
            metodo_pagamento = self.comboBox_forma_pgto_tela_finalizar_venda.currentText()
        except AttributeError:
            print("Erro: comboBox de forma de pagamento não encontrado")
            return False

        descricao = f'Venda no PDV por {self.label_operador.text()}'

        if valor_formato_pdv > 0 and metodo_pagamento:
            try:
                banco_cf = CONTROLE_FINANCEIRO()
                cn = banco_cf.conectar_ao_sqlite()
                banco_cf.inserir_transacao('Entrada', metodo_pagamento, valor_formato_pdv, descricao)
                return True
            except Exception as e:
                print("Erro ao coletar dados de transação:", str(e))
                return False
        else:
            return False
        
    def exibir_table_relatorio_vendas(self): # exibir table relatorio somente de vendas "entradas" e "Saidas"
               
        try:
            # Configurar o formato de moeda temporariamente
            try:
                locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
            except locale.Error:
                pass  # Se a configuração falhar, continue sem modificar o locale

            banco_cf = CONTROLE_FINANCEIRO()
            transacoes = banco_cf.exibir_dados_transacoes()  # Obter os dados das transações

            # Se não houver transações, limpar tabela e sair
            if not transacoes:
                self.tableWidget_relatorio_entradas.setRowCount(0)
                return

            # Ordenar transações pela data/hora (timestamp) do mais recente para o mais antigo
            # Supondo que o timestamp seja uma string no formato "YYYY-MM-DD HH:MM:SS"
            transacoes.sort(key=lambda x: x[3], reverse=True)

            # Limpar o conteúdo atual da tabela
            self.tableWidget_relatorio_entradas.clearContents()
            self.tableWidget_relatorio_entradas.setRowCount(len(transacoes))

            for row, transacao in enumerate(transacoes):
                tipo_receita, forma_pagamento, valor_recebido_pdv, timestamp, descricao = transacao
                valor_formatado = locale.currency(float(valor_recebido_pdv), grouping=True)

                self.tableWidget_relatorio_entradas.setItem(row, 0, QTableWidgetItem(tipo_receita))
                self.tableWidget_relatorio_entradas.setItem(row, 1, QTableWidgetItem(forma_pagamento))
                self.tableWidget_relatorio_entradas.setItem(row, 2, QTableWidgetItem(valor_formatado))
                self.tableWidget_relatorio_entradas.setItem(row, 3, QTableWidgetItem(timestamp))
                self.tableWidget_relatorio_entradas.setItem(row, 4, QTableWidgetItem(descricao))

                # Personalizar as células da tabela
                for col in range(5):
                    item = self.tableWidget_relatorio_entradas.item(row, col)
                    item.setForeground(QColor(255, 255, 255))
                    font = QFont()
                    font.setBold(True)
                    font.setPointSize(12)
                    item.setFont(font)
                    # Alternar cor de fundo para visual mais agradável
                    if row % 2 == 0:
                        item.setBackground(QColor(150, 149, 237, 0.2))
                    else:
                        item.setBackground(QColor(100, 100, 200, 0.1))
            
            # Ocultar as linhas das colunas 
            self.tableWidget_relatorio_entradas.setShowGrid(False)
            
            # Personalizar a tabela de relatório de vendas
            self.tableWidget_relatorio_entradas.setStyleSheet('''
                QHeaderView::section {
                    background-color: #ffffff; 
                    color: #0000FF;
                    border: 1px solid #cccccc;
                    padding: 1px;
                    border-radius: 3px;
                    font-size: 12px;
                    font-weight: bold;
                    text-align: center;
                }
                QTableView {
                    font-size: 12px;
                    selection-background-color: #d0e0f0;
                    selection-color: #000000;
                }
                QMenu {
                    background-color: rgb(000, 000, 000);
                    color: white;
                    font-size: 12px;
                }
                QScrollBar:vertical {
                    background-color: rgb(135,206,250);
                }
                QScrollBar::handle:vertical {
                    background-color: rgb(57, 69, 104);
                }
                QScrollBar::add-line:vertical,
                QScrollBar::sub-line:vertical {
                    background: none;
                }
                QScrollBar::add-page:vertical,
                QScrollBar::sub-page:vertical {
                    background: none;
                }
                QScrollBar:horizontal {
                    background-color: rgb(135,206,250);
                }
                QScrollBar::handle:horizontal {
                    background-color: rgb(57, 69, 104);
                }
                QScrollBar::add-line:horizontal,
                QScrollBar::sub-line:horizontal {
                    background: none;
                }
                QScrollBar::add-page:horizontal,
                QScrollBar::sub-page:horizontal {
                    background: none;
                }
            ''')

            # Ajustes visuais da tabela
            self.tableWidget_relatorio_entradas.sortItems(1, Qt.SortOrder.AscendingOrder)  # Classifica a coluna "Valor Pago" em ordem ascendente
            self.tableWidget_relatorio_entradas.resizeColumnsToContents()  # Ajusta o tamanho das colunas
            self.tableWidget_relatorio_entradas.resizeRowsToContents()  # Ajusta o tamanho das linhas
         
        except Exception as e:
            print("Erro ao exibir tabela de relatório de vendas:", str(e))

    def on_checkbox_entradas_changed(self, state): # FAZ O CHECK DAS ENTRADAS
        if state == Qt.Checked:
            self.checkBox_saidas.setChecked(False)
        self.filtrar_e_atualizar_tabela()

    def on_checkbox_saidas_changed(self, state): # FAZ O CHECK DAS SAIDAS
        
        if state == Qt.Checked:
            self.checkBox_entradas.setChecked(False)
        self.filtrar_e_atualizar_tabela()

    def filtrar_e_atualizar_tabela(self): # FILTRAR E ATUALIZAR A TABELA
        
        tipo_transacao = None
        forma_pagamento = None

        # Verificar qual QCheckBox de tipo de transação está marcado
        if self.checkBox_entradas.isChecked():
            tipo_transacao = 'Entrada'
        elif self.checkBox_saidas.isChecked():
            tipo_transacao = 'Saída'
        else:
            return

        # Verificar qual QRadioButton de forma de pagamento está marcado
        if self.radioButton_tudo.isChecked():
            forma_pagamento = 'Tudo'
        elif self.radioButton_dinheiro.isChecked():
            forma_pagamento = 'Dinheiro'
        elif self.radioButton_c_credito.isChecked():
            forma_pagamento = 'Cartão de Crédito'
        elif self.radioButton_c_debito.isChecked():
            forma_pagamento = 'Cartão de Débito'
        elif self.radioButton_pix.isChecked():
            forma_pagamento = 'Pix'
        else:
            return

        # Filtrar as transações por tipo de transação e forma de pagamento
        banco_cf = CONTROLE_FINANCEIRO()  # Supondo que CFENTRADA é a classe responsável pelo acesso ao banco de dados
        transacoes_filtradas = banco_cf.filtrar_por_forma_pagamento(tipo_transacao, forma_pagamento)

        # Atualizar a tabela com os dados filtrados
        self.atualizar_tabela_transacoes(transacoes_filtradas)
    
    def atualizar_tabela_transacoes(self, transacoes): # ATUALIZAR TABELA DE TRANSAÇÕES

        # Limpar o conteúdo atual da tabela
        self.tableWidget_relatorio_entradas.setRowCount(0)

        # Atualizar o número de linhas da tabela com base nos dados filtrados
        self.tableWidget_relatorio_entradas.setRowCount(len(transacoes))

        # Preencher a tabela com os dados filtrados e aplicar personalizações visuais
        for row, transacao in enumerate(transacoes):
            for col, valor in enumerate(transacao):
                item = QTableWidgetItem(str(valor))
                self.tableWidget_relatorio_entradas.setItem(row, col, item)

                # Personalizar as células da tabela
                if row % 2 == 0:
                    item.setBackground(QColor(150, 149, 237, 0.2))
                else:
                    item.setBackground(QColor(173, 216, 230, 0.6))

                # Personalizar a cor da fonte e o tamanho das letras
                item.setForeground(QColor(255, 255, 255))  # Definir a cor da fonte (Branca)
                font = QFont()
                font.setBold(True)  # Definir o texto em negrito
                font.setPointSize(12)  # Definir o tamanho da fonte para 10 pontos
                item.setFont(font)

        # Atualizar outras configurações da tabela (ex: redimensionar colunas, definir cores, etc.)
        self.tableWidget_relatorio_entradas.sortItems(1, Qt.SortOrder.AscendingOrder)
        self.tableWidget_relatorio_entradas.resizeColumnsToContents()

    def gerar_relatorio_excel(self): # Gera o relatorio em formato xlsx (Excel) 

        hora_atual = QTime.currentTime()
        self.time_text = hora_atual.toString('hh:mm:ss')

        data_atual = datetime.now()
        self.data_formatada = data_atual.strftime('%d/%m/%Y')

        banco_cf = CONTROLE_FINANCEIRO()
        
        # Obter receita final
        receita_final = banco_cf.calculo_receita_final()
        receita_entradas = banco_cf.somar_todas_entradas()
        receita_saidas = banco_cf.somar_todas_saidas()

        # Obtem Listar das receitas
        list_entradas = banco_cf.obter_list_entradas()
        list_saidas = banco_cf.obter_list_saidas()

        # Acessando os valores do dicionário pelas chaves
        list_entrada_dinheiro = list_entradas.get('Dinheiro', 0)
        list_entrada_cartao_credito = list_entradas.get('Cartão de Crédito', 0)
        list_entrada_cartao_debito = list_entradas.get('Cartão de Débito', 0)
        list_entrada_pix = list_entradas.get('Pix', 0)

        list_saida_dinheiro = list_saidas.get('Dinheiro', 0)
        list_saida_cartao_credito = list_saidas.get('Cartão de Crédito', 0)
        list_saida_cartao_debito = list_saidas.get('Cartão de Débito', 0)
        list_saida_pix = list_saidas.get('Pix', 0)

        # Configurar o formato de moeda
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

        # Converter receita_entradas para float antes de formatar como moeda
        receita_entradas_num = float(receita_entradas)
        self.entrada_total = locale.currency(receita_entradas_num, grouping=True)
    
        entrada_dinheiro_num = float(list_entrada_dinheiro)
        self.entrada_dinheiro = locale.currency(entrada_dinheiro_num, grouping=True)

        entrada_cartao_credito_num = float(list_entrada_cartao_credito)
        self.entrada_cartao_credito= locale.currency(entrada_cartao_credito_num, grouping=True)

        entrada_cartao_debito_num = float(list_entrada_cartao_debito)
        self.entrada_cartao_debito = locale.currency(entrada_cartao_debito_num, grouping=True)

        entrada_pix_num = float(list_entrada_pix)
        self.entrada_pix = locale.currency(entrada_pix_num, grouping=True)

        # Converter receita_saidas para float antes de formatar como moeda
        apurado_saidas_num = float(receita_saidas)
        self.saida_total = locale.currency(apurado_saidas_num, grouping=True)

        saida_dinheiro_num = float(list_saida_dinheiro)
        self.saida_dinheiro = locale.currency(saida_dinheiro_num, grouping=True)

        saida_cartao_credito_num = float(list_saida_cartao_credito)
        self.saida_cartao_credito= locale.currency(saida_cartao_credito_num, grouping=True)

        saida_cartao_debito_num = float(list_saida_cartao_debito)
        self.saida_cartao_debito = locale.currency(saida_cartao_debito_num, grouping=True)

        saida_pix_num = float(list_saida_pix)
        self.saida_pix = locale.currency(saida_pix_num, grouping=True)

        # Converter receita_final para float antes de formatar como moeda
        receita_final_num = float(receita_final)
        self.receita_final = locale.currency(receita_final_num, grouping=True)

        receita_entradas_num = float(receita_entradas)
        self.receita_entradas = locale.currency(receita_entradas_num, grouping=True)

        receita_saidas_num = float(receita_saidas)
        self.receita_saidas = locale.currency(receita_saidas_num, grouping=True)

        # Criar DataFrame com os dados
        dados = {

            'Planilha Relatório Geral': ['Descrição:', 'Dinheiro', 'Cartão de Crédito', 'Cartão de Débito', 'Pix', 'Total de Entradas', ' ', 'Dinheiro', 'Cartão de Crédito', 'Cartão de Débito', 'Pix', 'Total de Saídas', ' ', 'Receitas de Entradas', 'Receitas de Saídas', 'Saldo Final'],
            ' ': ['Categoria:', 'Receitas de Entradas', 'Receitas de Entradas', 'Receitas de Entradas', 'Receitas de Entradas', 'Total de Entradas', ' ', 'Receitas de Saídas', 'Receitas de Saídas', 'Receitas de Saídas', 'Receitas de Saídas', 'Total das Saídas', ' ', ' ', ' ', ' '],
            '  ': ['Valor:', self.entrada_dinheiro, self.entrada_cartao_credito, self.entrada_cartao_debito, self.entrada_pix, self.entrada_total, ' ', self.saida_dinheiro, self.saida_cartao_credito, self.saida_cartao_debito, self.saida_pix, self.saida_total, ' ', self.receita_entradas, self.receita_saidas, self.receita_final]
            }

        df = pd.DataFrame(dados)

         # Criar nome do arquivo com a data e hora atual
        nome_arquivo = f'Relatorios_Gerais_{self.data_formatada.replace("/", "-").replace(":", "").replace(" ", "-")}.xlsx'
        
        # Caminho completo para a pasta na área de trabalho
        caminho_pasta = os.path.expanduser("~/Desktop/Relatorios Gerais")
        
        # Verificar se a pasta não existe e criá-la
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)

        # Caminho completo para o arquivo Excel
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

        # Salvar o DataFrame como um arquivo Excel
        df.to_excel(caminho_arquivo, index=False)

        # Exibir mensagem de sucesso
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Relatório Excel")
        msg.setText(f"O relatório foi salvo em {caminho_arquivo}")
        msg.exec()

    def corte_papel_cupom_relatorio(self, tipo_impressora='default'):# FUNÇÃO QUE REALIZAR O CORTE DO PAPEL DA CUPOM RELATORIOS
        
        try:
            # Enviar comando de corte do papel para a impressora
            printer_name = self.verifica_impressora_padrao_tela_relatorio()
            hPrinter = win32print.OpenPrinter(str(printer_name))

            # Escolher o escape code com base no tipo de impressora
            if tipo_impressora == 'argox':
                escape_code = b'\x1B\x6D'  # Comandos específicos para ARGOX
            elif tipo_impressora == 'bema':
                escape_code = b'\x1B\x6E'  # Comandos específicos para BEMA
            else:
                escape_code = b'\x1B\x69'  # Escape code padrão para epson

            # Certificar-se de que o documento está aberto antes de enviar o comando de corte
            win32print.StartDocPrinter(hPrinter, 1, ("CupomRelatorio", None, "RAW"))  # type: ignore
            win32print.StartPagePrinter(hPrinter)
            win32print.WritePrinter(hPrinter, escape_code)  # type: ignore
            win32print.EndPagePrinter(hPrinter)
            win32print.EndDocPrinter(hPrinter)

            print("Corte de papel realizado com sucesso.")

        except Exception as e:
            print("Erro ao cortar papel:", str(e))

    def print_relatorio(self): # função que imprimi o cupom de raltorio geral
        
        try:
            # Chamada da função renomeada
            texto_cupom_relatorio = self.gerar_cupom_relatorio()

            if texto_cupom_relatorio is not None and isinstance(texto_cupom_relatorio, str):
                nome_impressora = self.verifica_impressora_padrao_tela_relatorio()

                if not nome_impressora:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Icon.Warning)
                    msg.setWindowTitle("Erro")
                    msg.setText("A impressora padrão não está definida 1.")
                    msg.exec()
                    return

                hPrinter = win32print.OpenPrinter(nome_impressora)
                win32print.StartDocPrinter(hPrinter, 1, ("CupomRelatorio", None, "RAW"))
                win32print.StartPagePrinter(hPrinter)

                # Tente com 'windows-1252' ou outro encoding
                cupom_texto_bytes = texto_cupom_relatorio.encode('windows-1252') # \\\ Windows-1252 (CP1252) Suporta os caracteres necessários para a língua portuguesa, incluindo caracteres especiais como ç, ã, e ~.\\\
                win32print.WritePrinter(hPrinter, cupom_texto_bytes)

                win32print.EndPagePrinter(hPrinter)
                win32print.EndDocPrinter(hPrinter)

                self.corte_papel_cupom_relatorio()
                print("O cupom relatorio foi impresso com sucesso!")
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setWindowTitle("Atenção Erro")
                msg.setText("Ocorreu um erro ao gerar o cupom Relatorio 2.")
                msg.exec()

        except Exception as e:
            print("Erro na Função imprimir cupom relatorio 3:", str(e))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("Ocorreu um erro ao tentar imprimir o cupom relatorio.")
            msg.exec()

    def gerar_cupom_relatorio(self):  # IMPRIMI UM RELATORIO RESUMIDO DAS RECEITAS (ENTRADAS, SAIDAS E RECEITA FINAL)
        
        banco_cf = CONTROLE_FINANCEIRO()

        # Obter receita final
        receita_final = banco_cf.calculo_receita_final()
        receita_entradas = banco_cf.somar_todas_entradas()
        receita_saidas = banco_cf.somar_todas_saidas()

        # Obtem Listar das receitas
        list_entradas = banco_cf.obter_list_entradas()
        list_saidas = banco_cf.obter_list_saidas()

        # Acessando os valores do dicionário pelas chaves
        list_entrada_dinheiro = list_entradas.get('Dinheiro', 0)
        list_entrada_cartao_credito = list_entradas.get('Cartão de Crédito', 0)
        list_entrada_cartao_debito = list_entradas.get('Cartão de Débito', 0)
        list_entrada_pix = list_entradas.get('Pix', 0)

        list_saida_dinheiro = list_saidas.get('Dinheiro', 0)
        list_saida_cartao_credito = list_saidas.get('Cartão de Crédito', 0)
        list_saida_cartao_debito = list_saidas.get('Cartão de Débito', 0)
        list_saida_pix = list_saidas.get('Pix', 0)

        # Configurar o formato de moeda
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

        # Converter receita_entradas para float antes de formatar como moeda
        receita_entradas_num = float(receita_entradas)
        self.entrada_total = locale.currency(receita_entradas_num, grouping=True)

        entrada_dinheiro_num = float(list_entrada_dinheiro)
        self.entrada_dinheiro = locale.currency(entrada_dinheiro_num, grouping=True)

        entrada_cartao_credito_num = float(list_entrada_cartao_credito)
        self.entrada_cartao_credito = locale.currency(entrada_cartao_credito_num, grouping=True)

        entrada_cartao_debito_num = float(list_entrada_cartao_debito)
        self.entrada_cartao_debito = locale.currency(entrada_cartao_debito_num, grouping=True)

        entrada_pix_num = float(list_entrada_pix)
        self.entrada_pix = locale.currency(entrada_pix_num, grouping=True)

        # Converter receita_saidas para float antes de formatar como moeda
        apurado_saidas_num = float(receita_saidas)
        self.saida_total = locale.currency(apurado_saidas_num, grouping=True)

        saida_dinheiro_num = float(list_saida_dinheiro)
        self.saida_dinheiro = locale.currency(saida_dinheiro_num, grouping=True)

        saida_cartao_credito_num = float(list_saida_cartao_credito)
        self.saida_cartao_credito = locale.currency(saida_cartao_credito_num, grouping=True)

        saida_cartao_debito_num = float(list_saida_cartao_debito)
        self.saida_cartao_debito = locale.currency(saida_cartao_debito_num, grouping=True)

        saida_pix_num = float(list_saida_pix)
        self.saida_pix = locale.currency(saida_pix_num, grouping=True)

        # Converter receita_final para float antes de formatar como moeda
        receita_final_num = float(receita_final)
        self.receita_final = locale.currency(receita_final_num, grouping=True)

        receita_entradas_num = float(receita_entradas)
        self.receita_entradas = locale.currency(receita_entradas_num, grouping=True)

        receita_saidas_num = float(receita_saidas)
        self.receita_saidas = locale.currency(receita_saidas_num, grouping=True)

        receita_final = locale.currency(receita_final, grouping=True)
        receita_entradas = locale.currency(receita_entradas, grouping=True)
        receita_saidas = locale.currency(receita_saidas, grouping=True)

        tipo_receita_entrada = "Entradas"
        tipo_receita_saidas = "Saidas"
        tipo_receita_liquida = "Receita Liquida"

        hora_atual = QTime.currentTime()
        self.time_text = hora_atual.toString('hh:mm:ss')

        data_atual = datetime.now()
        self.data_formatada = data_atual.strftime('%d/%m/%Y')

        try:
            cupom_text = " "
            cupom_text += "------------------------------------------\n"
            cupom_text += "\t\tRelatorio Geral\n"
            cupom_text += "------------------------------------------\n"
            cupom_text += f"\n\n"
            cupom_text += f"Descrição / Categoria              Valor\n"
            cupom_text += f"Dinheiro / Entradas                {self.entrada_dinheiro}\n"
            cupom_text += f"Cartão de Crédito/ Entradas        {self.entrada_cartao_credito}\n"
            cupom_text += f"Cartão de Débito/ Entradas         {self.entrada_cartao_debito}\n"
            cupom_text += f"Pix / Entradas                     {self.entrada_pix}\n"
            cupom_text += f"Total de Entradas                  {self.entrada_total}\n"
            cupom_text += f"________________________________________________\n"
            cupom_text += f"\n\n"
            cupom_text += f"Dinheiro / Saidas                  {self.saida_dinheiro}\n"
            cupom_text += f"Cartão de Crédito / Saidas         {self.saida_cartao_credito}\n"
            cupom_text += f"Cartão de Débito / Saidas          {self.saida_cartao_debito}\n"
            cupom_text += f"Pix / Saidas                       {self.saida_pix}\n"
            cupom_text += f"Total de Saidas                    {self.saida_total}\n"
            cupom_text += f"________________________________________________\n"
            cupom_text += f"\n\n"
            cupom_text += f"{tipo_receita_entrada}             {receita_entradas} \n"
            cupom_text += f"{tipo_receita_saidas}              {receita_saidas} \n"
            cupom_text += f"{tipo_receita_liquida}             {self.receita_final} \n"
            cupom_text += f"\n\n"
            cupom_text += "------------------------------------------\n"
            cupom_text += f"\t\tData: {self.data_formatada} \n"
            cupom_text += f"\t\tHora: {self.time_text}\n"
            cupom_text += "------------------------------------------\n"
            cupom_text += f"\n\n"

            return cupom_text

        except Exception as e:
            print("Erro ao gerar o cupom do relatorio:", str(e))
            return None

    def verifica_impressora_padrao_tela_relatorio(self):

        default_printer = win32print.GetDefaultPrinter()

        if default_printer:
            return default_printer
        else:
            return None
    
##################################### AREA DA TABLE DE CONFIGURAÇÕES ADICIONAIS ####################################
    def salvar_tipo_cupom(self):
        # Obtém o tipo de cupom selecionado no ComboBox
        tipo_cupom = self.comboBox_tipo_cupom.currentText()  # Obtém o texto selecionado

        # Salva o tipo de cupom no arquivo de configuração
        config = configparser.ConfigParser()
        config['Cupom'] = {'tipo': tipo_cupom}
        with open('config_001.ini', 'w') as configfile:
            config.write(configfile)

        # Exibe mensagem de confirmação
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Informação")
        msg.setText("Tipo de Cupom Salvo com Sucesso!")
        msg.exec()
    
    def carregar_tipo_cupom(self): # carregar o tipo do cupom ja definida na aba de configuracoes adicionais
    
        config = configparser.ConfigParser()
        config.read('config_001.ini')

        # Verifica se existe configuração de tipo
        tipo_cupom = config.get('Cupom', 'tipo', fallback='80mm')  # 80mm como padrão
        
        # Define o valor no ComboBox
        index = self.comboBox_tipo_cupom.findText(tipo_cupom)  # Localiza o índice do tipo salvo
        if index >= 0:
            self.comboBox_tipo_cupom.setCurrentIndex(index)

    def salvar_fonte_cupom(self):

        # Obtém o fonte de cupom selecionado no ComboBox
        fonte_cupom = self.comboBox_fonte_cupom.currentText()  # Obtém o texto selecionado

        # Salva o fonte de cupom no arquivo de configuração
        config = configparser.ConfigParser()
        config['Cupom'] = {'fonte': fonte_cupom}
        with open('config_002.ini', 'w') as configfile:
            config.write(configfile)

        # Exibe mensagem de confirmação
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Informação")
        msg.setText("fonte do Cupom Salvo com Sucesso!")
        msg.exec()
    
    def carregar_fonte_cupom(self):
            
        config = configparser.ConfigParser()
        config.read('config_002.ini')

        # Verifica se existe configuração de tipo
        fonte_cupom = config.get('Cupom', 'fonte', fallback='22')  # 22 como padrão
        # Define o valor no ComboBox
        index = self.comboBox_fonte_cupom.findText(fonte_cupom)  # Localiza o índice do tipo salvo
        if index >= 0:
            self.comboBox_fonte_cupom.setCurrentIndex(index)

    def salvar_configuracoes(self):
        dados = {
            "fonte": self.fontComboBox.currentFont().family(),
            "tamanho": self.spinBox_tamanho.value(),
            "cor": self.corFonte.name()  # ex: "#000000"
        }
        with open(CAMINHO_JSON, "w") as arquivo:
            json.dump(dados, arquivo, indent=4)
        print("Configurações salvas com sucesso!")

    def carregar_configuracoes(self):
        if os.path.exists(CAMINHO_JSON):
            with open(CAMINHO_JSON, "r") as arquivo:
                dados = json.load(arquivo)
                fonte = QFont(dados.get("fonte", "Arial"))
                tamanho = dados.get("tamanho", 12)
                cor = dados.get("cor", "#000000")

                fonte.setPointSize(tamanho)
                self.fontComboBox.setCurrentFont(fonte)
                self.spinBox_tamanho.setValue(tamanho)
                self.corFonte = QColor(cor)

                # Aplicar no preview
                self.label_preview.setFont(fonte)
                self.label_preview.setStyleSheet(f"color: {cor}")
        
################## AREA DO SERVIDO API #############################################################
    def ip_maquina(self): # """Retorna o IP da máquina local"""
        
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        self.txt_ip_servidor.setText(f"http://{ip}:")
        return ip

    def salvar_opcao_select_server(self): # """Função que salva a opção selecionada (servidor)"""
        # Obtém o IP e a porta configurados
        ip = self.ip_maquina()  # Obtém o IP da máquina local
        porta = self.comboBox_porta_servidor.currentText()  # Obtém a porta do ComboBox

        # Verifica se a porta é válida
        if not porta.isdigit():
            self.label_status_server.setText("Porta inválida. Selecione uma porta numérica.")
            return

        # Converte a porta para inteiro
        porta = int(porta)
        
        if self.radioButton_server.isChecked():
            self.on_salvar_server()
            time.sleep(0.5)
            self.iniciar_servidor()

        else:
            self.label_status_server.setText("Selecione uma opção: Servidor/Cliente.")

    def salvar_opcao_select_client(self): # """Função que salva a opção selecionada (cliente)"""
        # Obtém o IP e a porta configurados pelo cliente
        ip_servidor = self.txt_ip_client.text()  # Campo de entrada para o IP do servidor
        porta_servidor = self.txt_porta_client.text()  # Campo de entrada para a porta do servidor

        # Verifica se o IP e a porta são válidos
        if not ip_servidor or not porta_servidor.isdigit():
            self.label_status_server.setText("IP ou porta inválidos. Verifique as informações.")
            return

        # Converte a porta para inteiro
        porta_servidor = int(porta_servidor)
        # Cria a URL completa do servidor
        url_servidor = f"http://{ip_servidor}:{porta_servidor}/"
        
        if self.radioButton_client.isChecked():
            self.on_salvar_client()  # Chama a função para salvar configurações do cliente
            time.sleep(0.5)
            self.iniciar_servidor()  # Função para iniciar o cliente
            self.label_status_server.setText(f"Modo Cliente configurado. {url_servidor}")
        else:
            self.label_status_server.setText("Selecione a opção Servidor/Cliente")

    def on_salvar_client(self):
        
        try:
            # Obtém o IP e a porta configurados pelo cliente
            ip_servidor = self.txt_ip_client.text()  # Campo de entrada para o IP do servidor
            porta_servidor = self.txt_porta_client.text()  # Campo de entrada para a porta do servidor

            # Verifica se o IP e a porta são válidos
            if not ip_servidor or not porta_servidor.isdigit():
                self.label_status_server.setText("IP ou porta inválidos. Verifique as informações.")
                return

            # Converte a porta para inteiro
            porta_servidor = int(porta_servidor)

            # Cria a URL completa do servidor
            url_servidor = f"http://{ip_servidor}:{porta_servidor}/"

            # Salva as configurações no arquivo .ini
            config = configparser.ConfigParser()
            config['Rede'] = {
                'modo': 'client',
                'ip': ip_servidor,
                'porta': str(porta_servidor),

            }
            with open('config_rede.ini', 'w') as configfile:
                config.write(configfile)

            # Faz uma requisição HTTP para verificar a conexão com o servidor
            try:
                response = requests.get(url_servidor, timeout=5)  # Timeout para evitar longas esperas
                if response.status_code == 200:
                    self.label_status_server.setText(f"Conexão bem-sucedida com o servidor em {url_servidor}.")
                    print(f"Conexão bem-sucedida com o servidor em {url_servidor}.")
                else:
                    self.label_status_server.setText(f"Erro na conexão com o servidor. Código: {response.status_code}.")
                    print(f"Erro na conexão com o servidor. Código: {response.status_code}.")
                    return
            except requests.exceptions.ConnectionError:
                self.label_status_server.setText("Não foi possível conectar ao servidor. Verifique IP e porta.")
                return

            # Atualiza o status na interface
            self.label_status_server.setText(f"Cliente conectado ao Servidor em {url_servidor}.")
            print(f"Cliente conectado ao Servidor em {url_servidor}.")
        
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao salvar configurações do cliente: {e}")
            msg.exec()

    def on_salvar_server(self):

        try:
            # Obtém o IP e a porta configurados
            ip = self.ip_maquina()  # Obtém o IP da máquina local
            porta = self.comboBox_porta_servidor.currentText()  # Obtém a porta do ComboBox

            # Verifica se a porta é válida
            if not porta.isdigit():
                self.label_status_server.setText("Porta inválida. Selecione uma porta numérica.")
                return

            # Converte a porta para inteiro
            porta = int(porta)

            # Cria a URL completa
            url_completa = f"http://{ip}:{porta}/"

            # Salva as configurações no arquivo .ini
            config = configparser.ConfigParser()
            config['Rede'] = {
                'modo': 'server',
                'ip': ip,
                'porta': str(porta),
            }
            with open('config_rede.ini', 'w') as configfile:
                config.write(configfile)

            # Inicia o servidor FastAPI em uma thread separada
            server_thread = threading.Thread(target=self.iniciar_servidor) #, args=(ip, porta), daemon=True
            server_thread.start()

            # Atualiza o status na interface
            self.label_status_server.setText(f"Servidor iniciado em {url_completa}.")
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao salvar configurações do servidor: {e}")
            msg.exec()

    def carregar_servidor(self):
          
        try:    
            # Cria o objeto ConfigParser
            config = configparser.ConfigParser()

            # Verifica se o arquivo de configuração existe
            if not os.path.exists('config_rede.ini'):
                if not self.msg_exibida_carreg_server_client:
                    self.msg_exibida_carreg_server_client = True  # Evita exibir novamente

                    # Exibe mensagem de aviso para configurar a rede
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Icon.Information)
                    msg.setWindowTitle("Informação")
                    msg.setText("Configurar a rede antes de iniciar as operações.")
                    msg.exec()

                # Retorna None para forçar o usuário a configurar o arquivo antes de continuar
                return None, None, None

            # Lê o arquivo de configuração
            config.read('config_rede.ini')

            # Verifica se a seção 'Rede' existe
            if 'Rede' not in config:
                raise Exception("Seção 'Rede' não encontrada no arquivo de configuração.")

            # Obtém o IP, a porta e o modo
            ip = config['Rede'].get('ip', '').strip()
            porta = int(config['Rede'].get('porta', '0').strip())
            modo = config['Rede'].get('modo', '').strip().lower()
            
            # Validações básicas
            if not ip or not porta or not modo:
                raise Exception("Valores de configuração ausentes ou inválidos.")
            
            if modo not in ['server', 'client']:
                raise Exception(f"Modo inválido no arquivo de configuração: {modo}")

            # Retorna os valores para uso
            return ip, porta, modo

        except Exception as e:
            print(f"Erro ao carregar o arquivo de configuração: {e}")
            # Exibe uma mensagem de erro para o usuário
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao carregar a configuração: {str(e)}")
            msg.exec()
            return None, None, None
            
    def iniciar_modo(self): # essa função e respomsavel por iniciar o sistema da APIFast, ela e que iniciar apois isso os demais iram de forma automatica

        ip, porta, modo = self.carregar_servidor()

        if modo == "server":
            #self.label_status_server.setText("Iniciando o servidor...")
            self.iniciar_servidor()  # Chama a função para iniciar o servidor
            time.sleep(1)
            #self.exibir_table_estoque()
        elif modo == "client":
            #self.label_status_client.setText("Iniciando o cliente...")
            self.iniciar_cliente()  # Chama a função para iniciar o cliente
            time.sleep(1)
            #self.exibir_table_estoque()
        else:
            pass  # Apenas passa sem fazer nada
    
    def iniciar_cliente(self):
        try:
            # Obtém os dados do servidor
            ip, porta, modo = self.carregar_servidor()

            # Verifica se os valores são válidos
            if not ip or not porta:
                print("Erro: IP ou porta inválidos.")
                self.label_status_server.setText("Erro: Configuração de rede inválida.")
                return

            # Converte porta para inteiro
            try:
                porta = int(porta)
            except ValueError:
                print(f"Erro: Porta '{porta}' não é um número válido.")
                self.label_status_server.setText("Erro: Porta inválida no arquivo de configuração.")
                return

            # Monta a URL do servidor corretamente
            url_completa = f"http://{ip}:{porta}/"

            print(f"URL Montada: {url_completa}")  # Depuração

            # Testa a conexão com o servidor
            response = requests.get(url_completa, timeout=5)  # Timeout evita travamento
            if response.status_code == 200:
                print(f"Conexão bem-sucedida: {url_completa}")
                self.label_status_server.setText(f"Conectado ao servidor em {url_completa}.")
            else:
                print(f"Erro ao conectar, código: {response.status_code}")
                self.label_status_server.setText(f"Erro ao conectar ao servidor. Código: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão: {e}")
            self.label_status_server.setText(f"Erro ao conectar: {e}")

        except Exception as e:
            print(f"Erro inesperado: {e}")
            self.label_status_server.setText(f"Erro inesperado: {e}")
         
    def iniciar_servidor(self): # Função para iniciar o servidor
            
        # Retorna os dois valores
        ip_porta = self.carregar_servidor()

        # Atribui separadamente
        ip = ip_porta[0]  # Primeiro valor (IP)
        porta = ip_porta[1]  # Segundo valor (Porta)
        
        self.encerrar_processos(porta) # ecerrar os processos para pode iniciar o servidor
        time.sleep(2) #da uma pausa de 2 segudos para que ai sim inicier a Api

        try:
            app = FastAPI()

            # Instância das APIs
            estoque_api = APIEstoque()
            usuarios_api = APIUsuarios()
            financeiro_api = APIFinanceiro()

            ####### AREA ESTOQUE API ################################
           
            @app.get("/estoque")
            def listar_estoque():
                return {"estoque": estoque_api.listar_todos()}
            
            # Buscar produtos para exibir na table do estoque
            @app.get("/estoque/buscar_estoque")
            def buscar_estoque(codigo: str = None, barras: str = None, nome: str = None):
                if codigo:
                    produtos = estoque_api.buscar_estoque(codigo=codigo)
                elif barras:
                    produtos = estoque_api.buscar_estoque(barras=barras)
                elif nome:
                    produtos = estoque_api.buscar_estoque(nome=nome)
                else:
                    raise HTTPException(status_code=400, detail="Parâmetro de busca inválido")
                
                if not produtos:
                    raise HTTPException(status_code=404, detail="Produto não encontrado???")
                
                return {"produtos": produtos}
            
            @app.get("/estoque/buscar_estoque_pdv")
            def buscar_estoque_pdv(codigo: str = None, codigo_barras: str = None):
                if codigo:
                    produto = estoque_api.buscar_produto_por_codigo_ou_barras(str(codigo))  # Converte para string
                elif codigo_barras:
                    produto = estoque_api.buscar_produto_por_codigo_ou_barras(str(codigo_barras))  # Converte para string
                else:
                    raise HTTPException(status_code=400, detail="Parâmetro de busca inválido")
                if not produto:
                    raise HTTPException(status_code=404, detail="Produto não encontrado!!!!!")
                return {"produto": produto}   #  {"produto": [produto]}
            

            # Inserir novo produto
            @app.post("/estoque/estoque_inserir_produto")
            def inserir_produto(codigo_produto: int, barras: str, nome: str, descricao: str, quantidade: int, unidade: str, valor_compra: float, valor_venda: float):
                dados_produto = (codigo_produto, barras, nome, descricao, quantidade, unidade, valor_compra, valor_venda)
                novo_id = estoque_api.inserir_dados_produto(dados_produto)
                return {"message": "Produto inserido com sucesso", "id": novo_id}
        
            # Excluir produtos do estoque
            @app.post("/estoque/excluir_produto")
            def excluir_produto(dados: dict):
                try:
                    ids = dados.get("ids_a_excluir", [])

                    if not ids:
                        raise HTTPException(status_code=400, detail="Nenhum ID recebido.")

                    # Chama a função para excluir
                    sucesso = estoque_api.excluir_produtos(ids)

                    if sucesso:
                        return {"message": "Produtos excluídos com sucesso"}

                    raise HTTPException(status_code=500, detail="Erro ao excluir produtos no banco.")

                except Exception as e:
                    raise HTTPException(status_code=500, detail=f"ERRO API: {str(e)}")

            # Atualizar produto
            @app.patch("/estoque/estoque_atualizar_produto")
            def atualizar_produto(dados_produto: dict):
                # Extrai os dados recebidos do corpo da requisição
                codigo_produto = dados_produto.get("codigo_produto")
                dados_para_atualizar = {
                    "barras_prod": dados_produto.get("barras_prod"),
                    "nome_produto": dados_produto.get("nome_produto"),
                    "descricao_produto": dados_produto.get("descricao_produto"),
                    "qtda_produto": dados_produto.get("qtda_produto"),
                    "uni_pcto_produto": dados_produto.get("uni_pcto_produto"),
                    "valor_compra": dados_produto.get("valor_compra"),
                    "valor_produto": dados_produto.get("valor_produto"),
                }

                # Remove chaves com valores nulos para evitar erros de validação
                dados_para_atualizar = {k: v for k, v in dados_para_atualizar.items() if v is not None}

                # Verifica se o código do produto foi informado
                if not codigo_produto:
                    raise HTTPException(status_code=400, detail="Código do produto é obrigatório.")

                # Verifica se há dados para atualizar
                if not dados_para_atualizar:
                    raise HTTPException(status_code=400, detail="Nenhum dado foi fornecido para atualização.")

                # Chama a função de atualização parcial
                sucesso = estoque_api.atualizar_produto_parcial(codigo_produto, **dados_para_atualizar)

                if sucesso:
                    return {"message": "Produto atualizado com sucesso", "id": codigo_produto}
                else:
                    raise HTTPException(status_code=404, detail="Produto não encontrado")
            
            # Upgrade estoque de produto
            @app.patch("/estoque/qtdade_estoque_up")
            def qtdade_estoque_up(dados_produto: dict):
                # Extrai os dados recebidos do corpo da requisição
                codigo_produto = dados_produto.get("codigo_produto")
                nova_quantidade = dados_produto.get("nova_quantidade")

                # Verifica se o código do produto foi informado
                if not codigo_produto:
                    raise HTTPException(status_code=400, detail="Código do produto é obrigatório.")

                # Verifica se a nova quantidade foi informada
                if nova_quantidade is None:
                    raise HTTPException(status_code=400, detail="Nova quantidade é obrigatória.")

                # Chama a função para atualizar a quantidade no banco de dados
                sucesso = estoque_api.up_produt_quantiade(codigo_produto, nova_quantidade)

                if sucesso:
                    return {"status": "Produto atualizado com sucesso", "novo_estoque": nova_quantidade}
                else:
                    raise HTTPException(status_code=404, detail="Produto não encontrado")

            #########################################################
            ####### AREA USUARIOS API ###############################
            @app.get("/usuarios")
            def listar_usuarios():
                return {"usuarios": usuarios_api.listar_todos()}
            #########################################################
            ####### AREA FINACEIRO API ##############################
            @app.post("/financeiro")
            def registrar_transacao(tipo: str, valor: float, descricao: str):
                return financeiro_api.registrar_transacao(tipo, valor, descricao)
            #########################################################
            
            # Função para iniciar o Uvicorn em uma thread
            def run_uvicorn():
                uvicorn.run(app, host=ip, port=porta)

            # Inicia o servidor em uma thread
            thread = threading.Thread(target=run_uvicorn)
            thread.start()

        except Exception as e:
            print(f"Erro ao iniciar o servidor: {e}")

    def http_estoque(self, ip=None, porta=None, modo=None): # Retorna a URL do servidor de estoque com IP e porta definidos."""
        
        if not ip or not porta or not modo:
            ip, porta, modo = self.carregar_servidor()
        
        ip_definido = ip
        porta_definida = porta

        # Define as URLs do estoque
        http_estoque_exibir = f"http://{ip_definido}:{porta_definida}/estoque"
        http_buscar_produto = f"http://{ip_definido}:{porta_definida}/estoque/buscar_estoque"
        http_buscar_produto_pdv = f"http://{ip_definido}:{porta_definida}/estoque/buscar_estoque_pdv"
        http_inserir_produto = f"http://{ip_definido}:{porta_definida}/estoque/estoque_inserir_produto" 
        http_excluir_produto = f"http://{ip_definido}:{porta_definida}/estoque/excluir_produto"
        http_edit_produto = f"http://{ip_definido}:{porta_definida}/estoque/estoque_atualizar_produto"
        http_up_produt_quantidade = f"http://{ip_definido}:{porta_definida}/estoque/qtdade_estoque_up"

        # Retorna as URLs como uma tupla
        return http_estoque_exibir, http_buscar_produto, http_buscar_produto_pdv, http_inserir_produto, http_excluir_produto, http_edit_produto, http_up_produt_quantidade
    
    def stop_uvicorn(self): # Função para parar o Uvicorn
        os.kill(os.getpid(), signal.SIGINT)  # Simula Ctrl+C enviando SIGINT ao processo

    def encerrar_processos(self, porta): 
        #Encerra todos os processos que estão utilizando a porta especificada.
        #Garante que a porta fique disponível para uso posterior.

        try:
            # Itera sobre todas as conexões de rede
            for conn in psutil.net_connections(kind='inet'):
                # Verifica se a porta local corresponde à porta especificada
                if conn.laddr.port == porta:
                    pid = conn.pid  # Obtém o PID do processo associado
                    if pid:  # Se houver um processo associado
                        try:
                            process = psutil.Process(pid)
                            process.terminate()  # Encerra o processo
                            self.stop_uvicorn() # Encerra a API algo como "Stop"
                            process.wait(timeout=3)  # Aguarda o término do processo
                            print(f"Processo com PID {pid} encerrado na porta {porta}.")
                        except psutil.NoSuchProcess:
                            print(f"O processo com PID {pid} já foi encerrado.")
                        except psutil.TimeoutExpired:
                            print(f"O processo com PID {pid} não pôde ser encerrado a tempo, forçando o término.")
                            process.kill()  # Força o término do processo

        except Exception as e:
            print(f"Erro ao encerrar processos na porta {porta}: {e}")

        # Confirma se a porta foi liberada
        conexoes_restantes = [
            conn for conn in psutil.net_connections(kind='inet') if conn.laddr.port == porta
        ]
        if not conexoes_restantes:
            print(f"A porta {porta} foi liberada com sucesso e está disponível.")
        else:
            print(f"A porta {porta} ainda está em uso.")

############################### AREA de finalizar venda com formas de pagamentos ###################################

class Tela_Finalizar_Vendas(QDialog, Ui_Form_Pgto, Ui_W_W_AUTO_COM_PDV):
    
    def __init__(self, janela_principal: W_W_AUTO_COM_PDV) -> None:
        super().__init__()
        self.janela_principal = janela_principal  # Referência à janela principal
        self.setupUi(self)  # Configura sua interface
        
        self.setWindowTitle('Fechamento de venda')
        
        self.formatar_dinheiro_recebido()
        self.txt_dinheiro_finaliza.textChanged.connect(self.formatar_dinheiro_recebido)
        self.txt_dinheiro_finaliza.textChanged.connect(self.calcular_troco)
        self.btn_finalizar_venda.clicked.connect(self.exibir_cupom)
        self.labell_valor_venda.setText(self.janela_principal.txt_valor_total_pdv.text())
        self.dados_empresa = self.janela_principal.obter_dados_empresa_pdv()
        self.dados_compra = self.janela_principal.obter_dados_compra_pdv()

        # Desabilitar a comboBox de forma de pagamento inicialmente
        self.comboBox_forma_pgto.setEnabled(False)

        self.comboBox_forma_pgto.currentTextChanged.connect(self.atualizar_valor_combobox_forma_pgto_pdv)

        self.carregar_largura_cupom()

        self.carregar_fonte_cupom()

    def formatar_dinheiro_recebido(self):

        try:
            # Pegue o texto digitado no campo e remova caracteres desnecessários
            dinheiro_str = self.txt_dinheiro_finaliza.text().replace('R$', '').replace('.', '').replace(',', '').strip()

            # Se o campo não estiver vazio, converta para float e formate o valor
            if dinheiro_str:
                dinheiro = float(dinheiro_str) / 100  # Divide por 100 para adicionar as casas decimais corretamente
                dinheiro_formatado = locale.currency(dinheiro, grouping=True, symbol=False).strip()
                self.txt_dinheiro_finaliza.setText(dinheiro_formatado)
                self.txt_dinheiro_finaliza.setCursorPosition(len(dinheiro_formatado))  # Posiciona o cursor no final do texto
        except ValueError:
            pass  # Se o valor não for válido, apenas ignore
        
    def verifica_impressora_padrao_tela_venda_finalizada(self): #fução que faz a verificação da prit padrao e madna para imprimir o cupom

        default_printer = win32print.GetDefaultPrinter()

        if default_printer:
            return default_printer
        else:
            return None
    
    def obter_dados_lines_pdv(self):
    
        # Valor total da venda
        vl_total_str = self.janela_principal.txt_valor_total_pdv.text()
        vl_total = float(vl_total_str.replace("R$ ", "").replace(".", "").replace(",", "."))

        # Quantidade de itens distintos (linhas do modelo da tabela PDV)
        qtde_itens = self.janela_principal.modelo.rowCount()

        # Dinheiro recebido
        dinheiro_str = self.txt_dinheiro_finaliza.text()
        dinheiro_str = dinheiro_str.replace("R$ ", "").replace(".", "").replace(",", ".")
        dinheiro = float(dinheiro_str) if dinheiro_str else 0.0

        # Forma de pagamento
        forma_pgto = self.comboBox_forma_pgto.currentText()

        # Troco
        troco_str = self.label_troco_finalizar.text()
        troco_str = troco_str.replace("R$ ", "").replace(".", "").replace(",", ".")
        troco = float(troco_str) if troco_str else 0.0

        # Monta o dicionário com os dados do PDV
        self.dados_lines_pdv = {
            'Qtde. Itens': qtde_itens,
            'Valor total R$': vl_total,
            'Valor a Pagar R$': vl_total,
            'DINHEIRO': dinheiro,
            'Troco R$': troco,
            'FORMA DE PAGAMENTO': forma_pgto
        }

        return self.dados_lines_pdv

    def cupom_text_80mm(self, dados_compra, dados_empresa, dados_lines_pdv):
       
        """Função para criar e formatar os dados do cupom com alinhamento justificado."""
        try:
            cupom_text = ""  # Inicializando a variável para armazenar o texto do cupom

            # Data e hora formatadas
            current_time = QTime.currentTime()
            self.time_text_cupom = current_time.toString('hh:mm:ss')
            data_atual = datetime.now()
            self.data_formatada_cupom = data_atual.strftime('%d/%m/%Y')

            # Configurar o formato de moeda para o Brasil
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

            # Formatação dos valores como moeda
            self.valor_total_num = locale.currency(dados_lines_pdv['Valor total R$'], grouping=True)
            self.valor_pagar_num = locale.currency(dados_lines_pdv['Valor a Pagar R$'], grouping=True)
            self.valor_recebido_num = locale.currency(dados_lines_pdv['DINHEIRO'], grouping=True)
            self.troco_num = locale.currency(dados_lines_pdv['Troco R$'], grouping=True)

            # Cabeçalho do cupom
            cupom_text += f"CNPJ: {dados_empresa['CNPJ']}\n"
            cupom_text += f"Razão Social: {dados_empresa['Razão Social']}\n"
            cupom_text += f"Endereço: {dados_empresa['Endereço']}, {dados_empresa['Cidade']}\n"
            cupom_text += f"**********Cupom não fiscal**********\n"
            cupom_text += f"***************************************************************************\n"
            cupom_text += f"Código  Descrição    Qtd  Vl Unit   Vl Total\n"

            # Loop para adicionar os itens da compra
            for produto in dados_compra:
                codigo = str(produto.get('Código', '')).ljust(6)  # Ajusta código à esquerda
                descricao = str(produto.get('Descrição', '')).ljust(14)  # Ajusta descrição à esquerda
                qtde_un = str(produto.get('Qtde UN', '1.0')).rjust(4)  # Ajusta quantidade à direita
                vl_unitario = f"R$ {float(produto.get('Vl Unit', 0)):.2f}".rjust(8)  # Alinha valor unitário
                vl_total = f"R$ {float(produto.get('Vl Sub-Total', 0)):.2f}".rjust(9)  # Alinha total
                cupom_text += f"{codigo}  {descricao}  {qtde_un}  {vl_unitario}  {vl_total}\n"

            # Rodapé do cupom
            cupom_text += f"***************************************************************************\n"
            cupom_text += f"Qtd. Itens: {str(dados_lines_pdv['Qtde. Itens']).rjust(3)}\n"
            cupom_text += f"Total:{self.valor_total_num.rjust(10)}\n"
            cupom_text += f"***************************************************************************\n"
            cupom_text += f"A Pagar:{self.valor_pagar_num.rjust(10)}\n"
            cupom_text += f"Pgto:{self.valor_recebido_num.rjust(10)}\n"
            cupom_text += f"Troco:{self.troco_num.rjust(10)}\n"  
            cupom_text += f"Tipo Pgto: {dados_lines_pdv['FORMA DE PAGAMENTO']}\n"
            cupom_text += f"***************************************************************************\n"
            cupom_text += f"{self.data_formatada_cupom}\n"
            cupom_text += f"{self.time_text_cupom}\n"
            cupom_text += f"{dados_empresa['Rodape_Cupom']}\n"
            cupom_text += f"***************************************************************************\n"
            cupom_text += "\n" * 2  # Espaçamento final

            return cupom_text.strip()

        except Exception as e:
            print(f"Erro ao gerar o cupom: {e}")
            return None

    def carregar_fonte_cupom(self): # carregar a fonte do cupom ja definida em configurações
        
        config = configparser.ConfigParser()
        config.read('config_002.ini') 
        tamanho_fonte = config.getint('Cupom', 'fonte') #, fallback='22') # Valor padrão 80mm
        
        # Garantir que o tamanho da fonte seja um número par entre 2 e 30
        if tamanho_fonte < 2:
            return 2
        elif tamanho_fonte > 30:
            return 30
        elif tamanho_fonte % 2 != 0:  # Se for ímpar, arredondar para o próximo par
            return tamanho_fonte + 1
        
        return tamanho_fonte

    def carregar_largura_cupom(self): # carregar a largura do cupom ja definida em configurações
       
        config = configparser.ConfigParser()
        config.read('config_001.ini')
        tipo_cupom = config.get('Cupom', 'tipo', fallback='80mm')  # Valor padrão 80mm
        if tipo_cupom == '80mm':
            return 576  # Largura padrão para 80mm
        elif tipo_cupom == '58mm':
            return 384  # Largura padrão para 58mm
        return 576  # Valor padrão se não configurado

    def gerar_imagem_cupom(self, dados_compra, dados_empresa, dados_lines_pdv): # gerar a imagen do cupom fiscal

        largura = self.carregar_largura_cupom()
        tamanho_fonte = self.carregar_fonte_cupom()

        # Gerar o texto do cupom
        self.cupom_texto = self.cupom_text_80mm(dados_compra, dados_empresa, dados_lines_pdv)
        if not self.cupom_texto:
            return None

        self.salvar_cupom_txt(self.cupom_texto)
        # Diretório e nome do arquivo
        diretorio_instalacao = os.path.dirname(os.path.abspath(__file__))
        pasta_nfe = os.path.join(diretorio_instalacao, "NFe")
        if not os.path.exists(pasta_nfe):
            os.makedirs(pasta_nfe)
        caminho_imagem = os.path.join(pasta_nfe, "cupom_venda.png")

        # Calcular altura dinâmica com base no número de linhas do cupom
        linhas_cupom = self.cupom_texto.count("\n") + 1
        altura_por_linha = tamanho_fonte + 5  # Altura média de cada linha (fonte + espaçamento)
        altura_minima = 300  # Altura mínima para cupom vazio ou muito curto
        altura = max(altura_por_linha * linhas_cupom + 20, altura_minima)

        # Criar a imagem do cupom
        imagem = Image.new('RGB', (largura, altura), color=(255, 255, 255))
        draw = ImageDraw.Draw(imagem)

        # Carregar a fonte
        try:
            font = ImageFont.truetype("arial.ttf", tamanho_fonte)
        except IOError:
            font = ImageFont.load_default()

        # Desenhar o texto no cupom
        margem_x = 10
        margem_y = 10
        espaco_linhas = tamanho_fonte + 5
        y = margem_y
        for linha in self.cupom_texto.split("\n"):
            draw.text((margem_x, y), linha, font=font, fill=(0, 0, 0))
            y += espaco_linhas

        # Salvar a imagem
        try:
            imagem.save(caminho_imagem, format='PNG')
        except Exception as e:
            print(f"Erro ao salvar imagem: {str(e)}")
            return None

        print(f"Imagem do cupom salva: {caminho_imagem}")
        return caminho_imagem

    def exibir_cupom(self):  # Exibir o cupom fiscal para depois poder imprimir

        dados_empresa = self.janela_principal.obter_dados_empresa_pdv()
        dados_compra = self.janela_principal.obter_dados_compra_pdv()
        dados_lines_pdv = self.obter_dados_lines_pdv()

        # Gerar a imagem do cupom
        caminho_imagem = self.gerar_imagem_cupom(dados_compra, dados_empresa, dados_lines_pdv)
        if not caminho_imagem:
            print("Erro ao gerar a imagem do cupom.")
            return

        nome_impressora = self.verifica_impressora_padrao_tela_venda_finalizada()

        # Criar a janela para exibir o cupom
        dialog = QDialog()
        dialog.setWindowTitle("Visualizar Cupom")
        dialog.setWindowModality(Qt.ApplicationModal)

        layout = QVBoxLayout()

        # Carregar a imagem no QLabel
        label_imagem = QLabel()
        pixmap = QPixmap(caminho_imagem)
        label_imagem.setPixmap(pixmap)
        label_imagem.setScaledContents(True)
        label_imagem.setFixedSize(300, 500)

        layout.addWidget(label_imagem)

        # Botão para confirmar a impressão
        btn_imprimir = QPushButton("F2/Imprimir")

        def imprimir_e_fechar():
            self.imprimir_cupom(caminho_imagem, nome_impressora)
            QTimer.singleShot(200, dialog.close)
            QTimer.singleShot(200, self.janela_principal.close_windows_finalizar_venda)
            self.janela_principal.upgrade_itens_estoque()

        btn_imprimir.clicked.connect(imprimir_e_fechar)
        layout.addWidget(btn_imprimir)

        # Botão para sair sem imprimir
        btn_sair = QPushButton("ESC/Sair sem imprimir")

        def sair_sem_imprimir():
            dialog.close()
            self.janela_principal.close_windows_finalizar_venda()

        btn_sair.clicked.connect(sair_sem_imprimir)
        layout.addWidget(btn_sair)

        dialog.setLayout(layout)
        dialog.show()

        # Atalho de teclado para F2
        shortcut_f2 = QShortcut(Qt.Key_F2, dialog)
        shortcut_f2.activated.connect(imprimir_e_fechar)

        # Atalho de teclado para ESC
        shortcut_esc = QShortcut(Qt.Key_Escape, dialog)
        shortcut_esc.activated.connect(sair_sem_imprimir)

    def imprimir_cupom(self, caminho_imagem, nome_impressora): # imprimir o cupom fiscal e 
        
        largura_impressao = self.carregar_largura_cupom()

        try:
            if not os.path.exists(caminho_imagem):
                print(f"Erro: Arquivo de imagem '{caminho_imagem}' não encontrado.")
                return

            img = Image.open(caminho_imagem)

            try:
                hPrinter = win32print.OpenPrinter(nome_impressora)
                win32print.StartDocPrinter(hPrinter, 1, ("CupomFiscal", None, "RAW"))
                win32print.StartPagePrinter(hPrinter)

                hdc = win32ui.CreateDC()
                hdc.CreatePrinterDC(nome_impressora)
                hdc.StartDoc("Impressão do Cupom")
                hdc.StartPage()

                bmp = ImageWin.Dib(img)
                altura_impressao = int(img.size[1] * (largura_impressao / img.size[0]))  # Ajuste proporcional
                bmp.draw(hdc.GetHandleOutput(), (0, 0, largura_impressao, altura_impressao))

                hdc.EndPage()
                hdc.EndDoc()
                hdc.DeleteDC()

                win32print.EndPagePrinter(hPrinter)
                win32print.EndDocPrinter(hPrinter)
                win32print.ClosePrinter(hPrinter)

                print("Cupom impresso com sucesso!")

            except Exception as e:
                print("Erro durante a impressão:", str(e))
                return

        except Exception as e:
            print(f"Erro ao abrir imagem para impressão: {str(e)}")
            return

    def cortar_papel(self, tipo_impressora='default'): # FUNÇÃO QUE REALIZAR O CORTE DO PAPEL DA NFC-e 
        
        try:
            # Enviar comando de corte do papel para a impressora
            printer_name = self.verifica_impressora_padrao_tela_venda_finalizada()
            hPrinter = win32print.OpenPrinter(str(printer_name))

            # Escolher o escape code com base no tipo de impressora
            if tipo_impressora == 'argox':
                escape_code = b'\x1B\x6D'  # Comandos específicos para ARGOX
            elif tipo_impressora == 'bema':
                escape_code = b'\x1B\x6E'  # Comandos específicos para BEMA
            else:
                escape_code = b'\x1B\x69'  # Escape code padrão para epson

            # Certificar-se de que o documento está aberto antes de enviar o comando de corte
            win32print.StartDocPrinter(hPrinter, 1, ("CupomFiscal", None, "RAW")) # type: ignore
            win32print.StartPagePrinter(hPrinter)
            win32print.WritePrinter(hPrinter, escape_code) # type: ignore
            win32print.EndPagePrinter(hPrinter)
            win32print.EndDocPrinter(hPrinter)

            print("Corte de papel realizado com sucesso.")

        except Exception as e:
            print("Erro ao cortar papel:", str(e))

    def salvar_cupom_txt(self, cupom_text): # FUNÇÃO QUE SALVA UMA COPIAR NA PASTA RAIZ EM FORMATO .TXT

        # Diretório onde o programa está instalado
        diretorio_instalacao = os.path.dirname(os.path.abspath(__file__))
        pasta_nfe = os.path.join(diretorio_instalacao, "NFe")

        try:
            if not os.path.exists(pasta_nfe):
                os.makedirs(pasta_nfe)

            agora = datetime.now()
            agora_data = agora.strftime("%Y-%m-%d")
            agora_hora = agora.strftime("%H-%M-%S")
            nome_arquivo = f"{agora_data}_{agora_hora}.txt"

            caminho_arquivo = os.path.join(pasta_nfe, nome_arquivo)

            # Verificar se cupom_text é uma string antes de escrevê-lo no arquivo
            if isinstance(cupom_text, str):
                with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:  # Definindo a codificação utf-8 ao salvar o arquivo
                    arquivo.write(cupom_text)
                print(f"Cupom salvo em {caminho_arquivo}")
            else:
                print("O cupom_text não é uma string válida:")

        except Exception as e:
            print(f"Erro ao salvar o cupom: {str(e)}")

    def keyPressEvent(self, event): # funcao que ativa o evento da tecla F5

        # Verificar se a tecla F5 foi pressionada
        if event.key() == Qt.Key_F5:
            # Habilitar a comboBox de forma de pagamento
            self.comboBox_forma_pgto.setEnabled(True)
            # Selecionar a próxima opção (opcional)
            self.selecionar_proxima_opcao()

    def selecionar_proxima_opcao(self): # funcao que combinada com o keyPressEvent faz a selecao do tipo de pagamento
        """
        Seleciona a próxima opção na comboBox de forma de pagamento. 
        Se estiver na última opção, volta para a primeira.
        """
        # Obter o índice atual da opção selecionada
        indice_atual = self.comboBox_forma_pgto.currentIndex()
        
        # Obter o número total de opções na comboBox
        numero_opcoes = self.comboBox_forma_pgto.count()
        
        # Calcular o índice da próxima opção
        proximo_indice = (indice_atual + 1) % numero_opcoes
        
        # Selecionar a próxima opção
        self.comboBox_forma_pgto.setCurrentIndex(proximo_indice)

    def atualizar_valor_combobox_forma_pgto_pdv(self): # Atualiza o valor do campo de dinheiro finaliza com base na forma de pagamento selecionada.

        # Obter a forma de pagamento selecionada no comboBox
        forma_pagamento = self.comboBox_forma_pgto.currentText()

        # Obter o valor total do PDV do label
        valor_total_pdv = self.labell_valor_venda.text()

        # Verificar se o valor total foi recuperado corretamente
        if not valor_total_pdv:
            valor_total_pdv = "R$ 00,00"  # Valor padrão se estiver vazio

        # Se a forma de pagamento for "Cartão Débito", "Cartão Crédito" ou "Pix"
        if forma_pagamento in ['Cartão de Crédito', 'Cartão de Débito', 'Pix']:
            # Preencher o campo txt_dinheiro_finaliza com o valor total
            self.txt_dinheiro_finaliza.setText(valor_total_pdv)

        # Se a forma de pagamento for "Dinheiro"
        elif forma_pagamento == 'Dinheiro':
            # Preencher o campo txt_dinheiro_finaliza com "R$ 00,00"
            self.txt_dinheiro_finaliza.setText("R$ 00,00")

    def calcular_troco(self):  # Função que calcula o troco com base nos campos de entrada
   
        # Obter o valor total e remover símbolos de moeda
        valor_total_str = self.labell_valor_venda.text().replace('R$', '').replace('.', '').replace(',', '.')
        try:
            valor_total = float(valor_total_str)
        except ValueError:
            valor_total = 0.00

        # Obter o dinheiro recebido e remover símbolos de moeda
        dinheiro_recebido_str = self.txt_dinheiro_finaliza.text().replace('R$', '').replace('.', '').replace(',', '.')
        try:
            dinheiro_recebido = float(dinheiro_recebido_str)
        except ValueError:
            dinheiro_recebido = 0.00

        # Calcular o troco
        troco = dinheiro_recebido - valor_total

        # Formatar o troco no padrão brasileiro com separador de milhar e vírgula decimal
        troco_formatado = f'R$ {troco:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

        self.label_troco_finalizar.setText(troco_formatado)

        # Definir o estilo da label baseado no valor do troco
        if troco < 0:
            self.label_troco_finalizar.setStyleSheet(
                "background-color: rgb(255, 255, 255); font: bold 24pt 'Segoe UI'; border-radius: 5px; color: red;"
            )
        else:
            self.label_troco_finalizar.setStyleSheet(
                "background-color: rgb(255, 255, 255); font: bold 24pt 'Segoe UI'; border-radius: 5px; color: black;"
            )

############################### AREA DA Saida de Caixa #############################################################
class Saida_Sangria(Ui_Saida, Ui_W_W_AUTO_COM_PDV, QWidget):  # QWidget se Ui_W_W_AUTO_COM_PDV for baseado em QWidget
    def __init__(self, usuario_logado) -> None:
        super().__init__()
        self.usuario_logado = usuario_logado
        self.setupUi(self)
        self.setWindowTitle('Saídas / Sangrias')
        self.btn_salvar_saida.clicked.connect(self.coletar_dados_transacao_saidas)
        self.btn_salvar_saida.clicked.connect(self.imprimir_cupom_saidas)
        
    def verifica_impressora_padrao_saidas(self):
        default_printer = win32print.GetDefaultPrinter()

        if default_printer:
            #print(f"Impressora padrão: {default_printer}")
            return default_printer
        else:
            print("Nenhuma impressora padrão encontrada. Por favor, configure uma impressora padrão.")
            return None

    def coletar_dados_transacao_saidas(self):

        try:
            # Obter o valor da saída
            valor_saida = self.txt_valor_saida.text()
            
            # Remover pontos de milhar e substituir vírgula por ponto decimal
            valor_formatado_retirado = valor_saida.replace(".", "").replace(",", ".")

            try:
                # Converter o valor formatado para float
                valor_formatado_retirado = float(valor_formatado_retirado)
            except ValueError:
                valor_formatado_retirado = 0.0  # Definir um valor padrão se a conversão falhar

            # Extrair os dados relevantes
            metodo_retirada = self.comboBox_forma_pgto_saida.currentText()
            descricao_saida = f'Retirada no PDV por {self.usuario_logado} - {self.plainTextEdit_descricao_retirada.toPlainText()} - {self.comboBox_descricao_saidas.currentText()}'

            # Verificar se os dados são válidos
            if valor_formatado_retirado > 0 and metodo_retirada:
                try:
                    # Criar uma instância da classe CONTROLE_FINANCEIRO
                    banco_cf = CONTROLE_FINANCEIRO()
                    # Conectar ao banco de dados SQLite
                    cn = banco_cf.conectar_ao_sqlite()

                    # Inserir a transação de saída no banco de dados
                    banco_cf.inserir_transacao('Saída', metodo_retirada, valor_formatado_retirado, descricao_saida)

                    # Exibir mensagem de sucesso
                    self.exibir_mensagem_saidas('Sucesso', 'Dados de Saída/Sangria salvos com sucesso.', QMessageBox.Information)

                except Exception as e:
                    # Exibir mensagem de erro ao usuário em caso de falha na inserção dos dados
                    self.exibir_mensagem_saidas('Erro', f'Erro ao coletar dados de transação de Saídas/Sangrias: {str(e)}', QMessageBox.Critical)
            else:
                # Exibir mensagem de erro se os dados forem inválidos
                self.exibir_mensagem_saidas('Erro', 'Dados da Saída/Sangria são inválidos.', QMessageBox.Warning)
        except Exception as e:
            print("Erro ao coletar dados de transação de Saídas/Sangrias:", str(e))

    def limpar_campos_saidas(self):

        # Limpar os campos do formulário após a inserção bem-sucedida
        self.comboBox_forma_pgto_saida.setCurrentIndex(0)
        self.txt_valor_saida.clear()
        self.plainTextEdit_descricao_retirada.clear()
        self.comboBox_descricao_saidas.setCurrentIndex(0)

    def exibir_mensagem_saidas(self, titulo, texto, icon):
        # Exibir mensagem ao usuário
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setWindowTitle(titulo)
        msg.setText(texto)
        msg.setStyleSheet("color: black;")
        msg.exec()
    
    def obter_dados_saidas(self):

        hora_atual = QTime.currentTime()
        self.time_text = hora_atual.toString('hh:mm:ss')

        data_atual = datetime.now()
        self.data_formatada = data_atual.strftime('%d/%m/%Y')

        obter_dados_saidas = {}

        # Obter o valor da saída sem remover pontos ou substituir vírgulas por pontos
        valor_saida = self.txt_valor_saida.text()

        # Remover espaços em branco e pontos de milhar
        valor_formatado = valor_saida.replace(" ", "").replace(".", "")

        # Substituir a vírgula por ponto decimal
        valor_formatado = valor_formatado.replace(",", ".")

        # Remover o símbolo de moeda "R$" se estiver presente
        if valor_formatado.startswith("R$"):
            valor_formatado = valor_formatado[2:]  # Remove os dois primeiros caracteres (R$)

        try:
            # Converter para float após a formatação correta
            valor_retirado_saida = float(valor_formatado)

            metodo_retirada = self.comboBox_forma_pgto_saida.currentText()

            descricao_saida = f'{self.plainTextEdit_descricao_retirada.toPlainText()} - {self.comboBox_descricao_saidas.currentText()}'

            usuario_logado = f'{self.usuario_logado}'

            formatada_data_saida = self.data_formatada
            formatada_hora_saida = self.time_text
            data_hora_saidas = formatada_data_saida + '/' + formatada_hora_saida

            # Adicionar os dados dos campos de texto ao dicionário
            obter_dados_saidas['Caixa'] = usuario_logado
            obter_dados_saidas['Responsável'] = usuario_logado
            obter_dados_saidas['Data_Saida'] = formatada_data_saida
            obter_dados_saidas['Hora_Saida'] = formatada_hora_saida
            obter_dados_saidas['Retirada em'] = data_hora_saidas
            obter_dados_saidas['Metodo Retirada'] = metodo_retirada
            obter_dados_saidas['Descrição'] = descricao_saida
            obter_dados_saidas['Valor Total da Saida'] = valor_retirado_saida  # Usar o valor sem formatar novamente

            return obter_dados_saidas

        except Exception as e:
            print("Erro ao converter valor para float:", str(e))

    def imprimir_cupom_saidas(self): 
        
        try:
            dados_saidas = self.obter_dados_saidas()

            nome_impressora = self.verifica_impressora_padrao_saidas()
            if not nome_impressora:
                self.exibir_mensagem_saidas("Erro", "A impressora padrão não está definida.", QMessageBox.Warning)
                return

            cupom_texto_saidas = self.print_saidas_sangrias(dados_saidas)

            if cupom_texto_saidas is not None and isinstance(cupom_texto_saidas, str):
                hPrinter = win32print.OpenPrinter(nome_impressora)
                win32print.StartDocPrinter(hPrinter, 1, ("CupomFiscal", None, "RAW"))
                win32print.StartPagePrinter(hPrinter)

                # Convertendo a string do cupom para bytes antes de passá-la para WritePrinter
                cupom_texto_bytes = cupom_texto_saidas.encode('windows-1252') # \\\ Windows-1252 (CP1252) Suporta os caracteres necessários para a língua portuguesa, incluindo caracteres especiais como ç, ã, e ~.\\\
                win32print.WritePrinter(hPrinter, cupom_texto_bytes)

                win32print.EndPagePrinter(hPrinter)
                win32print.EndDocPrinter(hPrinter)

                self.cortar_papel_saidas()

                self.limpar_campos_saidas()

                self.exibir_mensagem_saidas("Impressão Realizada", "O cupom foi impresso com sucesso!", QMessageBox.Information)
            else:
                self.exibir_mensagem_saidas("Atenção Erro", "Ocorreu um erro ao gerar o cupom.", QMessageBox.Critical)

        except Exception as e:
            
            self.exibir_mensagem_saidas("Erro", "A impressora padrão não está definida.", QMessageBox.Warning)

            print("Erro:", str(e))

    def print_saidas_sangrias(self, obter_dados_saidas):
        
        # Configurar o formato de moeda
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

        valor_retirado_saida_num = obter_dados_saidas['Valor Total da Saida']
        # Converter o valor float para uma string formatada como moeda brasileira
        valor_formatado_moeda = locale.currency(valor_retirado_saida_num, grouping=True)

        try:
            cupom_text = " "
            cupom_text += "------------------------------------------\n"
            cupom_text += "\t\tSAIDAS-SANGRIAS\n"
            cupom_text += "------------------------------------------\n"
            cupom_text += f"{obter_dados_saidas['Caixa']}\n"
            cupom_text += f"Data:               {obter_dados_saidas['Data_Saida']}\n"
            cupom_text += f"Hora:               {obter_dados_saidas['Hora_Saida']}\n"
            cupom_text += "\n"
            cupom_text += f"Retirada em:        {obter_dados_saidas['Retirada em']}\n"
            cupom_text += f"Autorizado por:     {obter_dados_saidas['Responsável']}\n"
            # Tratar a descrição para garantir que caracteres diferentes sejam impressos corretamente
            descricao_tratada = obter_dados_saidas['Descrição']
            cupom_text += f"Descrição:\n\n" 
            cupom_text += f"{descricao_tratada}\n\n"
            cupom_text += f"Metodo de Retirada: {obter_dados_saidas['Metodo Retirada']}\n"
            cupom_text += f"Valor R$: {valor_formatado_moeda}\n"
            cupom_text += f"\n\n"
            cupom_text += f"\n\n"
            cupom_text += "ASS: _______________________________________\n"
            cupom_text += f"\n\n"
            cupom_text += f"\n\n"
            
            return cupom_text
            
        except Exception as e:
            print("Erro cupom: ", str(e))
            return None
  
    def cortar_papel_saidas(self, tipo_impressora='default'):
        try:
            printer_name = self.verifica_impressora_padrao_saidas()
            hPrinter = win32print.OpenPrinter(str(printer_name))

            if tipo_impressora == 'argox':
                escape_code = b'\x1B\x6D'
            elif tipo_impressora == 'bema':
                escape_code = b'\x1B\x6E'
            else:
                escape_code = b'\x1B\x69'

            win32print.StartDocPrinter(hPrinter, 1, ("CupomFiscal", None, "RAW")) 
            win32print.StartPagePrinter(hPrinter)
            win32print.WritePrinter(hPrinter, escape_code)
            win32print.EndPagePrinter(hPrinter)
            win32print.EndDocPrinter(hPrinter)

            print("Corte de papel realizado com sucesso.")
        except Exception as e:
            print("Erro ao cortar papel:", str(e))

############################### AREA DA EDIÇÃO DE PRODUTO ############################################################
class Tela_Edit_Produt(QWidget, Ui_Edicao_Produto):
    def __init__(self, W_W_AUTO_COM_PDV, modelo_estoque, tabela_estoque_controller=None, parent=None, http_estoque_main=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Edição de Produto')

        self.W_W_AUTO_COM_PDV = W_W_AUTO_COM_PDV  # Guarda a referência
        self.modelo_estoque = modelo_estoque
        self.tabela_estoque_controller = tabela_estoque_controller
        self.http_estoque_main = http_estoque_main

        self.btn_sair_sem_salvar_edicao_produto.clicked.connect(self.close)
        self.btn_salvar_edicao_produto.clicked.connect(self.salvar_edicao_produto)

        self.edit_produt()

    def edit_produt(self): # Função para editar produtos selecionados no modelo de estoque:
        
        model = self.modelo_estoque

        if not model:
            self.mostrar_mensagem_edit_produt("Nenhum produto selecionado para Edição")
            return

        ids_a_editar = []

        # Obtém os IDs dos produtos marcados para edição
        for row in range(model.rowCount()):
            cell_item = model.item(row, 0)  # Coluna do checkbox
            if cell_item and cell_item.isCheckable() and cell_item.checkState() == Qt.Checked:
                id_item = model.item(row, 1).text()  # Coluna do ID do produto
                ids_a_editar.append(id_item)

        # Verifica se algum item foi selecionado para edição
        if not ids_a_editar:
            self.mostrar_mensagem_edit_produt("Nenhum produto selecionado para edição.")
            return

        # Verifica a configuração do HTTP
        if not self.http_estoque_main or len(self.http_estoque_main) != 7:
            self.mostrar_mensagem_edit_produt("Configuração inválida do HTTP. Verifique os parâmetros.")
            return

        _, http_buscar_produto, _, _, _, _, _ = self.http_estoque_main
        
        # Usa o primeiro ID da lista de selecionados para buscar o produto
        id_item = ids_a_editar[0]  # Considera apenas o primeiro item selecionado

        try:
            # Primeiro tenta com o código do produto para busca-lo
            url = f"{http_buscar_produto}?codigo={id_item}"
            response = requests.get(url)
            response.raise_for_status()
            produto = response.json().get("produtos", [])

            # Se não encontrar, tenta com o código de barras para busca o produto
            if not produto:
                codigo_barras = self.modelo_estoque.item(0, 2).text()  # Exemplo de como pegar o código de barras
                url = f"{http_buscar_produto}?barras={codigo_barras}"
                response = requests.get(url)
                response.raise_for_status()
                produto = response.json().get("produtos", [])

            if not produto:
                self.mostrar_mensagem_edit_produt("Produto selecionado não encontrado na API.")
                return

            self._preencher_dados_para_edicao(produto[0])

        except requests.exceptions.RequestException as e:
            self.mostrar_mensagem_edit_produt(f"Erro ao acessar a API: {e}")

    def _preencher_dados_para_edicao(self, dados_produto): # Preenche os dados do produto para edição, caso encontrado.
        
        # Preenche os campos com os dados do produto
        self.label_codigo_anterior_produto.setText(str(dados_produto.get('codigo_produto', '')))
        self.label_codigo_barras_anterior_produto.setText(str(dados_produto.get('barras_prod', '')))
        self.label_nome_anterior_produto.setText(str(dados_produto.get('nome_produto', '')))
        self.label_descricao_anterior_produto.setText(str(dados_produto.get('descricao_produto', '')))
        self.label_qtde_anterior_produto.setText(str(dados_produto.get('qtda_produto', '')))
        self.label_tipo_anterior_produto.setText(str(dados_produto.get('uni_pcto_produto', '')))

        valor_compra = float(dados_produto.get('valor_compra', 0.0))
        valor_venda = float(dados_produto.get('valor_produto', 0.0))

        self.label_valor_compra_anterior_produto.setText(f"R$ {valor_compra:.2f}")
        self.label_valor_venda_anterior_produto.setText(f"R$ {valor_venda:.2f}")

        self.txt_edit_codigo_produt.setText(str(dados_produto.get('codigo_produto', '')))
        self.txt_edit_codigo_barras_produt.setText(str(dados_produto.get('barras_prod', '')))
        self.txt_edit_nome_produt.setText(str(dados_produto.get('nome_produto', '')))
        self.txt_edit_descricao_produt.setText(str(dados_produto.get('descricao_produto', '')))
        self.txt_edit_qtde_produt.setText(str(dados_produto.get('qtda_produto', '')))
        self.comboBox_novo_tipo_produto.setCurrentText(str(dados_produto.get('uni_pcto_produto', '')))
        self.txt_edit_valor_compra_produt.setText(f"{valor_compra:.2f}")
        self.txt_edit_valor_venda_produt.setText(f"{valor_venda:.2f}")

    def coleta_dados_produtos(self): # Coleta os dados dos campos de texto

        dados_produto = {
            "codigo_produto": self.txt_edit_codigo_produt.text().strip(),
            "barras_prod": self.txt_edit_codigo_barras_produt.text().strip(),
            "nome_produto": self.txt_edit_nome_produt.text().strip(),
            "descricao_produto": self.txt_edit_descricao_produt.text().strip(),
            "qtda_produto": int(self.txt_edit_qtde_produt.text().strip()),  # Converte para int
            "uni_pcto_produto": self.comboBox_novo_tipo_produto.currentText().strip(),
            "valor_compra": float(self.txt_edit_valor_compra_produt.text().strip()),  # Converte para float
            "valor_produto": float(self.txt_edit_valor_venda_produt.text().strip()),  # Converte para float
        }

        # Remove campos vazios (apenas envia os editados)
        dados_filtrados = {k: v for k, v in dados_produto.items() if v}

        # Verifica se há dados a serem enviados
        if not dados_filtrados:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("Nenhum dado foi editado para salvar.")
            msg.exec()
            return
        return dados_filtrados
    
    def salvar_edicao_produto(self): # Coleta os dados dos campos de texto
    
        dados_filtado = self.coleta_dados_produtos()

        # Verifica a configuração do HTTP
        if not self.http_estoque_main or len(self.http_estoque_main) != 7:
            self.mostrar_mensagem_edit_produt("Configuração inválida do HTTP. Verifique os parâmetros.")
            return

        # Define o endpoint da API
        _, _, _, _, _, http_edit_produto, _ = self.http_estoque_main
        url_atualizar_produto = f"{http_edit_produto}"
        try:
            # Envia os dados usando PATCH para atualização parcial
            response = requests.patch(url_atualizar_produto, json=dados_filtado)
            response.raise_for_status()

            # Verifica a resposta da API
            if response.status_code == 200:
                self.mostrar_mensagem_edit_produt("Produto editado com sucesso!")
                time.sleep(0.2) # da uma pausa de 0,2 segundos
                # fecha a janela edicao de produtos
                self.close_edit_produt()
            else:
                self.mostrar_mensagem_edit_produt(f"Erro ao editar produto: {response.text}")

        except requests.exceptions.RequestException as e:
            self.mostrar_mensagem_edit_produt(f"Erro ao acessar a API: {e}")

    def close_edit_produt(self):
        """Fecha a janela de edição do produto."""
        self.close()

    def keyPressEvent(self, event):  # Evento de tecla ESC para fechar a janela
        if event.key() == Qt.Key_Escape:
            self.close()

    def mostrar_mensagem_edit_produt(self, mensagem):
        # Exiba uma mensagem de sucesso
        msg = QMessageBox()
        msg.setWindowTitle("Aviso")
        msg.setText(mensagem)
        msg.exec()

############################### AREA De Fluxo de Caixa #############################################################
class FluxoCaixa:
    def __init__(self):
        # Inicializa os valores do caixa
        self.valor_inicial = 0.0
        self.total_vendas = 0.0
        self.total_saidas = 0.0

    def verifica_impressora_padrao_fecamento_cx(self):
        default_printer = win32print.GetDefaultPrinter()

        if default_printer:
            #print(f"Impressora padrão: {default_printer}")
            return default_printer
        else:
            print("Nenhuma impressora padrão encontrada. Por favor, configure uma impressora padrão.")
            return None
    
    def configurar_dados_financeiros(self):
        """Configura os valores de vendas e saídas no caixa com base nos dados da classe CONTROLE_FINANCEIRO."""
        try:
            banco_cf = CONTROLE_FINANCEIRO()
            self.total_vendas = banco_cf.somar_todas_entradas()
            self.total_saidas = banco_cf.somar_todas_saidas()
            print(f"Valores configurados: Total de Vendas: R$ {self.total_vendas:.2f}, Total de Saídas: R$ {self.total_saidas:.2f}")
            return self.total_vendas, self.total_saidas
        except Exception as e:
            print(f"Erro ao configurar dados financeiros: {str(e)}")

    def iniciar_dia(self):

        """Abre o diálogo para configurar o valor inicial do caixa."""
        dialog = QDialog()
        dialog.setWindowTitle("Abrir Caixa")
        dialog.setWindowModality(Qt.ApplicationModal)

        layout = QVBoxLayout()
        label_instrucao = QLabel("Digite o valor inicial do caixa:")
        layout.addWidget(label_instrucao)

        input_valor = QLineEdit()
        input_valor.setPlaceholderText("Exemplo: 100.00")
        input_valor.setAlignment(Qt.AlignCenter)
        layout.addWidget(input_valor)

        btn_confirmar = QPushButton("Confirmar")
        layout.addWidget(btn_confirmar)

        def confirmar_valor():
            try:
                valor_inicial = float(input_valor.text().replace(',', '.'))
                if valor_inicial < 0:
                    raise ValueError("O valor inicial deve ser positivo.")
                self.valor_inicial = valor_inicial
                self.salvar_txt("Caixa iniciado", valor_inicial=valor_inicial)
                QMessageBox.information(dialog, "Sucesso", f"Caixa iniciado com R$ {valor_inicial:.2f}")
                dialog.accept()
            except ValueError as e:
                QMessageBox.warning(dialog, "Erro", f"Valor inválido: {str(e)}")

        btn_confirmar.clicked.connect(confirmar_valor)
        dialog.setLayout(layout)
        dialog.exec()

    def gerar_cupom_resumo_caixa(self, saldo_final):
        """Gera o texto do cupom de fechamento de caixa."""
        try:
            cupom_text = ""
            cupom_text += "------------------------------------------\n"
            cupom_text += "\t\tRESUMO DO CAIXA\n"
            cupom_text += "------------------------------------------\n"
            cupom_text += f"Valor Inicial:       R$ {self.valor_inicial:.2f}\n"
            cupom_text += f"Total de Vendas:     R$ {self.total_vendas:.2f}\n"
            cupom_text += f"Total de Saidas:     R$ {self.total_saidas:.2f}\n"
            cupom_text += f"Saldo Final:         R$ {saldo_final:.2f}\n"
            cupom_text += "------------------------------------------\n"
            cupom_text += "                                          \n"
            cupom_text += "ASS: _______________________________\n"
            cupom_text += "                                          \n"
            cupom_text += "\n\n"
            return cupom_text
        except Exception as e:
            print("Erro ao gerar cupom: ", str(e))
            return None

    def fechar_caixa(self):
        """Calcula e exibe o saldo final do caixa, gera e imprime o resumo."""
        try:
            # Obter total de vendas e saídas
            self.total_vendas, self.total_saidas = self.configurar_dados_financeiros()

            # Calcular saldo final
            saldo_final = self.valor_inicial + self.total_vendas - self.total_saidas

            # Salvar informações no arquivo
            self.salvar_txt(
                "Fechamento do Caixa",
                valor_inicial=self.valor_inicial,
                total_vendas=self.total_vendas,
                total_saidas=self.total_saidas,
                saldo_final=saldo_final,
            )

            # Gerar o cupom
            cupom_text = self.gerar_cupom_resumo_caixa(saldo_final)

            # Exibir resumo em uma mensagem
            resumo = (
                f"--- Resumo do Caixa ---\n"
                f"Valor Inicial: R$ {self.valor_inicial:.2f}\n"
                f"Total de Vendas: R$ {self.total_vendas:.2f}\n"
                f"Total de Saidas: R$ {self.total_saidas:.2f}\n"
                f"Saldo Final: R$ {saldo_final:.2f}"
            )
            QMessageBox.information(None, "Resumo do Caixa", resumo)

            # Imprimir o cupom gerado
            if cupom_text:
                self.imprimir_cupom_fechamento_caixa(cupom_text)
            else:
                QMessageBox.warning(None, "Erro", "Falha ao gerar o cupom para impressão.")
        except Exception as e:
            print(f"Erro ao fechar caixa: {str(e)}")

    def imprimir_cupom_fechamento_caixa(self, cupom_text):
        """Envia o cupom de fechamento de caixa para a impressora padrão."""
        try:
            if not cupom_text:
                raise ValueError("Cupom vazio ou inválido.")

            # Configurar a impressão
            printer_name = win32print.GetDefaultPrinter()
            hPrinter = win32print.OpenPrinter(printer_name)
            job_info = ("Resumo do Caixa", None, "RAW")

            # Iniciar o documento e enviar dados
            win32print.StartDocPrinter(hPrinter, 1, job_info)
            win32print.StartPagePrinter(hPrinter)
            win32print.WritePrinter(hPrinter, cupom_text.encode("utf-8"))
            win32print.EndPagePrinter(hPrinter)
            win32print.EndDocPrinter(hPrinter)
            win32print.ClosePrinter(hPrinter)

            print("Cupom impresso com sucesso.")
            self.cortar_papel_fechamento()
        except Exception as e:
            print(f"Erro ao imprimir o cupom: {str(e)}")

    def cortar_papel_fechamento(self, tipo_impressora='default'):
        """Envia o comando de corte de papel para a impressora."""
        try:
            printer_name = self.verifica_impressora_padrao_fecamento_cx()
            hPrinter = win32print.OpenPrinter(str(printer_name))

            # Configuração do comando de corte
            if tipo_impressora == 'argox':
                escape_code = b'\x1B\x6D'  # Argox
            elif tipo_impressora == 'bema':
                escape_code = b'\x1B\x6E'  # Bematech
            else:
                escape_code = b'\x1B\x69'  # Default ESC/POS

            # Enviar comando para a impressora
            win32print.StartDocPrinter(hPrinter, 1, ("Corte de Papel", None, "RAW"))
            win32print.StartPagePrinter(hPrinter)
            win32print.WritePrinter(hPrinter, escape_code)
            win32print.EndPagePrinter(hPrinter)
            win32print.EndDocPrinter(hPrinter)

            print("Corte de papel realizado com sucesso.")
        except Exception as e:
            print("Erro ao cortar papel:", str(e))

    def salvar_txt(self, evento, **kwargs):
        """Salva as informações do evento no arquivo .txt."""
        try:
            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            nome_arquivo = f"caixa_{datetime.now().strftime('%Y%m%d')}.txt"
            os.makedirs("relatorios_caixa", exist_ok=True)
            caminho_arquivo = os.path.join("relatorios_caixa", nome_arquivo)

            with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
                arquivo.write(f"\n[{data_hora}] {evento}\n")
                for chave, valor in kwargs.items():
                    arquivo.write(f"{chave.replace('_', ' ').capitalize()}: R$ {valor:.2f}\n")

            print(f"Arquivo salvo em: {caminho_arquivo}")
        except Exception as e:
            print(f"Erro ao salvar TXT: {str(e)}")

    def registrar_venda(self, valor_venda):
        """Adiciona o valor de uma venda ao total de vendas."""
        try:
            self.total_vendas += valor_venda
            print(f"Venda registrada: R$ {valor_venda:.2f}")
        except Exception as e:
            print(f"Erro ao registrar venda: {str(e)}")

    def registrar_saida(self, valor_saida):
        """Registra uma saída de caixa (ex.: troco dado, retirada)."""
        try:
            self.total_saidas += valor_saida
            print(f"Saída registrada: R$ {valor_saida:.2f}")
        except Exception as e:
            print(f"Erro ao registrar saída: {str(e)}")

############################### AREA De Configurações #############################################################

    

if __name__ == "__main__":
    import sys
   

    app = QApplication(sys.argv)

    # --- Passo 1: Checa licença antes do login ---
    acesso, aviso = lm.check_on_start()
    if not acesso:
        dlg = LicenseDialog()  # sua janela de inserção de chave
        if dlg.exec() != QDialog.Accepted:
            sys.exit(0)  # Fecha o programa se não ativar
    else:
        if aviso:
            QMessageBox.warning(None, "Aviso de Licença", aviso)

    # --- Passo 2: Abrir a tela de login ---
    login = Login()
    login.show()

    sys.exit(app.exec())



