#
# %% importa pacotes

import numpy as np
import pandas as pd
import plotly.express as px
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
st.header('Pesquisa aplicada sobre transformação digital nas empresas no Brasil', divider=True)
st.text('\n\n\n\n\n')


st.subheader("Pesquisa CMA - Qual é o maior desafio para a transformação organizacional da sua organização nos próximos 2 anos?")
st.markdown("Nos dias atuais, quando falamos em transformação nas organizações, estamos quase que de forma intrinseca falando de transformação digital. \n"
            "A pesquisa quis entender, das organizações que tem e das que não tem um CMO estruturado, para o contexto da Transformação Digital,"
            " quais sãos maiores os desafios, relacionados a mudanças, vislumbrados nos próximos dois anos.") 
st.write(' \n')
st.write(' \n')
st.write(' \n')
st.write(' \n')

############## Se tem CMO ou não
sql = (
    f'SELECT ds_maiordesafioTD "Maior desafio" '
    f'FROM ft_cma_maiordesafiotd '
)
bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)

# 1. Agrupa e conta os registros
df_analise = df.groupby('Maior desafio').size().reset_index(name='Menções')

# 2. Calcula o percentual sobre o total da coluna 'Quantidade'
df_analise['Frequência (%)'] = (df_analise['Menções'] / df_analise['Menções'].sum()) * 100
df_analise['Frequência (%)'] = df_analise['Frequência (%)'].round(2)
# 3. Ordena do maior para o menor
df_analise = df_analise.sort_values(by='Frequência (%)', ascending=False)

col1, col2 = st.columns([0.70, 0.30])


#col1.table(df_analise, hide_index=True)

#col1.table(df_analise.style.format({"Maior desafio": None , "Menções": "{:.0f}", "Frequência (%)": "{:.1f}%"}), hide_index=True)
col1.table(df_analise.style.format({"Maior desafio": None , "Menções": "{:.0f}", "Frequência (%)": "{:.1f}%"}))

col2.write(' ')
#bd.close
