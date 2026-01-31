# Cria estrutura do Banco de Dados
# %% INÍCIO
 
import f_CriaDDLTabelasFato

monta_DLL = f_CriaDDLTabelasFato

v_schemaBD ='usp_dsa'

# %% Cria script DDL com a estrutura do BANCO DE DADOS

# Como é o início do scrit o utilizo o "w" para sobrescrever caso exista
with open('../ScriptsBD/CticBr_ScriptDDL.sql', 'w', encoding='utf-8') as f:
    sql = (
        f"\n/* CRIAÇÃO DA ESTRUTURA DO BANCO DE DADOS */\n\n"
        f"CREATE SCHEMA {v_schemaBD} DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;\n"
        f"\n\n/*********  ESTRUTURA DAS TABELAS DE DOMÍNIO *******/\n"

    )
    f.write(sql)

# %% Cria script DDL da tabela de RESUMO DA PESQUISA

# RESUMO DA PESQUISA
with open('../ScriptsBD/CticBr_ScriptDDL.sql', 'a', encoding='utf-8') as f:
    sql = (
        f"\n\n/* TABELA DE DOMÍNIO RESUMO DA PESQUISA */\n"     
        f"CREATE TABLE {v_schemaBD}.dm_resumo_pesquisa (ano_pesquisa varchar(8) NOT NULL, \n"
        f"amostra_planejada int DEFAULT NULL, \n"
        f"empresas_respondentes int NOT NULL, \n"
        f"link_publicacao VARCHAR(1024), \n"
        f"PRIMARY KEY (ano_pesquisa), \n"
        f"UNIQUE KEY ano_pesquisa_UNIQUE (ano_pesquisa)) \n"
        f"COMMENT='Tabela de resumo dos quantitativos das pesquisas';"
    )
    f.write(sql)


# %% Cria script DDL da tabela de RESPOSTAS SIMPLES

# TABELA DE RESPOSTAS
with open('../ScriptsBD/CticBr_ScriptDDL.sql', 'a', encoding='utf-8') as f:

    sql = (
        f"\n\n/* TABELA DE DOMÍNIO PARA RESPOSTAS SIMPLES */\n"
        f"CREATE TABLE {v_schemaBD}.dm_resposta_sn (id_resposta_sn int NOT NULL, "
        f"ds_resposta_sn varchar(16) NOT NULL, \n"
        f"PRIMARY KEY (id_resposta_sn), \n"
        f"UNIQUE KEY id_resposta_sn_UNIQUE (id_resposta_sn)) \n"
        f"COMMENT='Domínio para respostas simples sim ou não e mais algumas opções';"
    )
    f.write(sql)

# %% Cria script DDL da tabela de PORTE DE EMPRESA

# PORTE DE EMPRESA
with open('../ScriptsBD/CticBr_ScriptDDL.sql', 'a', encoding='utf-8') as f:
    sql = (
        f"\n\n/* TABELA DE DOMÍNIO DE PORTE DE EMPRESA PESQUISADA */\n"
        f"CREATE TABLE {v_schemaBD}.dm_porte_empresa (id_porte_empresa varchar(4) NOT NULL, "
        f"ds_porte_empresa varchar(32) NOT NULL, \n"
        f"PRIMARY KEY (id_porte_empresa), \n"
        f"UNIQUE KEY id_porte_empresa_UNIQUE (id_porte_empresa)) \n"
        f"COMMENT='Tamanho da empresa em pesquisada, em quantidade de funcionários.';"
    )
    f.write(sql)

# %% Cria script DDL da tabela de MERCADO DE ATUAÇÃO DA EMPRESA

# MERCADO DE ATUAÇÃO
with open('../ScriptsBD/CticBr_ScriptDDL.sql', 'a', encoding='utf-8') as f:
    sql = (
        f"\n\n/* TABELA DE DOMÍNIO DE MERCADO DE ATUAÇÃO EMPRESA PESQUISADA */\n"
        f"CREATE TABLE {v_schemaBD}.dm_mercado_atuacao (id_merc_atuacao varchar(4) NOT NULL, "
        f"ds_merc_atuacao varchar(256) DEFAULT NULL, \n"
        f"cod_ibge varchar(1) DEFAULT NULL, \n"
        f"PRIMARY KEY (id_merc_atuacao), \n"
        f"UNIQUE KEY id_merc_atuacao_UNIQUE (id_merc_atuacao)) \n"
        f"COMMENT='Marcado de atuação segundo pesquisa CeticBr';\n"
    )
    f.write(sql)

# %% separador para DDL das TABELAS FATO

# SEPARADOR PARA TABELAS FATO
with open('../ScriptsBD/CticBr_ScriptDDL.sql', 'a', encoding='utf-8') as f:
    sql = (
        f"\n\n\n/*********  ESTRUTURA DAS TABELAS FATO *******/\n"

    )
    f.write(sql)

# %% Cria script DDL da fato das pesquisa com 
# TABELA FATO CETICBR
# 
# TABELAS PARA B18   ##############################################
monta_DLL.criaDDL('B18a', v_schemaBD)

# TABELAS PARA B18   ##############################################
monta_DLL.criaDDL('B18b', v_schemaBD)

# TABELAS PARA B18   ##############################################
monta_DLL.criaDDL('B18c', v_schemaBD)

# TABELAS PARA B18   ##############################################
monta_DLL.criaDDL('B18d', v_schemaBD)

# TABELAS PARA E1
monta_DLL.criaDDL('E1', v_schemaBD)

# TABELAS PARA E2
monta_DLL.criaDDL('E2', v_schemaBD)

# TABELAS PARA G2
monta_DLL.criaDDL('G2', v_schemaBD)

# TABELAS PARA G3
monta_DLL.criaDDL('G3', v_schemaBD)

# TABELAS PARA H1
monta_DLL.criaDDL('H1Aa', v_schemaBD)

# TABELAS PARA H1
monta_DLL.criaDDL('H1Ab', v_schemaBD)

# TABELAS PARA H1
monta_DLL.criaDDL('H1Ac', v_schemaBD)

# TABELAS PARA H3
monta_DLL.criaDDL('H3', v_schemaBD)

# TABELAS PARA H3A
monta_DLL.criaDDL('H3a', v_schemaBD)

# TABELAS PARA H3A
monta_DLL.criaDDL('H3Ba', v_schemaBD)

# TABELAS PARA H3A
monta_DLL.criaDDL('H3Bb', v_schemaBD)

# TABELAS PARA H3A
monta_DLL.criaDDL('H3Bc', v_schemaBD)

# TABELAS PARA H3A
monta_DLL.criaDDL('H3Bd', v_schemaBD)

# TABELAS PARA H3A
monta_DLL.criaDDL('H3Be', v_schemaBD)

# TABELAS PARA H3A
monta_DLL.criaDDL('H3Bf', v_schemaBD)

# TABELAS PARA H3A
monta_DLL.criaDDL('H3Bg', v_schemaBD)

# TABELAS PARA H4
monta_DLL.criaDDL('H4', v_schemaBD)

# TABELAS PARA H8
monta_DLL.criaDDL('H8a', v_schemaBD)

# TABELAS PARA H8
monta_DLL.criaDDL('H8b', v_schemaBD)

# TABELAS PARA H8
monta_DLL.criaDDL('H8c', v_schemaBD)

# TABELAS PARA H8
monta_DLL.criaDDL('H8d', v_schemaBD)

# TABELAS PARA H8
monta_DLL.criaDDL('H8e', v_schemaBD)

# TABELAS PARA H8
monta_DLL.criaDDL('H8f', v_schemaBD)

# TABELAS PARA H9
monta_DLL.criaDDL('H9Aa', v_schemaBD)

# TABELAS PARA H9
monta_DLL.criaDDL('H9Ab', v_schemaBD)

# TABELAS PARA H9
monta_DLL.criaDDL('H9Ac', v_schemaBD)

# TABELAS PARA H9
monta_DLL.criaDDL('H9Ad', v_schemaBD)

# TABELAS PARA H9
monta_DLL.criaDDL('H9Ae', v_schemaBD)

# TABELAS PARA H9
monta_DLL.criaDDL('H9Af', v_schemaBD)

# TABELAS PARA H9
monta_DLL.criaDDL('H9Ag', v_schemaBD)

# TABELAS PARA H10

monta_DLL.criaDDL('H10a', v_schemaBD)

# TABELAS PARA H10
monta_DLL.criaDDL('H10b', v_schemaBD)

# TABELAS PARA H10
monta_DLL.criaDDL('H10c', v_schemaBD)

# TABELAS PARA H10
monta_DLL.criaDDL('H10d', v_schemaBD)

# TABELAS PARA H10
monta_DLL.criaDDL('H10e', v_schemaBD)

# TABELAS PARA H10
monta_DLL.criaDDL('H10f', v_schemaBD)

# TABELAS PARA H10
monta_DLL.criaDDL('H10g', v_schemaBD)


# TABELAS PARA H13

monta_DLL.criaDDL('H13a', v_schemaBD)

# TABELAS PARA H13
monta_DLL.criaDDL('H13b', v_schemaBD)

# TABELAS PARA H13
monta_DLL.criaDDL('H13c', v_schemaBD)

# TABELAS PARA H13
monta_DLL.criaDDL('H13d', v_schemaBD)

# TABELAS PARA H13
monta_DLL.criaDDL('H13e', v_schemaBD)

# TABELAS PARA H13
monta_DLL.criaDDL('H13f', v_schemaBD)

# TABELAS PARA H13
monta_DLL.criaDDL('H13g', v_schemaBD)

# TABELAS PARA H13
monta_DLL.criaDDL('H13h', v_schemaBD)

# TABELAS PARA H13
monta_DLL.criaDDL('H13i', v_schemaBD)


######################
################TABELAS CMA 
###############################################
# %% Cria script DDL das fato das pesquisa CMA Survey 2025 

# Como é o início do scrit o utilizo o "w" para sobrescrever caso exista
with open('../ScriptsBD/CticBr_ScriptDDL.sql', 'a', encoding='utf-8') as f:
    sql = (
        f"\n/* CRIAÇÃO DA ESTRUTURA DO BANCO DE DADOS */\n\n"
        f"CREATE SCHEMA {v_schemaBD} DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;\n"
        f"\n\n/*********  ESTRUTURA DAS TABELAS DA PESQUISA CMA *******/\n"

    )
    f.write(sql)



# DDL das fato das pesquisa CMA Survey 2025
monta_DLL.criaDDL_CMA_GMO(v_schemaBD)




# %% FIM!
