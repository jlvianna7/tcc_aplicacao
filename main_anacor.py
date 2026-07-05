#
# %% importa pacotes

import streamlit as st


# %% início
st.set_page_config(
    layout="wide",
    page_title="Transformação Digital e GMO"
    #    page_icon=""  pesquisar banco de ícones - talvez Keagle tenha
)

st.header(
    'Técnicas de Análise de Correspondência Simples e Análise de Correspondência Múltipla', divider=True)
st.text('\n\n\n\n\n')


st.subheader("\n\n\nAnálise de Correspondência Simples")
st.markdown('A **Análise de Correspondência Simples**, é usada quando você tem uma tabela de contingência entre duas variáveis ')
st.markdown('categóricas. Ela transforma as frequências em perfis de linha e de coluna e procura uma representação de baixa ')
st.markdown('dimensão em que categorias parecidas fiquem próximas no mapa perceptual demonstrando a associação entre tais variáveis.') 
st.write(' ')
st.write(' ')
          
st.subheader('Análise de Correspondência Múltipla', divider='gray')
st.markdown('A Análise de Correspondência Múltipla, ou ACM, é a extensão da AC para três ou mais variáveis categóricas. Ela costuma ')
st.markdown('ser categóricas aplicada a uma matriz de dados individuais codificada por categorias, como variáveis nominais em forma ')
st.markdown('indicadora, para revelar padrões conjuntos entre várias variáveis ao mesmo tempo.') 
st.write(' ')
st.write(' ')


## FIM