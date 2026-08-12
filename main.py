### Programa principal  


import streamlit as st

#from acs_anacor_ml import app
#from acs_anacor_ml import ca_core


pages = {
    "🏠 Início": [
        st.Page("Pesquisa Aplicada.py", title="Sobre a pesquisa"),
    ],
    "💶 Comércio Eletrônico": [
        st.Page("E1 - Compraram pela internet.py", title="Compraram pela internet"),
        st.Page("E2 - Venderam pela internet.py", title="Venderam pela internet"),
    ],
    "🏢 Softwares Corporativos  ": [
        st.Page("G2 - Uso de Plataformas de ERP.py", title="Uso de plataformas ERP"),
        st.Page("G3_CRM.py", title="Uso de sistemas CRM"),
    ],
    "📱 Novas Tecnologias": [
        st.Page("H1 - BigData.py", title="Análises de Big Data"),
        st.Page("B18 - Serv_Nuvem.py", title="Serviços de Nuvem"),
#        st.Page("H3 - Uso_de_Robos.py", title="Uso de robôs industriais"),
#        st.Page("H4 - Impressao_3D.py", title="Impressão 3D"),
        st.Page("H3B - Uso_de_Robos_Servico.py", title="Uso de robôs de Serviços"),
#        st.Page("H4 - Impressao_3D.py", title="Uso de Impressão 3D"),
        st.Page("H8_IOT.py", title="Uso de Dispositivos IoT"),
    ],
#    ">> Internet das Coisas (IoT)": [
#        st.Page("H7 - Dispositivos_IOT.py", title="Uso de Dispositivos IoT"),
#    ],
    "🎇 Inteligência Artificial": [
        st.Page("H9 - Uso_de_IA.py", title="Tipo de ferramenta"),
        st.Page("H10 - Aplicacao_de_IA.py", title="Área de aplicação de IA"),
        st.Page("H13 - Barreiras_de_IA.py", title="Barreiras para o uso de IA")
    ],
    "🌐 Pesquisa CMA": [
        st.Page("main_CMA.py", title="CMA - Resumo da pesquisa"),
        st.Page("cma_tipoMudanca.py", title="Tipos de mudanças"),
        st.Page("cma_areaCMO.py", title="CMO nas organizações"),
        st.Page("cma_maiorDesafioTD.py", title="Maior desafio para a TD"),
    ],
#    "🎇 Técnicas de Machine Learning": [
#        st.Page("main_anacor", title="ANACOR - Análise de Correspondência Simples"),
#        st.Page("app.py", title="Análise de Correspondência Simples"),
#    ],
}
st.sidebar.markdown("Pesquisa acadêmica   \n DSA - USP/ESALQ")
st.sidebar.write(" \n")
st.sidebar.markdown("Fonte de dados: [Cetic.br](https://cetic.br/pt/)")   
st.sidebar.markdown("Fonte de dados: [CMA](https://www.change-management-alliance.network/spaces/22440777/page)")   
st.sidebar.write("__________________________________________________________________________")
st.sidebar.markdown(":books: Desenvolvido por: [Joao Luiz Vianna](mailto:vianna.joaoluiz@gmail.com)")
st.sidebar.write("versão: 2.0.2")
st.sidebar.write("__________________________________________________________________________")
st.sidebar.write(" \n")
st.sidebar.write(" \n")
pg = st.navigation(pages, expanded=True, position='top')
pg.run()
