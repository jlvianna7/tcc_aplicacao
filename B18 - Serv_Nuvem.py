# H9 - EMPRESAS QUE UTILIZARAM TECNOLOGIAS DE Serviços de Nuvem

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

# TOTAL PARA O INDICADOR H9 - EMPRESAS QUE UTILIZARAM TECNOLOGIAS DE Serviços de Nuvem

st.sidebar.color_picker = "#FF7F27"
#st.sidebar.write("H1 - Empresas que fazem análises de Serviços de Nuvem")
st.sidebar.markdown("**H9 - Utilização de tecnologias de Serviços de Nuvem**")

# %% Evolução anual, geral do uso de Serviços de Nuvem

st.subheader("Evolução da utilização de :yellow-background[Serviços de Nuvem]")

col1, col2, col3 = st.columns([0.98, 0.01, 0.01])

col1.markdown("**Das empresas que utilizaram serviços de Nuvem, proporção (%) :yellow-background[por tipo de serviço de Nuvem] pública**")
col2.write(' ')
col3.write(' ')

##########################  GRÁFICO 1

sql = (
    f'SELECT cd_variavel, ano_pesquisa "Ano pesquisa", contexto "Serviço", ' 
    f'qtd_resposta_sim "% de Empresas que utilizam", ' 
    f'qtd_resposta_sim || " %" as "Proporção"  '
    f'FROM ft_ceticbr_totais '
    f'WHERE  (cd_variavel like "b18%" ) ' 
    f'order by 1, 2; '
)

bd = f_ConectaBD.conn
dfl = pd.read_sql(sql, bd)
dfl.to_csv("c:/Temp/nuvem.csv", index=False)
dfl.set_index("Ano pesquisa", inplace=True)

fig_L = px.line(dfl, y="Proporção", color="Serviço", height=600, markers=True)
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

#col1.line_chart(dfl, x="Ano pesquisa", y="% de Empresas que utilizam", color="Serviço", height=450)
#col2.write(' ')
#col3.write(' ')


############################################   BLOCO 2  #############################################
#
# B18 - Serviços de nuvem

# %% Demonstra a participação percentual por Mercado de atuação

col1.subheader("Evolução da utilização de :yellow-background[Nuvem pública] conforme Tipo de Serviço")
col2.write(' ')
col3.write(' ')

########  MERCADO
# %% Evuloção anual por POR MERCADO DE ATUAÇÃO
# Montando a ComboBox para o filtro
sql = (
    f'SELECT DISTINCT dic.nm_questao_variavel "Tipo de serviço" '
    f'FROM ft_ceticbr_mercado f, dm_dicionario_questoes_ceticbr dic '
    f'WHERE f.cd_variavel = dic.cd_questao_ceticbr '
    f'AND f.cd_variavel like "b18%" '
)

bd = f_ConectaBD.conn
dfOrigBox = pd.read_sql(sql, bd)

v_origem = dfOrigBox['Tipo de serviço'].value_counts().index
cbox_origem = col1.selectbox('Selecione o tipo de serviço de nuvem a pesquisar', v_origem)

sql = (
    f"SELECT DISTINCT f.ano_pesquisa 'Ano pesquisa', SUBSTR(d.ds_merc_atuacao_abrev, 1, 40) 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% de Empresas que utilizam', dic.nm_questao_variavel 'Tipo de serviço' "
    f"from ft_ceticbr_mercado f, dm_mercado_atuacao d, dm_dicionario_questoes_ceticbr dic "
    f"where f.id_dm_mercado = d.id_merc_atuacao "  
    f"and f.cd_variavel = dic.cd_questao_ceticbr "
    f'AND f.cd_variavel like "b18%" '
    f"order by 1 "  
)
#with open("G:/Meu Drive/MBA - USP/TCC/Resultados preliminares/Novos dados/nuvem_mercado.sql", "w", encoding="utf-8") as arquivo:
#    arquivo.write(sql)

bd = f_ConectaBD.conn
dfM = pd.read_sql(sql, bd)
dfM.set_index("Ano pesquisa", inplace=True)
dfM = dfM[dfM["Tipo de serviço"] == cbox_origem]

col1.write(' ')
col1.write(' ')
col1.markdown(f"**Proporção de empresas que utilizam :yellow-background[Nuvem pública para {cbox_origem}], conforme Mercado de atuação**")
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
# B18 - Uso de nuvem pública por tipo de serviço

# %% Demonstra a participação percentual por Porta da empresa

########  PORTE
# %% Evuloção anual por POR PORTE DA EMPRESA
# Utilizando o filtro acima
sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_porte_empresa 'Porte da empresa', " 
    f"f.qtd_resposta_sim '% de Empresas que utilizam', dic.nm_questao_variavel 'Tipo de serviço', "
    f"f.qtd_resposta_sim || ' %' as 'Proporção'  "
    f"from ft_ceticbr_porte f, dm_porte_empresa d, dm_dicionario_questoes_ceticbr dic "
    f"where f.id_dm_porte = d.id_porte_empresa "  
    f"and f.cd_variavel = dic.cd_questao_ceticbr "
    f"order by f.ano_pesquisa; "  
)
#with open("G:/Meu Drive/MBA - USP/TCC/Resultados preliminares/Novos dados/nuvem_porte.sql", "w", encoding="utf-8") as arquivo:
#    arquivo.write(sql)

bd = f_ConectaBD.conn
dfP = pd.read_sql(sql, bd)
dfP.set_index("Ano pesquisa", inplace=True)
dfP = dfP[dfP["Tipo de serviço"] == cbox_origem]
col1.markdown(f"**Proporção de empresas que utilizam :yellow-background[Nuvem pública para {cbox_origem}] por Porte da empresa**")
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
col1.subheader("Freqência de utilização de :yellow-background[Nuvem pública] conforme Ano da Pesquisa")
col2.write(' ')
col3.write(' ')

sql = (
    f'SELECT ano_pesquisa "Ano pesquisa" '
    f'FROM dm_resumo_pesquisa '
    f'order by ano_pesquisa desc; '
)

bd = f_ConectaBD.conn
dfAnoBox = pd.read_sql(sql, bd)

v_ano = dfAnoBox['Ano pesquisa'].value_counts().index
cbox_AnoPesq = col1.selectbox('Selecione o ano da pesquisa a observar', v_ano)

col1, col2, col3 = st.columns([0.49, 0.02, 0.49])

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', SUBSTR(d.ds_merc_atuacao_abrev, 1, 40) 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% de Empresas que utilizam', "
    f"f.qtd_resposta_sim || ' %' as 'Proporção'  "
    f"from ft_ceticbr_mercado f, dm_mercado_atuacao d "
    f"where f.id_dm_mercado = d.id_merc_atuacao "  
    f"and f.ano_pesquisa = {cbox_AnoPesq} "
    f'and f.cd_variavel = "b18d" '
    f"order by f.qtd_resposta_sim; "  
)
#with open("G:/Meu Drive/MBA - USP/TCC/Resultados preliminares/Novos dados/nuvem_mercado_data.sql", "w", encoding="utf-8") as arquivo:
#    arquivo.write(sql)

bd = f_ConectaBD.conn
dfM1 = pd.read_sql(sql, bd)
dfM1.set_index("Mercado de atuação", inplace=True)

########  PORTE
sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_porte_empresa 'Porte empresa', "
    f"f.qtd_resposta_sim '% de Empresas que utilizam', "
    f"f.qtd_resposta_sim || ' %' as 'Proporção'  "
    f"from ft_ceticbr_porte f, dm_porte_empresa d "
    f"where f.id_dm_porte = d.id_porte_empresa "
    f"and f.ano_pesquisa = {cbox_AnoPesq} "
    f'and f.cd_variavel = "b18b" '
    f"order by 3 ; "
)
with open("C:/Temp/nuvem_porte_data.sql", "w", encoding="utf-8") as arquivo:
    arquivo.write(sql)

bd = f_ConectaBD.conn
dfP1 = pd.read_sql(sql, bd)
dfP1.set_index("Porte empresa", inplace=True)


col1, col2, col3 = st.columns([0.98, 0.02, 0.02])

col1.markdown('**% de utilização de :yellow-background[Nuvem pública para Banco de Dados] por MERCADO de atuação, no ano selecionado**')
col2.write(' ')
col3.write(' ')

# %% Exibe os gráficos segmentados
fig_m = px.bar(dfM1, y="% de Empresas que utilizam", text="Proporção", height=640, color_discrete_sequence=['#D90E39'])
col1.plotly_chart(fig_m)
col2.write(' ')
col3.write(' ')

col1.write(' ')
col2.write(' ')
col3.write(' ')
col1.write(' ')
col2.write(' ')
col3.write(' ')

col1, col2, col3 = st.columns([0.98, 0.02, 0.02])

col1.markdown('**% de utilização de :yellow-background[Nuvem pública para Banco de Dados ] por PORTE de empresa, no ano selecionado**')
col2.write(' ')
col3.write(' ')

fig_p = px.bar(dfP1, y="% de Empresas que utilizam", text="Proporção", height=500, color_discrete_sequence=['#D90E39'])
col1.plotly_chart(fig_p)
col2.write(' ')
col3.write(' ')

#col1.bar_chart(dfM1["% de Empresas que utilizam"].astype(int), color='#0F3A69')
#col2.write(' ')
#col3.bar_chart(dfP1["% de Empresas que utilizam"].astype(int), color='#75FA8D')

# %% FIM!



# %% FIM!
