

/* TABELA PRINCIPAL DA PESQUISA CMA */
CREATE TABLE usp_dsa.ft_cma_principal ( 
id_principal int NOT NULL AUTO_INCREMENT, 
id_original int DEFAULT NULL, 
mercado_atuacao varchar(64), 
porte_empresa varchar(64), 
tem_cmo varchar(16), 
area_vinculo varchar(64), 
consistencia_engajamento varchar(128), 
maturidade_praticas varchar(128), 
projetos_com_gmo varchar(16), 
maturidade_gmo_pais varchar(32), 
UNIQUE KEY id_UNIQUE (id_principal)) 
COMMENT='TABELA PRINCIPAL DA PESQUISA CMA'; 

/* TABELA TIPOS DE MUDANÇA IMPLEMNTADAS DA PESQUISA CMA */
CREATE TABLE usp_dsa.ft_cma_tipoMudanca ( 
id_tipomudanca int NOT NULL AUTO_INCREMENT, 
ds_tipomudanca varchar(128), 
UNIQUE KEY id_UNIQUE (id_tipomudanca)) 
COMMENT='Que tipos de mudanças você tipicamente gerencia?'; 

/* TABELA MAIORES DESAFIOS DA TD DA PESQUISA CMA */
CREATE TABLE usp_dsa.ft_cma_maiorDesafioTD ( 
id_maiorDesafioTD int NOT NULL AUTO_INCREMENT, 
ds_maiordesafioTD varchar(128), 
UNIQUE KEY id_UNIQUE (id_maiorDesafioTD)) 
COMMENT='Qual é o maior desafio para a transformação organizacional da sua organização nos próximos 2 anos?'; 

/* TABELA ENGAJAMENTO TÍPICO DE STAKEHOLDERS DA PESQUISA CMA */
CREATE TABLE usp_dsa.ft_cma_engajamentoTipico ( 
id_engajamentoTipico int NOT NULL AUTO_INCREMENT, 
ds_engajamentotipico varchar(128), 
UNIQUE KEY id_UNIQUE (id_engajamentoTipico)) 
COMMENT='Qual é o maior desafio para a transformação organizacional da sua organização nos próximos 2 anos?'; 

/* TABELA e MAIoRES DESAFIOS PARA A GMO DA PESQUISA CMA */
CREATE TABLE usp_dsa.ft_cma_3DesafiosGMO ( 
id_3DesafiosGMO int NOT NULL AUTO_INCREMENT, 
ds_3DesafiosGMO varchar(128), 
UNIQUE KEY id_UNIQUE (id_3DesafiosGMO)) 
COMMENT='Qual é o maior desafio para a transformação organizacional da sua organização nos próximos 2 anos?'; 