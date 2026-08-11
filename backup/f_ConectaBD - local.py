import sqlite3
import pandas as pd


def conectar():
    try:
        conexao = sqlite3.connect('./bd/usp_dsa.db')
        print("Conexão ok!")
        return conexao
    except sqlite3.Error as e:
        print("Erro de conexão!", e)
        return None

conn = conectar()

'''
# EXEMPLO PARA UTILIZAÇÃO DIRETA DO Banco de Dados

query = 'select * from dm_mercado_atuacao'

df = pd.read_sql_query(query, conn)

df = pd.read_sql(query, conn)

# Exibindo o resultado
print(df)
'''
