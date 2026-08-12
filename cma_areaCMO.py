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


st.subheader("Pesquisa CMA - Sua organização tem um CMO?  -  Se sim, a qual área está vinculado?")
st.markdown("Nesta questão o objetivo foi entender se as empresas estão estruturando **Escritório de Gestão de Mudanças** e, se estão, "
             "como estão estruturados. E para as organizações que não tem um **Change Management Office (CMO)**, quais os principais desafios. ")
st.write(' \n')
st.write(' \n')
st.write(' \n')

############## Se tem CMO ou não
sql = (
    f'SELECT tem_cmo "Tem CMO estruturado" '
    f'FROM ft_cma_principal '
)

bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)
#bd.close()

col1, col2, col3 = st.columns([0.33, 0.02, 0.65])

# Prepara os dados: conta as ocorrências de uma coluna
df_pizza = df["Tem CMO estruturado"].value_counts().reset_index()
df_pizza.columns = ["Tem CMO estruturado", "Quantidade"]

# Cria o gráfico de pizza
fig = px.pie(df_pizza, values="Quantidade", names="Tem CMO estruturado", title="A organização possui um CMO estruturado")
# Exibe no Streamlit
col1.plotly_chart(fig)

############## Qual a vinculação
sql = (
    F'SELECT area_vinculo "Área de vínculo do CMO" '
    F'FROM ft_cma_principal '
    f'WHERE tem_cmo = "Sim";' 
)

bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)
#bd.close()

# 1. Agrupa e conta os registros
df_analise = df.groupby('Área de vínculo do CMO').size().reset_index(name='Menções')

# 2. Calcula o percentual sobre o total da coluna 'Quantidade'
df_analise['Frequência (%)'] = (df_analise['Menções'] / df_analise['Menções'].sum()) * 100
df_analise['Frequência (%)'] = df_analise['Frequência (%)'].round(1)
# 3. Ordena do maior para o menor
df_analise = df_analise.sort_values(by='Frequência (%)', ascending=False)

col2.write(' ')
df_analise.set_index('Área de vínculo do CMO', inplace=True)
col3.markdown('**Existindo, a qual área o CMO está vinculado**\n')

#col3.bar_chart(df_analise['Frequência (%)'], color='#3282F6', height=500, y_label="'Frequência (%)'")
fig_p = px.bar(df_analise, y="Frequência (%)", text=df_analise["Frequência (%)"].astype(str) + " %", height=500, color_discrete_sequence=["#3282F6"])
col3.plotly_chart(fig_p)


############## BLOCO 2 ###############
col1.write(' \n')
col2.write(' \n')
col3.write(' \n')

st.subheader("Pesquisa CMA - Empresas que não tem um **Change Management Office (CMO)**")
st.markdown("Como ocorrem os processos de as em organizações que não possuem um Escritório de Gestão de Mudanças estruturado,"
             " quais áreas, normalmente, conduzem os processos de mudanças na organização e quais são os principais desafios para a estruturação de um GMO. ")
st.write(' \n')
st.write(' \n')


############## QUEM CUIDA DE MUDANÇA ONDE NÃO TEM GMO
sql = (
    F'SELECT area_vinculo "Área responsável por gerir mudanças" '
    F'FROM ft_cma_principal '
    f'WHERE tem_cmo <> "Sim";' 
)

bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)
#bd.close()

col1, col2 = st.columns([0.98, 0.02])

# 1. Agrupa e conta os registros
df_analise = df.groupby('Área responsável por gerir mudanças').size().reset_index(name='Menções')

# 2. Calcula o percentual sobre o total da coluna 'Quantidade'
df_analise['Frequência (%)'] = (df_analise['Menções'] / df_analise['Menções'].sum()) * 100
df_analise['Frequência (%)'] = df_analise['Frequência (%)'].round(1)

# 3. Ordena do maior para o menor
df_analise = df_analise.sort_values(by='Frequência (%)', ascending=False)

df_analise.set_index('Área responsável por gerir mudanças', inplace=True)
col1.markdown('**Área, __normalmente__, responsável por gerir mudanças**\n')
#col1.bar_chart(df_analise['Frequência (%)'], color='#CF181F',horizontal=True, height=500, stack='layered')
#col1.bar_chart(df_analise['Frequência (%)'], color='#CF181F',horizontal=True, height=500, stack='layered')
# Criando o gráfico com rótulos de dados
#fig = px.bar(df_analise, x='Área responsável por gerir mudanças', y='Frequência (%)', text='Frequência (%)')

fig = px.bar(df_analise, y='Frequência (%)', text=df_analise["Frequência (%)"].astype(str) + " %", height=600, color_discrete_sequence=["#3282F6"])

# Ajustando a posição do texto (opcional)
#fig.update_traces(textposition='outside')

st.plotly_chart(fig, col1)


############## QUEM CUIDA DE MUDANÇA ONDE NÃO TEM GMO

sql = (
    f'SELECT ds_3DesafiosGMO "Descrição" '
    f'FROM ft_cma_3desafiosgmo '
)

bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)
#bd.close()

# 1. Agrupa e conta os registros
df_analise = df.groupby('Descrição').size().reset_index(name='Menções')

# 2. Calcula o percentual sobre o total da coluna 'Quantidade'
df_analise['Frequência (%)'] = (df_analise['Menções'] / df_analise['Menções'].sum()) * 100
df_analise['Frequência (%)'] = df_analise['Frequência (%)'].round(2)
# 3. Ordena do maior para o menor
df_analise = df_analise.sort_values(by='Frequência (%)', ascending=False)

col1, col2 = st.columns([0.70, 0.30])

col1.write(' ')
col2.write(' ')
col1.subheader("Principais desafios para a gestão de mudanças nestas organizações", divider='gray')
col1.table(df_analise)
col2.write(' ')
