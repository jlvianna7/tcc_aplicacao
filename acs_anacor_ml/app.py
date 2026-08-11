"""
app.py — Ferramenta interativa de Análise de Correspondência Simples (ACS)
==========================================================================
Aplicação Streamlit para analisar tabelas de contingência via Análise de
Correspondência Simples (Correspondence Analysis).

Executar localmente:
    streamlit run app.py

Dependências: streamlit, pandas, numpy, plotly, openpyxl (Excel), scipy (opcional).
"""

from __future__ import annotations

import io
from textwrap import dedent

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import prince
import plotly.graph_objects as go
import streamlit as st

from ca_core import CAError, CAResult, example_table, run_ca

from acs_anacor_ml.ca_core import CAError, CAResult, example_table, run_ca


# --------------------------------------------------------------------------- #
# Configuração da página e estilo
# --------------------------------------------------------------------------- #
st.set_page_config(
    page_title="Análise de Correspondência Simples (ACS)",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

CUSTOM_CSS = """
<style>
    .block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1400px; }
    h1, h2, h3 { letter-spacing: -0.01em; }
    .metric-card {
        background: #f7f8fa; border: 1px solid #e6e8eb; border-radius: 12px;
        padding: 16px 18px; height: 100%;
    }
    .metric-card .label { font-size: 0.78rem; color: #5b6470; text-transform: uppercase; letter-spacing: 0.04em; }
    .metric-card .value { font-size: 1.55rem; font-weight: 650; color: #11181c; margin-top: 2px; }
    .small-note { color: #5b6470; font-size: 0.85rem; }
    div[data-testid="stDataFrame"] { border-radius: 10px; }
    .stTabs [data-baseweb="tab-list"] { gap: 4px; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# --------------------------------------------------------------------------- #
# Funções utilitárias
# --------------------------------------------------------------------------- #
def df_to_csv_bytes(df: pd.DataFrame, index_label: str = "") -> bytes:
    buf = io.StringIO()
    out = df.copy()
    out.index.name = index_label or out.index.name or ""
    out.to_csv(buf, sep=";", decimal=",", float_format="%.6f")
    return buf.getvalue().encode("utf-8-sig")


def metric_card(label: str, value: str) -> str:
    return f'<div class="metric-card"><div class="label">{label}</div><div class="value">{value}</div></div>'


def parse_pasted_table(text: str) -> pd.DataFrame:
    """Lê uma tabela colada (TSV/CSV). Primeira coluna = nomes de linha."""
    text = text.strip("\n")
    if not text.strip():
        raise CAError("Nenhum texto foi colado.")
    # Detecta separador: tab tem prioridade (copiar/colar de planilha)
    sep = "\t" if "\t" in text else (";" if ";" in text else ",")
    try:
        df = pd.read_csv(io.StringIO(text), sep=sep, index_col=0, engine="python")
    except Exception as exc:  # noqa: BLE001
        raise CAError(f"Não foi possível interpretar o texto colado: {exc}")
    return df


def read_uploaded(file) -> pd.DataFrame:
    name = file.name.lower()
    if name.endswith((".xlsx", ".xls")):
        return pd.read_excel(file, index_col=0)
    # CSV: tentar detectar separador
    raw = file.getvalue().decode("utf-8-sig", errors="replace")
    sep = ";" if raw.count(";") > raw.count(",") else ","
    return pd.read_csv(io.StringIO(raw), sep=sep, index_col=0)

print(pd.DataFrame)


# --------------------------------------------------------------------------- #
# Cabeçalho
# --------------------------------------------------------------------------- #
st.title("Análise de Correspondência Simples (ACS)")
st.markdown(
    '<p class="small-note">Explore a associação entre as categorias de duas '
    "variáveis qualitativas a partir de uma tabela de contingência. "
    "A ferramenta calcula automaticamente perfis, inércias, coordenadas, "
    "contribuições e cos², e gera um biplot interativo.</p>",
    unsafe_allow_html=True,
)


# --------------------------------------------------------------------------- #
# Barra lateral — entrada de dados
# --------------------------------------------------------------------------- #
with st.sidebar:
    st.header("1. Dados de entrada")
    source = st.radio(
        "Fonte da tabela",
        ["Exemplo", "Enviar arquivo (CSV/Excel)", "Colar tabela"],
        index=0,
        help="A tabela deve conter frequências (contagens) não negativas, "
        "com nomes de linha na primeira coluna e nomes de coluna no cabeçalho.",
    )

    raw_df = None
    load_error = None

    if source == "Exemplo":
        raw_df = example_table()
        st.caption(
            "Exemplo clássico (Greenacre): categoria funcional × intensidade "
            "do hábito de fumar."
        )

    elif source == "Enviar arquivo (CSV/Excel)":
        up = st.file_uploader(
            "Selecione um arquivo .csv, .xlsx ou .xls",
            type=["csv", "xlsx", "xls"],
            help="A primeira coluna deve conter os nomes das linhas; "
            "a primeira linha, os nomes das colunas.",
        )
        if up is not None:
            try:
                raw_df = read_uploaded(up)
            except Exception as exc:  # noqa: BLE001
                load_error = f"Falha ao ler o arquivo: {exc}"

    else:  # Colar tabela
        st.caption("Cole a tabela (separada por tabulação, vírgula ou ponto e vírgula).")
        default_text = (
            "Categoria\tNão fuma\tLeve\tModerado\tIntenso\n"
            "Direção Sênior\t4\t2\t3\t2\n"
            "Direção Júnior\t4\t3\t7\t4\n"
            "Gerentes Sênior\t25\t10\t12\t4\n"
            "Gerentes Júnior\t18\t24\t33\t13\n"
            "Secretárias\t10\t6\t7\t2"
        )
        pasted = st.text_area("Tabela", value=default_text, height=200, label_visibility="collapsed")
        if st.button("Carregar tabela colada", use_container_width=True):
            st.session_state["_pasted_loaded"] = True
        if st.session_state.get("_pasted_loaded"):
            try:
                raw_df = parse_pasted_table(pasted)
            except CAError as exc:
                load_error = str(exc)

    st.divider()
    st.header("2. Opções do biplot")
    show_what = st.radio(
        "Mostrar pontos de",
        ["Ambos", "Apenas linhas", "Apenas colunas"],
        index=0,
        horizontal=False,
    )
    show_labels = st.checkbox("Exibir rótulos dos pontos", value=True)
    scale_by_contrib = st.checkbox(
        "Dimensionar marcadores pela contribuição", value=True,
        help="O tamanho do marcador reflete a contribuição do ponto para as "
        "dimensões exibidas — destaca os pontos que mais explicam a associação.",
    )


# --------------------------------------------------------------------------- #
# Tratamento de erros de carregamento
# --------------------------------------------------------------------------- #
if load_error:
    st.error(load_error)

if raw_df is None:
    st.info(
        "Selecione uma fonte de dados na barra lateral para começar. "
        "Você pode usar o **Exemplo**, **enviar um arquivo** CSV/Excel ou "
        "**colar** uma tabela."
    )
    with st.expander("Como devem ser os dados? (instruções de uso)", expanded=True):
        st.markdown(
            dedent(
                """
                **Formato esperado da tabela de contingência**

                | (nomes das linhas) | Categoria A | Categoria B | Categoria C |
                |--------------------|-------------|-------------|-------------|
                | Grupo 1            | 12          | 5           | 8           |
                | Grupo 2            | 3           | 20          | 7           |
                | Grupo 3            | 9           | 6           | 15          |

                - A **primeira coluna** contém os nomes das linhas.
                - A **primeira linha** (cabeçalho) contém os nomes das colunas.
                - As demais células são **frequências (contagens) não negativas**.
                - Não use percentuais nem totais; informe as contagens brutas.
                - Mínimo de **2 linhas** e **2 colunas**.
                """
            )
        )
    st.stop()


# --------------------------------------------------------------------------- #
# Validação e cálculo
# --------------------------------------------------------------------------- #
try:
    res: CAResult = run_ca(raw_df)
    teste_qui2 = chi2_contingency(raw_df)
except CAError as exc:
    st.error(f"**Tabela inválida:** {exc}")
    st.markdown("Confira a tabela carregada abaixo e ajuste os dados de origem.")
    st.dataframe(raw_df, use_container_width=True)
    st.stop()
except Exception as exc:  # noqa: BLE001
    st.error(f"Erro inesperado no cálculo: {exc}")
    st.stop()

st.success(
    f"Tabela válida: **{res.table.shape[0]} linhas × {res.table.shape[1]} colunas**. "
    f"Análise concluída com **{res.n_dims} dimensão(ões)** não trivial(is)."
)

# Cartões-resumo
c1, c2, c3, c4 = st.columns(4)
#c1.markdown(metric_card("Total geral (N)", f"{res.grand_total:,.0f}".replace(",", ".")), unsafe_allow_html=True)
#print(f"p-valor da estatística: {round(teste_qui2[1], 4)}")
c1.markdown(metric_card("p-valor da estatística:", f"{round(teste_qui2[1], 4)}".replace(",", ".")), unsafe_allow_html=True)
c2.markdown(metric_card("Inércia total", f"{res.total_inertia:.4f}"), unsafe_allow_html=True)
c3.markdown(metric_card("Qui-quadrado", f"{res.chi2:.2f}"), unsafe_allow_html=True)
c4.markdown(metric_card("Graus de liberdade", f"{res.chi2_df}"), unsafe_allow_html=True)
st.write("")


# --------------------------------------------------------------------------- #
# Abas de resultados
# --------------------------------------------------------------------------- #
tab_biplot, tab_resumo, tab_inercia, tab_coord, tab_perfis, tab_resid, tab_ajuda = st.tabs(
    ["📈 Biplot", "📝 Resumo", "📐 Inércia & autovalores", "🎯 Coordenadas / contrib. / cos²",
     "📋 Perfis & totais", "🔢 Resíduos", "❓ Instruções & método"]
)

# Eixos disponíveis
dim_options = list(range(1, res.n_dims + 1))


# ---------------------------- Aba: Biplot ---------------------------------- #
with tab_biplot:
    st.subheader("Biplot interativo (mapa simétrico)")
    cax, cay, _ = st.columns([1, 1, 3])
    with cax:
        dim_x = st.selectbox("Dimensão do eixo X", dim_options, index=0,
                             format_func=lambda d: f"Dim {d} ({res.inertia_pct[d-1]:.1f}%)")
    with cay:
        default_y = 1 if res.n_dims >= 2 else 0
        dim_y = st.selectbox("Dimensão do eixo Y", dim_options, index=default_y,
                             format_func=lambda d: f"Dim {d} ({res.inertia_pct[d-1]:.1f}%)")

    ix, iy = dim_x - 1, dim_y - 1
    col_x, col_y = f"Dim {dim_x}", f"Dim {dim_y}"

    def build_trace(coords, contrib, cos2, mass, name, color):
        size = np.full(len(coords), 12.0)
        if scale_by_contrib:
            contr_xy = (contrib[col_x].to_numpy() + contrib[col_y].to_numpy()) / 2.0
            mn, mx = contr_xy.min(), contr_xy.max()
            norm = (contr_xy - mn) / (mx - mn) if mx > mn else np.full_like(contr_xy, 0.5)
            size = 9 + norm * 28
        custom = np.column_stack([
            mass * 100,
            contrib[col_x].to_numpy() * 100,
            contrib[col_y].to_numpy() * 100,
            cos2[col_x].to_numpy() * 100,
            cos2[col_y].to_numpy() * 100,
            (cos2[col_x].to_numpy() + cos2[col_y].to_numpy()) * 100,
        ])
        hover = (
            "<b>%{text}</b><br>"
            f"{col_x}: %{{x:.3f}} &nbsp; {col_y}: %{{y:.3f}}<br>"
            "Massa: %{customdata[0]:.2f}%<br>"
            f"Contrib. {col_x}: %{{customdata[1]:.1f}}%<br>"
            f"Contrib. {col_y}: %{{customdata[2]:.1f}}%<br>"
            f"cos² {col_x}: %{{customdata[3]:.1f}}%<br>"
            f"cos² {col_y}: %{{customdata[4]:.1f}}%<br>"
            "Qualidade no plano: %{customdata[5]:.1f}%<extra></extra>"
        )
        return go.Scatter(
            x=coords[col_x], y=coords[col_y],
            mode="markers+text" if show_labels else "markers",
            text=list(coords.index),
            textposition="top center",
            textfont=dict(size=11),
#            marker=dict(size=size, color=color, line=dict(width=1, color="white"), opacity=0.85),
            marker=dict(size=size, color=color, line=dict(width=1, color="white")),
            name=name, customdata=custom, hovertemplate=hover,
        )

    fig = go.Figure()
    if show_what in ("Ambos", "Apenas linhas"):
        fig.add_trace(build_trace(res.row_coords, res.row_contrib, res.row_cos2,
                                  res.row_mass, "Linhas", "#2563eb"))
    if show_what in ("Ambos", "Apenas colunas"):
        fig.add_trace(build_trace(res.col_coords, res.col_contrib, res.col_cos2,
                                  res.col_mass, "Colunas", "#dc2626"))

    fig.add_hline(y=0, line_width=1, line_color="#c8ccd1")
    fig.add_vline(x=0, line_width=1, line_color="#c8ccd1")
    fig.update_layout(
        height=620,
        xaxis_title=f"{col_x} — {res.inertia_pct[ix]:.1f}% da inércia",
        yaxis_title=f"{col_y} — {res.inertia_pct[iy]:.1f}% da inércia",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        plot_bgcolor="white", margin=dict(l=40, r=20, t=40, b=40),
        hoverlabel=dict(font_size=12),
    )
    fig.update_xaxes(showgrid=True, gridcolor="#eef0f2", zeroline=False, scaleanchor="y", scaleratio=1)
    fig.update_yaxes(showgrid=True, gridcolor="#eef0f2", zeroline=False)
    st.plotly_chart(fig, use_container_width=True)
    st.caption(
        "Mapa simétrico: linhas (azul) e colunas (vermelho) em coordenadas principais. "
        "Pontos próximos da origem têm perfil próximo à média; pontos próximos entre si "
        "(de conjuntos diferentes) tendem a estar associados. Eixos com proporção 1:1 "
        "preservam as distâncias do mapa."
    )


# ---------------------------- Aba: Resumo ---------------------------------- #
with tab_resumo:
    st.subheader("Resumo explicativo")

    ix, iy = dim_x - 1, dim_y - 1
    cx, cy = f"Dim {dim_x}", f"Dim {dim_y}"
    plano_pct = res.inertia_pct[ix] + (res.inertia_pct[iy] if iy != ix else 0)

    st.markdown(f"**Inércia explicada por dimensão**")
    bullet = ""
    for k in range(res.n_dims):
        bullet += (f"- **Dim {k+1}**: {res.inertia_pct[k]:.1f}% da inércia "
                   f"(acumulado {res.inertia_cum[k]:.1f}%) — autovalor {res.eigenvalues[k]:.4f}\n")
    st.markdown(bullet)

    if iy != ix:
        st.markdown(
            f"O plano formado por **{cx}** e **{cy}** retém **{plano_pct:.1f}%** da inércia total, "
            "ou seja, dessa fração da associação entre linhas e colunas está representada no biplot atual."
        )
    else:
        st.markdown(f"As duas seleções de eixo apontam para a mesma dimensão (**{cx}**). "
                    "Escolha dimensões diferentes para X e Y para visualizar um plano.")

    # Interpretação por contribuição nas dimensões selecionadas
    def top_contrib(contrib, dim_label, n=3):
        s = contrib[dim_label].sort_values(ascending=False)
        return s.head(n)

    st.markdown("**Interpretação das dimensões selecionadas**")
    for dlabel, didx in ([(cx, ix)] if iy == ix else [(cx, ix), (cy, iy)]):
        rt = top_contrib(res.row_contrib, dlabel)
        ct = top_contrib(res.col_contrib, dlabel)
        # sinais para descrever oposição de polos
        rc = res.row_coords[dlabel]
        cc = res.col_coords[dlabel]
        pos_rows = ", ".join(rc[rc > 0].sort_values(ascending=False).head(2).index)
        neg_rows = ", ".join(rc[rc < 0].sort_values().head(2).index)
        rows_txt = ", ".join(f"{n} ({v*100:.0f}%)" for n, v in rt.items())
        cols_txt = ", ".join(f"{n} ({v*100:.0f}%)" for n, v in ct.items())
        st.markdown(
            f"- **{dlabel}** ({res.inertia_pct[didx]:.1f}% da inércia). "
            f"Linhas que mais a definem: {rows_txt}. Colunas que mais a definem: {cols_txt}. "
            + (f"Esse eixo contrapõe, de um lado, **{pos_rows}** e, de outro, **{neg_rows}**."
               if pos_rows and neg_rows else "")
        )

    # Pontos de maior contribuição global para a associação (somando todas as dimensões pela massa·dist²)
    st.markdown("**Pontos com maior peso na associação (inércia)**")
    row_inertia = (res.row_mass * (res.row_coords.to_numpy() ** 2).sum(axis=1))
    col_inertia = (res.col_mass * (res.col_coords.to_numpy() ** 2).sum(axis=1))
    row_share = pd.Series(row_inertia / res.total_inertia, index=res.row_names).sort_values(ascending=False)
    col_share = pd.Series(col_inertia / res.total_inertia, index=res.col_names).sort_values(ascending=False)
    cca, ccb = st.columns(2)
    with cca:
        st.markdown("_Linhas_")
        st.markdown("\n".join(f"- {n}: {v*100:.1f}% da inércia total" for n, v in row_share.head(3).items()))
    with ccb:
        st.markdown("_Colunas_")
        st.markdown("\n".join(f"- {n}: {v*100:.1f}% da inércia total" for n, v in col_share.head(3).items()))

    # Aviso sobre dimensões de baixa inércia
    low = [k + 1 for k in range(res.n_dims) if res.inertia_pct[k] < 5.0]
    if low:
        st.warning(
            "⚠️ Dimensão(ões) com baixa inércia (< 5%): "
            + ", ".join(f"Dim {d} ({res.inertia_pct[d-1]:.1f}%)" for d in low)
            + ". Interprete-as com cautela — explicam pouca da associação e podem refletir ruído."
        )
    if iy != ix and plano_pct < 60:
        st.info(
            f"ℹ️ O plano selecionado retém apenas {plano_pct:.1f}% da inércia. "
            "Parte relevante da estrutura pode estar em outras dimensões; "
            "considere examinar dimensões adicionais."
        )


# --------------------- Aba: Inércia & autovalores -------------------------- #
with tab_inercia:
    st.subheader("Autovalores e decomposição da inércia")
    inercia_df = pd.DataFrame({
        "Valor singular": res.singular_values,
        "Autovalor (inércia)": res.eigenvalues,
        "% da inércia": res.inertia_pct,
        "% acumulado": res.inertia_cum,
    }, index=res.dim_labels)
    st.dataframe(inercia_df.style.format({
        "Valor singular": "{:.4f}", "Autovalor (inércia)": "{:.5f}",
        "% da inércia": "{:.2f}%", "% acumulado": "{:.2f}%",
    }), use_container_width=True)

    scree = go.Figure()
    scree.add_bar(x=res.dim_labels, y=res.inertia_pct, marker_color="#2563eb", name="% inércia")
    scree.add_scatter(x=res.dim_labels, y=res.inertia_cum, mode="lines+markers",
                      line=dict(color="#dc2626"), name="% acumulado", yaxis="y")
    scree.update_layout(height=380, plot_bgcolor="white", yaxis_title="% da inércia",
                        margin=dict(l=40, r=20, t=30, b=30),
                        legend=dict(orientation="h", y=1.1, x=1, xanchor="right"))
    scree.update_yaxes(gridcolor="#eef0f2")
    st.plotly_chart(scree, use_container_width=True)
    st.download_button("⬇️ Baixar inércia (CSV)", df_to_csv_bytes(inercia_df, "Dimensão"),
                       "acs_inercia.csv", "text/csv")


# ---------------- Aba: Coordenadas / contribuições / cos² ------------------ #
with tab_coord:
    st.subheader("Coordenadas principais, contribuições e cos²")
    alvo = st.radio("Conjunto", ["Linhas", "Colunas"], horizontal=True)
    if alvo == "Linhas":
        coords, contrib, cos2, mass, names = (res.row_coords, res.row_contrib,
                                              res.row_cos2, res.row_mass, res.row_names)
    else:
        coords, contrib, cos2, mass, names = (res.col_coords, res.col_contrib,
                                              res.col_cos2, res.col_mass, res.col_names)

    st.markdown("**Coordenadas principais**")
    coord_show = coords.copy()
    coord_show.insert(0, "Massa", mass)
    st.dataframe(coord_show.style.format("{:.4f}"), use_container_width=True)

    cc1, cc2 = st.columns(2)
    with cc1:
        st.markdown("**Contribuições (% por dimensão — somam 100%)**")
        st.dataframe((contrib * 100).style.format("{:.2f}%")
                     .background_gradient(cmap="Blues", axis=0), use_container_width=True)
    with cc2:
        st.markdown("**cos² — qualidade da representação (por dimensão)**")
        st.dataframe((cos2 * 100).style.format("{:.2f}%")
                     .background_gradient(cmap="Greens", axis=None), use_container_width=True)

    d1, d2, d3 = st.columns(3)
    d1.download_button("⬇️ Coordenadas (CSV)", df_to_csv_bytes(coord_show, alvo),
                       f"acs_coordenadas_{alvo.lower()}.csv", "text/csv")
    d2.download_button("⬇️ Contribuições (CSV)", df_to_csv_bytes(contrib, alvo),
                       f"acs_contribuicoes_{alvo.lower()}.csv", "text/csv")
    d3.download_button("⬇️ cos² (CSV)", df_to_csv_bytes(cos2, alvo),
                       f"acs_cos2_{alvo.lower()}.csv", "text/csv")


# ---------------------- Aba: Perfis & totais ------------------------------- #
with tab_perfis:
    st.subheader("Tabela observada, totais e perfis")
    obs = res.table.copy()
    obs["Total"] = obs.sum(axis=1)
    obs.loc["Total"] = obs.sum(axis=0)
    st.markdown("**Frequências observadas com totais marginais**")
    st.dataframe(obs.style.format("{:.0f}"), use_container_width=True)

    pc1, pc2 = st.columns(2)
    with pc1:
        st.markdown("**Perfis de linha** (cada linha soma 100%)")
        st.dataframe((res.row_profiles * 100).style.format("{:.1f}%"), use_container_width=True)
    with pc2:
        st.markdown("**Perfis de coluna** (cada coluna soma 100%)")
        st.dataframe((res.col_profiles * 100).style.format("{:.1f}%"), use_container_width=True)

    st.markdown("**Frequências esperadas sob independência**")
    st.dataframe(res.expected.style.format("{:.2f}"), use_container_width=True)

    e1, e2 = st.columns(2)
    e1.download_button("⬇️ Perfis de linha (CSV)", df_to_csv_bytes(res.row_profiles, "Linha"),
                       "acs_perfis_linha.csv", "text/csv")
    e2.download_button("⬇️ Perfis de coluna (CSV)", df_to_csv_bytes(res.col_profiles, "Linha"),
                       "acs_perfis_coluna.csv", "text/csv")


# ---------------------------- Aba: Resíduos -------------------------------- #
with tab_resid:
    st.subheader("Resíduos padronizados de Pearson")
    st.markdown(
        "Cada célula é \\((p_{ij} - r_i c_j)/\\sqrt{r_i c_j}\\). "
        "Valores positivos (azul) indicam frequência **acima** do esperado sob "
        "independência; negativos (vermelho), **abaixo**. São o insumo da SVD."
    )
    st.dataframe(
        res.std_residuals.style.format("{:.3f}").background_gradient(cmap="RdBu", axis=None, vmin=-0.3, vmax=0.3),
        use_container_width=True,
    )
    st.download_button("⬇️ Resíduos padronizados (CSV)", df_to_csv_bytes(res.std_residuals, "Linha"),
                       "acs_residuos_padronizados.csv", "text/csv")


# ------------------------ Aba: Instruções & método ------------------------- #
with tab_ajuda:
    st.subheader("Instruções de uso")
    st.markdown(
        dedent(
            """
            1. **Escolha a fonte dos dados** na barra lateral: use o *Exemplo*,
               *envie um arquivo* CSV/Excel ou *cole* uma tabela.
            2. A **primeira coluna** deve conter os nomes das linhas e a
               **primeira linha** os nomes das colunas. As demais células são
               **frequências (contagens) não negativas** — não use percentuais
               nem inclua linhas/colunas de totais.
            3. A análise roda **automaticamente** após o carregamento. Navegue
               pelas abas para ver o biplot, o resumo e as tabelas.
            4. No **Biplot**, escolha as dimensões dos eixos X e Y, alterne entre
               linhas/colunas/ambos, ative rótulos e o dimensionamento por
               contribuição. Passe o cursor sobre um ponto para ver massa,
               contribuição, cos² e qualidade no plano.
            5. Baixe os resultados em **CSV** nas abas de inércia, coordenadas e
               perfis (separador `;`, decimal `,`, compatível com Excel pt-BR).
            """
        )
    )

    st.subheader("Notas metodológicas")
    st.markdown(
        dedent(
            r"""
            A **Análise de Correspondência Simples (ACS)** decompõe a associação
            entre as categorias de duas variáveis qualitativas de uma tabela de
            contingência.

            - **Matriz de correspondência:** \(P = N / n\), com massas de linha
              \(r_i = \sum_j p_{ij}\) e de coluna \(c_j = \sum_i p_{ij}\).
            - **Resíduos padronizados:**
              \(S = D_r^{-1/2}\,(P - r c^{\top})\,D_c^{-1/2}\), onde \(D_r\) e
              \(D_c\) são matrizes diagonais das massas.
            - **Decomposição (SVD):** \(S = U \Lambda V^{\top}\). Os **autovalores**
              \(\lambda_k = \sigma_k^2\) (valores singulares ao quadrado) são as
              **inércias** de cada dimensão; a **inércia total** \(= \sum_k \lambda_k\)
              equivale a \(\chi^2 / n\).
            - **Coordenadas principais** (mapa simétrico):
              linhas \(F = D_r^{-1/2} U \Lambda\); colunas \(G = D_c^{-1/2} V \Lambda\).
            - **Contribuição** do ponto à dimensão \(k\):
              \( \text{massa} \cdot \text{coord}_k^2 / \lambda_k\) (soma 100% por dimensão).
            - **cos²** (qualidade): fração da distância do ponto à origem explicada
              pela dimensão; soma 100% considerando todas as dimensões.

            **Interpretação.** Pontos próximos da origem têm perfil próximo da média
            geral. Categorias de uma mesma variável próximas entre si têm perfis
            semelhantes. No mapa simétrico, a proximidade entre uma linha e uma coluna
            sugere associação, mas distâncias linha–coluna devem ser lidas com cautela
            (não são distâncias qui-quadrado diretas). Use **contribuições** para
            saber quais pontos *constroem* cada eixo e **cos²** para saber se um ponto
            está *bem representado* no plano exibido.

            **Limitações.** A ACS é exploratória e descritiva; o número de dimensões
            não triviais é \(\min(\text{linhas}-1, \text{colunas}-1)\). Dimensões com
            inércia muito baixa tendem a captar ruído. O qui-quadrado é exibido a
            título informativo; sua validade pressupõe frequências esperadas
            suficientes.

            **Referências:** Greenacre, M. (2007) *Correspondence Analysis in Practice*;
            Benzécri, J.-P. (1973) *L'Analyse des Données*; Abdi & Williams (2010).
            """
        )
    )

st.divider()
st.caption(
    "Ferramenta ACS · cálculo via SVD da matriz de resíduos padronizados (numpy). "
    "Mapa simétrico. Resultados conferidos com o conjunto clássico de Greenacre."
)
