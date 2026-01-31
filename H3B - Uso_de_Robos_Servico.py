# Execução das pesquisas sobre Robôs de serviços
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
st.header(
    'Pesquisa aplicada sobre transformação digital nas empresas no Brasil', divider=True)
st.text('\n\n\n\n\n')

# TOTAL PARA O INDICADOR H3A - EMPRESAS, POR USO DE Robôs de serviços


st.sidebar.color_picker = "#FF7F27"
#st.sidebar.write("H1 - Empresas que fazem análises de Robôs de serviços")
st.sidebar.markdown("**H3B - Empresas que utilizam Robôs de serviços**")

# %% Evolução anual, geral do uso de Robôs de serviços

st.subheader("Evolução da utilização de :yellow-background[Robôs de serviços]")

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
col3.markdown("**Proporção de empresas que utilizam :yellow-background[Robôs de serviços]**")

dfpesq = df[["Ano pesquisa", "Amostra"]]
col1.table(dfpesq)


sql = (
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Tipo de serviço", qtd_resposta_sim "% de Empresas que utilizam" FROM ft_h3ba_totais '
    F'WHERE ANO_PESQUISA > "2015" ' 
    f'UNION '
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Tipo de serviço", qtd_resposta_sim "% de Empresas que utilizam" FROM ft_h3bb_totais '
    F'WHERE ANO_PESQUISA > "2015" ' 
    f'UNION '
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Tipo de serviço", qtd_resposta_sim "% de Empresas que utilizam" FROM ft_h3bc_totais '
    F'WHERE ANO_PESQUISA > "2015" ' 
    f'UNION '
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Tipo de serviço", qtd_resposta_sim "% de Empresas que utilizam" FROM ft_h3bd_totais '
    F'WHERE ANO_PESQUISA > "2015" ' 
    f'UNION '
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Tipo de serviço", qtd_resposta_sim "% de Empresas que utilizam" FROM ft_h3be_totais '
    F'WHERE ANO_PESQUISA > "2015" ' 
    f'UNION '
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Tipo de serviço", qtd_resposta_sim "% de Empresas que utilizam" FROM ft_h3bf_totais '
    F'WHERE ANO_PESQUISA > "2015" ' 
    f'UNION '
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Tipo de serviço", qtd_resposta_sim "% de Empresas que utilizam" FROM ft_h3bg_totais '
    F'WHERE ANO_PESQUISA > "2015" ' 
    f'order by "Ano_pesquisa", "Tipo de serviço"; '
)
bd = f_ConectaBD.conn
dfl = pd.read_sql(sql, bd)

col3.line_chart(dfl, x="Ano pesquisa", y="% de Empresas que utilizam", color="Tipo de serviço")

############################################   BLOCO 2  #############################################

### GRÁFICOS AUXILIARES

col1, col2, col3 = st.columns([0.49, 0.02, 0.49])

col1.markdown('**Evolução cronológica do uso de :yellow-background[Robôs de serviços], por mercado de atuação**')
col2.write(' ')
col3.markdown('**Evolução cronológica do uso de :yellow-background[Robôs de serviços], por porte de empresa**')


# %% Evuloção anual por POR MERCADO DE ATUAÇÃO
# Montando a ComboBox para o filtro
sql = (
    f'SELECT DISTINCT d.ds_merc_atuacao "Mercado de atuação" ' 
    f'FROM usp_dsa.ft_h3a_mercado f, usp_dsa.dm_mercado_atuacao d '
    f'WHERE f.id_mercado = d.id_merc_atuacao '
    f'ORDER BY d.ds_merc_atuacao ; '
)
bd = f_ConectaBD.conn
dfMBox = pd.read_sql(sql, bd)

v_mercado = dfMBox['Mercado de atuação'].value_counts().index
cbox_mercado = col1.selectbox('Selecione o Mercado de atuação a pesquisar', v_mercado)

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_merc_atuacao 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% Empresas que utilizam' "
    f"from usp_dsa.ft_h3a_mercado f, usp_dsa.dm_mercado_atuacao d "
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
    f'FROM usp_dsa.ft_h3a_porte f, usp_dsa.dm_porte_empresa d '
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
    f"f.qtd_resposta_sim '% Empresas que utilizam' "
    f"from usp_dsa.ft_h3a_porte f, usp_dsa.dm_porte_empresa d "
    f"where f.id_porte = d.id_porte_empresa "
    f"order by f.ano_pesquisa ; "
)
bd = f_ConectaBD.conn
dfP = pd.read_sql(sql, bd)

dfP.set_index("Ano pesquisa", inplace=True)
dfP = dfP[dfP["Porte empresa"] == cbox_porte]

# %% Exibe os gráficos segmentados
col1.bar_chart(dfM["% Empresas que utilizam"].astype(int), color='#0F3A69')
col2.write(' ')
col3.bar_chart(dfP["% Empresas que utilizam"].astype(int), color='#75FA8D')


############################################   BLOCO 3  #############################################

# %% Demonstra a prticipação percentual por Mercado de atuação

st.write('')
#col1 = st.columns([0.99])
st.write('')

sql = (
    f'SELECT DISTINCT ano_pesquisa "Ano pesquisa" '
    f'FROM usp_dsa.ft_h3a_totais '
    f'order by ano_pesquisa; '
)

bd = f_ConectaBD.conn
dfAnoBox = pd.read_sql(sql, bd)

v_ano = dfAnoBox['Ano pesquisa'].value_counts().index
cbox_AnoPesq = col1.selectbox('Selecione o ano da pesquisa a observar', v_ano)

col1, col2, col3 = st.columns([0.49, 0.02, 0.49])

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_merc_atuacao 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% Empresas que utilizam' "
    f"from usp_dsa.ft_h3a_mercado f, usp_dsa.dm_mercado_atuacao d "
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
    f"f.qtd_resposta_sim '% Empresas que utilizam' "
    f"from usp_dsa.ft_h3a_porte f, usp_dsa.dm_porte_empresa d "
    f"where f.id_porte = d.id_porte_empresa "
    f"and f.ano_pesquisa = {cbox_AnoPesq} "
    f"order by f.ano_pesquisa ; "
)
bd = f_ConectaBD.conn
dfP1 = pd.read_sql(sql, bd)
dfP1.set_index("Porte empresa", inplace=True)


col1.markdown('**% de utilização de :yellow-background[Robôs de serviços] por MERCADO de atuação, no ano selecionado**')
col2.write(' ')
col3.markdown('**% de utilização de :yellow-background[Robôs de serviços] por PORTE de empresa, no ano selecionado**')

# col3.markdown(f"**Peso:** {dados_jogador['Weight(lbs.)']*0.453:0.2f}")

col1.bar_chart(dfM1["% Empresas que utilizam"].astype(int), color='#0F3A69')
col2.write(' ')
col3.bar_chart(dfP1["% Empresas que utilizam"].astype(int), color='#75FA8D')

# %% FIM!
