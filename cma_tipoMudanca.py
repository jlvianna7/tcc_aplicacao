#
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
st.header('Pesquisa aplicada sobre transformação digital nas empresas no Brasil', divider=True)
st.text(' \n')


st.sidebar.color_picker = "#FF7F27"
st.subheader("Pesquisa CMA - Que tipos de mudanças você tipicamente gerencia?\n")
st.markdown("A ideia da pergunta é entender quais foram as mudanças mais frequentes nas organizações, nos últimos anos.")
st.write(' \n')
st.write(' \n')
st.write(' \n')


sql = (
    f'SELECT ds_tipomudanca "Tipos de mudanças" '
    f'from ft_cma_tipomudanca '
)


bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)


# 1. Agrupa e conta os registros
df_analise = df.groupby('Tipos de mudanças').size().reset_index(name='Menções')

# 2. Calcula o percentual sobre o total da coluna 'Quantidade'
df_analise['Frequência (%)'] = (df_analise['Menções'] / df_analise['Menções'].sum()) * 100
df_analise['Frequência (%)'] = df_analise['Frequência (%)'].round(2)
# 3. Ordena do maior para o menor
df_analise = df_analise.sort_values(by='Frequência (%)', ascending=False)

#df_analise = df['Tipos de mudanças'].value_counts(normalize=True) * 100

col1, col2, col3 = st.columns([0.33, 0.02, 0.65])

col1.table(df_analise)
col2.write(' ')
df_analise.set_index('Tipos de mudanças', inplace=True)
col3.bar_chart(df_analise['Frequência (%)'], color='#75FA8D')

#value=f"£{dados_jogador['Value(£)']:,}"
