#
### SCRIPT PARA GERAR DDLs DAS TABELAS FATO
#

def criaDDL(p_pesquisa, p_schema):

    
    # CRIA TABELA FATO COM TOTAIS DA VARIÁVEL PESQUISADA
    
    v_schemaBD = p_schema
    v_nomeTabela = ('ft_' + p_pesquisa + '_totais').lower()
    
    # Como Como estou incrementando no final o parâmetro tem se a = append
    with open('../ScriptsBD/CticBr_ScriptDDL.sql', 'a', encoding='utf-8') as f:
        sql = (
            f"\n\n/* TABELA DE TOTAIS DA VARIÁVE PESQUISADA {p_pesquisa} */\n"
            f"CREATE TABLE {v_schemaBD}.{v_nomeTabela} (ano_pesquisa varchar(8) NOT NULL, \n"
            f"contexto varchar(64) NOT NULL, \n"
            f"qtd_resposta_sim int DEFAULT NULL, \n"
            f"PRIMARY KEY (ano_pesquisa), \n"
            f"UNIQUE KEY ano_pesquisa_UNIQUE (ano_pesquisa)) \n"
            f"COMMENT='{p_pesquisa} TOTAIS - EMPRESAS QUE UTILIZARAM PACOTES DE SOFTWARE ERP PARA INTEGRAR OS DADOS E PROCESSOS DE SEUS DEPARTAMENTOS EM UM SISTEMA ÚNICO NOS ÚLTIMOS 12 MESES'; "
        )
        f.write(sql)
    
    # CRIA TABELA FATO POR PORTE
    
    v_schemaBD = p_schema
    v_nomeTabela = ('ft_' + p_pesquisa + '_porte').lower()
    
    # Como Como estou incrementando no final o parâmetro tem se a = append
    with open('../ScriptsBD/CticBr_ScriptDDL.sql', 'a', encoding='utf-8') as f:
        sql = (
            f"\n\n/* TABELA DE PESQUISA {p_pesquisa} - Por porte de empresa */\n"
            f"CREATE TABLE {v_schemaBD}.{v_nomeTabela} (id_{v_nomeTabela} int NOT NULL AUTO_INCREMENT, \n"
            f"ano_pesquisa varchar(8) NOT NULL, \n"
            f"id_porte varchar(4) NOT NULL, \n"
            f"qtd_resposta_sim int DEFAULT NULL, \n"
            f"PRIMARY KEY (id_{v_nomeTabela}), \n"
            f"UNIQUE KEY id_{v_nomeTabela}_UNIQUE (id_{v_nomeTabela})) \n"
            f"COMMENT='{p_pesquisa} PORTE –  EMPRESAS QUE UTILIZARAM PACOTES DE SOFTWARE ERP PARA INTEGRAR OS DADOS E PROCESSOS DE SEUS DEPARTAMENTOS EM UM SISTEMA ÚNICO NOS ÚLTIMOS 12 MESES'; "
        )
        f.write(sql)

    # CRIA TABELA FATO POR MERCADO DE ATUAÇÃO
    sql = ''
 
    v_schemaBD = p_schema
    v_nomeTabela = ('ft_' + p_pesquisa + '_mercado').lower()

    # Como Como estou incrementando no final o parâmetro tem se a = append
    with open('../ScriptsBD/CticBr_ScriptDDL.sql', 'a', encoding='utf-8') as f:
        sql = (
            f"\n\n/* TABELA DE PESQUISA {p_pesquisa} - Por mercado de atuação */\n"
            f"CREATE TABLE {v_schemaBD}.{v_nomeTabela} (id_{v_nomeTabela} int NOT NULL AUTO_INCREMENT, \n"
            f"ano_pesquisa varchar(8) NOT NULL, \n"
            f"id_mercado varchar(4) NOT NULL, \n"
            f"qtd_resposta_sim int DEFAULT NULL, \n"
            f"PRIMARY KEY (id_{v_nomeTabela}), \n"
            f"UNIQUE KEY id_{v_nomeTabela}_UNIQUE (id_{v_nomeTabela})) \n"
            f"COMMENT='{p_pesquisa} MERCADO –  EMPRESAS QUE UTILIZARAM PACOTES DE SOFTWARE ERP PARA INTEGRAR OS DADOS E PROCESSOS DE SEUS DEPARTAMENTOS EM UM SISTEMA ÚNICO NOS ÚLTIMOS 12 MESES'; "
        )
        f.write(sql)

    return


def criaDDLB18(p_pesquisa, p_schema):

    
    # CRIA TABELA FATO COM TOTAIS DA VARIÁVEL PESQUISADA
    
    v_schemaBD = p_schema
    v_nomeTabela = ('ft_' + p_pesquisa + '_totais').lower()
    
    # Como Como estou incrementando no final o parâmetro tem se a = append
    with open('../ScriptsBD/CticBr_ScriptDDL.sql', 'a', encoding='utf-8') as f:
        sql = (
            f"\n\n/* TABELA DE TOTAIS DA VARIÁVE PESQUISADA {p_pesquisa} */\n"
            f"CREATE TABLE {v_schemaBD}.{v_nomeTabela} (ano_pesquisa varchar(8) NOT NULL, \n"
            f"contexto varchar(64) NOT NULL, \n"
            f"qtd_bd int DEFAULT NULL, \n"
            f"qtd_processamento int DEFAULT NULL, \n"
            f"qtd_desenv int DEFAULT NULL, \n"
            f"PRIMARY KEY (ano_pesquisa), \n"
            f"UNIQUE KEY ano_pesquisa_UNIQUE (ano_pesquisa)) \n"
            f"COMMENT='{p_pesquisa} TOTAIS - EMPRESAS QUE UTILIZARAM PACOTES DE SOFTWARE ERP PARA INTEGRAR OS DADOS E PROCESSOS DE SEUS DEPARTAMENTOS EM UM SISTEMA ÚNICO NOS ÚLTIMOS 12 MESES'; "
        )
        f.write(sql)
    
    # CRIA TABELA FATO POR PORTE
    
    v_schemaBD = p_schema
    v_nomeTabela = ('ft_' + p_pesquisa + '_porte').lower()
    
    # Como Como estou incrementando no final o parâmetro tem se a = append
    with open('../ScriptsBD/CticBr_ScriptDDL.sql', 'a', encoding='utf-8') as f:
        sql = (
            f"\n\n/* TABELA DE PESQUISA {p_pesquisa} - Por porte de empresa */\n"
            f"CREATE TABLE {v_schemaBD}.{v_nomeTabela} (id_{v_nomeTabela} int NOT NULL AUTO_INCREMENT, \n"
            f"ano_pesquisa varchar(8) NOT NULL, \n"
            f"id_porte varchar(4) NOT NULL, \n"
            f"qtd_bd int DEFAULT NULL, \n"
            f"qtd_processamento int DEFAULT NULL, \n"
            f"qtd_desenv int DEFAULT NULL, \n"
            f"PRIMARY KEY (id_{v_nomeTabela}), \n"
            f"UNIQUE KEY id_{v_nomeTabela}_UNIQUE (id_{v_nomeTabela})) \n"
            f"COMMENT='{p_pesquisa} PORTE –  EMPRESAS QUE UTILIZARAM PACOTES DE SOFTWARE ERP PARA INTEGRAR OS DADOS E PROCESSOS DE SEUS DEPARTAMENTOS EM UM SISTEMA ÚNICO NOS ÚLTIMOS 12 MESES'; "
        )
        f.write(sql)

    # CRIA TABELA FATO POR MERCADO DE ATUAÇÃO
    sql = ''
 
    v_schemaBD = p_schema
    v_nomeTabela = ('ft_' + p_pesquisa + '_mercado').lower()

    # Como Como estou incrementando no final o parâmetro tem se a = append
    with open('../ScriptsBD/CticBr_ScriptDDL.sql', 'a', encoding='utf-8') as f:
        sql = (
            f"\n\n/* TABELA DE PESQUISA {p_pesquisa} - Por mercado de atuação */\n"
            f"CREATE TABLE {v_schemaBD}.{v_nomeTabela} (id_{v_nomeTabela} int NOT NULL AUTO_INCREMENT, \n"
            f"ano_pesquisa varchar(8) NOT NULL, \n"
            f"id_mercado varchar(4) NOT NULL, \n"
            f"qtd_bd int DEFAULT NULL, \n"
            f"qtd_processamento int DEFAULT NULL, \n"
            f"qtd_desenv int DEFAULT NULL, \n"
            f"PRIMARY KEY (id_{v_nomeTabela}), \n"
            f"UNIQUE KEY id_{v_nomeTabela}_UNIQUE (id_{v_nomeTabela})) \n"
            f"COMMENT='{p_pesquisa} MERCADO –  EMPRESAS QUE UTILIZARAM PACOTES DE SOFTWARE ERP PARA INTEGRAR OS DADOS E PROCESSOS DE SEUS DEPARTAMENTOS EM UM SISTEMA ÚNICO NOS ÚLTIMOS 12 MESES'; "
        )
        f.write(sql)

    return


#
####  CRIA TABELA PRINCIPAL DA PESQUISA CMA ###########################
#
def criaDDL_CMA_GMO (p_schema):
    
    v_schemaBD = p_schema
    
    # Como Como estou incrementando no final o parâmetro tem se a = append
    with open('../ScriptsBD/CMA_ScriptDDL.sql', 'w', encoding='utf-8') as f:
        sql = (
            f"\n\n/* TABELA PRINCIPAL DA PESQUISA CMA */\n"
            f"CREATE TABLE {v_schemaBD}.ft_cma_principal ( \n"
            f"id_principal int NOT NULL AUTO_INCREMENT, \n"
            f"id_original int DEFAULT NULL, \n"
            f"mercado_atuacao varchar(64), \n"
            f"porte_empresa varchar(64), \n"
            f"tem_cmo varchar(16), \n"
            f"area_vinculo varchar(64), \n"
            f"consistencia_engajamento varchar(128), \n"
            f"maturidade_praticas varchar(128), \n"
            f"projetos_com_gmo varchar(16), \n"
            f"maturidade_gmo_pais varchar(32), \n"
            f"UNIQUE KEY id_UNIQUE (id_principal)) \n"
            f"COMMENT='TABELA PRINCIPAL DA PESQUISA CMA'; "
        )
        f.write(sql)
    
    # Como Como estou incrementando no final o parâmetro tem se a = append
    with open('../ScriptsBD/CMA_ScriptDDL.sql', 'a', encoding='utf-8') as f:
        sql = (
            f"\n\n/* TABELA TIPOS DE MUDANÇA IMPLEMNTADAS DA PESQUISA CMA */\n"
            f"CREATE TABLE {v_schemaBD}.ft_cma_tipoMudanca ( \n"
            f"id_tipomudanca int NOT NULL AUTO_INCREMENT, \n"
            f"ds_tipomudanca varchar(128), \n"
            f"UNIQUE KEY id_UNIQUE (id_tipomudanca)) \n"
            f"COMMENT='Que tipos de mudanças você tipicamente gerencia?'; "
        )
        f.write(sql)
    
    
    # Como Como estou incrementando no final o parâmetro tem se a = append
    with open('../ScriptsBD/CMA_ScriptDDL.sql', 'a', encoding='utf-8') as f:
        sql = (
            f"\n\n/* TABELA MAIORES DESAFIOS DA TD DA PESQUISA CMA */\n"
            f"CREATE TABLE {v_schemaBD}.ft_cma_maiorDesafioTD ( \n"
            f"id_maiorDesafioTD int NOT NULL AUTO_INCREMENT, \n"
            f"ds_maiordesafioTD varchar(128), \n"
            f"UNIQUE KEY id_UNIQUE (id_maiorDesafioTD)) \n"
            f"COMMENT='Qual é o maior desafio para a transformação organizacional da sua organização nos próximos 2 anos?'; "
        )
        f.write(sql)
    
    
    # Como Como estou incrementando no final o parâmetro tem se a = append
    with open('../ScriptsBD/CMA_ScriptDDL.sql', 'a', encoding='utf-8') as f:
        sql = (
            f"\n\n/* TABELA ENGAJAMENTO TÍPICO DE STAKEHOLDERS DA PESQUISA CMA */\n"
            f"CREATE TABLE {v_schemaBD}.ft_cma_engajamentoTipico ( \n"
            f"id_engajamentoTipico int NOT NULL AUTO_INCREMENT, \n"
            f"ds_engajamentotipico varchar(128), \n"
            f"UNIQUE KEY id_UNIQUE (id_engajamentoTipico)) \n"
            f"COMMENT='Qual é o maior desafio para a transformação organizacional da sua organização nos próximos 2 anos?'; "
        )
        f.write(sql)
    
    
    # Como Como estou incrementando no final o parâmetro tem se a = append
    with open('../ScriptsBD/CMA_ScriptDDL.sql', 'a', encoding='utf-8') as f:
        sql = (
            f"\n\n/* TABELA e MAIoRES DESAFIOS PARA A GMO DA PESQUISA CMA */\n"
            f"CREATE TABLE {v_schemaBD}.ft_cma_3DesafiosGMO ( \n"
            f"id_3DesafiosGMO int NOT NULL AUTO_INCREMENT, \n"
            f"ds_3DesafiosGMO varchar(128), \n"
            f"UNIQUE KEY id_UNIQUE (id_3DesafiosGMO)) \n"
            f"COMMENT='Qual é o maior desafio para a transformação organizacional da sua organização nos próximos 2 anos?'; "
        )
        f.write(sql)
    
    
    return