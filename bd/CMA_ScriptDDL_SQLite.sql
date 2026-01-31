

/* TABELA PRINCIPAL DA PESQUISA CMA */
CREATE TABLE ft_cma_principal ( 
id_principal INTEGER NOT NULL , 
id_original INTEGER DEFAULT NULL, 
mercado_atuacao varchar(64), 
porte_empresa varchar(64), 
tem_cmo varchar(16), 
area_vinculo varchar(64), 
consistencia_engajamento varchar(128), 
maturidade_praticas varchar(128), 
projetos_com_gmo varchar(16), 
maturidade_gmo_pais varchar(32), 
PRIMARY KEY (id_principal AUTOINCREMENT)
);


/* TABELA TIPOS DE MUDANÇA IMPLEMNTADAS DA PESQUISA CMA */
CREATE TABLE ft_cma_tipoMudanca ( 
id_tipomudanca INTEGER NOT NULL , 
ds_tipomudanca varchar(128), 
PRIMARY KEY (id_tipomudanca AUTOINCREMENT)
); 


/* TABELA MAIORES DESAFIOS DA TD DA PESQUISA CMA */
CREATE TABLE ft_cma_maiorDesafioTD ( 
id_maiorDesafioTD INTEGER NOT NULL , 
ds_maiordesafioTD varchar(128), 
PRIMARY KEY (id_maiorDesafioTD AUTOINCREMENT)
); 

/* TABELA ENGAJAMENTO TÍPICO DE STAKEHOLDERS DA PESQUISA CMA */
CREATE TABLE ft_cma_engajamentoTipico ( 
id_engajamentoTipico INTEGER NOT NULL , 
ds_engajamentotipico varchar(128), 
PRIMARY KEY (id_engajamentoTipico AUTOINCREMENT)
);


/* TABELA e MAIoRES DESAFIOS PARA A GMO DA PESQUISA CMA */
CREATE TABLE ft_cma_3DesafiosGMO ( 
id_3DesafiosGMO INTEGER NOT NULL , 
ds_3DesafiosGMO varchar(128), 
PRIMARY KEY (id_3DesafiosGMO AUTOINCREMENT)
); 



