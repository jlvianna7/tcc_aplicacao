# Execução das pesquisas sobre CRM
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

# TOTAL PARA O INDICADOR g3 –  EMPRESAS QUE UTILIZARAM PACOTES DE SOFTWARE CRM PARA INTEGRAR OS DADOS E PROCESSOS DE SEUS DEPARTAMENTOS EM UM SISTEMA ÚNICO NOS ÚLTIMOS 12 MESES


st.sidebar.color_picker = "#FF7F27"
st.sidebar.write("G3 - Uso de Sistemas CRM")

# %% Evolução anual, geral do uso de CRMs

st.subheader("Evolução cronológica da proporção de empresas que utilizaram :yellow-background[Sistemas CRM]")


sql = (
    f'SELECT ano_pesquisa "Ano pesquisa", qtd_resposta_sim "% Utilizam CRM" '
    f'FROM ft_ceticbr_totais '
    f'WHERE cd_variavel = "g3" '
    f'ORDER BY ano_pesquisa; '
)
with open("logs/CRM.sql", "w", encoding="utf-8") as arquivo:
    arquivo.write(sql)

bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)
df.to_csv("./logs/crm.csv", index=False)

col1, col2, col3 = st.columns([0.96, 0.02, 0.02])

col1.markdown("**Proporção :yellow-background[geral] de empresas que utilizaram plataformas CRM**")

fig_L = px.line(df, x="Ano pesquisa", y="% Utilizam CRM", height=460, color_discrete_sequence=["#FFABAB"], markers=True)
fig_L.update_xaxes(dtick="M12",tickformat="%Y")
col1.plotly_chart(fig_L)
col1.write('\n')
col2.write('\n')
col3.write('\n')

#
# G3 - Evolução cronológica de empresas que utilizaram plataforma CRM por Mercado de atuação
#

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_merc_atuacao 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% Utiliza CRM' "
    f"from ft_ceticbr_mercado f, dm_mercado_atuacao d "
    f"where f.id_dm_mercado = d.id_merc_atuacao "  
    f'and f.cd_variavel = "g3" '
    f"order by f.ano_pesquisa; "  
)

bd = f_ConectaBD.conn
dfM = pd.read_sql(sql, bd)
dfM.set_index("Ano pesquisa", inplace=True)

col1, col2, col3 = st.columns([0.98, 0.01, 0.01])

fig_L = px.line(dfM, y="% Utiliza CRM", color="Mercado de atuação", height=540, markers=True)
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
col2.write(' ')
col3.write(' ')

############################################   BLOCO 2  #############################################

### GRÁFICOS AUXILIARES

col1, col2, col3 = st.columns([0.49, 0.02, 0.49])

col1.markdown('**Evolução cronológica do uso de sistemas CRM, :yellow-background[por mercado de atuação] selecionado**')
col2.write(' ')
col3.markdown('**Evolução cronológica do uso de sistemas CRM, :yellow-background[por porte de empresa] selecionado**')


# %% Evuloção anual por POR MERCADO DE ATUAÇÃO
# Montando a ComboBox para o filtro
sql = (
    f'SELECT DISTINCT d.ds_merc_atuacao "Mercado de atuação" ' 
    f'FROM ft_ceticbr_mercado f, dm_mercado_atuacao d '
    f'WHERE f.id_dm_mercado = d.id_merc_atuacao '
    f'and f.cd_variavel = "g3" '
    f'ORDER BY d.ds_merc_atuacao ; '
)
bd = f_ConectaBD.conn
dfMBox = pd.read_sql(sql, bd)

v_mercado = dfMBox['Mercado de atuação'].value_counts().index
cbox_mercado = col1.selectbox('Selecione o Mercado de atuação a pesquisar', v_mercado)

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_merc_atuacao 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% Utiliza CRM' "
    f"from ft_ceticbr_mercado f, dm_mercado_atuacao d "
    f"where f.id_dm_mercado = d.id_merc_atuacao "  
    f'and f.cd_variavel = "g3" '
    f"order by f.ano_pesquisa; "  
)

bd = f_ConectaBD.conn
dfM = pd.read_sql(sql, bd)
dfM.to_excel("./logs/crm.xlsx", index=False)


dfM.set_index("Ano pesquisa", inplace=True)
dfM = dfM[dfM["Mercado de atuação"] == cbox_mercado]

# %% Evuloção anual por POR PORTE DAS EMPRESAS

sql = (
    f'SELECT DISTINCT d.ds_porte_empresa "Porte empresa" ' 
    f'FROM ft_ceticbr_porte f, dm_porte_empresa d '
    f'WHERE f.id_dm_porte = d.id_porte_empresa; '
#    f'ORDER BY id_porte_empresa; '
)
bd = f_ConectaBD.conn
dfPBox = pd.read_sql(sql, bd)

# Montando a ComboBox para o filtro
v_porte = dfPBox["Porte empresa"].value_counts().index
cbox_porte = col3.selectbox('Selecione o porte das empresas', v_porte)

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_porte_empresa 'Porte empresa', "
    f"f.qtd_resposta_sim '% Utiliza CRM' "
    f"from ft_ceticbr_porte f, dm_porte_empresa d "
    f"where f.id_dm_porte = d.id_porte_empresa "
    f'and f.cd_variavel = "g3" '
    f"order by f.ano_pesquisa ; "
)
bd = f_ConectaBD.conn
dfP = pd.read_sql(sql, bd)

dfP.set_index("Ano pesquisa", inplace=True)
dfP = dfP[dfP["Porte empresa"] == cbox_porte]

# %% Exibe os gráficos segmentados
#col1.bar_chart(dfM["% Utiliza CRM"].astype(int), color='#0F3A69')
fig_p = px.line(dfM, y="% Utiliza CRM", height=500, color_discrete_sequence=["#FFABAB"])
col1.plotly_chart(fig_p)
#col3.bar_chart(dfP["% Utiliza CRM"].astype(int), color='#75FA8D')
fig_p = px.line(dfP, y="% Utiliza CRM", height=500,  color_discrete_sequence=["#FFABAB"])
col3.plotly_chart(fig_p)


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
    f'order by ano_pesquisa desc; '
)

bd = f_ConectaBD.conn
dfAnoBox = pd.read_sql(sql, bd)

v_ano = dfAnoBox['Ano pesquisa'].value_counts().index
cbox_AnoPesq = col1.selectbox('Selecione o ano da pesquisa a observar', v_ano)

col1, col2, col3 = st.columns([0.98, 0.01, 0.01])

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', substr(d.ds_merc_atuacao_abrev, 1, 25) 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% Utiliza CRM', "
    f"f.qtd_resposta_sim || ' %' as 'valor'  "
    f"from ft_ceticbr_mercado f, dm_mercado_atuacao d "
    f"where f.id_dm_mercado = d.id_merc_atuacao "  
    f"and f.ano_pesquisa = {cbox_AnoPesq} "
    f'and f.cd_variavel = "g3" '
    f"order by 3 desc; "  
)

bd = f_ConectaBD.conn
dfM1 = pd.read_sql(sql, bd)
dfM1.set_index("Mercado de atuação", inplace=True)
with open("./logs/crm_mercado.sql", "w", encoding="utf-8") as arquivo:
    arquivo.write(sql)
# dfM = dfM[dfM["Mercado de atuação"] == cbox_mercado]

########  PORTE
sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', f.id_dm_porte, d.ds_porte_empresa 'Porte empresa', "
    f"f.qtd_resposta_sim '% Utiliza CRM', "
    f"f.qtd_resposta_sim || ' %' as 'valor'  "
    f"from ft_ceticbr_porte f, dm_porte_empresa d "
    f"where f.id_dm_porte = d.id_porte_empresa "
    f"and f.ano_pesquisa = {cbox_AnoPesq} "
    f'and f.cd_variavel = "g3" '
    f"order by 2 ; "
)
bd = f_ConectaBD.conn
dfP1 = pd.read_sql(sql, bd)
dfP1.set_index("Porte empresa", inplace=True)


col1.markdown('**% de utilização de sistemas CRM :yellow-background[por mercado de atuação], no ano selecionado**')
#col1.bar_chart(dfM1["% Utiliza CRM"].astype(int), color='#0F3A69')
fig_p = px.bar(dfM1, y="% Utiliza CRM", height=500, text="valor", color_discrete_sequence=["#FFABAB"])
col1.plotly_chart(fig_p)

# Saltando 2 linhas para separar os gráficos
col1.markdown(" <br> " * 2, unsafe_allow_html=True)

col1.markdown('**% de utilização de sistemas CRM :yellow-background[por porte de empresa], no ano selecionado**')
fig_p = px.bar(dfP1, y="% Utiliza CRM", height=500, text="valor", color_discrete_sequence=["#FFABAB"])
col1.plotly_chart(fig_p)

#col3.bar_chart(dfP1["% Utiliza CRM"].astype(int), color='#75FA8D')

# %% FIM!
