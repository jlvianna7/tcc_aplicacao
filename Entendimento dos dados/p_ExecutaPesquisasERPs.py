#
# Execução das pesquisas
#
# %% importa pacotes

import pandas as pd
import numpy as np
import seaborn as sns
import f_ConectaBD
import streamlit as st

# %% Configuração incial da Página

st.set_page_config(
    layout="wide",
    page_title="Transformação Digital com GMO"
    #    page_icon=""  pesquisar banco de ícones - talvez Keagle tenha

)
st.sidebar.color_picker = "#FF7F27"
st.sidebar.write("Evolução do uso de ERPs")


# %% Evolução anual, geral do uso de ERPs

sql = (
    f'select ano_pesquisa, sum(qtd_resposta_sim) as total '
    f'from usp_dsa.ft_g2_mercado '
    f'group by ano_pesquisa '
    f'order by ano_pesquisa; '
)
bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)

df.set_index("ano_pesquisa", inplace=True)
st.bar_chart(df["total"], color='#FF7F27')


col1, col2 = st.columns(2)

# %% Evuloção anual por POR MERCADO DE ATUAÇÃO

sql = (
    f'select ano_pesquisa, ds_mercado, sum(qtd_resposta_sim) as total '
    f'from usp_dsa.ft_g2_mercado '
    f'group by ano_pesquisa, ds_mercado '
    f'order by ano_pesquisa, ds_mercado;'
)
bd = f_ConectaBD.conn
dfM = pd.read_sql(sql, bd)

# Montando a ComboBox para o filtro
v_mercado = dfM["ds_mercado"].value_counts().index
dfM.set_index("ano_pesquisa", inplace=True)
cbox_mercado = col1.selectbox('Mercado de atuação', v_mercado)
dfM = dfM[dfM["ds_mercado"] == cbox_mercado]
# col1.st.bar_chart(dfM["total"])

# %% Evuloção anual por POR PORTE DAS EMPRESAS

sql = (
    f'select ano_pesquisa, ds_porte, sum(qtd_resposta_sim) as total '
    f'from usp_dsa.ft_g2_porte '
    f'group by ano_pesquisa, ds_porte '
    f'order by ano_pesquisa, ds_porte;'
)
bd = f_ConectaBD.conn
dfP = pd.read_sql(sql, bd)

# Montando a ComboBox para o filtro
v_porte = dfP["ds_porte"].value_counts().index
dfP.set_index("ano_pesquisa", inplace=True)
cbox_porte = col2.selectbox('Porte das empresas', v_porte)
dfP = dfP[dfP["ds_porte"] == cbox_porte]
# col2.st.bar_chart(dfP["total"])


# %% Exibe os gráficos segmentados
col1.bar_chart(dfM["total"], color='#0F3A69')
col2.bar_chart(dfP["total"], color='#385723')


# %% Demonstra a prticipação percentual por Mercado de atuação

sql = (
    f'select ds_mercado, sum(qtd_resposta_sim) as total_sim '
    f'from usp_dsa.ft_g2_mercado '
    f'group by ds_mercado '
    f'order by total_sim desc; '
)

bd = f_ConectaBD.conn
dfMpp = pd.read_sql(sql, bd)
dfMpp['Participação_%'] = (dfMpp['total_sim'] / dfMpp["total_sim"].sum()) * 100

# Montando a ComboBox para o filtro
dfMpp.set_index("ds_mercado", inplace=True)
# col1.bar_chart(dfMpp["Participação_%"])

# %% Demonstra a prticipação percentual por PORTE DAS EMPRESAS

sql = (
    f'select ds_porte, sum(qtd_resposta_sim) as total_sim '
    f'from usp_dsa.ft_g2_porte '
    f'group by ds_porte '
    f'order by total_sim desc; '
)

bd = f_ConectaBD.conn
dfPpp = pd.read_sql(sql, bd)
dfPpp['Participação_%'] = (dfPpp['total_sim'] / dfPpp["total_sim"].sum()) * 100

# Montando a ComboBox para o filtro
dfPpp.set_index("ds_porte", inplace=True)
# col1.bar_chart(dfPM["Participação_%"])


# %% Exibe os gráficos segmentados
col1.bar_chart(dfMpp["Participação_%"], color='#0F3A69')
col2.bar_chart(dfPpp["Participação_%"], color='#385723')


# %% SEGUE O PROGRAMA


# %% FIM!
