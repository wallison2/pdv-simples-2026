import sqlite3
import os

class Banco_Estoque:
    def __init__(self, est_db="bdestoque.db") -> None:
        self.est_db = est_db
        self.conexao = None
        self.conectar_ao_sqlite()  # Garante que a conexão seja feita ao instanciar

    def conectar_ao_sqlite(self):
        try:
            caminho_bd = os.path.join('bd', self.est_db)
            self.conexao = sqlite3.connect(caminho_bd)
            #print("Conexão ao Banco Estoque estabelecida.")
            self.criar_tabela_estoque()  # Garante que a tabela será criada
            return self.conexao
        except sqlite3.Error as erro:
            print(f"Erro ao conectar ao SQLite: {erro}")
            return None

    def criar_tabela_estoque(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS estoque (
                    codigo_produto INTEGER PRIMARY KEY AUTOINCREMENT,
                    barras_prod TEXT,
                    nome_produto TEXT,
                    descricao_produto TEXT,
                    qtda_produto INTEGER,
                    uni_pcto_produto TEXT,
                    valor_compra REAL,
                    valor_produto REAL
                )
            """)
            self.conexao.commit()  # Confirma a criação da tabela
            #print("Tabela 'estoque' criada ou já existe.")
        except sqlite3.Error as erro_criacao:
            print(f"Erro ao criar a tabela de estoque: {erro_criacao}")
            raise Exception("Erro na criação da tabela de estoque")

    def inserir_dados_produto(self, codigo_produto, barras_prod, nome_produto, descricao_produto, qtda_produto, uni_pcto_produto, valor_compra, valor_produto):
        try:
            cursor = self.conexao.cursor()
            sql = """
                INSERT INTO estoque (codigo_produto, barras_prod, nome_produto, descricao_produto, qtda_produto, uni_pcto_produto, valor_compra, valor_produto)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            valores = (codigo_produto, barras_prod, nome_produto, descricao_produto, qtda_produto, uni_pcto_produto, valor_compra, valor_produto)
            cursor.execute(sql, valores)
            self.conexao.commit()
            print("Dados inseridos com sucesso na tabela estoque.")
        except sqlite3.Error as erro:
            print(f"Erro ao inserir dados na tabela: {erro}")

    def excluir_item_estoque(self, idEstoque):
        try:
            cursor = self.conexao.cursor()
            for id_a_excluir in idEstoque:
                sql = "DELETE FROM estoque WHERE codigo_produto = ?"
                cursor.execute(sql, (id_a_excluir,))
            self.conexao.commit()
            cursor.close()
        except sqlite3.Error as err:
            print(f"Erro ao excluir o(s) produto(s): {err}")

     # Função para excluir todos os dados da tabela estoque
    
    def excluir_todos_dados_estoque(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM estoque")  # Remove todos os dados da tabela
            self.conexao.commit()
            print("Todos os dados foram excluídos da tabela 'estoque'.")
        except sqlite3.Error as erro:
            print(f"Erro ao excluir todos os dados da tabela estoque: {erro}")

    def atualizar_dados_estoque(self, codigo_produto, coluna, novo_valor):
        try:
            cursor = self.conexao.cursor()
            if coluna in ["barras_prod", "nome_produto", "descricao_produto", "qtda_produto", "uni_pcto_produto", "valor_compra", "valor_produto"]:
                sql = f"UPDATE estoque SET {coluna} = ? WHERE codigo_produto = ?"
                cursor.execute(sql, (novo_valor, codigo_produto))  # Usando o código como filtro
                self.conexao.commit()
                return True
            else:
                print("Erro: Coluna inválida especificada.")
                return False
        except sqlite3.Error as erro:
            print(f"Erro ao atualizar os dados: {erro}")
            return False

    def buscar_produto(self, texto_pesquisa):
        try:
            cursor = self.conexao.cursor()
            sql = "SELECT * FROM estoque WHERE nome_produto LIKE ? OR codigo_produto = ?"
            cursor.execute(sql, ('%' + texto_pesquisa + '%', texto_pesquisa))
            produtos = cursor.fetchall()
            return produtos
        except sqlite3.Error as erro:
            print(f"Erro ao buscar o produto: {erro}")
            return None

    def buscar_produto_por_codigo_ou_barras(self, codigo_produto_ou_barras):
        """ Busca um produto pelo código do produto ou código de barras."""
        try:
            cursor = self.conexao.cursor()
            sql = """
                SELECT codigo_produto, barras_prod, nome_produto, descricao_produto, qtda_produto, uni_pcto_produto, valor_compra, valor_produto
                FROM estoque
                WHERE codigo_produto = ? OR barras_prod = ?
            """
            # Converte o valor para string para evitar problemas de tipo na busca
            codigo_produto_ou_barras = str(codigo_produto_ou_barras)

            cursor.execute(sql, (codigo_produto_ou_barras, codigo_produto_ou_barras))  
            resultado = cursor.fetchone()  # Retorna uma única linha

            if resultado:
                codigo_prod = resultado[0]  # codigo_produto
                nome = resultado[2]  # nome_produto
                quantidade_estoque = int(resultado[4])  # qtda_produto (converte para int)
                valor_unitario = float(resultado[7])  # valor_produto (converte para float)
                return codigo_prod, nome, quantidade_estoque, valor_unitario

            return None
        except sqlite3.Error as erro:
            print(f"Erro ao buscar produto por código ou barras: {erro}")
            return None

    def produto_upgrade_estoque(self, codigo_produto):
        """
        Busca as informações do produto a partir do código,
        retornando código, barras_prod, nome, descrição, quantidade, valor da compra e valor da venda.
        """
        try:
            cursor = self.conexao.cursor()
            sql = """
                SELECT codigo_produto, barras_prod, nome_produto, descricao_produto, 
                    qtda_produto, uni_pcto_produto, valor_compra, valor_produto
                FROM estoque 
                WHERE codigo_produto = ?
            """
            cursor.execute(sql, (codigo_produto,))
            resultado = cursor.fetchone()  # Retorna uma única linha com todos os campos
            
            if resultado:
                # Retorna os valores na sequência desejada
                return (resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5],  resultado[6], resultado[7])  
                # código, barras_prod, nome, descrição, quantidade, tipo, valor da compra, valor da venda
            
            return None
        except sqlite3.Error as erro:
            print(f"Erro ao buscar produto por código: {erro}")
            return None
        
    def atualizar_dados_estoque(self, codigo_produto, coluna, novo_valor):
        try:
            cursor = self.conexao.cursor()
            # Verifique se a coluna é válida
            colunas_validas = ["codigo_produto", "barras_prod", "nome_produto", "descricao_produto", "qtda_produto", "uni_pcto_produto", "valor_compra", "valor_produto"]
            if coluna not in colunas_validas:
                raise ValueError(f"Coluna {coluna} inválida.")
            
            # Atualize o banco
            sql = f"UPDATE estoque SET {coluna} = ? WHERE codigo_produto = ?"
            cursor.execute(sql, (novo_valor, codigo_produto))
            self.conexao.commit()
            return True
        except sqlite3.Error as erro:
            print(f"Erro ao atualizar os dados no banco de dados: {erro}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False

    def check_database_connection(self):
        try:
            connection = sqlite3.connect(self.est_db)
            #print("Conexão com o banco de Estoque estabelecida 'COD: 200'")
            return True, connection
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False, None

    def listar_dados_estoque(self):
        try:
            cursor = self.conexao.cursor()
            consulta_sql = "SELECT codigo_produto, barras_prod, nome_produto, descricao_produto, qtda_produto, uni_pcto_produto, valor_compra, valor_produto FROM estoque"
            cursor.execute(consulta_sql)
            resultados = cursor.fetchall()
            return resultados
        except sqlite3.Error as erro:
            print(f"Erro ao listar dados da tabela: {erro}")
            return None

    def listar_todos_produtos(self):
        self.conectar_ao_sqlite()  # Garante que a conexão esteja estabelecida
        if self.conexao is not None:
            try:
                todos_produtos = self.listar_dados_estoque()
                return todos_produtos
            except Exception as e:
                print(f"Erro ao listar todos os produtos: {e}")
                return None
        else:
            print("Erro: Conexão não estabelecida.")
            return None

    def close_connection(self):
        if self.conexao:
            self.conexao.close()

    def query(self, sql, params=()):
        cursor = self.conexao.cursor()
        cursor.execute(sql, params)
        resultado = cursor.fetchone()  # Retorna uma única linha
        return resultado


