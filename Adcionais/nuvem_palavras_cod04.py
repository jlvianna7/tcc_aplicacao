import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

st.title("☁️ Nuvem com Formato Customizado")

# 1. Upload da máscara
arquivo_mascara = st.file_uploader("Envie uma imagem para servir de molde (Fundo branco!)", type=["png", "jpg", "jpeg"])

texto = st.text_area("Cole seu texto aqui:")

if texto and arquivo_mascara:
    # 2. Processar a imagem da máscara
    img = Image.open(arquivo_mascara)
    mask = np.array(img)

    # 3. Gerar a nuvem usando a máscara
    wc = WordCloud(
        background_color="white",
        mask=mask,
        contour_width=1,       # Desenha o contorno da forma
        contour_color='black', # Cor do contorno
        width=1200, 
        height=600
    ).generate(texto)

    # 4. Exibir
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
    
elif not arquivo_mascara:
    st.warning("Por favor, envie uma imagem de máscara para ver o efeito.")