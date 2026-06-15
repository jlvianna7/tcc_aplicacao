# Execução das pesquisas sobre empresas que COMPRARAM pela internet
#
# %% importa pacotes

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

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

# TOTAL PARA O INDICADOR e1 - EMPRESAS QUE COMPRARAM PELA INTERNET NOS ÚLTIMOS 12 MESES SISTEMA ÚNICO NOS ÚLTIMOS 12 MESES


st.sidebar.color_picker = "#FF7F27"
st.sidebar.write("E1 - Compraram pela internet")

# %% Evolução anual, geral do uso de ERPs

st.subheader("Evolução cronológica da proporção de empresas que :yellow-background[compraram pela internet]")

#sql = (
#    f'SELECT ano_pesquisa "Ano pesquisa", empresas_respondentes "Amostra" '
#    f'FROM dm_resumo_pesquisa '
#    f'order by ano_pesquisa; '
#)

#bd = f_ConectaBD.conn
#df = pd.read_sql(sql, bd)

col1, col2, col3 = st.columns([0.96, 0.02, 0.02])

col1.markdown("**Proporção de empresas que :yellow-background[compraram pela internet]**")

sql = (
    f'SELECT ano_pesquisa "Ano pesquisa", qtd_resposta_sim "% Compraram pela internet" '
    f'FROM ft_ceticbr_totais '
    f'WHERE cd_variavel = "e1" '
    f'ORDER BY ano_pesquisa; '
)

bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)

fig_L = px.line(df, x="Ano pesquisa", y="% Compraram pela internet", height=460)
fig_L.update_xaxes(dtick="M12",tickformat="%Y")
col1.plotly_chart(fig_L)
col2.write(' ')

#
# E1 - Evolução cronológoia de empresas que COMPRARAM pela internet por Mercado de atuação
#

col1, col2, col3 = st.columns([0.98, 0.01, 0.1])

col1.markdown('**Evolução cronológica da proporção de empresas que :yellow-background[compraram pela internet], por mercado de atuação**')

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_merc_atuacao 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% Compraram pela internet' "
    f"FROM ft_ceticbr_mercado f, dm_mercado_atuacao d "
    f"where f.id_dm_mercado = d.id_merc_atuacao "  
    f"AND f.cd_variavel = 'e1' "
    f"order by 1, 2; "  
)
bd = f_ConectaBD.conn
dfM = pd.read_sql(sql, bd)
dfM.set_index("Ano pesquisa", inplace=True)

fig_L = px.line(dfM, y="% Compraram pela internet", color="Mercado de atuação", height=650, markers=True)
fig_L.update_layout(
    legend=dict(
        orientation="h",
        x=0.5,
        xanchor="center",
        y=-0.2,
        yanchor="top"
    )
)
fig_L.update_layout(margin=dict(t=20, b=240))
col1.plotly_chart(fig_L)












############################################   BLOCO 2  #############################################

### GRÁFICOS AUXILIARES

col1, col2, col3 = st.columns([0.49, 0.02, 0.49])

col1.markdown('**Evolução cronológica da proporção de empresas que :yellow-background[compraram pela internet], por mercado de atuação**')
col2.write(' ')
col3.markdown('**Evolução cronológica da proporção de empresas que :yellow-background[compraram pela internet], por porte de empresa**')


# %% Evuloção anual por POR MERCADO DE ATUAÇÃO
# Montando a ComboBox para o filtro
sql = (
    f'SELECT DISTINCT d.ds_merc_atuacao "Mercado de atuação" ' 
    f'FROM ft_ceticbr_mercado f, dm_mercado_atuacao d '
    f'WHERE f.id_dm_mercado = d.id_merc_atuacao ' 
    f'AND f.cd_variavel = "e1" '
    f'ORDER BY d.ds_merc_atuacao ; '
)
bd = f_ConectaBD.conn
dfMBox = pd.read_sql(sql, bd)

v_mercado = dfMBox['Mercado de atuação'].value_counts().index
cbox_mercado = col1.selectbox('Selecione o Mercado de atuação a pesquisar', v_mercado)

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_merc_atuacao 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% Compraram pela internet' "
    f"FROM ft_ceticbr_mercado f, dm_mercado_atuacao d "
    f"where f.id_dm_mercado = d.id_merc_atuacao "  
    f"AND f.cd_variavel = 'e1' "
    f"order by f.ano_pesquisa; "  
)

bd = f_ConectaBD.conn
dfM = pd.read_sql(sql, bd)
dfM.set_index("Ano pesquisa", inplace=True)
dfM = dfM[dfM["Mercado de atuação"] == cbox_mercado]

# %% Evuloção anual por POR PORTE DAS EMPRESAS

sql = (
    f'SELECT DISTINCT d.ds_porte_empresa "Porte empresa" ' 
    f'FROM ft_ceticbr_porte f, dm_porte_empresa d '
    f'WHERE f.id_dm_porte = d.id_porte_empresa '
    f'AND f.cd_variavel = "e1" '
    f'ORDER BY d.id_porte_empresa; '
)
bd = f_ConectaBD.conn
dfPBox = pd.read_sql(sql, bd)

col2.write()

# Montando a ComboBox para o filtro
v_porte = dfPBox["Porte empresa"].value_counts().index
cbox_porte = col3.selectbox('Selecione o porte das empresas', v_porte)

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_porte_empresa 'Porte empresa', "
    f"f.qtd_resposta_sim '% Compraram pela internet' "
    f"from ft_ceticbr_porte f, dm_porte_empresa d "
    f"where f.id_dm_porte = d.id_porte_empresa "
    f"AND f.cd_variavel = 'e1' "
    f"order by f.ano_pesquisa ; "
)
bd = f_ConectaBD.conn
dfP = pd.read_sql(sql, bd)

dfP.set_index("Ano pesquisa", inplace=True)
dfP = dfP[dfP["Porte empresa"] == cbox_porte]

# %% Exibe os gráficos segmentados
col1.bar_chart(dfM["% Compraram pela internet"].astype(int), color='#CF181F')
col2.write(' ')
col3.bar_chart(dfP["% Compraram pela internet"].astype(int), color='#3282F6')


############################################   BLOCO 3  #############################################

# %% Demonstra a prticipação percentual por Mercado de atuação
# %% Evuloção anual por POR MERCADO DE ATUAÇÃO
# Montando a ComboBox para o filtro

st.write('')
#col1 = st.columns([0.99])
st.write('')

sql = (
    f'SELECT ano_pesquisa "Ano pesquisa" '
    f'FROM dm_resumo_pesquisa '
    f'order by ano_pesquisa; '
)

bd = f_ConectaBD.conn
dfAnoBox = pd.read_sql(sql, bd)

v_ano = dfAnoBox['Ano pesquisa'].value_counts().index
cbox_AnoPesq = col1.selectbox('Selecione o ano da pesquisa a observar', v_ano)

col1, col2, col3 = st.columns([0.49, 0.02, 0.49])

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_merc_atuacao 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% Compraram pela internet' "
    f"from ft_ceticbr_mercado f, dm_mercado_atuacao d "
    f"where f.id_dm_mercado = d.id_merc_atuacao "  
    f"and f.ano_pesquisa = {cbox_AnoPesq} "
    f"and f.cd_variavel = 'e1' "
    f"order by f.qtd_resposta_sim ; "  
)

bd = f_ConectaBD.conn
dfM1 = pd.read_sql(sql, bd)
dfM1.set_index("Mercado de atuação", inplace=True)
# dfM = dfM[dfM["Mercado de atuação"] == cbox_mercado]

########  PORTE
sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_porte_empresa 'Porte empresa', "
    f"f.qtd_resposta_sim '% Compraram pela internet' "
    f"from ft_ceticbr_porte f, dm_porte_empresa d "
    f"where f.id_dm_porte = d.id_porte_empresa "
    f"and f.ano_pesquisa = {cbox_AnoPesq} "
    f"and f.cd_variavel = 'e1' "
    f"order by f.qtd_resposta_sim ; "
)
bd = f_ConectaBD.conn
dfP1 = pd.read_sql(sql, bd)
dfP1.set_index("Porte empresa", inplace=True)


col1.markdown('**% de empresas que :yellow-background[compraram pela internet], por MERCADO de atuação, no ano selecionado**')
col2.write(' ')
col3.markdown('**% de empresas que :yellow-background[compraram pela internet], por PORTE de empresa, no ano selecionado**')

col1.bar_chart(dfM1["% Compraram pela internet"].astype(int), color='#CF181F')
col2.write(' ')
col3.bar_chart(dfP1["% Compraram pela internet"].astype(int), color='#3282F6')


# %% FIM!
