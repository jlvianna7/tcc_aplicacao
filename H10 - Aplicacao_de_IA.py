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
st.sidebar.markdown("**H10 - Aáreas de utilização de Inteligência artificial**")

# %% Evolução anual, geral do uso de Inteligência artificial

st.subheader("Evolução da utilização de :yellow-background[Inteligência artificial]")

sql = (
    f'SELECT ano_pesquisa "Ano pesquisa", empresas_respondentes "Amostra" '
    f'FROM usp_dsa.dm_resumo_pesquisa '
    f'order by ano_pesquisa; '
)

bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)

col1, col2, col3 = st.columns([0.15, 0.02, 0.83])

col1.markdown("\n\n\n**Empresas pesquisadas**")
col2.write(' ')
col3.markdown("**Proporção de empresas que utilizam :yellow-background[Inteligência artificial]**")

dfpesq = df[["Ano pesquisa", "Amostra"]]
col1.table(dfpesq)

###
###
sql = (
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Aplicação", qtd_resposta_sim "% de Empresas que utilizam" FROM ft_h10a_totais '
    F'WHERE ANO_PESQUISA > "2015" ' 
    f'UNION '
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Aplicação", qtd_resposta_sim "% de Empresas que utilizam" FROM ft_h10b_totais '
    F'WHERE ANO_PESQUISA > "2015" ' 
    f'UNION '
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Aplicação", qtd_resposta_sim "% de Empresas que utilizam" FROM ft_h10c_totais '
    F'WHERE ANO_PESQUISA > "2015" ' 
    f'UNION '
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Aplicação", qtd_resposta_sim "% de Empresas que utilizam" FROM ft_h10d_totais '
    F'WHERE ANO_PESQUISA > "2015" ' 
    f'UNION '
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Aplicação", qtd_resposta_sim "% de Empresas que utilizam" FROM ft_h10e_totais '
    F'WHERE ANO_PESQUISA > "2015" ' 
    f'UNION '
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Aplicação", qtd_resposta_sim "% de Empresas que utilizam" FROM ft_h10f_totais '
    F'WHERE ANO_PESQUISA > "2015" ' 
    f'UNION '
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Aplicação", qtd_resposta_sim "% de Empresas que utilizam" FROM ft_h10g_totais '
    F'WHERE ANO_PESQUISA > "2015" ' 
    f'order by "Ano_pesquisa", "Aplicação"; '
)
bd = f_ConectaBD.conn
dfl = pd.read_sql(sql, bd)

#col3.line_chart(dfl, x="Ano pesquisa", y="% de Empresas que utilizam", color="Serviço")
#col3.bar_chart(dfl, x="Ano pesquisa", y="% de Empresas que utilizam", color="Aplicação", stack=False)
col3.bar_chart(dfl, x="Aplicação", y="% de Empresas que utilizam", color="Ano pesquisa", stack=False)


# %% FIM!
