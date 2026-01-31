

## Código para nuvem de palavras

import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 1. Título do App
st.title("Gerador de Nuvem de Palavras")

# 2. Entrada de texto
texto = st.text_area("Cole seu texto aqui:", "Streamlit é excelente para ciência de dados dados dados visualização python")

if texto:
    # 3. Gerar a nuvem de palavras
    nuvem = WordCloud(width=800, height=400, background_color="white").generate(texto)

    # 4. Criar a figura do Matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(nuvem, interpolation='bilinear')
    ax.axis("off") # Esconder os eixos do gráfico

    # 5. Exibir no Streamlit
    st.pyplot(fig)


## complemento

nuvem = WordCloud(
    background_color="black", 
    max_words=50, 
    colormap="viridis"
).generate(texto)
