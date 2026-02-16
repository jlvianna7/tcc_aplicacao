###
# Anotações diversas
#
#
# Cores utilizadas
Cinza = '#3B3838'
Verde = '#385723'
Verde médio = '#ABD91B'
Verde claro = '#75FA8D'
Azul =  '#0F3A69'
Azul médio = '#3282F6'
Azul claro = '#64DADB'
Laranja = '#FF7F27'
Vermelho = '#ED1C24'
Sangue = '#EB3324'
Vinho = '#CF181F'
Barro = '#843C0C'
Rocho = '#EA3FF7'

# Paletas de cores ('_r' reverte a sequência de cores):
# viridis
# inferno
# magma
# cividis
# coolwarm
# Blues
# Greens
# Reds


# para executar o streamlit

streamlit run .\'Pesquisa Aplicada'.py



# Biblioteca adcional do Streamlit
https://arnaudmiribel.github.io/streamlit-extras/


#
# **Criando ambiente virtual**
#

*Para criar o ambiente*
- cd até o projeto
- python -m venv "nome a ser dados para a pasta de ambiente" normalmente venv, ficaria (python -m venv venv)

*Ativando o ambiente*
venv\Scripts\activate

*DESAtivando o ambiente*
venv\Scripts\deactivate

***Conferindo a Instalação dp python***
Verifique a instalação do Python dentro do ambiente virtual:
where python 


***Conferindo a Instalação de uma biblioteca***
pip show <biblioteca>

**Gerando o arquivo "requirements.txt"**
pip install -r requirements.txt



# **PARA FAZER WEB SCRAPING SIMULANDO O NAVEGADOR** #

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# #################
import requests

# URL do site que você quer acessar
url = 'https://www.example.com'

# Definindo um cabeçalho User-Agent comum de navegador
# Você pode encontrar listas atualizadas de User-Agents online
simula_browser = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

try:
    # Fazendo a solicitação com o cabeçalho personalizado
    response = requests.get(url, headers=**simula_browser**)
    response.raise_for_status() # Lança um erro para códigos de status ruins (4xx ou 5xx)

    # Imprimindo o conteúdo (HTML) da página
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro: {e}")


# ALGUNS INDICADORES TEM A MENSAGEM ABAIXO
¹Este indicador foi coletado somente entre as empresas que possuem área ou departamento de TI. Para fins de divulgação, são apresentados os resultados pelo total de empresas.

# Executando App no Streamlit
https://tcc-dsa242.streamlit.app/ 


%load_ext autoreload
%autoreload 2



EM RELAÇÃO A PESQUISA CETIC

PENSAR SE VALE A PENA DETALHAR PERFIL DA AMOSTRA POR PORTE E POR MERCADO CONFORME EXPLICITADO NOS RELATÓRIOS


SELECT 
    Vendedor,
    Valor,
    ROUND(Valor * 100.0 / SUM(Valor) OVER(), 2) AS Percentual_Formatado
FROM Vendas;

SELECT 
    Regiao,
    Vendedor,
    Valor,
    Valor * 100.0 / SUM(Valor) OVER(PARTITION BY Regiao) AS Percentual_Na_Regiao
FROM Vendas;