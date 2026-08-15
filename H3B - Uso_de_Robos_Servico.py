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
with open("./logs/robo_serviço_servico.sql", "w", encoding="utf-8") as arquivo:
   arquivo.write(sql)


bd = f_ConectaBD.conn
dfl = pd.read_sql(sql, bd)


#col1.line_chart(dfl, x="Ano pesquisa", y="% de Empresas que utilizam", color="Tipo de serviço", height=460)
#col2.write(' ')

fig_L = px.line(dfl, x="Ano pesquisa", y="% de Empresas que utilizam", color="Tipo de serviço", height=640)
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



############################################   BLOCO 2  #############################################

# %% Demonstra a prticipação percentual por Mercado de atuação

st.write('')
col1, col2 = st.columns([0.98, 0.02])
st.write(' \n')

########  MERCADO

sql = (
    f'SELECT SUBSTRING(d.ds_merc_atuacao, 1, 25) || "..." as "Mercado de atuação",  '
    f'ROUND(AVG(f.qtd_resposta_sim),1) "% de Empresas que utilizam", '
    f'ROUND(AVG(f.qtd_resposta_sim),1) || " %" as "valor" '
    f'from ft_ceticbr_mercado f, dm_mercado_atuacao d '
    f'where f.id_dm_mercado = d.id_merc_atuacao '  
    f'and f.cd_variavel like "h3b%" '  
    f'group by f.id_dm_mercado '
    f'order by 2 desc;  '
)
#with open("c:/Temp/robo_mercado_data.sql", "w", encoding="utf-8") as arquivo:
#    arquivo.write(sql)

bd = f_ConectaBD.conn
dfM1 = pd.read_sql(sql, bd)
dfM1.set_index("Mercado de atuação", inplace=True)

col1.markdown('**% :yellow-background[médio] de utilização de :yellow-background[Robôs de serviços], por MERCADO de atuação**')
col2.write(' ')

fig_m = px.bar(dfM1, y="% de Empresas que utilizam", text="valor", color="% de Empresas que utilizam", height=640, color_discrete_sequence=['#0161BC'])
fig_m.update_coloraxes(showscale=False)
col1.plotly_chart(fig_m)

col2.write(' ')


########  PORTE
sql = (
    f'SELECT d.ds_porte_empresa "Porte empresa", ROUND(AVG(f.qtd_resposta_sim),1) as "% de Empresas que utilizam", ' 
    f'f.id_dm_porte, '
    f'ROUND(AVG(f.qtd_resposta_sim),1) || " %" as "valor"  '
    f'from ft_ceticbr_porte f, dm_porte_empresa d '
    f'where f.id_dm_porte = d.id_porte_empresa '
    f'and f.cd_variavel like "h3b%"   '
    f'group by f.id_dm_porte '
    f'order by f.id_dm_porte ; '  
)
#with open("G:/Meu Drive/MBA - USP/TCC/Resultados preliminares/Novos dados/robo_porte_data.sql", "w", encoding="utf-8") as arquivo:
#    arquivo.write(sql)

bd = f_ConectaBD.conn
dfP1 = pd.read_sql(sql, bd)
dfP1.set_index("Porte empresa", inplace=True)

col1.write(' ')
col1.markdown('**% :yellow-background[médio] de utilização de :yellow-background[Robôs de serviços], por PORTE de empresa**')

fig_p = px.bar(dfP1, y="% de Empresas que utilizam", text="valor", color="% de Empresas que utilizam", height=640, color_discrete_sequence=['#0161BC'])
fig_p.update_coloraxes(showscale=False)
col1.plotly_chart(fig_p)


# %% FIM!
