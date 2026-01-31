
/* ---- SCRIPT DE CARGA DAS TABELAS DO BANCO DE DADOS ---- */


/* TABELA DE DOMÍNIO PARA RESPOSTAS SIMPLES */
INSERT INTO dm_resposta_sn (id_resposta_sn, ds_resposta_sn) VALUES (0 , 'Não'); 
INSERT INTO dm_resposta_sn (id_resposta_sn, ds_resposta_sn) VALUES (1 , 'Sim'); 
INSERT INTO dm_resposta_sn (id_resposta_sn, ds_resposta_sn) VALUES (97 , 'Não sabe'); 
INSERT INTO dm_resposta_sn (id_resposta_sn, ds_resposta_sn) VALUES (98 , 'Não respondeu'); 
INSERT INTO dm_resposta_sn (id_resposta_sn, ds_resposta_sn) VALUES (99 , 'Não se aplica');
COMMIT;


/* TABELA DE DOMÍNIO COM RESUMO DAS PESQUISA */
INSERT INTO dm_resumo_pesquisa (ano_pesquisa, amostra_planejada, empresas_respondentes, link_publicacao) VALUES ('2014', 7000, 7198, 'https://cetic.br/media/docs/publicacoes/2/TIC_Empresas_2014_livro_eletronico.pdf'); 
INSERT INTO dm_resumo_pesquisa (ano_pesquisa, amostra_planejada, empresas_respondentes, link_publicacao) VALUES ('2015', 7000, 7076, 'https://cetic.br/media/docs/publicacoes/2/TIC_Empresas_2015_livro_eletronico.pdf'); 
INSERT INTO dm_resumo_pesquisa (ano_pesquisa, amostra_planejada, empresas_respondentes, link_publicacao) VALUES ('2017', 7000, 7062, 'http://cetic.br/media/docs/publicacoes/2/10522920190604-TIC-EMPRESAS-2017-ed-rev.pdf'); 
INSERT INTO dm_resumo_pesquisa (ano_pesquisa, amostra_planejada, empresas_respondentes, link_publicacao) VALUES ('2019', 7000, 7019, 'https://cetic.br/media/docs/publicacoes/2/20200707094721/tic_empresas_2019_livro_eletronico.pdf'); 
INSERT INTO dm_resumo_pesquisa (ano_pesquisa, amostra_planejada, empresas_respondentes, link_publicacao) VALUES ('2021', 7000, 4064, 'https://cetic.br/media/docs/publicacoes/2/20221121122540/tic_empresas_2021_livro_eletronico.pdf'); 
INSERT INTO dm_resumo_pesquisa (ano_pesquisa, amostra_planejada, empresas_respondentes, link_publicacao) VALUES ('2023', 4500, 4447, 'https://cetic.br/media/docs/publicacoes/2/20241104103155/tic_empresas_2023_livro_eletronico.pdf'); 
INSERT INTO dm_resumo_pesquisa (ano_pesquisa, amostra_planejada, empresas_respondentes, link_publicacao) VALUES ('2024', 4500, 4641, 'https://cetic.br/media/docs/publicacoes/2/20250512122204/tic_empresas_2024_livro_eletronico.pdf'); 
COMMIT;


/* TABELA DE DOMÍNIO PARA PORTE DE EMPRESA */
INSERT INTO dm_porte_empresa (id_porte_empresa, ds_porte_empresa) VALUES ('2', '10 a 49 pessoas ocupadas'); 
INSERT INTO dm_porte_empresa (id_porte_empresa, ds_porte_empresa) VALUES ('3', '50 a 249 pessoas ocupadas'); 
INSERT INTO dm_porte_empresa (id_porte_empresa, ds_porte_empresa) VALUES ('4', '250  pessoas ocupadas ou mais');
COMMIT;


/* TABELA DE DOMÍNIO PARA PORTE DE EMPRESA */
INSERT INTO dm_porte_empresa (id_porte_empresa, ds_porte_empresa) VALUES ('2', '10 a 49 pessoas ocupadas'); 
INSERT INTO dm_porte_empresa (id_porte_empresa, ds_porte_empresa) VALUES ('3', '50 a 249 pessoas ocupadas'); 
INSERT INTO dm_porte_empresa (id_porte_empresa, ds_porte_empresa) VALUES ('4', '250  pessoas ocupadas ou mais');
COMMIT;


/* TABELA DE DOMÍNIO PARA MERCADO DE ATUAÇÃO */
INSERT INTO dm_mercado_atuacao (id_merc_atuacao, ds_merc_atuacao, cod_ibge) VALUES ('1', 'Indústria de Transformação','C'); 
INSERT INTO dm_mercado_atuacao (id_merc_atuacao, ds_merc_atuacao, cod_ibge) VALUES ('2', 'Construção','F'); 
INSERT INTO dm_mercado_atuacao (id_merc_atuacao, ds_merc_atuacao, cod_ibge) VALUES ('3', 'Comércio; reparação de veículos automotores, objetos pessoais e domésticos','G'); 
INSERT INTO dm_mercado_atuacao (id_merc_atuacao, ds_merc_atuacao, cod_ibge) VALUES ('4', 'Transporte, Armazenagem e Correio','H');
INSERT INTO dm_mercado_atuacao (id_merc_atuacao, ds_merc_atuacao, cod_ibge) VALUES ('5', 'Alojamento e Alimentação','I'); 
INSERT INTO dm_mercado_atuacao (id_merc_atuacao, ds_merc_atuacao, cod_ibge) VALUES ('6', 'Informação e Comunicação','J'); 
INSERT INTO dm_mercado_atuacao (id_merc_atuacao, ds_merc_atuacao, cod_ibge) VALUES ('7', 'Atividades imobiliárias, Atividades profissionais, científicas e técnicas, Atividades administrativas e serviços complementares','L,M,N'); 
INSERT INTO dm_mercado_atuacao (id_merc_atuacao, ds_merc_atuacao, cod_ibge) VALUES ('8', 'Artes, cultura, esportes e recreação, Outras atividades de serviços','R,S');
COMMIT;

