
import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

st.set_page_config(page_title="Nuvenator PT-BR", layout="wide")

st.title("☁️ Nuvem de Palavras Inteligente")
st.markdown("Este gerador remove automaticamente conectivos e palavras comuns do português.")

# 1. Configuração de Stopwords (Palavras a ignorar)
# Começamos com a lista padrão da biblioteca
palavras_irrelevantes = set(STOPWORDS)

# Lista customizada de stopwords em Português
stopwords_pt = [
    "de", "a", "o", "que", "e", "do", "da", "em", "um", "para", "é", "com", "não", 
    "uma", "os", "no", "se", "na", "por", "mais", "as", "dos", "das", "pelo", "pela",
    "através", "seu", "sua", "seus", "suas", "meu", "minha", "nossos", "nas", "aos",
    "este", "esta", "está", "isso", "isto", "mim", "você", "vocês", "com", "como"
]
palavras_irrelevantes.update(stopwords_pt)

# 2. Barra Lateral para Customização
st.sidebar.header("Configurações")
cor_fundo = st.sidebar.color_picker("Cor do fundo", "#ffffff")
palavras_extras = st.sidebar.text_input("Adicione outras palavras para ignorar (separadas por vírgula):")

if palavras_extras:
    extras = [p.strip().lower() for p in palavras_extras.split(",")]
    palavras_irrelevantes.update(extras)

# 3. Entrada de Texto
texto = st.text_area("Cole seu texto abaixo:", height=250)

if texto:
    # 4. Geração da Nuvem
    # O parâmetro 'stopwords' é o segredo aqui
    wc = WordCloud(
        stopwords=palavras_irrelevantes,
        background_color=cor_fundo,
        width=1200,
        height=600,
        colormap="viridis",
        max_words=100
    ).generate(texto)

    # 5. Exibição
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
else:
    st.info("Aguardando texto para gerar a nuvem...")