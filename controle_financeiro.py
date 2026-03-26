import sqlite3
import os
from datetime import datetime

class CONTROLE_FINANCEIRO:
    def __init__(self, bd_name='bd/transacoes_entrada_saida.db'):
        self.bd_name = bd_name
        self.conn = None

    def conectar_ao_sqlite(self):
        try:
            # Verificar se o diretório 'bd' existe, caso contrário, criá-lo
            if not os.path.exists('bd'):
                os.makedirs('bd')

            # Conectar ao banco de dados SQLite
            self.conn = sqlite3.connect(self.bd_name)
            self.criar_tabela_transacoes()  # Chamando o método para criar a tabela
            self.criar_tabela_totais_entradas() # Chamando o método para criar a tabela
            self.criar_tabela_totais_saidas()  # Chamando o método para criar a tabela
            self.criar_tabela_receita_total() # Chamando o método para criar a tabela

            return self.conn
        except sqlite3.Error as e:
            print(f'Erro ao conectar ao banco de dados SQLite: {e}')
            return None
    #########################################################################################################################################################
    ##########################################    TABELA TRANSAÇÕES COMUNS (como vendas e retiradas do dia a dia)   ##########################################
    def criar_tabela_transacoes(self):
        if self.conn:
            cursor = self.conn.cursor()
            # Criar tabela se ela não existir
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transacoes_entrada_saida (
                    id INTEGER PRIMARY KEY,
                    tipo_transacao TEXT,
                    forma_pagamento TEXT,
                    valor REAL,
                    timestamp TEXT,
                    descricao TEXT
                )
            ''')
            # Salvar as alterações
            self.conn.commit()
    
    def inserir_transacao(self, tipo_transacao, forma_pagamento, valor, descricao):
        
        if not self.conn:
            self.conectar_ao_sqlite()

        # Formatar o timestamp
        timestamp_formatado = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')

        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO transacoes_entrada_saida (tipo_transacao, forma_pagamento, valor, timestamp, descricao)
            VALUES (?, ?, ?, ?, ?)
        ''', (tipo_transacao, forma_pagamento, valor, timestamp_formatado, descricao))

        self.conn.commit()

        # Chamar a função para inserir/atualizar o total de saidas
        if tipo_transacao == 'Saída':
            self.inserir_total_saidas(forma_pagamento, valor)

        # Chamar a função para inserir/atualizar o total de entradas
        elif tipo_transacao == 'Entrada':
            self.inserir_total_entrada(forma_pagamento, valor)
            
    def exibir_dados_transacoes(self):
        if not self.conn:
            self.conectar_ao_sqlite()

        cursor = self.conn.cursor()
        cursor.execute('SELECT tipo_transacao, forma_pagamento, valor, timestamp, descricao FROM transacoes_entrada_saida')
        rows = cursor.fetchall()

        return rows if rows else []

    def filtrar_por_forma_pagamento(self, tipo_transacao, forma_pagamento):
        if not self.conn:
            self.conectar_ao_sqlite()

        if forma_pagamento == "Tudo":  # Se selecionado "Tudo", exibir todas as transações
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT tipo_transacao, forma_pagamento, valor, timestamp, descricao
                FROM transacoes_entrada_saida
                WHERE tipo_transacao = ?
            ''', (tipo_transacao,))
            rows = cursor.fetchall()
            return rows if rows else []
        else:  # Caso contrário, filtrar por forma de pagamento específica
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT tipo_transacao, forma_pagamento, valor, timestamp, descricao
                FROM transacoes_entrada_saida 
                WHERE tipo_transacao = ? AND forma_pagamento = ?
            ''', (tipo_transacao, forma_pagamento))

            rows = cursor.fetchall()
            return rows if rows else []
        
    #####################################################################################################################
    ###########################################    TABELA TOTAIS DE ENTRADAS    ##########################################
    def criar_tabela_totais_entradas(self):
        if self.conn:
            cursor = self.conn.cursor()
            # Criar tabela de totais de entradas se ela não existir
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Totais_entradas(
                    Forma_Pagamento TEXT PRIMARY KEY,
                    Total REAL
                )
            ''')
            # Salvar as alterações
            self.conn.commit()

    def inserir_total_entrada(self, forma_pagamento, valor):
        if not self.conn:
            self.conectar_ao_sqlite()

        cursor = self.conn.cursor()

        # Verificar se a forma de pagamento já está na tabela
        cursor.execute('SELECT Total FROM Totais_entradas WHERE Forma_Pagamento = ?', (forma_pagamento,))
        existente = cursor.fetchone()

        if existente:
            # Atualizar o valor existente
            cursor.execute('UPDATE Totais_entradas SET Total = Total + ? WHERE Forma_Pagamento = ?', (valor, forma_pagamento))
        else:
            # Inserir novo registro
            cursor.execute('INSERT INTO Totais_entradas (Forma_Pagamento, Total) VALUES (?, ?)', (forma_pagamento, valor))

        self.conn.commit()

    def obter_totais_entradas(self):

        if not self.conn:
            self.conectar_ao_sqlite()

        cursor = self.conn.cursor()
        cursor.execute('SELECT Total FROM Totais_entradas')
        totais_entradas = cursor.fetchall()

        totais_entradas = sum(float(total[0]) for total in totais_entradas)
        return totais_entradas

    def somar_todas_entradas(self):
        if not self.conn:
            self.conectar_ao_sqlite()

        cursor = self.conn.cursor()
        cursor.execute('SELECT SUM(Total) FROM Totais_entradas')
        total_entradas = cursor.fetchone()[0]

        return float(total_entradas) if total_entradas else 0.0
    
    def obter_list_entradas(self):

        if not self.conn:
            self.conectar_ao_sqlite()

        cursor = self.conn.cursor()
        cursor.execute('SELECT Forma_Pagamento, Total FROM Totais_entradas')
        totais_entradas = cursor.fetchall()

        return dict(totais_entradas) if totais_entradas else {}

    #####################################################################################################################  
    ###########################################    TABELA TOTAIS DE SAÍDAS    ###########################################
    def criar_tabela_totais_saidas(self):
        if self.conn:
            cursor = self.conn.cursor()
            # Criar tabela de totais de saídas se ela não existir
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Totais_saidas(
                    Forma_Pagamento TEXT PRIMARY KEY,
                    Total REAL
                )
            ''')
            # Salvar as alterações
            self.conn.commit()

    def inserir_total_saidas(self, forma_pagamento, valor):
        if not self.conn:
            self.conectar_ao_sqlite()

        cursor = self.conn.cursor()

        # Verificar se a forma de pagamento já está na tabela
        cursor.execute('SELECT Total FROM Totais_saidas WHERE Forma_Pagamento = ?', (forma_pagamento,))
        existente = cursor.fetchone()

        if existente:
            # Atualizar o valor existente
            cursor.execute('UPDATE Totais_saidas SET Total = Total + ? WHERE Forma_Pagamento = ?', (valor, forma_pagamento))
        else:
            # Inserir novo registro
            cursor.execute('INSERT INTO Totais_saidas (Forma_Pagamento, Total) VALUES (?, ?)', (forma_pagamento, valor))

        self.conn.commit()
    
    def obter_totais_saidas(self):

        if not self.conn:
            self.conectar_ao_sqlite()

        cursor = self.conn.cursor()
        cursor.execute('SELECT Total FROM Totais_saidas')
        totais_saidas = cursor.fetchall()

        total_saidas = sum(float(total[0]) for total in totais_saidas)
        return total_saidas

    def somar_todas_saidas(self):
        if not self.conn:
            self.conectar_ao_sqlite()

        cursor = self.conn.cursor()
        cursor.execute('SELECT SUM(Total) FROM Totais_saidas')
        total_saidas = cursor.fetchone()[0]

        return float(total_saidas) if total_saidas else 0.0
    
    def obter_list_saidas(self):
        
        if not self.conn:
            self.conectar_ao_sqlite()

        cursor = self.conn.cursor()
        cursor.execute('SELECT Forma_Pagamento, Total FROM Totais_saidas')
        total_saidas = cursor.fetchall()

        return dict(total_saidas) if total_saidas else {}
    
    ########################################################################################################################################
    ###########################################    TABELA RECEITA FINAL "Entradas (-) Saidas"    ###########################################
    def criar_tabela_receita_total(self):
        if self.conn:
            cursor = self.conn.cursor()
            # Criar tabela de receita total se ela não existir
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Receita_Total(
                    Total_de_Entradas REAL,
                    Total_de_Saidas REAL,
                    Receita_Final REAL
                )
            ''')
            # Salvar as alterações
            self.conn.commit()

    def calculo_receita_final(self):
        total_entradas = self.somar_todas_entradas()
        total_saidas = self.somar_todas_saidas()

        if total_entradas is not None and total_saidas is not None:
            receita_final = round(float(total_entradas) - float(total_saidas), 2)
            return receita_final
        else:
            return None

    def update_total_receita_total(self):

        total_entradas = self.somar_todas_entradas()
        total_saidas = self.somar_todas_saidas()
        receita_final = self.calculo_receita_final()

        if not self.conn:
            self.conectar_ao_sqlite()

        cursor = self.conn.cursor()

        # Verificar se já existe um registro na tabela (assumindo que há apenas um registro único)
        cursor.execute('SELECT COUNT(*) FROM Receita_Total')
        count = cursor.fetchone()[0]

        if count > 0:
            # Atualizar o registro existente com a soma das entradas e saídas
            cursor.execute('UPDATE Receita_Total SET Total_de_Entradas = ?, Total_de_Saidas = ?, Receita_Final = ?',
                            (total_entradas, total_saidas, receita_final))  # Corrigido aqui
        else:
            # Inserir novo registro com a soma das entradas e saídas
            cursor.execute('INSERT INTO Receita_Total (Total_de_Entradas, Total_de_Saidas, Receita_Final) VALUES (?, ?, ?)',
                            (total_entradas, total_saidas, receita_final))

        self.conn.commit()

    def limpar_tabelas(self): 
        
        if not self.conn:
            self.conectar_ao_sqlite()

        cursor = self.conn.cursor()
        
        # Deletar os dados de cada tabela
        cursor.execute('DELETE FROM transacoes_entrada_saida')
        cursor.execute('DELETE FROM Totais_entradas')
        cursor.execute('DELETE FROM Totais_saidas')
        cursor.execute('DELETE FROM Receita_Total')
        
        # Confirmar as alterações
        self.conn.commit()

        print("Todas as tabelas foram limpas com sucesso.")


    ########################################################################################################################################
    def close_connection(self):
        if self.conn:
            self.conn.close()
    ####################################################################################################
    ################################# Verificação das transações ######################################
    def verificar_transacoes(self):
        #print('\nVerificando transações inseridas:')
        transacoes = self.exibir_dados_transacoes()
        for transacao in transacoes:
            pass
            #print(transacao)
    ###################################################################################################
    ################################# Verificação dos totais de entradas ##############################
    def verificar_totais_entradas(self):
        #print('\nVerificando totais de entradas:')
        totais_entradas = self.obter_totais_entradas()
        #
    ####################################################################################################
    ################################# Verificação dos totais de saídas #################################
    def verificar_totais_saidas(self):
        #print('\nVerificando totais de saídas:')
        totais_saidas = self.obter_totais_saidas()
        #print(totais_saidas)
    ####################################################################################################
    ################################# Verificação da receita final #####################################
    def verificar_receita_final(self):
       # print('\nVerificando receita final:')
        receita_final = self.calculo_receita_final()
       # print(receita_final)
    ####################################################################################################

# Exemplo de uso
if __name__ == "__main__":
    banco_cf = CONTROLE_FINANCEIRO()
    banco_cf.conectar_ao_sqlite()
    banco_cf.update_total_receita_total()
    
"""    # Fechar a conexão com o banco de dados fora do loop
    banco_cf.close_connection()

    for i in range(2):
        # Inserir transações
        banco_cf.inserir_transacao('Entrada', 'Dinheiro', 36.89 + (i + 6) / 100, f'Venda no PDV {i + 1}')
        banco_cf.inserir_transacao('Entrada', 'Cartão de Crédito', 15.0 + (i + 23) / 100, f'Venda no PDV {i + 1}')
        banco_cf.inserir_transacao('Entrada', 'Cartão de Débito', 11.63 + (i + 132) / 100, f'Venda no PDV {i + 1}')
        banco_cf.inserir_transacao('Entrada', 'Pix', 26.36 + (i + 38) / 100, f'Venda no PDV {i + 1}')

        banco_cf.inserir_transacao('Saída', 'Dinheiro', 26.39 + (i + 11) / 100, f'Pagamento de fornecedor {i + 1}')
        banco_cf.inserir_transacao('Saída', 'Cartão de Crédito', 1.67 + (i + 1) / 100, f'Pagamento de fornecedor {i + 1}')
        banco_cf.inserir_transacao('Saída', 'Cartão de Débito', 2.0 + (i + 12) / 100, f'Pagamento de fornecedor {i + 1}')
        banco_cf.inserir_transacao('Saída', 'Pix', 7.0 + (i + 87) / 100, f'Pagamento de fornecedor {i + 1}')



    # Verificação das transações, totais de entradas, totais de saídas e receita final
    banco_cf.verificar_transacoes()
    banco_cf.verificar_totais_entradas()
    banco_cf.verificar_totais_saidas()
    banco_cf.verificar_receita_final()
"""