CREATE DATABASE `dsa_tcc` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_bin */ /*!80016 DEFAULT ENCRYPTION='N' */;



CREATE TABLE `dsa_tcc`.`resposta_sn` (
  `id_resposta_sn` INT NOT NULL,
  `ds_resposta_sn` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`id_resposta_sn`),
  UNIQUE INDEX `id_resposta_sn_UNIQUE` (`id_resposta_sn` ASC) VISIBLE)
COMMENT = 'Domínio para respostas simples sim ou não e mais algumas opções';

/* TABELA DE DOMÍNIO PARA RESPOSTAS SIMPLES */

INSERT INTO dsa_tcc.resposta_sn (id_resposta_sn, ds_resposta_sn) VALUES (0 , 'Não');
INSERT INTO dsa_tcc.resposta_sn (id_resposta_sn, ds_resposta_sn) VALUES (1 , 'Sim');
INSERT INTO dsa_tcc.resposta_sn (id_resposta_sn, ds_resposta_sn) VALUES (97 , 'Não sabe');
INSERT INTO dsa_tcc.resposta_sn (id_resposta_sn, ds_resposta_sn) VALUES (98 , 'Não respondeu');
INSERT INTO dsa_tcc.resposta_sn (id_resposta_sn, ds_resposta_sn) VALUES (99 , 'Não se aplica');
COMMIT;


/* TABELA DE DOMÍNIO DE ATIVIDADE OU MERCADO DE ATUAÇÃO DA EMPRESA */

CREATE TABLE `mercado_atuacao` (
  `id_merc_atuacao` int NOT NULL,
  `ds_merc_atuacao` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id_merc_atuacao`),
  UNIQUE KEY `id_merc_atuacao_UNIQUE` (`id_merc_atuacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='Marcado de atuação segundo pesquisa CeticBr';


INSERT INTO dsa_tcc.mercado_atuacao (id_merc_atuacao, ds_merc_atuacao) VALUES (1, 'Indústria de Transformação');
INSERT INTO dsa_tcc.mercado_atuacao (id_merc_atuacao, ds_merc_atuacao) VALUES (2, 'Construção');
INSERT INTO dsa_tcc.mercado_atuacao (id_merc_atuacao, ds_merc_atuacao) VALUES (3, 'Comércio; reparação de veículos automotores, objetos pessoais e domésticos');
INSERT INTO dsa_tcc.mercado_atuacao (id_merc_atuacao, ds_merc_atuacao) VALUES (4, 'Transporte, Armazenagem e Correio');
INSERT INTO dsa_tcc.mercado_atuacao (id_merc_atuacao, ds_merc_atuacao) VALUES (5, 'Alojamento e Alimentação');
INSERT INTO dsa_tcc.mercado_atuacao (id_merc_atuacao, ds_merc_atuacao) VALUES (6, 'Informação e Comunicação');
INSERT INTO dsa_tcc.mercado_atuacao (id_merc_atuacao, ds_merc_atuacao) VALUES (7, 'Atividades imobiliárias, Atividades profissionais, científicas e técnicas, Atividades administrativas e serviços complementares');
INSERT INTO dsa_tcc.mercado_atuacao (id_merc_atuacao, ds_merc_atuacao) VALUES (8, 'Artes, cultura, esportes e recreação, Outras atividades de serviços');
COMMIT;

/* TABELA DE DOMÍNIO DE PORTE DE EMPRESA PESQUISADA */

CREATE TABLE `dsa_tcc`.`porte_empresa` (
  `id_porte_empresa` INT NOT NULL,
  `ds_porte_empresa` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`id_porte_empresa`),
  UNIQUE INDEX `id_porte_empresa_UNIQUE` (`id_porte_empresa` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Tamanho da empresa em pesquisada, em quantidade de funcionários.';

INSERT INTO dsa_tcc.porte_empresa (id_porte_empresa, ds_porte_empresa) VALUES (1, '10 a 19 pessoas ocupadas');
INSERT INTO dsa_tcc.porte_empresa (id_porte_empresa, ds_porte_empresa) VALUES (2, '20 a 49 pessoas ocupadas');
INSERT INTO dsa_tcc.porte_empresa (id_porte_empresa, ds_porte_empresa) VALUES (3, '50 a 249 pessoas ocupadas');
INSERT INTO dsa_tcc.porte_empresa (id_porte_empresa, ds_porte_empresa) VALUES (4, '250  pessoas ocupadas ou mais'):
COMMIT;

/* TABELA FATO DE AVALIAÇÃO DO USO DE ERPs */