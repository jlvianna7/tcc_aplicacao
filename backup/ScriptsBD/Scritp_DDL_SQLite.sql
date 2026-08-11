
/*********  ESTRUTURA DAS TABELAS DE DOMÍNIO *******/


/* TABELA DE DOMÍNIO RESUMO DA PESQUISA */
CREATE TABLE dm_resumo_pesquisa (
ano_pesquisa text(8) NOT NULL, 
amostra_planejada INTEGER DEFAULT NULL, 
empresas_respondentes INTEGER NOT NULL, 
link_publicacao text(1024), 
PRIMARY KEY (ano_pesquisa)
); 

/* TABELA DE DOMÍNIO RESPOSTAS SIMPLES */
CREATE TABLE dm_resposta_sn (
id_resposta_sn INTEGER NOT NULL, 
ds_resposta_sn text(16) NOT NULL, 
PRIMARY KEY (id_resposta_sn)
);

/* TABELA DE DOMÍNIO DE PORTE DE EMPRESA PESQUISADA */
CREATE TABLE dm_porte_empresa (
id_porte_empresa text(4) NOT NULL, 
ds_porte_empresa text(32) NOT NULL, 
PRIMARY KEY (id_porte_empresa)
); 

/* TABELA DE DOMÍNIO DE MERCADO DE ATUAÇÃO EMPRESA PESQUISADA */
CREATE TABLE dm_mercado_atuacao (
id_merc_atuacao text(4) NOT NULL, 
ds_merc_atuacao text(256) DEFAULT NULL, 
cod_ibge text(1) DEFAULT NULL, 
PRIMARY KEY (id_merc_atuacao)
); 

/*********  ESTRUTURA DAS TABELAS FATO *******/


/* TABELA DE TOTAIS DA VARIÁVE PESQUISADA */
CREATE TABLE ft_ceticbr_totais (
id_totais INTEGER NOT NULL , 
ano_pesquisa_totais text(8) NOT NULL,
cd_variavel_totais text(8) NOT NULL, 
contexto_totais text(64) NOT NULL, 
qtd_resposta_sim_totais INTEGER DEFAULT NULL, 
PRIMARY KEY (id_totais AUTOINCREMENT)
);  


/* TABELA DE PESQUISA - Por porte de empresa */
CREATE TABLE ft_ceticbr_porte (
id_ceticbr_porte INTEGER NOT NULL, 
ano_pesquisa_porte text(8) NOT NULL, 
cd_variavel_porte text(8) NOT NULL, 
id_dm_porte text(4) NOT NULL, 
qtd_resposta_sim_porte INTEGER DEFAULT NULL, 
PRIMARY KEY (id_ceticbr_porte AUTOINCREMENT) 
); 

/* TABELA DE PESQUISA - Por mercado de atuação */
CREATE TABLE ft_ceticbr_mercado (
id_ceticbr_mercado INTEGER NOT NULL, 
ano_pesquisa_mercado text(8) NOT NULL, 
cd_variavel_porte text(8) NOT NULL, 
id_dm_mercado text(4) NOT NULL, 
qtd_resposta_sim INTEGER DEFAULT NULL, 
PRIMARY KEY (id_ceticbr_mercado AUTOINCREMENT)
); 
