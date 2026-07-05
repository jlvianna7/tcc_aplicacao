# Ferramenta ACS interativa — Análise de Correspondência Simples

Aplicação **Streamlit** para Análise de Correspondência Simples (ACS /
*Correspondence Analysis*) de tabelas de contingência. Calcula totais, perfis,
resíduos padronizados, autovalores, inércias, coordenadas principais,
contribuições e cos², e gera um **biplot interativo (Plotly)** com resumo
explicativo em português do Brasil.

## Requisitos

- Python 3.9+
- Pacotes em `requirements.txt` (Streamlit, pandas, numpy, plotly, openpyxl, scipy)

## Instalação e execução

```bash
cd acs-tool
python -m pip install -r requirements.txt
streamlit run app.py
```

A aplicação abre no navegador (por padrão em `http://localhost:8501`).

## Como usar

1. Na barra lateral, escolha a fonte dos dados:
   - **Exemplo** — conjunto clássico de Greenacre (cargo × hábito de fumar);
   - **Enviar arquivo (CSV/Excel)** — `.csv`, `.xlsx` ou `.xls`;
   - **Colar tabela** — cole de uma planilha (tab, vírgula ou ponto e vírgula).
2. A tabela deve ter **nomes de linha na primeira coluna**, **nomes de coluna
   no cabeçalho** e **frequências não negativas** nas demais células.
3. A análise roda automaticamente. Navegue pelas abas:
   - **Biplot** — mapa simétrico interativo, com seletor de Dimensão X/Y,
     opção linhas/colunas/ambos, rótulos, dimensionamento por contribuição e
     hover detalhado (massa, contribuição, cos², qualidade no plano);
   - **Resumo** — inércia por dimensão, interpretação dos eixos, pontos de
     maior contribuição e avisos sobre dimensões de baixa inércia;
   - **Inércia & autovalores**, **Coordenadas/contrib./cos²**,
     **Perfis & totais**, **Resíduos** — tabelas com download em CSV;
   - **Instruções & método** — guia de uso e notas metodológicas.

## Arquivos

| Arquivo | Descrição |
|---|---|
| `app.py` | Interface Streamlit (entrada de dados, biplot, resumo, tabelas, downloads). |
| `ca_core.py` | Núcleo de cálculo da ACS (validação + SVD) e tabela de exemplo. |
| `requirements.txt` | Dependências. |
| `exemplo_contingencia.csv` / `.xlsx` | Tabela de exemplo para testar o upload. |

## Testes rápidos

Validar o núcleo de cálculo (imprime inércias e coordenadas):

```bash
python ca_core.py
```

Verificação automatizada da execução (sem abrir navegador):

```bash
python test_smoke.py
```

## Decisões técnicas

- **Cálculo sem dependência de ML.** A ACS é feita por SVD da matriz de resíduos
  padronizados de Pearson usando apenas `numpy` — resultados conferidos com o
  conjunto clássico de Greenacre (inércia total 0,0852; Dim 1 = 87,8%,
  Dim 2 = 11,8%). `scipy`/`sklearn` ficam opcionais.
- **Mapa simétrico** para o biplot (coordenadas principais de linhas e colunas),
  padrão na literatura de ACS.
- **Eixos com proporção 1:1** no biplot para preservar distâncias.
- **CSV pt-BR**: downloads usam separador `;` e decimal `,` (compatível com Excel
  em português), codificação UTF-8 com BOM.

## Limitações

- ACS é exploratória/descritiva; o número de dimensões não triviais é
  `min(linhas-1, colunas-1)`.
- Distâncias linha–coluna no mapa simétrico devem ser lidas com cautela.
- O qui-quadrado é informativo e pressupõe frequências esperadas suficientes.
- Não trata pontos suplementares nem análise de correspondência múltipla (MCA).
