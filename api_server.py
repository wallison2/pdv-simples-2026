from fastapi import FastAPI, HTTPException
import sqlite3
import os
import fastapi
import signal
import uvicorn
from pydantic import BaseModel
from typing import List     


# ===========================================
# Inicialização da API
# ===========================================

app = FastAPI()

@app.get("/status", status_code=200)
def status():
    return {}

def shutdown():
    os.kill(os.getpid(), signal.SIGTERM)
    return fastapi.Response(status_code=200, content='Server shutting down...')


# ===========================================
# Classe base para operações no banco
# ===========================================

class Database:
    def __init__(self, db_name):
        self.db_path = db_name   # caminho centralizado

    def connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn


# ===========================================
# Classe para operações no estoque
# ===========================================

class APIEstoque(Database):
    def __init__(self):
        super().__init__("./bd/bdestoque.db")  # único caminho usado

    # ---------------- LISTAR ----------------
    def listar_todos(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM estoque")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    # ---------------- BUSCAR ----------------
    def buscar_estoque(self, codigo=None, barras=None, nome=None):
        conn = self.connect()
        cursor = conn.cursor()

        query = """
            SELECT codigo_produto, barras_prod, nome_produto, descricao_produto, 
                   qtda_produto, uni_pcto_produto, valor_compra, valor_produto
            FROM estoque
            WHERE 1=1
        """
        params = []

        if codigo:
            query += " AND codigo_produto = ?"
            params.append(codigo)

        if barras:
            query += " AND barras_prod = ?"
            params.append(barras)

        if nome:
            query += " AND nome_produto LIKE ?"
            params.append(f"%{nome}%")

        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    # ---------------- INSERIR ----------------
    def inserir_dados_produto(self, produto):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(""" 
            INSERT INTO estoque (codigo_produto, barras_prod, nome_produto, descricao_produto, 
                                 qtda_produto, uni_pcto_produto, valor_compra, valor_produto)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, produto)

        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    # ---------------- ATUALIZAR PARCIAL ----------------
    def atualizar_produto_parcial(self, codigo_produto, **dados_atualizados):
        try:
            if not codigo_produto:
                raise ValueError("Código do produto obrigatório.")
            if not dados_atualizados:
                raise ValueError("Nenhum dado enviado para atualizar.")

            campos_validos = {
                "barras_prod": str,
                "nome_produto": str,
                "descricao_produto": str,
                "qtda_produto": (int, float),
                "uni_pcto_produto": str,
                "valor_compra": (int, float),
                "valor_produto": (int, float),
            }

            sql_set = []
            valores = []

            for campo, valor in dados_atualizados.items():
                if campo not in campos_validos:
                    raise ValueError(f"Campo inválido: {campo}")
                if not isinstance(valor, campos_validos[campo]):
                    raise ValueError(f"Tipo inválido para {campo}")

                sql_set.append(f"{campo} = ?")
                valores.append(valor)

            sql = f"UPDATE estoque SET {', '.join(sql_set)} WHERE codigo_produto = ?"
            valores.append(codigo_produto)

            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()

            alterados = cursor.rowcount
            conn.close()

            return alterados > 0

        except Exception as e:
            print("Erro ao atualizar produto:", e)
            return False

    # ---------------- EXCLUIR ----------------
    def excluir_produtos(self, lista_ids):
        try:
            conn = self.connect()
            cursor = conn.cursor()

            for id_produto in lista_ids:
                cursor.execute("DELETE FROM estoque WHERE codigo_produto = ?", (id_produto,))

            conn.commit()
            conn.close()
            return True

        except Exception as e:
            print("ERRO BANCO:", e)
            return False

    # ---------------- ATUALIZAR QUANTIDADE ----------------
    def up_produt_quantiade(self, codigo_produto, nova_quantidade):
        try:
            if not codigo_produto:
                raise ValueError("Código obrigatório.")
            if nova_quantidade is None:
                raise ValueError("Quantidade ausente.")
            if not isinstance(nova_quantidade, (int, float)):
                raise ValueError("Quantidade inválida.")

            conn = self.connect()
            cursor = conn.cursor()

            sql = "UPDATE estoque SET qtda_produto = ? WHERE codigo_produto = ?"
            cursor.execute(sql, (nova_quantidade, codigo_produto))

            conn.commit()
            alterados = cursor.rowcount
            conn.close()
            return alterados > 0

        except Exception as e:
            print("Erro ao atualizar quantidade:", e)
            return False

    # ---------------- BUSCAR UM PRODUTO ----------------
    def buscar_produto_por_codigo_ou_barras(self, valor):
        try:
            conn = self.connect()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT codigo_produto, barras_prod, nome_produto, descricao_produto,
                       qtda_produto, uni_pcto_produto, valor_compra, valor_produto
                FROM estoque
                WHERE codigo_produto = ? OR barras_prod = ?
            """, (str(valor), str(valor)))

            row = cursor.fetchone()
            conn.close()

            if row:
                return {
                    "codigo_produto": row[0],
                    "barras_prod": row[1],
                    "nome_produto": row[2],
                    "descricao_produto": row[3],
                    "qtda_produto": int(row[4]),
                    "uni_pcto_produto": row[5],
                    "valor_compra": float(row[6]),
                    "valor_produto": float(row[7]),
                }

            return None

        except Exception as e:
            print("Erro ao buscar produto:", e)
            return None



# ===========================================
# Classe de usuários
# ===========================================

class APIUsuarios(Database):
    def __init__(self):
        super().__init__("./bd/bduser.db")

    def listar_todos(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]


# ===========================================
# Classe de financeiro
# ===========================================

class APIFinanceiro(Database):
    def __init__(self):
        super().__init__("./bd/transacoes_entrada_saida.db")

    def registrar_transacao(self, tipo, valor, descricao):
        try:
            conn = self.connect()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO transacoes (tipo, valor, descricao)
                VALUES (?, ?, ?)
            """, (tipo, valor, descricao))

            conn.commit()
            conn.close()

            return {"status": "Transação registrada com sucesso"}

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


# Classe para operações de usuários
class APIUsuarios(Database):
    def __init__(self):
        super().__init__("./bd/bduser.db")

    def listar_todos(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

# Classe para operações financeiras
class APIFinanceiro(Database):
    def __init__(self):
        super().__init__("./bd/transacoes_entrada_saida.db")

    def registrar_transacao(self, tipo, valor, descricao):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO transacoes (tipo, valor, descricao) VALUES (?, ?, ?)
            """, (tipo, valor, descricao))
            conn.commit()
            conn.close()
            return {"status": "Transação registrada com sucesso"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))



# Classe para operações de usuários
class APIUsuarios(Database):
    def __init__(self):
        super().__init__("./bd/bduser.db")

    def listar_todos(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

# Classe para operações financeiras
class APIFinanceiro(Database):
    def __init__(self):
        super().__init__("./bd/transacoes_entrada_saida.db")

    def registrar_transacao(self, tipo, valor, descricao):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO transacoes (tipo, valor, descricao) VALUES (?, ?, ?)
            """, (tipo, valor, descricao))
            conn.commit()
            conn.close()
            return {"status": "Transação registrada com sucesso"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))



