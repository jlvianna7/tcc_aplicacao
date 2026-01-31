#
# Script consolidar, prepara e selecionar as variáveis a serem trabalhadas
#

# %% Importando os pacotes
import pandas as pd
import numpy as np
import seaborn as sns

colunas = ['Tamanho', 'Id_var',
           'Desc_var', 'Tipo_Var', 'Conteudo_var']

v_pathCtiBr = 'C:/Users/joao.vianna/Documents/Temp_TCC_USP_ESALQ/BaseDadosTCC/TD-Ctic.br'


# %% Importando dicionário 2017

df = pd.read_excel(v_pathCtiBr + '/tic_empresas_2017_dicionario_de_variaveis_v1.0.xlsx',
                   names=colunas, sheet_name='Datamap', skiprows=3)

# Inserindo na posição desejada
variaveis_2017 = df.assign(Ano_pesquisa=2017)

# %% Importando dicionário 2019

df = pd.read_excel(v_pathCtiBr + '/tic_empresas_2019_dicionario_de_variaveis_v1.0.xlsx',
                   names=colunas, sheet_name='TIC EMP 2019', skiprows=3)

variaveis_2019 = df.assign(Ano_pesquisa=2019)

# %% Importando dicionário 2021

df = pd.read_excel(v_pathCtiBr + '/tic_empresas_2021_dicionario_de_variaveis_v1.0.xlsx',
                   names=colunas, sheet_name='Datamap', skiprows=3)

variaveis_2021 = df.assign(Ano_pesquisa=2021)

# %% Importando dicionário 2023

df = pd.read_excel(v_pathCtiBr + '/tic_empresas_2023_dicionario_de_variaveis_v1.0.xlsx',
                   names=colunas, sheet_name='Datamap', skiprows=3)

variaveis_2023 = df.assign(Ano_pesquisa=2023)

# %% Importando dicionário 2024

df = pd.read_excel(v_pathCtiBr + '/tic_empresas_2024_dicionario_de_variaveis_v1.0.xlsx',
                   names=colunas, sheet_name='Datamap', skiprows=3)

variaveis_2024 = df.assign(Ano_pesquisa=2024)

# %%  Salva arquivo novo

# Concatena todos os Dataframes em um único para salvar como Tabela
dicionario_global = pd.concat([variaveis_2017, variaveis_2019,
                              variaveis_2021, variaveis_2023, variaveis_2024], ignore_index=True)

# Apaga as linhas em que o nome da variável está em branco (neste caso, objetivamente serve
# para excluir as linhas separadores de assuntos)
dicionario_global = dicionario_global.dropna(subset=['Id_var'])

# Duplica a o código da variável (Id_var), pois nos arquivos de dados pode aparecer com novo código
dicionario_global = dicionario_global.assign(
    Id_varNew=dicionario_global['Id_var'])

# Cria duas colunas novas para eu poder manipular no momneto selecionar
# e contextualizar a escolha ou algum detalhe importante
dicionario_global = dicionario_global.assign(Observacao='', Tipo_Selecao='')

# Mudo a ordem das variáreis para melhorar a minha visualização (pode ser vir também
# para selecionar as variáveis que serão utilizadas)
colunas_reorder = ['Id_var', 'Ano_pesquisa', 'Id_varNew', 'Tamanho',
                   'Desc_var', 'Tipo_Var', 'Conteudo_var', 'Observacao', 'Tipo_Selecao']
dicionario_global = dicionario_global[colunas_reorder]

# Classifico a tabela conforme o nome das variáveis e o ano para poder identificar mudanças
dicionario_global = dicionario_global.sort_values(by=['Id_var', 'Ano_pesquisa'],
                                                  ascending=[True, True]).reset_index(drop=True)
# Gero um excel final de todo o contexto
dicionario_global.to_excel('dicionario_global_variaveis.xlsx')


# %% FIM!
