import sqlite3
import os

class Banco_Users:
    def __init__(self):
        self.conexao = None

    def conectar_ao_sqlite(self):
        try:
            caminho_bd = os.path.join('bd', 'bduser.db')
            conexao = sqlite3.connect(caminho_bd)
            print("Conexão ao Banco User estabelecida.")
            cursor = conexao.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    password TEXT,
                    privilegio TEXT
                )
            """)
            #print("Banco de dados User Criado ou já Existe.")
            self.conexao = conexao
            return conexao
        except sqlite3.Error as erro:
            print(f"Erro ao conectar ao SQLite: {erro}")
            return None

    def inserir_new_user(self, nome, password, privilegio):
        try:
            cursor = self.conexao.cursor()
            sql = "INSERT INTO usuarios (nome, password, privilegio) VALUES (?, ?, ?)"
            valores = (nome, password, privilegio)
            cursor.execute(sql, valores)
            self.conexao.commit()
            print("Dados inseridos com sucesso na tabela user.")
        except sqlite3.Error as erro:
            print(f"Erro ao inserir dados na tabela: {erro}")
    
    def deletar_user(self, id_usuario):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
            self.conexao.commit()  # Confirme a transação
            print("Usuário deletado com sucesso.")
        except sqlite3.Error as e:
            self.conexao.rollback()  # Reverta a transação em caso de erro
            print("Erro ao deletar usuário:", e)

    def listar_user(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT * FROM usuarios")
            usuarios = cursor.fetchall()
            return usuarios
        except sqlite3.Error as e:
            print("Erro ao listar usuários:", e)
            return None

    def check_user(self, name, password):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND password = ?", (name, password))
            usuario = cursor.fetchone()
            if usuario:
                # Verifica se a tupla retornada tem pelo menos 5 elementos (0-indexed)
                if len(usuario) >= 4:
                    privilegio = usuario[3]  # A quinta coluna contém o privilégio do usuário
                    return (name, password, privilegio)
                else:
                    print("Erro: a tupla retornada não tem elementos suficientes.")
                    return None
            else:
                return None  # Usuário não encontrado
        except Exception as e:
            print("Erro ao Verificar Usuário:", e)
            return None
        
    def close_connection(self):
        if self.conexao:
            self.conexao.close()


############### ADICIONA USUARIOS #############

"""# Criar uma instância da classe Banco_Users
banco_users = Banco_Users()

nome = "admin"
senha = "admin"
privilegio = "Admin"

# Conectar ao banco de dados SQLite
conexao = banco_users.conectar_ao_sqlite()

# Verificar se a conexão foi bem-sucedida antes de adicionar o novo usuário
if conexao is not None:
    banco_users.inserir_new_user(nome, senha, privilegio)
else:
    print("Não foi possível estabelecer uma conexão com o banco de dados.")
"""

############### LISTAR USUARIOS #############
    
"""# Criar uma instância da classe Banco_Users
banco_users = Banco_Users()

# Conectar ao banco de dados SQLite
conexao = banco_users.conectar_ao_sqlite()

if conexao:
    # Listar usuários
    listar = banco_users.listar_user()  # Não é necessário passar a conexão
    if listar:
        print("Lista de usuários:")
        for usuario in listar:
            print(usuario)
    else:
        print("Não foi possível listar os usuários.")
else:
    print("Não foi possível conectar ao banco de dados.")"""

############### DELETAR USUARIOS #############

"""# Criar uma instância da classe Banco_Users
banco_users = Banco_Users()

# Conectar ao banco de dados SQLite
conexao = banco_users.conectar_ao_sqlite()

if conexao:
    # Deletar um usuário (substitua 1 pelo ID do usuário que você deseja deletar)
    banco_users.deletar_user(1)
else:
    print("Não foi possível conectar ao banco de dados.")"""

############### CHECAR USUARIOS #############

