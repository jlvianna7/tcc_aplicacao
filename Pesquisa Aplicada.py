# Página prinicipal

import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(
    layout="wide",
    page_title="Transformação Digital e GMO"
    #    page_icon=""  pesquisar banco de ícones - talvez Keagle tenha
)

st.header(
    'Pesquisa aplicada sobre transformação digital nas empresas no Brasil', divider=True)
#st.text('\n\n\n\n\n')

st.header("Objetivo.\n\n")
st.markdown('O objetivo deste trabalho é acadêmico e a ideia foi explorar e entender a **cronologia da :yellow-background[transformação digital] nas organizações brasileiras** - considerando'
            ' empresas privadas, segmentadas por porte e por mercado de atuação. Procurou-se verificar ainda em quais áreas da cadeia produtiva estão utilizando '
            '**novas tecnologias**, quais obstáculos enfrentados (se existentes), e quais mecanismos estão sendo utilizados para enfrentá-los, como por '
            'exemplo a estruturação de processos ou áreas de :yellow-background[**Gerenciamento de Mudanças Organizacionais [GMO]**]. Adicionalmente tentou '
            'identificar quais destas organizações estão conseguindo se tornar :yellow-background[**“data-driven”**], ou seja, quantas já conduzem os '
            'seus **processos decisórios com base em dados**.'
            )

st.header("\n\n\nMétodo")
st.markdown('Este estudo realizou uma **pesquisa exploratória aplicada**, buscando correlacionar dados consolidados de pesquisas do ***Centro Regional de Estudos para '
            'o Desenvolvimento da Sociedade da Informação [Cetic.br]***, entidade vinculada ao ***Comitê Gestor da Internet no Brasil [CGI]***, com os resultados '
            'da **Change Management Survey 2025** realizada pela ***Change Management Alliance [CMA]***, associação internacional de profissionais de gestão de mudança, '
            'com participação significativa de gestores e consultores brasileiros.\n'
            'O Cetic.br publica, periodicamente, desde 2008, uma série de levantamentos sobre a utilização de **Tecnologia da Informação e Comunicação [TIC]** no Brasil'
            ', abrangendo desde o uso da internet em domicílios, a infraestrutura de TIC em educação, em eventos de cultura, dentre outros. No entanto,'
            ' este estudo irá se ater as pesquisas ***TIC Empresas***, que em 2024 representou um universo aproximado de 500 mil empresas a partir de uma amostragem '
            'de 4.600 entrevistas. Os dados do Cetic.br foram utilizados para identificar a evolução cronológica da **transformação digital** nas organizações '
            'no Brasil, durante este período.\n\n')
st.markdown('Para os processos de compilação, tabulação e demonstrações gráficas foi utilizada a ***linguagem Python*** e suas “bibliotecas” próprias '
            'para tratamento de dados, como ***Pandas, Numpy, Plotly, Streamlit***, podendo ser utilizado também o “Power BI”, caso facilite as apresentações visuais.')


