# H9 - EMPRESAS QUE UTILIZARAM TECNOLOGIAS DE Serviços de Nuvem

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

# TOTAL PARA O INDICADOR H9 - EMPRESAS QUE UTILIZARAM TECNOLOGIAS DE Serviços de Nuvem

st.sidebar.color_picker = "#FF7F27"
#st.sidebar.write("H1 - Empresas que fazem análises de Serviços de Nuvem")
st.sidebar.markdown("**H9 - Utilização de tecnologias de Serviços de Nuvem**")

# %% Evolução anual, geral do uso de Serviços de Nuvem

st.subheader("Evolução da utilização de :yellow-background[Serviços de Nuvem]")

sql = (
    f'SELECT ano_pesquisa "Ano pesquisa", empresas_respondentes "Amostragem" '
    f'FROM dm_resumo_pesquisa '
    f'order by ano_pesquisa; '
)

bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)

col1, col2, col3 = st.columns([0.15, 0.02, 0.83])

col1.markdown("\n\n\n**Empresas pesquisadas**")
col2.write(' ')
col3.markdown("**Proporção de empresas que utilizam :yellow-background[Serviços de Nuvem] para armazenamento ou Banco de Dados")

dfpesq = df[["Ano pesquisa", "Amostragem"]]
col1.table(dfpesq)

#####

sql = (
    f'SELECT cd_variavel, ano_pesquisa "Ano pesquisa", contexto "Serviço", qtd_resposta_sim "% de Empresas que utilizam" ' 
    f'FROM ft_ceticbr_totais '
    f'WHERE  (cd_variavel like "b18%" ) ' 
    f'order by 1, 2; '
)

bd = f_ConectaBD.conn
dfl = pd.read_sql(sql, bd)

col3.line_chart(dfl, x="Ano pesquisa", y="% de Empresas que utilizam", color="Serviço", height=400)
#col3.table(dfl)



############################################   BLOCO 2  #############################################

### GRÁFICOS AUXILIARES

##col1, col2, col3 = st.columns([0.96, 0.02, 0.02])

###col1.markdown('**Evolução cronológica do uso de :yellow-background[Serviços de Nuvem], por mercado de atuação**')
###col2.write(' ')
###col3.write(' ')

# %% Evuloção anual 
# Montando a ComboBox para o filtro

# %% FIM!
