# Execução das pesquisas sobre Robôs de serviços
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
st.header(
    'Pesquisa aplicada sobre transformação digital nas empresas no Brasil', divider=True)
st.text('\n\n\n\n\n')

# TOTAL PARA O INDICADOR H3A - EMPRESAS, POR USO DE Robôs de serviços


st.sidebar.color_picker = "#FF7F27"
#st.sidebar.write("H1 - Empresas que fazem análises de Robôs de serviços")
st.sidebar.markdown("**H3B - Empresas que utilizam Robôs de serviços**")

# %% Evolução anual, geral do uso de Robôs de serviços

st.subheader("Evolução da utilização de :yellow-background[Robôs de serviços]")

col1, col2 = st.columns([0.98, 0.02])

col1.markdown("**Proporção de empresas que utilizaram :yellow-background[Robôs de serviços], no respectivo período**")
col2.write(' ')

sql = (
    f'SELECT cd_variavel, ano_pesquisa "Ano pesquisa", contexto "Tipo de serviço", qtd_resposta_sim "% de Empresas que utilizam" ' 
    f'FROM ft_ceticbr_totais '
    f'WHERE cd_variavel like "h3b%" '  
    f'order by 1, 2;'
)
bd = f_ConectaBD.conn
dfl = pd.read_sql(sql, bd)


#col1.line_chart(dfl, x="Ano pesquisa", y="% de Empresas que utilizam", color="Tipo de serviço", height=460)
#col2.write(' ')

fig_L = px.line_3d(dfl, x="Ano pesquisa", y="% de Empresas que utilizam", color="Tipo de serviço", text="% de Empresas que utilizam", height=460)
col1.plotly_chart(fig_L)
col2.write(' ')



############################################   BLOCO 2  #############################################

# %% Demonstra a prticipação percentual por Mercado de atuação

st.write('')
#col1 = st.columns([0.99])
st.write(' \n')

########  MERCADO

sql = (
    f'SELECT SUBSTRING(d.ds_merc_atuacao, 1, 25) || "..." as "Mercado de atuação",  ROUND(AVG(f.qtd_resposta_sim),1) "% Empresas que utilizam" '
    f'from ft_ceticbr_mercado f, dm_mercado_atuacao d '
    f'where f.id_dm_mercado = d.id_merc_atuacao '  
    f'and f.cd_variavel like "h3b%" '  
    f'group by f.id_dm_mercado '
    f'order by f.ano_pesquisa;  '
)

bd = f_ConectaBD.conn
dfM1 = pd.read_sql(sql, bd)
dfM1.set_index("Mercado de atuação", inplace=True)


########  PORTE
sql = (
    f'SELECT d.ds_porte_empresa "Porte empresa", ROUND(AVG(f.qtd_resposta_sim),1) as "% Empresas que utilizam", f.id_dm_porte  '
    f'from ft_ceticbr_porte f, dm_porte_empresa d '
    f'where f.id_dm_porte = d.id_porte_empresa '
    f'and f.cd_variavel like "h3b%"   '
    f'group by f.id_dm_porte '
    f'order by 3; '  
)
bd = f_ConectaBD.conn
dfP1 = pd.read_sql(sql, bd)
dfP1.set_index("Porte empresa", inplace=True)


# col3.markdown(f"**Peso:** {dados_jogador['Weight(lbs.)']*0.453:0.2f}")

#fig_p = px.bar(dfP1)

col1, col2, col3 = st.columns([0.64, 0.02, 0.34])

col1.markdown('**% :yellow-background[médio] de utilização de :yellow-background[Robôs de serviços], por MERCADO de atuação**')
col2.write(' ')
col3.markdown('**% :yellow-background[médio] de utilização de :yellow-background[Robôs de serviços], por PORTE de empresa**')

fig_m = px.bar(dfM1, y="% Empresas que utilizam", text="% Empresas que utilizam", height=500, color_discrete_sequence=['#CF181F', '#FF5733', '#FF33A1'])
col1.plotly_chart(fig_m)

col2.write(' ')

fig_p = px.bar(dfP1, y="% Empresas que utilizam", text="% Empresas que utilizam", height=500, color_discrete_sequence=['#3282F6', '#FF33A1', '#33FF57'])
col3.plotly_chart(fig_p)

col1.write(' \n')
col2.write(' \n')
col3.write(' \n')
col1.write(' \n')
col2.write(' \n')
col3.write(' \n')
col1.write(' \n')
col2.write(' \n')
col3.write(' \n')


############################################   BLOCO 3  #############################################

### GRÁFICOS AUXILIARES

col1, col2, col3 = st.columns([0.49, 0.02, 0.49])

col1.markdown('**Evolução cronológica do uso de :yellow-background[Robôs de serviços], por mercado de atuação**')
col2.write(' ')
col3.markdown('**Evolução cronológica do uso de :yellow-background[Robôs de serviços], por porte de empresa**')


# %% Evuloção anual por POR MERCADO DE ATUAÇÃO
# Montando a ComboBox para o filtro
sql = (
    f'SELECT DISTINCT d.ds_merc_atuacao "Mercado de atuação" ' 
    f'FROM ft_ceticbr_mercado f, dm_mercado_atuacao d '
    f'WHERE f.id_dm_mercado = d.id_merc_atuacao '
    f'and f.cd_variavel like "h3b%" '  
    f'ORDER BY d.ds_merc_atuacao ; '
)
bd = f_ConectaBD.conn
dfMBox = pd.read_sql(sql, bd)

v_mercado = dfMBox['Mercado de atuação'].value_counts().index
cbox_mercado = col1.selectbox('Selecione o Mercado de atuação a pesquisar', v_mercado)

sql = (
    f"SELECT f.ano_pesquisa 'Ano pesquisa', d.ds_merc_atuacao 'Mercado de atuação', " 
    f"f.qtd_resposta_sim '% Empresas que utilizam', q.nm_questao_variavel 'Variável' "
    f"from ft_ceticbr_mercado f, dm_mercado_atuacao d, dm_dicionario_questoes_ceticbr q "
    f"where f.id_dm_mercado = d.id_merc_atuacao "  
    f"and f.cd_variavel like 'h3b%' "  
    f"and f.cd_variavel = q.cd_questao_ceticbr "
    f"order by 1, 3 desc, 4; "  
)

bd = f_ConectaBD.conn
dfM = pd.read_sql(sql, bd)
#dfM.set_index("Ano pesquisa", inplace=True)
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

col2.write()

# Montando a ComboBox para o filtro
v_porte = dfPBox["Porte empresa"].value_counts().index
cbox_porte = col3.selectbox('Selecione o porte das empresas', v_porte)

sql = (
    f'SELECT f.ano_pesquisa "Ano pesquisa", d.ds_porte_empresa "Porte empresa", '
    f'f.qtd_resposta_sim "% Empresas que utilizam", q.nm_questao_variavel "Variável"  '
    f'from ft_ceticbr_porte f, dm_porte_empresa d, dm_dicionario_questoes_ceticbr q '
    f'where f.id_dm_porte = d.id_porte_empresa '
    f'and f.cd_variavel = q.cd_questao_ceticbr '
    f'and f.cd_variavel like "h3b%" '
    f'order by 1, 3 desc, 4; '
)
bd = f_ConectaBD.conn
dfP = pd.read_sql(sql, bd)

#dfP.set_index("Ano pesquisa", inplace=True)
dfP = dfP[dfP["Porte empresa"] == cbox_porte]

# %% Exibe os gráficos segmentados
fig_m = px.bar(dfM, x="Ano pesquisa", y="% Empresas que utilizam", color="Variável", text="Variável", height=460)
fig_m.update_layout(showlegend=False)

fig_p = px.bar(dfP, x="Ano pesquisa", y="% Empresas que utilizam", color="Variável", text="Variável", height=460)
fig_p.update_layout(showlegend=False)

#st.plotly_chart(fig, col1)
#col1.plotly_chart(px.bar(dfM, x="Ano pesquisa", y="% Empresas que utilizam", color="Variável", text="Variável", leg))
col1.plotly_chart(fig_m)
col2.write(' ')
col3.plotly_chart(fig_p)


# %% FIM!
