# H9 - EMPRESAS QUE UTILIZARAM TECNOLOGIAS DE INTELIGÊNCIA ARTIFICIAL

# %% importa pacotes

import numpy as np
import pandas as pd
import streamlit as st
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

# TOTAL PARA O INDICADOR H9 - EMPRESAS QUE UTILIZARAM TECNOLOGIAS DE INTELIGÊNCIA ARTIFICIAL

st.sidebar.color_picker = "#FF7F27"
#st.sidebar.write("H1 - Empresas que fazem análises de Inteligência artificial")
st.sidebar.markdown("**H13 - Barreiras para utilização de Inteligência artificial**")

# %% Evolução anual, geral do uso de Inteligência artificial

st.subheader(":yellow-background[Barreiras] enfrentadas por empresas no uso de :yellow-background[Inteligência artificial] em 2025")

col1, col2, col3 = st.columns([0.96, 0.02, 0.02])

###
###
sql = (
    f'SELECT contexto "Obstáculo", qtd_resposta_sim "% de Empresas que utilizam", '
    f'qtd_resposta_sim || " %" as "valor"  '
    f'FROM ft_ceticbr_totais '
    f'WHERE  cd_variavel like "h13%"  ' 
    f' and ano_pesquisa = 2025 '
    f'order by 2 desc'
)
with open("./logs/IA_barreiras_totais.sql", "w", encoding="utf-8") as arquivo:
    arquivo.write(sql)

bd = f_ConectaBD.conn
dfl = pd.read_sql(sql, bd)
dfl.set_index("Obstáculo", inplace=True)
fig_L = px.bar(dfl, y="% de Empresas que utilizam", text="valor", color="% de Empresas que utilizam", height=640, color_continuous_scale='blugrn')
#'viridis', 'plasma', 'cividis' 

#fig_L = px.bar(dfl, y="% de Empresas que utilizam", text="% de Empresas que utilizam", height=640)
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



############################################   BLOCO 3  #############################################

# %% Demonstra a Frequencia de utilização, conforme ano selecioando.
# %% Evuloção anual por POR MERCADO DE ATUAÇÃO
# Montando a ComboBox para o filtro


col1, col2, col3 = st.columns([0.96, 0.02, 0.02])
col1.subheader(":yellow-background[Barreiras] para utilização de :yellow-background[Inteligência artificial] conforme Ano da Pesquisa")
col2.write(' ')
col3.write(' ')

sql = (
    f'SELECT DISTINCT f.Ano_pesquisa "Ano pesquisa" '
    f'FROM ft_ceticbr_mercado f '
    f'WHERE f.Ano_pesquisa = 2025 '
    f'and f.cd_variavel like "h13%" '
)
bd = f_ConectaBD.conn
dfAnoBox = pd.read_sql(sql, bd)

v_ano = dfAnoBox['Ano pesquisa'].value_counts().index
cbox_AnoPesq = col1.selectbox('Selecione o ano da pesquisa a observar', v_ano)

col1, col2, col3 = st.columns([0.49, 0.02, 0.49])

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', SUBSTR(d.ds_merc_atuacao_abrev, 1, 40) 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% de Empresas que utilizam', f.qtd_resposta_sim || ' %' as 'valor'  "
    f"from ft_ceticbr_mercado f, dm_mercado_atuacao d "
    f"where f.id_dm_mercado = d.id_merc_atuacao "  
    f"and f.Ano_pesquisa = 2025 "
    f'and f.cd_variavel = "h13c" '
    f"order by f.qtd_resposta_sim desc ; "  
)
with open("./logs/IA_barreira_mercado_2.sql", "w", encoding="utf-8") as arquivo:
    arquivo.write(sql)

bd = f_ConectaBD.conn
dfM1 = pd.read_sql(sql, bd)
dfM1.set_index("Mercado de atuação", inplace=True)


col1, col2, col3 = st.columns([0.98, 0.02, 0.02])

col1.write(f'** Proporção de :yellow-background[barreiras] para utilização de :yellow-background[Plataformas de Inteligência artificial] por MERCADO de atuação, no ano de {cbox_AnoPesq} **')
col2.write(' ')
col3.write(' ')

# %% Exibe os gráficos segmentados

fig_m = px.bar(dfM1, y="% de Empresas que utilizam", text='valor', color="% de Empresas que utilizam", height=640, color_continuous_scale='blugrn')
#, color_continuous_scale='viridis'
col1.plotly_chart(fig_m)
col2.write(' ')
col3.write(' ')

col1.write(' ')
col2.write(' ')
col3.write(' ')
col1.write(' ')
col2.write(' ')
col3.write(' ')

########  PORTE
sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', f.id_dm_porte, d.ds_porte_empresa 'Porte empresa', "
    f"f.qtd_resposta_sim '% de Empresas que utilizam', f.qtd_resposta_sim || ' %' as 'valor'  "
    f"from ft_ceticbr_porte f, dm_porte_empresa d "
    f"where f.id_dm_porte = d.id_porte_empresa "
    f"and f.ano_pesquisa = 2025 "
    f"and f.cd_variavel = 'h13c' "
    f"order by 2 ; "
)
#with open("./logs/IA_barreira_porte_2.sql", "w", encoding="utf-8") as arquivo:
 #   arquivo.write(sql)

bd = f_ConectaBD.conn
dfP1 = pd.read_sql(sql, bd)

dfP1.set_index("Porte empresa", inplace=True)

col1, col2, col3 = st.columns([0.98, 0.02, 0.02])

col1.write(f'** Porporção de:yellow-background[barreiras] enfrentadas para % de utilização de :yellow-background[Plataformas de Inteligência artificial] por PORTE de empresa, no ano de {cbox_AnoPesq} **')
col2.write(' ')
col3.write(' ')

fig_p = px.bar(dfP1, y="% de Empresas que utilizam", text="valor", height=500, color="% de Empresas que utilizam", color_continuous_scale='blugrn')
col1.plotly_chart(fig_p)
col2.write(' ')
col3.write(' ')

# color_discrete_sequence=['#33FF57', '#3282F6', '#FF33A1']
#color_continuous_scale=['#33FF57', '#3282F6', '#FF33A1']
# %% FIM!
