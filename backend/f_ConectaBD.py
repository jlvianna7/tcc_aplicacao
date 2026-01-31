import sqlite3
import threading

#import pandas as pd

local = threading.local()

def conectar():
    try:
        if not hasattr(local, 'conn'):
            local.conn = sqlite3.connect('./bd/usp_dsa.db', check_same_thread=False)
#            print("Conexão ok!")
        return local.conn
    except sqlite3.Error as e:
        print("Erro de conexão!", e)
        return None

conn = conectar()


'''

import threading
local = threading.local()

def get_db_connection():
    if not hasattr(local, 'conn'):
        local.conn = sqlite3.connect('sua_base.db', check_same_thread=False)
    return local.conn


# EXEMPLO PARA UTILIZAÇÃO DIRETA DO Banco de Dados

query = 'select * from dm_mercado_atuacao'

df = pd.read_sql_query(query, conn)

df = pd.read_sql(query, conn)

# Exibindo o resultado
print(df)

'''