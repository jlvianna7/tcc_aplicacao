# H8 - EMPRESAS QUE UTILIZARAM DISPOSITIVOS INTELIGENTES OU INTERNET DAS COISAS
#

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

# TOTAL PARA O INDICADOR H8 - EMPRESAS QUE UTILIZARAM DISPOSITIVOS INTELIGENTES OU INTERNET DAS COISAS


st.sidebar.color_picker = "#FF7F27"
#st.sidebar.write("H8 - Empresas que fazem análises de Dispositivos IoT")
st.sidebar.markdown("**H8 - Empresas que utilizaram Dispositivos IoT**")

# %% Evolução anual, geral do uso de Dispositivos IoT

st.subheader("Evolução da utilização de :yellow-background[Dispositivos IoT]")

col1, col2, col3 = st.columns([0.96, 0.02, 0.02])

col1.markdown("**Proporção de empresas que utilizaram :yellow-background[Dispositivos IoT]**")
col2.write(' ')
col3.write(' ')


#####
sql = (
    f'SELECT cd_variavel, ano_pesquisa "Ano pesquisa", contexto "Aplicação", qtd_resposta_sim "% de Empresas que utilizaram" ' 
    f'FROM ft_ceticbr_totais '
    F'WHERE cd_variavel like "h8%" '  
    f'order by 1, 2;'
)
#with open("G:/Meu Drive/MBA - USP/TCC/Resultados preliminares/Novos dados/IOT_totais.sql", "w", encoding="utf-8") as arquivo:
 #   arquivo.write(sql)

bd = f_ConectaBD.conn
dfl = pd.read_sql(sql, bd)
dfl.to_excel("./logs/iot.xlsx", index=False)
dfl.set_index("Ano pesquisa", inplace=True)


fig_L = px.line(dfl, y="% de Empresas que utilizaram", color="Aplicação", height=640, markers=True)
fig_L.update_xaxes(dtick="M12",tickformat="%Y")
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


#col1.line_chart(dfl, x="Ano pesquisa", y="% de Empresas que utilizaram", color="Aplicação", height=500)
#col2.write(' ')
#col3.write(' ')


############################################   BLOCO 2  #############################################

#
# H8 - EMPRESAS QUE UTILIZARAM DISPOSITIVOS INTELIGENTES OU INTERNET DAS COISAS
# %% Demonstra a prticipação percentual por Mercado de atuação

col1.subheader("Evolução da utilização de :yellow-background[Dispositivos inteligentes (IoT)] conforme Área de aplicação")
col2.write(' ')
col3.write(' ')

########  MERCADO
# %% Evuloção anual por POR MERCADO DE ATUAÇÃO
# Montando a ComboBox para o filtro
sql = (
    f'SELECT DISTINCT dic.nm_questao_variavel "Área de aplicação" '
    f'FROM ft_ceticbr_mercado f, dm_dicionario_questoes_ceticbr dic '
    f'WHERE f.cd_variavel = dic.cd_questao_ceticbr '
    f'AND f.cd_variavel like "h8%" '
)
#with open("G:/Meu Drive/MBA - USP/TCC/Resultados preliminares/Novos dados/IOT_combo_box.sql", "w", encoding="utf-8") as arquivo:
 #   arquivo.write(sql)


bd = f_ConectaBD.conn
dfOrigBox = pd.read_sql(sql, bd)

v_origem = dfOrigBox['Área de aplicação'].value_counts().index
cbox_origem = col1.selectbox('Selecione a Origem dos dados do Dispositivos inteligentes (IoT) a pesquisar', v_origem)

sql = (
    f"SELECT Round(f.ano_pesquisa,0) 'Ano pesquisa', d.ds_merc_atuacao_abrev 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% de Empresas que utilizaram', dic.nm_questao_variavel 'Área de aplicação' "
    f"from ft_ceticbr_mercado f, dm_mercado_atuacao d, dm_dicionario_questoes_ceticbr dic "
    f"where f.id_dm_mercado = d.id_merc_atuacao "  
    f"and f.cd_variavel = dic.cd_questao_ceticbr "
    f"order by f.ano_pesquisa; "  
)
#with open("./logs/iot_mercado.sql", "w", encoding="utf-8") as arquivo:
 #   arquivo.write(sql)

bd = f_ConectaBD.conn
dfM = pd.read_sql(sql, bd)
dfM.set_index("Ano pesquisa", inplace=True)
dfM = dfM[dfM["Área de aplicação"] == cbox_origem]

col1.write(' ')
col1.write(' ')
col1.markdown(f"**Proporção de empresas que utilizaram :yellow-background[{cbox_origem}] por Mercado de atuação**")
col2.write(' ')
col3.write(' ')

fig_L = px.line(dfM, y="% de Empresas que utilizaram", color="Mercado de atuação", height=640, markers=True)
fig_L.update_xaxes(dtick="M12",tickformat="%Y")
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
# H8 - Evolução cronológoia de empresas que utilizaram plataformas Dispositivos inteligentes (IoT) por Porte da empresa

# %% Demonstra a prticipação percentual por Porta da empresa

########  PORTE
# %% Evuloção anual por POR PORTE DA EMPRESA
# Utilizando o filtro acima
sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_porte_empresa 'Porte da empresa', " 
    f"f.qtd_resposta_sim '% de Empresas que utilizaram', dic.nm_questao_variavel 'Área de aplicação' "
    f"from ft_ceticbr_porte f, dm_porte_empresa d, dm_dicionario_questoes_ceticbr dic "
    f"where f.id_dm_porte = d.id_porte_empresa "  
    f"and f.cd_variavel = dic.cd_questao_ceticbr "
    f"order by f.ano_pesquisa; "  
)
#with open("./logs/iot_porte.sql", "w", encoding="utf-8") as arquivo:
 #   arquivo.write(sql)

bd = f_ConectaBD.conn
dfP = pd.read_sql(sql, bd)
dfP.set_index("Ano pesquisa", inplace=True)
dfP = dfP[dfP["Área de aplicação"] == cbox_origem]
col1.markdown(f"**Proporção de empresas que utilizaram :yellow-background[{cbox_origem}] por Porte da empresa**")
col3.write(' ')


fig_L = px.line(dfP, y="% de Empresas que utilizaram", color="Porte da empresa", height=640, markers=True)
fig_L.update_xaxes(dtick="M12",tickformat="%Y")
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

# %% Demonstra a prticipação percentual por Mercado de atuação

st.write('')
#col1 = st.columns([0.99])
st.write('')

sql = (
    f'SELECT DISTINCT ano_pesquisa "Ano pesquisa" '
    f'FROM ft_ceticbr_totais '
    f'WHERE cd_variavel like "h8%" '
    f'order by ano_pesquisa desc; '
)

bd = f_ConectaBD.conn
dfAnoBox = pd.read_sql(sql, bd)

v_ano = dfAnoBox['Ano pesquisa'].value_counts().index
cbox_AnoPesq = col1.selectbox('Selecione o ano da pesquisa a observar', v_ano)

col1, col2, col3 = st.columns([0.98, 0.01, 0.01])

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', SUBSTR(d.ds_merc_atuacao_abrev, 1, 40) 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% de Empresas que utilizaram',  "
    f"f.qtd_resposta_sim || ' %' as 'valor'  "
    f"from ft_ceticbr_mercado f, dm_mercado_atuacao d "
    f"where f.id_dm_mercado = d.id_merc_atuacao "  
    f"and f.ano_pesquisa = {cbox_AnoPesq} "
#    f"and f.cd_variavel like 'h8%' "
    f"and f.cd_variavel = 'h8a' "
    f"order by 3 desc; "  
)

bd = f_ConectaBD.conn
dfM1 = pd.read_sql(sql, bd)
dfM1.set_index("Mercado de atuação", inplace=True)
# dfM = dfM[dfM["Mercado de atuação"] == cbox_mercado]

########  PORTE
sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', f.id_dm_porte, d.ds_porte_empresa 'Porte empresa', "
    f"f.qtd_resposta_sim '% de Empresas que utilizaram',  "
    f"f.qtd_resposta_sim || ' %' as 'valor'  "
    f"from ft_ceticbr_porte f, dm_porte_empresa d "
    f"where f.id_dm_porte = d.id_porte_empresa "
    f"and f.ano_pesquisa = {cbox_AnoPesq} "
#    f"and f.cd_variavel like 'h8%' "
    f"and f.cd_variavel = 'h8a' "
    f"order by 2 ; "
)
bd = f_ConectaBD.conn
dfP1 = pd.read_sql(sql, bd)
dfP1.set_index("Porte empresa", inplace=True)

col1.markdown('**Proporção de utilização em :yellow-background[dispositivos de segurança], das empresas que fizeram uso de :yellow-background[tecnologia de IoT], por MERCADO de atuação, no ano selecionado**')
col2.write(' ')
col3.write(' ')

#col1.bar_chart(dfM1["% Empresas que utilizaram"].astype(int), color='#0F3A69')
fig_m = px.bar(dfM1, y="% de Empresas que utilizaram", text="valor", height=500, color_discrete_sequence=["#27A594"])
col1.plotly_chart(fig_m)
col2.write(' ')
col3.write(' ')

col1.markdown('**Proporção de utilização em :yellow-background[dispositivos de segurança], das empresas que fizeram uso de :yellow-background[tecnologia de IoT], por PORTE de empresa, no ano selecionado**')
col2.write(' ')
col3.write(' ')
#col1.bar_chart(dfP1["% Empresas que utilizaram"].astype(int), color='#75FA8D')
fig_p = px.bar(dfP1, y="% de Empresas que utilizaram", text="valor", height=500, color_discrete_sequence=["#27A594"])
col1.plotly_chart(fig_p)
col2.write(' ')
col3.write(' ')

# %% FIM!
