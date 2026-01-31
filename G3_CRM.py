# Execução das pesquisas sobre CRM
#
# %% importa pacotes

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
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

# TOTAL PARA O INDICADOR g3 –  EMPRESAS QUE UTILIZARAM PACOTES DE SOFTWARE CRM PARA INTEGRAR OS DADOS E PROCESSOS DE SEUS DEPARTAMENTOS EM UM SISTEMA ÚNICO NOS ÚLTIMOS 12 MESES


st.sidebar.color_picker = "#FF7F27"
st.sidebar.write("G3 - Uso de Sistemas CRM")

# %% Evolução anual, geral do uso de CRMs

st.subheader("Evolução da utilização de :yellow-background[Sistemas CRM]")

sql = (
    f'SELECT ano_pesquisa "Ano pesquisa", empresas_respondentes "Empresas participantes" '
    f'FROM usp_dsa.dm_resumo_pesquisa '
    f'order by ano_pesquisa; '
)

bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)

col1, col2, col3 = st.columns([0.20, 0.02, 0.78])

col1.markdown("\n\n\n**Empresas pesquisadas**")
col2.write(' ')
col3.markdown("**Proporção de empresas que utilizam :yellow-background[sistemas CRM]**")

dfpesq = df[["Ano pesquisa", "Empresas participantes"]]
col1.table(dfpesq)

sql = (
    f'SELECT ano_pesquisa "Ano pesquisa", qtd_resposta_sim "% Utilizam CRM" '
    f'FROM usp_dsa.ft_g3_totais '
    f'ORDER BY ano_pesquisa; '
)

bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)

col2.write(' ')
df.set_index("Ano pesquisa", inplace=True)
col3.line_chart(df["% Utilizam CRM"].astype(float), color='#FF7F27')

############################################   BLOCO 2  #############################################

### GRÁFICOS AUXILIARES

col1, col2, col3 = st.columns([0.49, 0.02, 0.49])

col1.markdown('**Evolução cronológica do uso de :yellow-background[sistemas CRM], por mercado de atuação**')
col2.write(' ')
col3.markdown('**Evolução cronológica do uso de :yellow-background[sistemas CRM], por porte de empresa**')


# %% Evuloção anual por POR MERCADO DE ATUAÇÃO
# Montando a ComboBox para o filtro
sql = (
    f'SELECT DISTINCT d.ds_merc_atuacao "Mercado de atuação" ' 
    f'FROM usp_dsa.ft_g3_mercado f, usp_dsa.dm_mercado_atuacao d '
    f'WHERE f.id_mercado = d.id_merc_atuacao '
    f'ORDER BY d.ds_merc_atuacao ; '
)
bd = f_ConectaBD.conn
dfMBox = pd.read_sql(sql, bd)

v_mercado = dfMBox['Mercado de atuação'].value_counts().index
cbox_mercado = col1.selectbox('Selecione o Mercado de atuação a pesquisar', v_mercado)

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_merc_atuacao 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% Utiliza CRM' "
    f"from usp_dsa.ft_g3_mercado f, usp_dsa.dm_mercado_atuacao d "
    f"where f.id_mercado = d.id_merc_atuacao "  
    f"order by f.ano_pesquisa; "  
)

bd = f_ConectaBD.conn
dfM = pd.read_sql(sql, bd)
dfM.set_index("Ano pesquisa", inplace=True)
dfM = dfM[dfM["Mercado de atuação"] == cbox_mercado]

# %% Evuloção anual por POR PORTE DAS EMPRESAS

sql = (
    f'SELECT DISTINCT d.ds_porte_empresa "Porte empresa" ' 
    f'FROM usp_dsa.ft_g3_porte f, usp_dsa.dm_porte_empresa d '
    f'WHERE f.id_porte = d.id_porte_empresa; '
#    f'ORDER BY id_porte_empresa; '
)
bd = f_ConectaBD.conn
dfPBox = pd.read_sql(sql, bd)

col2.write()

# Montando a ComboBox para o filtro
v_porte = dfPBox["Porte empresa"].value_counts().index
cbox_porte = col3.selectbox('Selecione o porte das empresas', v_porte)

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_porte_empresa 'Porte empresa', "
    f"f.qtd_resposta_sim '% Utiliza CRM' "
    f"from usp_dsa.ft_g3_porte f, usp_dsa.dm_porte_empresa d "
    f"where f.id_porte = d.id_porte_empresa "
    f"order by f.ano_pesquisa ; "
)
bd = f_ConectaBD.conn
dfP = pd.read_sql(sql, bd)

dfP.set_index("Ano pesquisa", inplace=True)
dfP = dfP[dfP["Porte empresa"] == cbox_porte]

# %% Exibe os gráficos segmentados
col1.bar_chart(dfM["% Utiliza CRM"].astype(int), color='#0F3A69')
col2.write(' ')
col3.bar_chart(dfP["% Utiliza CRM"].astype(int), color='#75FA8D')


############################################   BLOCO 3  #############################################

# %% Demonstra a prticipação percentual por Mercado de atuação
# %% Evuloção anual por POR MERCADO DE ATUAÇÃO
# Montando a ComboBox para o filtro

st.write('')
#col1 = st.columns([0.99])
st.write('')

sql = (
    f'SELECT ano_pesquisa "Ano pesquisa" '
    f'FROM usp_dsa.dm_resumo_pesquisa '
    f'order by ano_pesquisa; '
)

bd = f_ConectaBD.conn
dfAnoBox = pd.read_sql(sql, bd)

v_ano = dfAnoBox['Ano pesquisa'].value_counts().index
cbox_AnoPesq = col1.selectbox('Selecione o ano da pesquisa a observar', v_ano)

col1, col2, col3 = st.columns([0.49, 0.02, 0.49])

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_merc_atuacao 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% Utiliza CRM' "
    f"from usp_dsa.ft_g3_mercado f, usp_dsa.dm_mercado_atuacao d "
    f"where f.id_mercado = d.id_merc_atuacao "  
    f"and f.ano_pesquisa = {cbox_AnoPesq} "
    f"order by f.ano_pesquisa; "  
)

bd = f_ConectaBD.conn
dfM1 = pd.read_sql(sql, bd)
dfM1.set_index("Mercado de atuação", inplace=True)
# dfM = dfM[dfM["Mercado de atuação"] == cbox_mercado]

########  PORTE
sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_porte_empresa 'Porte empresa', "
    f"f.qtd_resposta_sim '% Utiliza CRM' "
    f"from usp_dsa.ft_g3_porte f, usp_dsa.dm_porte_empresa d "
    f"where f.id_porte = d.id_porte_empresa "
    f"and f.ano_pesquisa = {cbox_AnoPesq} "
    f"order by f.ano_pesquisa ; "
)
bd = f_ConectaBD.conn
dfP1 = pd.read_sql(sql, bd)
dfP1.set_index("Porte empresa", inplace=True)


col1.markdown('**% de utilização de :yellow-background[sistemas CRM] por MERCADO de atuação, no ano selecionado**')
col2.write(' ')
col3.markdown('**% de utilização de :yellow-background[sistemas CRM] por PORTE de empresa, no ano selecionado**')

# col3.markdown(f"**Peso:** {dados_jogador['Weight(lbs.)']*0.453:0.2f}")

col1.bar_chart(dfM1["% Utiliza CRM"].astype(int), color='#0F3A69')
col2.write(' ')
col3.bar_chart(dfP1["% Utiliza CRM"].astype(int), color='#75FA8D')

# %% FIM!
