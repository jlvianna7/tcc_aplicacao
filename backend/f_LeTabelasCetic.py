#
# Função para montar a pesquisa conforme TAB SHEE das planilhas
#
import numpy as np
import seaborn as sns
import pandas as pd
from openpyxl import Workbook

def tabelaCtic(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name=cod_tabela, skiprows=2)
  
    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-1]
    
    # Excluindo a primeira linha que é de Totais
    df = df.iloc[1:]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:3]

    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    # Reorganiza as colunas
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df


def tabelaTOTAIS(vpath, ano_pesquisa, cod_tabela):
    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name=cod_tabela, skiprows=2)

    # Exclui a última linha, que é nota de rodapé
    if ano_pesquisa != '2014' and ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.iloc[1:]

    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-17]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:3]
 
    #if ano_pesquisa != '2015' and ano_pesquisa != '2017':
    #    df = df.drop(0).reset_index(drop=True)
 
    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    # Mudo o nome da coluna que ficou sem título
    df = df.fillna('Valores totais')
    if ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.replace('Total', 'Valores totais')

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    # Reorganiza as colunas
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df




###################  H3B USO DE ROBÔS DE SERVIÇOS  ##########################################################################

def tabelaCtic_H3B(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name='H3B', skiprows=2)
  
    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-1]
    
    # Excluindo a primeira linha que é de Totais
    df = df.iloc[1:]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:10]
    ##print(df.iloc[:, 1:9])

    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    # Mudo o nome das colunas relativas a pesquisa B18
    df = df.rename(columns={
        'Vigilância, segurança ou tarefas de inspeção, como o uso de drones, etiquetas de identificação de radiofrequência, etc.': 'vigilancia',
        'Transporte de pessoas ou mercadorias, como o uso de veículo guiado automaticamente, etc.': 'transporte',
        'Limpeza ou tarefas de eliminação de resíduos': 'limpeza',
        'Sistemas de gerenciamento de estoque, como paletização e manuseio de mercadorias': 'estoque',
        'Trabalhos de montagem': 'montagem',
        'Tarefas de balconista de loja robótico': 'balconista',
        'Trabalhos de construção ou reparos': 'reparos',
        })

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    #print(df)
    # Reorganiza as colunas
    if cod_tabela == "H3Ba":
        df = df.rename(columns={'vigilancia': 'Sim'})
    elif cod_tabela == 'H3Bb':
        df = df.rename(columns={'transporte': 'Sim'})
    elif cod_tabela == 'H3Bc':
        df = df.rename(columns={'limpeza': 'Sim'})
    elif cod_tabela == 'H3Bd':
        df = df.rename(columns={'estoque': 'Sim'})
    elif cod_tabela == 'H3Be':
        df = df.rename(columns={'montagem': 'Sim'})
    elif cod_tabela == 'H3Bf':
        df = df.rename(columns={'balconista': 'Sim'})
    elif cod_tabela == 'H3Bg':
        df = df.rename(columns={'reparos': 'Sim'})
    #print(df)
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df


def tabelaTOTAIS_H3B(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name='H3B', skiprows=2)

    # Exclui a última linha, que é nota de rodapé
    if ano_pesquisa != '2014' and ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.iloc[1:]

    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-17]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:9]

    #if ano_pesquisa != '2015' and ano_pesquisa != '2017':
    #    df = df.drop(0).reset_index(drop=True)
 
    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    #print(df)
    # Mudo o nome da coluna que ficou sem título
    df = df.fillna('Valores totais')
    if ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.replace('Total', 'Valores totais')
    #print(df)

    df = df.rename(columns={
        'Vigilância, segurança ou tarefas de inspeção, como o uso de drones, etiquetas de identificação de radiofrequência, etc.': 'vigilancia',
        'Transporte de pessoas ou mercadorias, como o uso de veículo guiado automaticamente, etc.': 'transporte',
        'Limpeza ou tarefas de eliminação de resíduos': 'limpeza',
        'Sistemas de gerenciamento de estoque, como paletização e manuseio de mercadorias': 'estoque',
        'Trabalhos de montagem': 'montagem',
        'Tarefas de balconista de loja robótico': 'balconista',
        'Trabalhos de construção ou reparos': 'reparos',
        })

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    #print(df)
    # Reorganiza as colunas
    if cod_tabela == "H3Ba":
        df = df.rename(columns={'vigilancia': 'Sim'})
    elif cod_tabela == 'H3Bb':
        df = df.rename(columns={'transporte': 'Sim'})
    elif cod_tabela == 'H3Bc':
        df = df.rename(columns={'limpeza': 'Sim'})
    elif cod_tabela == 'H3Bd':
        df = df.rename(columns={'estoque': 'Sim'})
    elif cod_tabela == 'H3Be':
        df = df.rename(columns={'montagem': 'Sim'})
    elif cod_tabela == 'H3Bf':
        df = df.rename(columns={'balconista': 'Sim'})
    elif cod_tabela == 'H3Bg':
        df = df.rename(columns={'reparos': 'Sim'})
    #print(df)
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df



####################################  B18 - SERVIÇOS DE NUVEM

def tabelaCtic_B18(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name='B18', skiprows=2)
  
    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-1]
    
    # Excluindo a primeira linha que é de Totais
    df = df.iloc[1:]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:9]
    ##print(df.iloc[:, 1:9])

    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    # Mudo o nome das colunas relativas a pesquisa B18
    if ano_pesquisa != '2017' and ano_pesquisa != '2019':    
        df = df.rename(columns={
            'E-mail em nuvem': 'email',
            'Software de escritório em nuvem': 'office',
            'Armazenamento de arquivos ou banco de dados em nuvem': 'armazenamento',
            'Capacidade de processamento em nuvem': 'processamento',
            'Software de finanças ou contabilidade': 'contabil',
            'Software de segurança': 'seguranca',
            'Plataforma de computação que fornece um ambiente hospedado para desenvolvimento, teste ou implantação de aplicativos': 'desenvolvimento'
            })
    elif ano_pesquisa == '2019':    
        df = df.rename(columns={
            'E-mail em nuvem': 'email',
            'Software de escritório em nuvem': 'office',
            'Armazenamento de arquivos ou banco de dados em nuvem': 'armazenamento',
            'Capacidade de processamento em nuvem': 'processamento'
            })
    else:
        df = df.rename(columns={
            'E-mail': 'email',
            'Software de escritório': 'office',  
            'Armazenamento de arquivos ou banco de dados': 'armazenamento',
            'Capacidade de processamento': 'processamento'
            })

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    #print(df)
    # Reorganiza as colunas
    if ano_pesquisa != '2017' and ano_pesquisa != '2019':
        if cod_tabela == "B18a":
            df = df.rename(columns={'office': 'Sim'})
        elif cod_tabela == 'B18b':
            df = df.rename(columns={'armazenamento': 'Sim'})
        elif cod_tabela == 'B18c':
            df = df.rename(columns={'processamento': 'Sim'})
        elif cod_tabela == 'B18d':
            df = df.rename(columns={'desenvolvimento': 'Sim'})
    else:
        if cod_tabela == "B18a":
            df = df.rename(columns={'office': 'Sim'})
        elif cod_tabela == 'B18b':
            df = df.rename(columns={'armazenamento': 'Sim'})
        elif cod_tabela == 'B18c':
            df = df.rename(columns={'processamento': 'Sim'})
        elif cod_tabela == 'B18d':
            df = df.rename(columns={'desenvolvimento': 'Sim'})
    #print('.....TOTAIS........' )
    #print(df)
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df


def tabelaTOTAIS_B18(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name='B18', skiprows=2)

    # Exclui a última linha, que é nota de rodapé
    if ano_pesquisa != '2014' and ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.iloc[1:]

    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-17]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:9]

    #if ano_pesquisa != '2015' and ano_pesquisa != '2017':
    #    df = df.drop(0).reset_index(drop=True)
 
    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    #print(df)
    # Mudo o nome da coluna que ficou sem título
    df = df.fillna('Valores totais')
    if ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.replace('Total', 'Valores totais')
    #print(df)

    # Mudo o nome das colunas relativas a pesquisa B18
    if ano_pesquisa != '2017' and ano_pesquisa != '2019':    
        df = df.rename(columns={
            'E-mail em nuvem': 'email',
            'Software de escritório em nuvem': 'office',
            'Armazenamento de arquivos ou banco de dados em nuvem': 'armazenamento',
            'Capacidade de processamento em nuvem': 'processamento',
            'Software de finanças ou contabilidade': 'contabil',
            'Software de segurança': 'seguranca',
            'Plataforma de computação que fornece um ambiente hospedado para desenvolvimento, teste ou implantação de aplicativos': 'desenvolvimento'
            })
    elif ano_pesquisa == '2019':    
        df = df.rename(columns={
            'E-mail em nuvem': 'email',
            'Software de escritório em nuvem': 'office',
            'Armazenamento de arquivos ou banco de dados em nuvem': 'armazenamento',
            'Capacidade de processamento em nuvem': 'processamento'
            })
    else:
        df = df.rename(columns={
            'E-mail': 'email',
            'Software de escritório': 'office',  
            'Armazenamento de arquivos ou banco de dados': 'armazenamento',
            'Capacidade de processamento': 'processamento'
            })

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    #print(df)
    # Reorganiza as colunas
    if ano_pesquisa != '2017' and ano_pesquisa != '2019':
        if cod_tabela == "B18a":
            df = df.rename(columns={'office': 'Sim'})
        elif cod_tabela == 'B18b':
            df = df.rename(columns={'armazenamento': 'Sim'})
        elif cod_tabela == 'B18c':
            df = df.rename(columns={'processamento': 'Sim'})
        elif cod_tabela == 'B18d':
            df = df.rename(columns={'desenvolvimento': 'Sim'})
    else:
        if cod_tabela == "B18a":
            df = df.rename(columns={'office': 'Sim'})
        elif cod_tabela == 'B18b':
            df = df.rename(columns={'armazenamento': 'Sim'})
        elif cod_tabela == 'B18c':
            df = df.rename(columns={'processamento': 'Sim'})
        elif cod_tabela == 'B18d':
            df = df.rename(columns={'desenvolvimento': 'Sim'})
    #print('.....TOTAIS........' )
    #print(df)
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df



###################  H1A - BIGDATA

def tabelaCtic_H1A(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name='H1A', skiprows=2)
  
    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-1]
    
    # Excluindo a primeira linha que é de Totais
    df = df.iloc[1:]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:9]
    ##print(df.iloc[:, 1:9])

    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    # Mudo o nome das colunas relativas a pesquisa B18
    df = df.rename(columns={
        'A partir de dados próprios da empresa, provenientes de dispositivos inteligentes ou sensores, como trocas de dados entre máquinas, sensores digitais, etiquetas de identificação por radiofrequência, etc.': 'dados_proprios',
        'A partir de dados de geolocalização provenientes do uso de dispositivos portáteis, como telefone móvel, conexão wireless ou GPS': 'geolocalizacao_mobile',
        'A partir de dados gerados a partir de mídias sociais, como redes sociais, blogs, sites de compartilhamento de conteúdo de multimídia': 'midias_socias',
        })

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    #print(df)
    # Reorganiza as colunas
    if cod_tabela == "H1Aa":
        df = df.rename(columns={'dados_proprios': 'Sim'})
    elif cod_tabela == 'H1Ab':
        df = df.rename(columns={'geolocalizacao_mobile': 'Sim'})
    elif cod_tabela == 'H1Ac':
        df = df.rename(columns={'midias_socias': 'Sim'})
    #print(df)
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df


def tabelaTOTAIS_H1A(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name='H1A', skiprows=2)

    # Exclui a última linha, que é nota de rodapé
    if ano_pesquisa != '2014' and ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.iloc[1:]

    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-17]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:9]

    #if ano_pesquisa != '2015' and ano_pesquisa != '2017':
    #    df = df.drop(0).reset_index(drop=True)
 
    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    #print(df)
    # Mudo o nome da coluna que ficou sem título
    df = df.fillna('Valores totais')
    if ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.replace('Total', 'Valores totais')
    #print(df)

    # Mudo o nome das colunas relativas a pesquisa B18
    df = df.rename(columns={
        'A partir de dados próprios da empresa, provenientes de dispositivos inteligentes ou sensores, como trocas de dados entre máquinas, sensores digitais, etiquetas de identificação por radiofrequência, etc.': 'dados_proprios',
        'A partir de dados de geolocalização provenientes do uso de dispositivos portáteis, como telefone móvel, conexão wireless ou GPS': 'geolocalizacao_mobile',
        'A partir de dados gerados a partir de mídias sociais, como redes sociais, blogs, sites de compartilhamento de conteúdo de multimídia': 'midias_socias',
        })

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    #print(df)
    # Reorganiza as colunas
    if cod_tabela == "H1Aa":
        df = df.rename(columns={'dados_proprios': 'Sim'})
    elif cod_tabela == 'H1Ab':
        df = df.rename(columns={'geolocalizacao_mobile': 'Sim'})
    elif cod_tabela == 'H1Ac':
        df = df.rename(columns={'midias_socias': 'Sim'})
    #print(df)
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df




###################  H8 DISPOSITIVOS DE IOT  ############################################

def tabelaCtic_H8(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name='H8', skiprows=2)
  
    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-1]
    
    # Excluindo a primeira linha que é de Totais
    df = df.iloc[1:]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:9]
    ##print(df.iloc[:, 1:9])

    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    # Mudo o nome das colunas relativas a pesquisa B18
    df = df.rename(columns={
        'Gerenciamento de consumo de energia, como medidores, termostatos ou lâmpadas inteligentes': 'Gerenciamentos de consumos, medidores inteligentes',
        'Segurança de instalações, como sistemas de alarme, detectores de fumaça, travas de portas e câmeras de segurança inteligentes': 'Dispositivos de segurança',
        'Processos de produção, como sensores ou etiquetas de identificação por radiofrequência que são monitorados ou controlados via Internet e usados para monitorar ou automatizar processos': 'Automatização de processo de produção',
        'Gestão de logística, como sensores monitorados ou controlados via Internet para rastreamento de produtos ou veículos na gestão de depósito': 'Gestão de logística',
        'Manutenção de equipamentos, como sensores monitorados ou controlados através da Internet para monitorar as necessidades de manutenção de máquinas ou veículos': 'Monitoramento e manutenção de equipamentos',
        'Atendimento ao cliente, como câmeras ou sensores inteligentes monitorados ou controlados através da Internet para monitorar as atividades dos clientes ou oferecer-lhes uma experiência de compra personalizada': 'Atendimento ao cliente',
        })

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    #print(df)
    # Reorganiza as colunas
    if cod_tabela == "H8a":
        df = df.rename(columns={'Gerenciamentos de consumos, medidores inteligentes': 'Sim'})
    elif cod_tabela == 'H8b':
        df = df.rename(columns={'Dispositivos de segurança': 'Sim'})
    elif cod_tabela == 'H8c':
        df = df.rename(columns={'Automatização de processo de produção': 'Sim'})
    elif cod_tabela == 'H8d':
        df = df.rename(columns={'Gestão de logística': 'Sim'})
    elif cod_tabela == 'H8e':
        df = df.rename(columns={'Monitoramento e manutenção de equipamentos': 'Sim'})
    elif cod_tabela == 'H8f':
        df = df.rename(columns={'Atendimento ao cliente': 'Sim'})
    #print(df)
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df


def tabelaTOTAIS_H8(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name='H8', skiprows=2)

    # Exclui a última linha, que é nota de rodapé
    if ano_pesquisa != '2014' and ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.iloc[1:]

    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-17]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:9]

    #if ano_pesquisa != '2015' and ano_pesquisa != '2017':
    #    df = df.drop(0).reset_index(drop=True)
 
    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    #print(df)
    # Mudo o nome da coluna que ficou sem título
    df = df.fillna('Valores totais')
    if ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.replace('Total', 'Valores totais')

    df = df.rename(columns={
        'Gerenciamento de consumo de energia, como medidores, termostatos ou lâmpadas inteligentes': 'Gerenciamentos de consumos, medidores inteligentes',
        'Segurança de instalações, como sistemas de alarme, detectores de fumaça, travas de portas e câmeras de segurança inteligentes': 'Dispositivos de segurança',
        'Processos de produção, como sensores ou etiquetas de identificação por radiofrequência que são monitorados ou controlados via Internet e usados para monitorar ou automatizar processos': 'Automatização de processo de produção',
        'Gestão de logística, como sensores monitorados ou controlados via Internet para rastreamento de produtos ou veículos na gestão de depósito': 'Gestão de logística',
        'Manutenção de equipamentos, como sensores monitorados ou controlados através da Internet para monitorar as necessidades de manutenção de máquinas ou veículos': 'Monitoramento e manutenção de equipamentos',
        'Atendimento ao cliente, como câmeras ou sensores inteligentes monitorados ou controlados através da Internet para monitorar as atividades dos clientes ou oferecer-lhes uma experiência de compra personalizada': 'Atendimento ao cliente',
        })

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    #print(df)
    # Reorganiza as colunas
    if cod_tabela == "H8a":
        df = df.rename(columns={'Gerenciamentos de consumos, medidores inteligentes': 'Sim'})
    elif cod_tabela == 'H8b':
        df = df.rename(columns={'Dispositivos de segurança': 'Sim'})
    elif cod_tabela == 'H8c':
        df = df.rename(columns={'Automatização de processo de produção': 'Sim'})
    elif cod_tabela == 'H8d':
        df = df.rename(columns={'Gestão de logística': 'Sim'})
    elif cod_tabela == 'H8e':
        df = df.rename(columns={'Monitoramento e manutenção de equipamentos': 'Sim'})
    elif cod_tabela == 'H8f':
        df = df.rename(columns={'Atendimento ao cliente': 'Sim'})
    #print(df)
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]


    return df





###################  H9A IA  INTELIGENCIA ARTIFICIAL ##########################################################################

def tabelaCtic_H9A(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name='H9A', skiprows=2)
  
    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-1]
    
    # Excluindo a primeira linha que é de Totais
    df = df.iloc[1:]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:10]
    ##print(df.iloc[:, 1:9])

    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    # Mudo o nome das colunas relativas a pesquisa B18
    df = df.rename(columns={
        'Mineração de texto e análise da linguagem escrita': 'texto',
        'Reconhecimento de fala, que converte a linguagem falada em formato legível para máquinas': 'fala',
        'Geração de linguagem natural (GLN) para linguagem escrita ou falada': 'gnl',
        'Reconhecimento e processamento de imagens que identificam objetos ou pessoas': 'imagem',
        'Machine learning, como deep learning, para predição e análise de dados': 'learning',
        'Automatização de processos de fluxos de trabalho': 'processos',
        'Movimentação física de máquinas por meio de decisões autônomas, como robôs, veículos e drones autônomos': 'autonomos',
        })

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    #print(df)
    # Reorganiza as colunas
    if cod_tabela == "H9Aa":
        df = df.rename(columns={'texto': 'Sim'})
    elif cod_tabela == 'H9Ab':
        df = df.rename(columns={'fala': 'Sim'})
    elif cod_tabela == 'H9Ac':
        df = df.rename(columns={'gnl': 'Sim'})
    elif cod_tabela == 'H9Ad':
        df = df.rename(columns={'imagem': 'Sim'})
    elif cod_tabela == 'H9Ae':
        df = df.rename(columns={'learning': 'Sim'})
    elif cod_tabela == 'H9Af':
        df = df.rename(columns={'processos': 'Sim'})
    elif cod_tabela == 'H9Ag':
        df = df.rename(columns={'autonomos': 'Sim'})
    #print(df)
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df


def tabelaTOTAIS_H9A(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name='H9A', skiprows=2)

    # Exclui a última linha, que é nota de rodapé
    if ano_pesquisa != '2014' and ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.iloc[1:]

    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-17]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:9]

    #if ano_pesquisa != '2015' and ano_pesquisa != '2017':
    #    df = df.drop(0).reset_index(drop=True)
 
    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    #print(df)
    # Mudo o nome da coluna que ficou sem título
    df = df.fillna('Valores totais')
    if ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.replace('Total', 'Valores totais')
    #print(df)

    df = df.rename(columns={
        'Mineração de texto e análise da linguagem escrita': 'texto',
        'Reconhecimento de fala, que converte a linguagem falada em formato legível para máquinas': 'fala',
        'Geração de linguagem natural (GLN) para linguagem escrita ou falada': 'gnl',
        'Reconhecimento e processamento de imagens que identificam objetos ou pessoas': 'imagem',
        'Machine learning, como deep learning, para predição e análise de dados': 'learning',
        'Automatização de processos de fluxos de trabalho': 'processos',
        'Movimentação física de máquinas por meio de decisões autônomas, como robôs, veículos e drones autônomos': 'autonomos',
        })

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    #print(df)
    # Reorganiza as colunas
    if cod_tabela == "H9Aa":
        df = df.rename(columns={'texto': 'Sim'})
    elif cod_tabela == 'H9Ab':
        df = df.rename(columns={'fala': 'Sim'})
    elif cod_tabela == 'H9Ac':
        df = df.rename(columns={'gnl': 'Sim'})
    elif cod_tabela == 'H9Ad':
        df = df.rename(columns={'imagem': 'Sim'})
    elif cod_tabela == 'H9Ae':
        df = df.rename(columns={'learning': 'Sim'})
    elif cod_tabela == 'H9Af':
        df = df.rename(columns={'processos': 'Sim'})
    elif cod_tabela == 'H9Ag':
        df = df.rename(columns={'autonomos': 'Sim'})
    #print(df)
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df


###################  H10 APLICAÇÃO DE IA  ##########################################################################

def tabelaCtic_H10(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name='H10', skiprows=2)
  
    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-1]
    
    # Excluindo a primeira linha que é de Totais
    df = df.iloc[1:]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:10]
    ##print(df.iloc[:, 1:9])

    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    # Mudo o nome das colunas relativas a pesquisa B18
    df = df.rename(columns={
        'Marketing ou vendas': 'vendas',
        'Processos de produção': 'producao',
        'Organização de processos de administração de negócios': 'adm',
        'Gestão de empresas': 'gestao',
        'Logística': 'logistica',
        'Segurança digital': 'seguranca',
        'Gestão de recursos humanos ou recrutamento': 'rh',
        })

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    #print(df)
    # Reorganiza as colunas
    if cod_tabela == "H10a":
        df = df.rename(columns={'vendas': 'Sim'})
    elif cod_tabela == 'H10b':
        df = df.rename(columns={'producao': 'Sim'})
    elif cod_tabela == 'H10c':
        df = df.rename(columns={'adm': 'Sim'})
    elif cod_tabela == 'H10d':
        df = df.rename(columns={'gestao': 'Sim'})
    elif cod_tabela == 'H10e':
        df = df.rename(columns={'logistica': 'Sim'})
    elif cod_tabela == 'H10f':
        df = df.rename(columns={'seguranca': 'Sim'})
    elif cod_tabela == 'H10g':
        df = df.rename(columns={'rh': 'Sim'})
    #print(df)
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df


def tabelaTOTAIS_H10(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name='H10', skiprows=2)

    # Exclui a última linha, que é nota de rodapé
    if ano_pesquisa != '2014' and ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.iloc[1:]

    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-17]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:9]

    #if ano_pesquisa != '2015' and ano_pesquisa != '2017':
    #    df = df.drop(0).reset_index(drop=True)
 
    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    #print(df)
    # Mudo o nome da coluna que ficou sem título
    df = df.fillna('Valores totais')
    if ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.replace('Total', 'Valores totais')
    #print(df)

    df = df.rename(columns={
        'Marketing ou vendas': 'vendas',
        'Processos de produção': 'producao',
        'Organização de processos de administração de negócios': 'adm',
        'Gestão de empresas': 'gestao',
        'Logística': 'logistica',
        'Segurança digital': 'seguranca',
        'Gestão de recursos humanos ou recrutamento': 'rh',
        })

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    #print(df)
    # Reorganiza as colunas
    if cod_tabela == "H10a":
        df = df.rename(columns={'vendas': 'Sim'})
    elif cod_tabela == 'H10b':
        df = df.rename(columns={'producao': 'Sim'})
    elif cod_tabela == 'H10c':
        df = df.rename(columns={'adm': 'Sim'})
    elif cod_tabela == 'H10d':
        df = df.rename(columns={'gestao': 'Sim'})
    elif cod_tabela == 'H10e':
        df = df.rename(columns={'logistica': 'Sim'})
    elif cod_tabela == 'H10f':
        df = df.rename(columns={'seguranca': 'Sim'})
    elif cod_tabela == 'H10g':
        df = df.rename(columns={'rh': 'Sim'})
    #print(df)
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df




###################  H13 BARREIRAS PARA O USO DE IA  ##########################################################################

def tabelaCtic_H13(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name='H13', skiprows=2)
  
    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-1]
    
    # Excluindo a primeira linha que é de Totais
    df = df.iloc[1:]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:11]
    ##print(df.iloc[:, 1:9])

    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    # Mudo o nome das colunas relativas a pesquisa B18
    df = df.rename(columns={
        'Porque os custos parecem ser muito altos': 'custo',
        'Por falta de pessoas capacitadas na empresa para usar essas tecnologias': 'pessoas',
        'Por incompatibilidade com equipamentos, software ou sistemas existentes na empresa': 'equipamento',
        'Por dificuldades de disponibilidade ou qualidade dos dados necessários para o uso dessas tecnologias': 'qualidade',
        'Por preocupações com relação à violação da proteção de dados e privacidade': 'privacidade',
        'Por falta de clareza sobre as consequências legais do uso dessas tecnologias, como em casos de danos causados pelo uso de Inteligência Artificial': 'legal',
        'Por considerações éticas': 'etica',
        'Porque as tecnologias de Inteligência Artificial não são úteis para a empresa': 'utilidade',
        'Por falta de conhecimento sobre tecnologias de Inteligência Artificial adequadas para as atividades da empresa': 'falta',
        })

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    #print(df)
    # Reorganiza as colunas
    if cod_tabela == "H13a":
        df = df.rename(columns={'custo': 'Sim'})
    elif cod_tabela == 'H13b':
        df = df.rename(columns={'pessoas': 'Sim'})
    elif cod_tabela == 'H13c':
        df = df.rename(columns={'equipamento': 'Sim'})
    elif cod_tabela == 'H13d':
        df = df.rename(columns={'qualidade': 'Sim'})
    elif cod_tabela == 'H13e':
        df = df.rename(columns={'privacidade': 'Sim'})
    elif cod_tabela == 'H13f':
        df = df.rename(columns={'legal': 'Sim'})
    elif cod_tabela == 'H13g':
        df = df.rename(columns={'etica': 'Sim'})
    elif cod_tabela == 'H13h':
        df = df.rename(columns={'utilidade': 'Sim'})
    elif cod_tabela == 'H13i':
        df = df.rename(columns={'falta': 'Sim'})
    #print(df)
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df


def tabelaTOTAIS_H13(vpath, ano_pesquisa, cod_tabela):

    tabela = vpath + '/tic_empresas_' + ano_pesquisa + '_tabela_proporcao_v1.0.xlsx'

    df = pd.read_excel(tabela, sheet_name='H13', skiprows=2)

    # Exclui a última linha, que é nota de rodapé
    if ano_pesquisa != '2014' and ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.iloc[1:]

    # Exclui a última linha, que é nota de rodapé
    df = df.iloc[:-17]

    # Selecionao as colunas que vou utilizar, neste caso a partir da segunda
    df = df.iloc[:, 1:11]

    #if ano_pesquisa != '2015' and ano_pesquisa != '2017':
    #    df = df.drop(0).reset_index(drop=True)
 
    # Mudo o nome da coluna que ficou sem título
    df = df.rename(columns={'Unnamed: 1': 'Contexto'})

    #print(df)
    # Mudo o nome da coluna que ficou sem título
    df = df.fillna('Valores totais')
    if ano_pesquisa != '2015' and ano_pesquisa != '2017':
        df = df.replace('Total', 'Valores totais')
    #print(df)

    df = df.rename(columns={
        'Porque os custos parecem ser muito altos': 'custo',
        'Por falta de pessoas capacitadas na empresa para usar essas tecnologias': 'pessoas',
        'Por incompatibilidade com equipamentos, software ou sistemas existentes na empresa': 'equipamento',
        'Por dificuldades de disponibilidade ou qualidade dos dados necessários para o uso dessas tecnologias': 'qualidade',
        'Por preocupações com relação à violação da proteção de dados e privacidade': 'privacidade',
        'Por falta de clareza sobre as consequências legais do uso dessas tecnologias, como em casos de danos causados pelo uso de Inteligência Artificial': 'legal',
        'Por considerações éticas': 'etica',
        'Porque as tecnologias de Inteligência Artificial não são úteis para a empresa': 'utilidade',
        'Por falta de conhecimento sobre tecnologias de Inteligência Artificial adequadas para as atividades da empresa': 'falta',
        })

    # Incluiíndo o ano da pesquisa
    df = df.assign(Ano_pesquisa=ano_pesquisa)

    #print(df)
    # Reorganiza as colunas
    if cod_tabela == "H13a":
        df = df.rename(columns={'custo': 'Sim'})
    elif cod_tabela == 'H13b':
        df = df.rename(columns={'pessoas': 'Sim'})
    elif cod_tabela == 'H13c':
        df = df.rename(columns={'equipamento': 'Sim'})
    elif cod_tabela == 'H13d':
        df = df.rename(columns={'qualidade': 'Sim'})
    elif cod_tabela == 'H13e':
        df = df.rename(columns={'privacidade': 'Sim'})
    elif cod_tabela == 'H13f':
        df = df.rename(columns={'legal': 'Sim'})
    elif cod_tabela == 'H13g':
        df = df.rename(columns={'etica': 'Sim'})
    elif cod_tabela == 'H13h':
        df = df.rename(columns={'utilidade': 'Sim'})
    elif cod_tabela == 'H13i':
        df = df.rename(columns={'falta': 'Sim'})
    #print(df)
    colunas_reorder = ['Ano_pesquisa', 'Contexto', 'Sim']
    df = df[colunas_reorder]

    return df
