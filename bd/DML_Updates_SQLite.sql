

/*****  AJUSTE NO CONTECUDO DAS TABELA DE H3B  *******/

UPDATE ft_ceticbr_totais SET contexto = 'Vigilância, segurança ou tarefas de inspeção' 
where ano_pesquisa > '2000' and cd_variavel = 'h3ba';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Transporte de pessoas ou mercadorias' 
where ano_pesquisa > '2000' and cd_variavel = 'h3bb';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Limpeza ou eliminação de resíduos' 
where ano_pesquisa > '2000' and cd_variavel = 'h3bc';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Gerenciamento de estoque' 
where ano_pesquisa > '2000' and cd_variavel = 'h3bd';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Trabalhos de montagem' 
where ano_pesquisa > '2000' and cd_variavel = 'h3be';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Atendimento ao cliente' 
where ano_pesquisa > '2000' and cd_variavel = 'h3bf';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Construção e reparos' 
where ano_pesquisa > '2000' and cd_variavel = 'h3bg';
COMMIT;


/*****  AJUSTE NO CONTECUDO DAS TABELA DE B18  *******/


UPDATE ft_ceticbr_totais SET contexto = 'Software de escritório' 
where ano_pesquisa > '2000' and cd_variavel = 'b18a';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Armazenamento e/ou Banco de Dados' 
where ano_pesquisa > '2000' and cd_variavel = 'b18b';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Capacidade de processamento' 
where ano_pesquisa > '2000' and cd_variavel = 'b18c';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Ambiente de desenvolvimento' 
where ano_pesquisa > '2000' and cd_variavel = 'b18d';
COMMIT;


/*****  AJUSTE NO CONTECUDO DAS TABELA DE H1A  *******/

UPDATE ft_ceticbr_totais SET contexto = 'Dados próprios da empresa' 
where ano_pesquisa > '2000' and cd_variavel = 'h1aa';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Dados de geolocalização de dispositivos móveis' 
where ano_pesquisa > '2000' and cd_variavel = 'h1ab';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Dados de mídidas sociais' 
where ano_pesquisa > '2000' and cd_variavel = 'h1ac';
COMMIT;


/*****  AJUSTE NO CONTECUDO DAS TABELA DE H8  *******/

UPDATE ft_ceticbr_totais SET contexto = 'Gerenciamentos de consumos, medidores inteligentes' 
where ano_pesquisa > '2000' and cd_variavel = 'h8a';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Dispositivos de segurança' 
where ano_pesquisa > '2000' and cd_variavel = 'h8b';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Automatização de processo de produção' 
where ano_pesquisa > '2000' and cd_variavel = 'h8c';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Gestão de logística' 
where ano_pesquisa > '2000' and cd_variavel = 'h8d';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Monitoramento e manutenção de equipamentos' 
where ano_pesquisa > '2000' and cd_variavel = 'h8e';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Atendimento ao cliente' 
where ano_pesquisa > '2000' and cd_variavel = 'h8f';
COMMIT;


/*****  AJUSTE NO CONTECUDO DAS TABELA DE H9A  *******/

UPDATE ft_ceticbr_totais SET contexto = 'Análise de textos' 
where ano_pesquisa > '2000' and cd_variavel = 'h9aa';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Reconhecimento de fala' 
where ano_pesquisa > '2000' and cd_variavel = 'h9ab';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Geração de linguagem natural' 
where ano_pesquisa > '2000' and cd_variavel = 'h9ac';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Processamento de imagens' 
where ano_pesquisa > '2000' and cd_variavel = 'h9ad';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Machine learning' 
where ano_pesquisa > '2000' and cd_variavel = 'h9ae';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Automatização de processos' 
where ano_pesquisa > '2000' and cd_variavel = 'h9af';
COMMIT;


UPDATE ft_ceticbr_totais SET contexto = 'Máquinas e veículos autônomos' 
where ano_pesquisa > '2000' and cd_variavel = 'h9ag';
COMMIT;


/*****  AJUSTE NO CONTECUDO DAS TABELA DE H10  *******/

UPDATE ft_ceticbr_totais SET contexto = 'Marketing ou vendas' 
where ano_pesquisa > '2000' and cd_variavel = 'h10a';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Processos de produção' 
where ano_pesquisa > '2000' and cd_variavel = 'h10b';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Porcessos administrativos' 
where ano_pesquisa > '2000' and cd_variavel = 'h10c';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Gestão de empresas' 
where ano_pesquisa > '2000' and cd_variavel = 'h10d';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Logística' 
where ano_pesquisa > '2000' and cd_variavel = 'h10e';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Segurança digital' 
where ano_pesquisa > '2000' and cd_variavel = 'h10f';
COMMIT;

UPDATE ft_ceticbr_totais SET contexto = 'Recursos humanos' 
where ano_pesquisa > '2000' and cd_variavel = 'h10g';
COMMIT;



/*****  AJUSTE NO CONTECUDO DAS TABELA DE h13  *******/

UPDATE ft_ceticbr_totais SET contexto = 'Custos' 
where cd_variavel = 'h13a';

UPDATE ft_ceticbr_totais SET contexto = 'Por falta de pessoas capacitadas' 
where cd_variavel = 'h13b';

UPDATE ft_ceticbr_totais SET contexto = 'Limitação tecnológica' 
where cd_variavel = 'h13c';

UPDATE ft_ceticbr_totais SET contexto = 'Dificuldade com os dados' 
where cd_variavel = 'h13d';

UPDATE ft_ceticbr_totais SET contexto = 'Preocupação com LGPD' 
where cd_variavel = 'h13e';

UPDATE ft_ceticbr_totais SET contexto = 'Preocupação com consequências legais' 
where cd_variavel = 'h13f';

UPDATE ft_ceticbr_totais SET contexto = 'Questões éticas' 
where cd_variavel = 'h13g';

UPDATE ft_ceticbr_totais SET contexto = 'Não enxergam utilidade' 
where cd_variavel = 'h13h';

UPDATE ft_ceticbr_totais SET contexto = 'Falta de conhecimento técnico' 
where cd_variavel = 'h13i';
COMMIT;
