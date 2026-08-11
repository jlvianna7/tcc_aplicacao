# H9 - EMPRESAS QUE UTILIZARAM TECNOLOGIAS DE INTELIGÊNCIA ARTIFICIAL

# %% importa pacotes

import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns

from backend import f_ConectaBD

#from aplicacao.app.pasta.arquivo import nome_da_funcao

# %% Configuração incial da Página

st.set_page_config(
    layout="wide",
    page_title="Transformação Digital e GMO"
    #    page_icon=""  pesquisar banco de ícones - talvez Keagle tenha
)
st.header(
    'Pesquisa aplicada sobre transformação digital nas empresas no Brasil', divider=True)
st.text('\n\n\n\n\n')

# TOTAL PARA O INDICADOR H9 - EMPRESAS QUE UTILIZARAM TECNOLOGIAS DE INTELIGÊNCIA ARTIFICIAL

st.sidebar.color_picker = "#FF7F27"
#st.sidebar.write("H1 - Empresas que fazem análises de Inteligência artificial")
st.sidebar.markdown("**H13 - Barreiras para utilização de Inteligência artificial**")

# %% Evolução anual, geral do uso de Inteligência artificial

st.subheader("Barreiras enfrentadas para a utilização de :yellow-background[Inteligência artificial]")

sql = (
    f'SELECT ano_pesquisa "Ano pesquisa", empresas_respondentes "Amostra" '
    f'FROM dm_resumo_pesquisa '
    f'order by ano_pesquisa; '
)

bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)

col1, col2 = st.columns([0.98, 0.02])

#col1.markdown("\n\n\n**Empresas pesquisadas**")
col1.markdown("**Proporção de barreiras mencionadas no uso de :yellow-background[Inteligência artificial]**")
col2.write(' ')

dfpesq = df[["Ano pesquisa", "Amostra"]]
#col1.table(dfpesq)

###
###
sql = (
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Obstáculo", qtd_resposta_sim "% de Empresas que utilizam" '
    f'FROM ft_ceticbr_totais '
    f'WHERE  cd_variavel like "h13%"  ' 
    f'order by 3 desc, "Obstáculo"; '
)


bd = f_ConectaBD.conn
dfl = pd.read_sql(sql, bd)

#col3.line_chart(dfl, x="Ano pesquisa", y="% de Empresas que utilizam", color="Serviço")
col1.bar_chart(dfl, x="Ano pesquisa", y="% de Empresas que utilizam", color="Obstáculo", stack=False, height=500)
col2.write(' ')

##############  BLOCO 2

st.subheader("Principais obstáculos no uso de :yellow-background[Inteligência artificial] em 2024")


sql = (
    f'SELECT t1.contexto "Obstáculo", ROUND(t1.qtd_resposta_sim * 100.0 / SUM(t1.qtd_resposta_sim) OVER(),1) AS "Frequência (%)" '
    f'FROM ft_ceticbr_totais t1 '
    f'WHERE  cd_variavel like "h13%"  ' 
    f'GROUP BY t1.contexto '
    f'ORDER BY 2 DESC; '
)
bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)


col1, col2 = st.columns([0.70, 0.30])

col1.write(' \n')
col2.write(' \n')
col1.write(' \n')
col2.write(' \n')


df.set_index('Obstáculo', inplace=True)
col1.write(' ')
col2.write(' ')
col1.bar_chart(df['Frequência (%)'], color='#0F3A69',horizontal=True, height=500, stack='layered')
col2.write(' ')



# %% FIM!
