# Página prinicipal

import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Transformação Digital e GMO"
    #    page_icon=""  pesquisar banco de ícones - talvez Keagle tenha
)

st.header(
    'CMA Survey 2025 - Pesquisa Gerenciamento de Mudanças', divider=True)
st.text('\n\n\n\n\n')


st.header("\n\n\nA pesquisa")
st.markdown('A **Change Management Alliance [CMA]**, é um comunidade internacional que agrega profissionais de gestão de mudança e demais interessados'
            ' na disciplina. Ela conta com cerca de 1500 associados, com uma expressiva participação de profissionais do Brasil.'
            ' e consultores brasileiros.\n'
            'Durante o ano de 20205 a CMA realizou uma pesquisa em seu portal sobre questões relacionadas à Gestão de Mudanças Organizacionais visando identificar'
            'o quão gerenciadas são as mudança que ocorrem nas organizações dos associados, as principais características, principais pontos positivos'
            'barreiras e a percepçaõ destes em relação maturidade desses processo nas susa organizações nos seus países.\n'
            'como este trabalho está restrito a perspectivas brasileiras, iremos utilizaar apenas as respostas referentes a empresas no Brasil')
st.write(' ')
st.write(' ')
          
st.subheader('Resumo da pesquisa', divider='gray')

