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
#st.sidebar.write("H9 - Empresas que fazem análises de Inteligência artificial")
st.sidebar.markdown("**H9 - Utilização de tecnologias de Inteligência artificial**")

# %% Evolução anual, geral do uso de Inteligência artificial

st.subheader("Evolução da utilização de :yellow-background[Inteligência artificial]")

col1, col2, col3 = st.columns([0.96, 0.02, 0.02])

sql = (
    f'SELECT ano_pesquisa "Ano pesquisa", contexto "Tipo de ferramenta", '
    f'qtd_resposta_sim "% de Empresas que utilizam",  (qtd_resposta_sim || " %") as valor ' 
    f'FROM ft_ceticbr_totais '
    F'WHERE cd_variavel like "h9a%" '  
#    f'order by 1, 2;'
)
#with open("G:/Meu Drive/MBA - USP/TCC/Resultados preliminares/Novos dados/IA_totais.sql", "w", encoding="utf-8") as arquivo:
#    arquivo.write(sql)

bd = f_ConectaBD.conn
dfl = pd.read_sql(sql, bd)
dfl.set_index("Ano pesquisa", inplace=True)

fig_L = px.line(dfl, y="% de Empresas que utilizam", text='valor', color="Tipo de ferramenta", height=640, markers=True)
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

#
# H9 - Evolução cronológica de empresas que utilizaram plataformas ERP por Mercado de atuação

# %% Demonstra a prticipação percentual por Mercado de atuação

col1.subheader("Evolução da utilização de :yellow-background[Inteligência artificial] conforme :yellow-background[tipo de ferramenta]")
col2.write(' ')
col3.write(' ')



########  MERCADO
# %% Evuloção anual por POR MERCADO DE ATUAÇÃO
# Montando a ComboBox para o filtro
sql = (
    f'SELECT DISTINCT dic.nm_questao_variavel "Tipo de ferramenta" '
    f'FROM ft_ceticbr_mercado f, dm_dicionario_questoes_ceticbr dic '
    f'WHERE f.cd_variavel = dic.cd_questao_ceticbr '
    f'AND f.cd_variavel like "h9a%" '
)

bd = f_ConectaBD.conn
dfOrigBox = pd.read_sql(sql, bd)

v_origem = dfOrigBox['Tipo de ferramenta'].value_counts().index
cbox_origem = col1.selectbox('Selecione o Mercado de Atuação a pesquisar', v_origem)

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_merc_atuacao_abrev 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% de Empresas que utilizam', dic.nm_questao_variavel 'Tipo de ferramenta' "
    f"from ft_ceticbr_mercado f, dm_mercado_atuacao d, dm_dicionario_questoes_ceticbr dic "
    f"where f.id_dm_mercado = d.id_merc_atuacao "  
    f"and f.cd_variavel = dic.cd_questao_ceticbr "
    f"order by f.ano_pesquisa; "  
)
#with open("G:/Meu Drive/MBA - USP/TCC/Resultados preliminares/Novos dados/IA_mercado.sql", "w", encoding="utf-8") as arquivo:
 #   arquivo.write(sql)

bd = f_ConectaBD.conn
dfM = pd.read_sql(sql, bd)
dfM.set_index("Ano pesquisa", inplace=True)
dfM = dfM[dfM["Tipo de ferramenta"] == cbox_origem]

col1.write(' ')
col1.write(' ')
col1.markdown("**Proporção de empresas que utilizam :yellow-background[Inteligência artificial] por :yellow-background[Mercado de atuação]**")
col2.write(' ')
col3.write(' ')

fig_L = px.line(dfM, y="% de Empresas que utilizam", color="Mercado de atuação", height=640, markers=True)
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


###############################################################################################
#
# H9 - Evolução cronológoia de empresas que utilizaram plataformas Inteligência artificial por Porte da empresa

# %% Demonstra a prticipação percentual por Porta da empresa

########  PORTE
# %% Evuloção anual por POR PORTE DA EMPRESA
# Utilizando o filtro acima
sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_porte_empresa 'Porte da empresa', " 
    f"f.qtd_resposta_sim '% de Empresas que utilizam', dic.nm_questao_variavel 'Tipo de ferramenta' "
    f"from ft_ceticbr_porte f, dm_porte_empresa d, dm_dicionario_questoes_ceticbr dic "
    f"where f.id_dm_porte = d.id_porte_empresa "  
    f"and f.cd_variavel = dic.cd_questao_ceticbr "
    f"order by f.ano_pesquisa; "  
)
#with open("G:/Meu Drive/MBA - USP/TCC/Resultados preliminares/Novos dados/IA_porte.sql", "w", encoding="utf-8") as arquivo:
 #   arquivo.write(sql)

bd = f_ConectaBD.conn
dfP = pd.read_sql(sql, bd)
dfP.set_index("Ano pesquisa", inplace=True)
dfP = dfP[dfP["Tipo de ferramenta"] == cbox_origem]
col1.markdown(f"**Proporção de empresas que utilizam :yellow-background[Inteligência artificial], para {cbox_origem}  por :yellow-background[Porte da empresa]**")
col3.write(' ')


fig_L = px.line(dfP, y="% de Empresas que utilizam", color="Porte da empresa", height=640, markers=True)
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
col1.subheader("Freqência de utilização de :yellow-background[Inteligência artificial] conforme Ano da Pesquisa")
col2.write(' ')
col3.write(' ')

sql = (
    f'SELECT DISTINCT f.Ano_pesquisa "Ano pesquisa" '
    f'FROM ft_ceticbr_mercado f '
    f'WHERE f.cd_variavel like "h9a%" '
)
bd = f_ConectaBD.conn
dfAnoBox = pd.read_sql(sql, bd)

v_ano = dfAnoBox['Ano pesquisa'].value_counts().index
cbox_AnoPesq = col1.selectbox('Selecione o ano da pesquisa a observar', v_ano)

col1, col2, col3 = st.columns([0.49, 0.02, 0.49])

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', SUBSTR(d.ds_merc_atuacao_abrev, 1, 40) 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% de Empresas que utilizam', "
    f"f.qtd_resposta_sim || ' %' as 'valor'  "
    f"from ft_ceticbr_mercado f, dm_mercado_atuacao d "
    f"where f.id_dm_mercado = d.id_merc_atuacao "  
    f"and f.ano_pesquisa = {cbox_AnoPesq} "
    f'and f.cd_variavel = "h9af" '
    f"order by f.qtd_resposta_sim desc "  
)
#with open("G:/Meu Drive/MBA - USP/TCC/Resultados preliminares/Novos dados/IA_mercado_2.sql", "w", encoding="utf-8") as arquivo:
 #   arquivo.write(sql)

bd = f_ConectaBD.conn
dfM1 = pd.read_sql(sql, bd)
dfM1.set_index("Mercado de atuação", inplace=True)


col1, col2, col3 = st.columns([0.98, 0.02, 0.02])

col1.write(f'**% de utilização de :yellow-background[Plataformas de Inteligência artificial] por MERCADO de atuação, no ano de {cbox_AnoPesq} **')
col2.write(' ')
col3.write(' ')

# %% Exibe os gráficos segmentados
fig_m = px.bar(dfM1, y="% de Empresas que utilizam", text="valor", color="% de Empresas que utilizam", height=500, color_continuous_scale='rdylbu')
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
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_porte_empresa 'Porte empresa', "
    f"f.qtd_resposta_sim '% de Empresas que utilizam', "
    f"f.qtd_resposta_sim || ' %' as 'valor'  "
    f"from ft_ceticbr_porte f, dm_porte_empresa d "
    f"where f.id_dm_porte = d.id_porte_empresa "
    f"and f.ano_pesquisa = {cbox_AnoPesq} "
    f'and f.cd_variavel = "h9af" '
    f"order by f.qtd_resposta_sim desc ; "
)
#with open("G:/Meu Drive/MBA - USP/TCC/Resultados preliminares/Novos dados/IA_porte_2.sql", "w", encoding="utf-8") as arquivo:
 #   arquivo.write(sql)

bd = f_ConectaBD.conn
dfP1 = pd.read_sql(sql, bd)
dfP1.set_index("Porte empresa", inplace=True)



col1, col2, col3 = st.columns([0.98, 0.02, 0.02])

col1.write(f'**% de utilização de :yellow-background[Plataformas de Inteligência artificial] por PORTE de empresa, no ano de {cbox_AnoPesq} **')
col2.write(' ')
col3.write(' ')

fig_p = px.bar(dfP1, y="% de Empresas que utilizam", text="valor", color="% de Empresas que utilizam",  height=500, color_continuous_scale='rdylbu')
col1.plotly_chart(fig_p)
col2.write(' ')
col3.write(' ')


# %% FIM!


###############################################################################################