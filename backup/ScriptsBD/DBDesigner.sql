CREATE TABLE dm_resposta_sn (
  id_resposta_sn INTEGER  NOT NULL AUTO_INCREMENT,
  ds_resposta_sn VARCHAR(16) NOT NULL,
  PRIMARY KEY(id_resposta_sn)
);

CREATE TABLE dm_porte_empresa (
  id_porte_empresa INTEGER  NOT NULL AUTO_INCREMENT,
  dm_porte_empresa VARCHAR(32) NOT NULL,
  PRIMARY KEY(id_porte_empresa)
);

CREATE TABLE dm_mercado_atuacao (
  id_mercado INTEGER  NOT NULL AUTO_INCREMENT,
  ds_merc_atuacao VARCHAR(256) NULL,
  PRIMARY KEY(id_mercado)
);

CREATE TABLE ft_g2_porte (
  id_ft_g2_porte INTEGER  NOT NULL AUTO_INCREMENT,
  dm_porte_empresa_id_porte_empresa INTEGER  NOT NULL,
  ano_pesquisa VARCHAR(8) NULL,
  qtd_resposta_sim INTEGER  NULL,
  qtd_resposta_nao INTEGER  NULL,
  qtd_resposta_naosabe INTEGER  NULL,
  qtd_resposta_naorespondeu INTEGER  NULL,
  PRIMARY KEY(id_ft_g2_porte),
  INDEX ft_g_porte_FKIndex1(dm_porte_empresa_id_porte_empresa),
  FOREIGN KEY(dm_porte_empresa_id_porte_empresa)
    REFERENCES dm_porte_empresa(id_porte_empresa)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE ft_g2_mercado (
  id_ft_g2_mercado INTEGER  NOT NULL AUTO_INCREMENT,
  dm_mercado_atuacao_id_mercado INTEGER  NOT NULL,
  ano_pesquisa VARCHAR(8) NULL,
  qtd_resposta_sim INTEGER  NULL,
  qtd_resposta_nao INTEGER  NULL,
  qtd_resposta_naosabe INTEGER  NULL,
  qtd_resposta_naorespondeu INTEGER  NULL,
  PRIMARY KEY(id_ft_g2_mercado),
  INDEX ft_g2_mercado_FKIndex1(dm_mercado_atuacao_id_mercado),
  FOREIGN KEY(dm_mercado_atuacao_id_mercado)
    REFERENCES dm_mercado_atuacao(id_mercado)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);


