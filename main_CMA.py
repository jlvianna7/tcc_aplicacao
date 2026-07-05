#
# %% importa pacotes

import numpy as np
import pandas as pd
import seaborn as sns

from backend import f_ConectaBD

import streamlit as st


# %% início
st.set_page_config(
    layout="wide",
    page_title="Transformação Digital e GMO"
    #    page_icon=""  pesquisar banco de ícones - talvez Keagle tenha
)

st.header(
    'CMA Survey 2025 - Gerenciamento de Mudanças Organizacionais', divider=True)
st.text('\n\n\n\n\n')


st.subheader("\n\n\nA pesquisa")
st.markdown('A **Change Management Alliance [CMA]**, é um comunidade internacional que agrega profissionais de gestão de mudança e demais interessados'
            ' na disciplina. Ela conta com cerca de 1500 associados, em todo o mundo, com uma expressiva participação de profissionais do Brasil.\n\n'
            'Durante o ano de 20205 a CMA realizou uma pesquisa em seu portal sobre questões relacionadas à Gestão de Mudanças Organizacionais visando identificar'
            ' o quão gerenciadas são as mudança que ocorrem nas organizações dos associados, as principais características, principais pontos positivos,'
            ' barreiras enfrentadas e a percepção deste grupo em relação maturidade da Gestão de Mudanças em suas organizações nos seus países.\n\n'
            'Como este trabalho é restrito a perspectivas brasileiras, iremos utilizaar apenas as respostas das empresas do Brasil')
st.write(' ')
st.write(' ')
          
st.subheader('Resumo da pesquisa', divider='gray')

#
# %% importa pacotes

col1, col2, col3, col4, col5 = st.columns([0.20, 0.02, 0.35, 0.02, 0.41])

col1.write("Período da pesquisa")
col1.markdown("**09/06/2025 a 10/10/2025**")
col1.write(" ")
col1.write("Respondentes")
col1.markdown("**278**")
col1.write(" ")
col1.write("Representantes de empresas brasileiras")
col1.markdown("**113**")
col1.write(" ")
col1.write("Participação de empresas brasileira")
col1.markdown("**40%**")
#col1.metric(label="Período da pesquisa", value=f"09/06/2025 a 10/10/2025", height='stretch', width='stretch')
#col1.metric(label="Respondentes", value=f"278", width='stretch')
#col1.metric(label="Representantes de empresas brasileiras", value=f"113", width='stretch')
#col1.metric(label="Participação de empresas brasileira", value=f"40%", width='stretch')

col2.write(' ')


sql = (
    f'SELECT porte_empresa "Porte da empresa", count(*) "Respondentes" '''
    f'from ft_cma_principal '
    f'group by porte_empresa '
    f'order by 2 '
)

bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)
#bd.close

#df.set_index("Porte da Empresa", inplace=True)
col3.table(df)

col4.write(' ')

sql = (
    f'SELECT mercado_atuacao "Atividade econômica", count(*) "Respondentes" '
    f'from ft_cma_principal '
    f'group by mercado_atuacao '
    f'order by 2 DESC '
)

bd = f_ConectaBD.conn
df = pd.read_sql(sql, bd)
col5.table(df)
#bd.close()
