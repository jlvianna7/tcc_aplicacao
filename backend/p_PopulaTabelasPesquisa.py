#
# PRORAMA QUE REALIZA A MONTAGEM DO BANCO DE DADOS

#%% Importando os pacotes

#import numpy as np
#import seaborn as sns
import pandas as pd
import f_LeTabelasCetic
import warnings
#from openpyxl import Workbook

v_pathCtiBr = 'C:/Viery/BaseDadosTCC/TIC_Empresas-Ctic.br'
v_pathScripts = 'C:/GitHub/tcc_aplicacao/ScriptsBD'

monta_df = f_LeTabelasCetic

warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

# %% seleciona qual tabela (aba excel) a ser lida

v_tabelaCetic = 'B18'  ###  <<<<<<--------  SELECIONAR A PESQUISA (SHEET)
v_append_or_write = 'a'  ###  <<<<<<------ SE GERA NOVO SCRIPT OU SE INCLUI NO FINAL

#variaveis = ['B18a','B18b','B18c','B18d','E1','E2B','G2','G3','H10a','H10b','H10c','H10d','H10e','H10f','H10g','H13a','H13b','H13c','H13d','H13e','H13f','H13g','H13h','H13i','H1aa','H1ab','H1ac','H1ad','H3ba','H3bb','H3bc','H3bd','H3be','H3bf','H3bg','H4','H8a','H8b','H8c','H8d','H8e','H8f','H9aa','H9ab','H9ac','H9ad','H9ae','H9af','H9ag']
variaveis = ['E1','E2B','G2','G3','H1','H7','H9','B18','B18a','B18b','B18c','B18d','H10a','H10b','H10c','H10d','H10e','H10f','H10g','H13a','H13b','H13c','H13d','H13e','H13f','H13g','H13h','H13i','H1aa','H1ab','H1ac','H3ba','H3bb','H3bc','H3bd','H3Be','H3Bf','H3Bg','H8a','H8b','H8c','H8d','H8e','H8f','H9aa','H9ab','H9ac','H9ad','H9ae','H9af','H9ag']
variaveis = ['B18']


for v_tabelaCetic in variaveis: 
    # %% Prepara contexto 2014

    v_ano = '2014'    # <-- Mudar o ano

    if v_tabelaCetic in ['E1', 'E2B', 'G2', 'G3']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2014 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[0:3,]
        df_porte2014 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[8:]
        #df_mercado.to_excel('mercado.xlsx')
        df_mercado2014 = df_mercado         # <-- Mudar o ano do Dtaframe

    # %% Prepara contexto 2015

    v_ano = '2015'    # <-- Mudar o ano

    if v_tabelaCetic in ['E1', 'E2B', 'G2', 'G3']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2015 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[0:3,]
        df_porte2015 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[8:]
        #df_mercado.to_excel('mercado.xlsx')
        df_mercado2015 = df_mercado         # <-- Mudar o ano do Dtaframe

    # %% Prepara contexto  2017

    v_ano = '2017'    # <-- Mudar o ano

    if v_tabelaCetic in ['E1', 'E2B', 'G2', 'G3', 'B18','B18a','B18b','B18c']:
        if v_tabelaCetic not in ['B18a','B18b','B18c']:
            # Separa a pesquisa para gerar um dataframe separado por TOTAIS
            df_TOTAIS = monta_df.tabelaTOTAIS(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_TOTAIS2017 = df_TOTAIS             # <-- Mudar o ano do Dtaframe
            # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
            df_porte = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_porte = df_porte.iloc[0:3,]
            #df_porte.to_excel('./porte.xlsx')
            df_porte2017 = df_porte             # <-- Mudar o ano do Dtaframe

            # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
            df_mercado = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_mercado = df_mercado.iloc[8:]
            #df_mercado.to_excel('mercado.xlsx')
            df_mercado2017 = df_mercado         # <-- Mudar o ano do Dtaframe
        else:
            df_TOTAIS = monta_df.tabelaTOTAIS_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_TOTAIS2017 = df_TOTAIS             # <-- Mudar o ano do Dtaframe
            # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
            df_porte = monta_df.tabelaCtic_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_porte = df_porte.iloc[0:3,]
            #df_porte.to_excel('./porte.xlsx')
            df_porte2017 = df_porte             # <-- Mudar o ano do Dtaframe

            # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
            df_mercado = monta_df.tabelaCtic_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_mercado = df_mercado.iloc[8:]
            #df_mercado.to_excel('mercado.xlsx')
            df_mercado2017 = df_mercado         # <-- Mudar o ano do Dtaframe


    # %% Prepara contexto 2019

    v_ano = '2019'    # <-- Mudar o ano

    if v_tabelaCetic in ['E1', 'E2B', 'G2', 'G3','H1', 'H1Aa', 'H1Ab', 'H1Ac', 'H1Ad','H3', 'H3A', 
                        'H3Ba', 'H3Bb', 'H3Bc', 'H3Bd', 'H3Be', 'H3Bf', 'H3Bg', 'H4', 'B18','B18a','B18b','B18c']:
        if v_tabelaCetic not in ['B18','B18a','B18b','B18c','B18d', 'H1Aa', 'H1Ab', 'H1Ac','H3Ba', 'H3Bb', 'H3Bc', 'H3Bd', 'H3Be', 'H3Bf', 'H3Bg']:
            # Separa a pesquisa para gerar um dataframe separado por TOTAIS
            df_TOTAIS = monta_df.tabelaTOTAIS(v_pathCtiBr, v_ano, v_tabelaCetic)
            #print(df_TOTAIS)
            df_TOTAIS2019 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

            # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
            df_porte = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_porte = df_porte.iloc[1:4,]
            # df_porte.to_excel('porte.xlsx')
            df_porte2019 = df_porte             # <-- Mudar o ano do Dtaframe

            # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
            df_mercado = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_mercado = df_mercado.iloc[9:]
            # df_mercado.to_excel('mercado.xlsx')
            df_mercado2019 = df_mercado         # <-- Mudar o ano do Dtaframe

        elif v_tabelaCetic in ['H1Aa', 'H1Ab', 'H1Ac', 'H1Ad']:
            # Separa a pesquisa para gerar um dataframe separado por TOTAIS
            df_TOTAIS = monta_df.tabelaTOTAIS_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_TOTAIS2019 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

            # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
            df_porte = monta_df.tabelaCtic_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_porte = df_porte.iloc[1:4,]
            # df_porte.to_excel('porte.xlsx')
            df_porte2019 = df_porte             # <-- Mudar o ano do Dtaframe

            # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
            df_mercado = monta_df.tabelaCtic_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_mercado = df_mercado.iloc[9:]
            # df_mercado.to_excel('mercado.xlsx')
            df_mercado2019 = df_mercado         # <-- Mudar o ano do Dtaframe

        elif v_tabelaCetic in ['H3Ba', 'H3Bb', 'H3Bc', 'H3Bd', 'H3Be', 'H3Bf', 'H3Bg']:
            # Separa a pesquisa para gerar um dataframe separado por TOTAIS
            df_TOTAIS = monta_df.tabelaTOTAIS_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_TOTAIS2019 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

            # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
            df_porte = monta_df.tabelaCtic_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_porte = df_porte.iloc[1:4,]
            # df_porte.to_excel('porte.xlsx')
            df_porte2019 = df_porte             # <-- Mudar o ano do Dtaframe

            # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
            df_mercado = monta_df.tabelaCtic_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_mercado = df_mercado.iloc[9:]
            # df_mercado.to_excel('mercado.xlsx')
            df_mercado2019 = df_mercado         # <-- Mudar o ano do Dtaframe

        else:
            # Separa a pesquisa para gerar um dataframe separado por TOTAIS
            df_TOTAIS = monta_df.tabelaTOTAIS_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
            #print(df_TOTAIS)
            df_TOTAIS2019 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

            # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
            df_porte = monta_df.tabelaCtic_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_porte = df_porte.iloc[1:4,]
            # df_porte.to_excel('porte.xlsx')
            df_porte2019 = df_porte             # <-- Mudar o ano do Dtaframe

            # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
            df_mercado = monta_df.tabelaCtic_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
            df_mercado = df_mercado.iloc[9:]
            # df_mercado.to_excel('mercado.xlsx')
            df_mercado2019 = df_mercado         # <-- Mudar o ano do Dtaframe

    # %% Prepara contexto 2021

    v_ano = '2021'    # <-- Mudar o ano

    if v_tabelaCetic not in ['B18','B18a','B18b','B18c','B18d', 'H1Aa', 'H1Ab', 'H1Ac', 
                            'H8a', 'H8b', 'H8c', 'H8d', 'H8e', 'H8f', 'H9Aa', 'H9Ab', 'H9Ac', 'H9Ad', 'H9Ae', 'H9Af', 'H9Ag',
                            'H3Ba', 'H3Bb', 'H3Bc', 'H3Bd', 'H3Be', 'H3Bf', 'H3Bg',
                            'H10a', 'H10b', 'H10c', 'H10d', 'H10e', 'H10f', 'H10g',
                            'H13a', 'H13b', 'H13c', 'H13d', 'H13e', 'H13f', 'H13g', 'H13h', 'H13i']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2021 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2021 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2021 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H1Aa', 'H1Ab', 'H1Ac']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2021 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2021 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2021 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H3Ba', 'H3Bb', 'H3Bc', 'H3Bd', 'H3Be', 'H3Bf', 'H3Bg']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2021 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2021 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2021 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H8a', 'H8b', 'H8c', 'H8d', 'H8e', 'H8f']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H8(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2021 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H8(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2021 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H8(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2021 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H9Aa', 'H9Ab', 'H9Ac', 'H9Ad', 'H9Ae', 'H9Af', 'H9Ag']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H9A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2021 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H9A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2021 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H9A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2021 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H10a', 'H10b', 'H10c', 'H10d', 'H10e', 'H10f', 'H10g']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H10(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2021 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H10(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2021 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H10(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2021 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H13a', 'H13b', 'H13c', 'H13d', 'H13e', 'H13f', 'H13g', 'H13h', 'H13i']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H13(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2021 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H13(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2021 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H13(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2021 = df_mercado         # <-- Mudar o ano do Dtaframe

    else:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2021 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2021 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2021 = df_mercado         # <-- Mudar o ano do Dtaframe
        
        
    # %% Prepara contexto 2023

    v_ano = '2023'    # <-- Mudar o ano 

    if v_tabelaCetic not in ['B18','B18a','B18b','B18c','B18d', 'H1Aa', 'H1Ab', 'H1Ac', 
                            'H8a', 'H8b', 'H8c', 'H8d', 'H8e', 'H8f', 'H9Aa', 'H9Ab', 'H9Ac', 'H9Ad', 'H9Ae', 'H9Af', 'H9Ag',
                            'H3Ba', 'H3Bb', 'H3Bc', 'H3Bd', 'H3Be', 'H3Bf', 'H3Bg',
                            'H10a', 'H10b', 'H10c', 'H10d', 'H10e', 'H10f', 'H10g',
                            'H13a', 'H13b', 'H13c', 'H13d', 'H13e', 'H13f', 'H13g', 'H13h', 'H13i']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2023 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2023 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2023 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H1Aa', 'H1Ab', 'H1Ac']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2023 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2023 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2023 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H3Ba', 'H3Bb', 'H3Bc', 'H3Bd', 'H3Be', 'H3Bf', 'H3Bg']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2023 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2023 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2023 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H8a', 'H8b', 'H8c', 'H8d', 'H8e', 'H8f']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H8(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2023 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H8(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2023 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H8(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2023 = df_mercado         # <-- Mudar o ano do Dtaframe
    elif v_tabelaCetic in ['H9Aa', 'H9Ab', 'H9Ac', 'H9Ad', 'H9Ae', 'H9Af', 'H9Ag']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H9A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2023 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H9A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2023 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H9A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2023 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H10a', 'H10b', 'H10c', 'H10d', 'H10e', 'H10f', 'H10g']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H10(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2023 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H10(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2023 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H10(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2023 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H13a', 'H13b', 'H13c', 'H13d', 'H13e', 'H13f', 'H13g', 'H13h', 'H13i']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H13(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2023 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H13(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2023 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H13(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2023 = df_mercado         # <-- Mudar o ano do Dtaframe

    else:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2023 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2023 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2023 = df_mercado         # <-- Mudar o ano do Dtaframe
        
    # %% Prepara contexto 2024

    v_ano = '2024'     # <-- Mudar o ano

    if v_tabelaCetic not in ['B18','B18a','B18b','B18c','B18d', 'H1Aa', 'H1Ab', 'H1Ac', 
                            'H8a', 'H8b', 'H8c', 'H8d', 'H8e', 'H8f', 'H9Aa', 'H9Ab', 'H9Ac', 'H9Ad', 'H9Ae', 'H9Af', 'H9Ag',
                            'H3Ba', 'H3Bb', 'H3Bc', 'H3Bd', 'H3Be', 'H3Bf', 'H3Bg',
                            'H10a', 'H10b', 'H10c', 'H10d', 'H10e', 'H10f', 'H10g',
                            'H13a', 'H13b', 'H13c', 'H13d', 'H13e', 'H13f', 'H13g', 'H13h', 'H13i']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2024 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2024 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado por Mercado de atuação da empresa
        df_mercado = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        df_mercado2024 = df_mercado         # <-- Mudar o ano do Dtaframe
    elif v_tabelaCetic in ['H1Aa', 'H1Ab', 'H1Ac']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2024 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2024 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2024 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H3Ba', 'H3Bb', 'H3Bc', 'H3Bd', 'H3Be', 'H3Bf', 'H3Bg']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2024 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2024 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2024 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H8a', 'H8b', 'H8c', 'H8d', 'H8e', 'H8f']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H8(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2024 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H8(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2024 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H8(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2024 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H9Aa', 'H9Ab', 'H9Ac', 'H9Ad', 'H9Ae', 'H9Af', 'H9Ag']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H9A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2024 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H9A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2024 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H9A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2024 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H10a', 'H10b', 'H10c', 'H10d', 'H10e', 'H10f', 'H10g']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H10(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2024 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H10(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2024 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H10(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2024 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H13a', 'H13b', 'H13c', 'H13d', 'H13e', 'H13f', 'H13g', 'H13h', 'H13i']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H13(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2024 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H13(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2024 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H13(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2024 = df_mercado         # <-- Mudar o ano do Dtaframe

    else:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2024 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2024 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2024 = df_mercado         # <-- Mudar o ano do Dtaframe

######################################################################################################

    # %% Prepara contexto 2025

    v_ano = '2025'     # <-- Mudar o ano

    if v_tabelaCetic not in ['B18','B18a','B18b','B18c','B18d', 'H1Aa', 'H1Ab', 'H1Ac', 
                            'H8a', 'H8b', 'H8c', 'H8d', 'H8e', 'H8f', 'H9Aa', 'H9Ab', 'H9Ac', 'H9Ad', 'H9Ae', 'H9Af', 'H9Ag',
                            'H3Ba', 'H3Bb', 'H3Bc', 'H3Bd', 'H3Be', 'H3Bf', 'H3Bg',
                            'H10a', 'H10b', 'H10c', 'H10d', 'H10e', 'H10f', 'H10g',
                            'H13a', 'H13b', 'H13c', 'H13d', 'H13e', 'H13f', 'H13g', 'H13h', 'H13i']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2025 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2025 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado por Mercado de atuação da empresa
        df_mercado = monta_df.tabelaCtic(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        df_mercado2025 = df_mercado         # <-- Mudar o ano do Dtaframe
    elif v_tabelaCetic in ['H1Aa', 'H1Ab', 'H1Ac']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2025 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2025 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H1A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2025 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H3Ba', 'H3Bb', 'H3Bc', 'H3Bd', 'H3Be', 'H3Bf', 'H3Bg']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2025 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2025 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H3B(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2025 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H8a', 'H8b', 'H8c', 'H8d', 'H8e', 'H8f']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H8(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2025 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H8(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2025 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H8(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2025 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H9Aa', 'H9Ab', 'H9Ac', 'H9Ad', 'H9Ae', 'H9Af', 'H9Ag']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H9A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2025 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H9A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2025 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H9A(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2025 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H10a', 'H10b', 'H10c', 'H10d', 'H10e', 'H10f', 'H10g']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H10(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2025 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H10(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2025 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H10(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2025 = df_mercado         # <-- Mudar o ano do Dtaframe

    elif v_tabelaCetic in ['H13a', 'H13b', 'H13c', 'H13d', 'H13e', 'H13f', 'H13g', 'H13h', 'H13i']:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_H13(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2025 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_H13(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2025 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_H13(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2025 = df_mercado         # <-- Mudar o ano do Dtaframe

    else:
        # Separa a pesquisa para gerar um dataframe separado por TOTAIS
        df_TOTAIS = monta_df.tabelaTOTAIS_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_TOTAIS2025 = df_TOTAIS             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar um dataframe separado por Porte da empresa
        df_porte = monta_df.tabelaCtic_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_porte = df_porte.iloc[1:4,]
        # df_porte.to_excel('porte.xlsx')
        df_porte2025 = df_porte             # <-- Mudar o ano do Dtaframe

        # Separa a pesquisa para gerar o dataframe separado Mercado de atividades da empresa
        df_mercado = monta_df.tabelaCtic_B18(v_pathCtiBr, v_ano, v_tabelaCetic)
        df_mercado = df_mercado.iloc[9:]
        # df_mercado.to_excel('mercado.xlsx')
        df_mercado2025 = df_mercado         # <-- Mudar o ano do Dtaframe


######################################################################################################
    # %% Concatena os dataframes para gerar o script DML TOTAIS DO CONTEXTO
    ####  Concatena TOTAIS

    if v_tabelaCetic in ['E1', 'E2B', 'G2', 'G3']:
        df_tabTotais = pd.concat([df_TOTAIS2014, df_TOTAIS2015, df_TOTAIS2017, df_TOTAIS2019,
                                df_TOTAIS2021, df_TOTAIS2023, df_TOTAIS2024, df_TOTAIS2025], ignore_index=True)
    elif v_tabelaCetic in ['B18', 'B18a', 'B18b', 'B18c']:
        df_tabTotais = pd.concat([df_TOTAIS2017, df_TOTAIS2019, df_TOTAIS2021, df_TOTAIS2023, 
                                df_TOTAIS2024, df_TOTAIS2025], ignore_index=True)
    elif v_tabelaCetic in ['H1','H1Aa', 'H1Ab', 'H1Ac', 'H3', 'H3A', 'H3B', 'H4']:
        df_tabTotais = pd.concat([df_TOTAIS2019, df_TOTAIS2021, df_TOTAIS2023, 
                                df_TOTAIS2024, df_TOTAIS2025], ignore_index=True)
    else:
        df_tabTotais = pd.concat([df_TOTAIS2021, df_TOTAIS2023, df_TOTAIS2024, df_TOTAIS2025], ignore_index=True) 
  
#    nomeTabela = ('usp_dsa.ft_' + v_tabelaCetic + '_TOTAIS').lower()
    nomeTabela = (v_tabelaCetic).lower()
    arquivoScriptis = v_pathScripts + '/CticBr_ScriptDML_SQLite_3.sql' 

    #v_append_or_write = 'w'

    with open(arquivoScriptis, v_append_or_write, encoding='utf-8') as f:
        sql = (
            f"\n/* POPULA TABELA DE TOTAIS COM A VARIAVEL {v_tabelaCetic} */\n\n"
        )
        f.write(sql)
        print (sql)
        for _, row in df_tabTotais.iterrows():
            ano_pesquisa = row['Ano_pesquisa'].replace(
                "'", "''")  # Escapa aspas simples
            contexto = monta_df.busca_contexto(nomeTabela)
            #contexto = row['Contexto'].replace("'", "''")
            sim = round(float(row['Sim']))
            sim = int(sim)

            sql = (
                f"INSERT INTO ft_ceticbr_totais (ano_pesquisa, cd_variavel, contexto, qtd_resposta_sim) "
                f"VALUES ('{ano_pesquisa}', '{nomeTabela}', '{contexto}', {sim}); \n"
            )
            f.write(sql)
        f.write("COMMIT; \n\n")

######################################################################################################
 # %% Concatena os dataframes para gerar o script DML por PORTE, conforme qtd funcionários
    ####  Concatena PORTE EMPRESAS

    if v_tabelaCetic in ['E1', 'E2B', 'G2', 'G3']:
        df_tabporte = pd.concat([df_porte2014, df_porte2015, df_porte2017, df_porte2019,
                                df_porte2021, df_porte2023, df_porte2024, df_porte2025], ignore_index=True)
    elif v_tabelaCetic in ['B18', 'B18a', 'B18b', 'B18c']:
        df_tabporte = pd.concat([df_porte2017, df_porte2019,  df_porte2021, df_porte2023, df_porte2024, df_porte2025], ignore_index=True)

    elif v_tabelaCetic in ['H1','H1Aa', 'H1Ab', 'H1Ac', 'H3', 'H3A', 'H3B', 'H4']:
        df_tabporte = pd.concat([df_porte2019,  df_porte2021, df_porte2023, df_porte2024, df_porte2025], ignore_index=True)
    else:
        df_tabporte = pd.concat([df_porte2021, df_porte2023, df_porte2024, df_porte2025], ignore_index=True)
        
#    nomeTabela = ('usp_dsa.ft_' + v_tabelaCetic + '_porte').lower()
    nomeTabela = (v_tabelaCetic).lower()
    arquivoScriptis = v_pathScripts + '/CticBr_ScriptDML_SQLite_3.sql' 

    #v_append_or_write = 'a'

    with open(arquivoScriptis, v_append_or_write, encoding='utf-8') as f:
        sql = (
            f"\n/* POPULA TABELA POR PORTE DE EMPRESA COM A VARIAVEL {v_tabelaCetic}  */\n\n"
        )
        f.write(sql)

        for _, row in df_tabporte.iterrows():
            ano_pesquisa = row['Ano_pesquisa'].replace(
                "'", "''")  # Escapa aspas simples
            if 'De 10 a' in row['Contexto']:
                contexto = '2'
            elif 'De 50 a' in row['Contexto']:
                contexto = '3'
            elif '250 pess' in row['Contexto']:
                contexto = '4'
            elif 'De 250' in row['Contexto']:
                contexto = '4'
            else:
                contexto = row['Contexto']
            contexto = contexto.replace("'", "''")
            sim = round(float(row['Sim']))
            sim = int(sim)


            sql = (
                f"INSERT INTO ft_ceticbr_porte (ano_pesquisa, cd_variavel, id_dm_porte, qtd_resposta_sim) "
                f"VALUES ('{ano_pesquisa}', '{nomeTabela}', '{contexto}', {sim});\n"
            )
            f.write(sql)
        f.write("COMMIT; \n\n")

######################################################################################################
# %% Concatena os dataframes para gerar o script DML por MERCADO DE ATUAÇÃO
    ####  Concatena MERCADO

    if v_tabelaCetic in ['E1', 'E2B', 'G2', 'G3']:
        df_tabmercado = pd.concat([df_mercado2014, df_mercado2015, df_mercado2017, df_mercado2019,
                                df_mercado2021, df_mercado2023, df_mercado2024, df_mercado2025], ignore_index=True)
    elif v_tabelaCetic in ['B18','B18a','B18b','B18c']:
        df_tabmercado = pd.concat([df_mercado2017, df_mercado2019, df_mercado2021, df_mercado2023, df_mercado2024, df_mercado2025], ignore_index=True)
    elif v_tabelaCetic in ['H1', 'H1Aa', 'H1Ab', 'H1Ac', 'H3', 'H3A', 'H3B', 'H4']:
        df_tabmercado = pd.concat([df_mercado2019, df_mercado2021, df_mercado2023, df_mercado2024, df_mercado2025], ignore_index=True)
    else:
        df_tabmercado = pd.concat([df_mercado2021, df_mercado2023, df_mercado2024, df_mercado2025], ignore_index=True)

#    nomeTabela = ('usp_dsa.ft_' + v_tabelaCetic + '_mercado').lower()
    nomeTabela = (v_tabelaCetic).lower()
    arquivoScriptis = v_pathScripts + '/CticBr_ScriptDML_SQLite_3.sql' 

    #v_append_or_write = 'a'

    with open(arquivoScriptis, v_append_or_write, encoding='utf-8') as f:
        sql = (
            f"\n/* POPULA TABELA POR MERCADO DE ATUAÇÃO COM A VARIAVEL {v_tabelaCetic}  */\n\n"
        )
        f.write(sql)

        for _, row in df_tabmercado.iterrows():
            print(v_tabelaCetic, " ... ", row['Ano_pesquisa'], " ... ", row['Contexto'])
            ano_pesquisa = row['Ano_pesquisa'].replace(
                "'", "''")  # Escapa aspas simples
            if  'Indústria de' in row['Contexto']:
                contexto = '1'
            elif 'Industria de' in row['Contexto']:
                contexto = '1'
            elif 'Construção' in row['Contexto']:
                contexto = '2'
            elif 'Construcao' in row['Contexto']:
                contexto = '2'
            elif 'Comércio' in row['Contexto']:
                contexto = '3'
            elif 'Comercio' in row['Contexto']:
                contexto = '3'
            elif 'Transporte' in row['Contexto']:
                contexto = '4'
            elif 'Alojamento e' in row['Contexto']:
                contexto = '5'
            elif 'Informação' in row['Contexto']:
                contexto = '6'
            elif 'Informacao' in row['Contexto']:
                contexto = '6'
            elif 'Atividade' in row['Contexto']:
                contexto = '7'
            elif 'Artes,' in row['Contexto']:
                contexto = '8'
            else:
                contexto = row['Contexto']
            contexto = contexto.replace("'", "''")
            sim = round(float(row['Sim']))
            sim = int(sim)

            sql = (
                f"INSERT INTO ft_ceticbr_mercado (ano_pesquisa, cd_variavel, id_dm_mercado, qtd_resposta_sim) "
                f"VALUES ('{ano_pesquisa}', '{nomeTabela}', '{contexto}', {sim});\n"
            )
            f.write(sql)
        f.write("COMMIT; \n\n")



# %% FIM!
