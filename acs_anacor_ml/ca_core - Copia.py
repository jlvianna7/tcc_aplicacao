"""
ca_core.py
==========
Núcleo de cálculo para Análise de Correspondência Simples (ACS).

Implementa a ACS clássica de uma tabela de contingência usando decomposição
em valores singulares (SVD) da matriz de resíduos padronizados (matriz de
Pearson). Não depende de bibliotecas de ML — apenas numpy e pandas.

Referências metodológicas:
- Greenacre, M. (2007). Correspondence Analysis in Practice. 2nd ed.
- Benzécri, J.-P. (1973). L'Analyse des Données.
- Abdi, H. & Williams, L.J. (2010). Correspondence analysis.

Convenção de coordenadas:
- Coordenadas PRINCIPAIS de linhas:   F = Dr^{-1/2} · U · Λ
- Coordenadas PRINCIPAIS de colunas:  G = Dc^{-1/2} · V · Λ
  onde Λ = diag(valores singulares) e os autovalores (inércias) são Λ².
Esse é o chamado mapa simétrico (symmetric map), padrão para biplots de ACS.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

import numpy as np
import pandas as pd


@dataclass
class CAResult:
    """Recipiente com todos os resultados de uma ACS."""

    # Identificadores
    row_names: List[str]
    col_names: List[str]

    # Tabela e totais
    table: pd.DataFrame                 # frequências observadas
    grand_total: float
    row_mass: np.ndarray                # massas das linhas (perfis marginais)
    col_mass: np.ndarray                # massas das colunas
    row_profiles: pd.DataFrame          # perfis de linha (linhas somam 1)
    col_profiles: pd.DataFrame          # perfis de coluna (colunas somam 1)
    expected: pd.DataFrame              # frequências esperadas sob independência
    std_residuals: pd.DataFrame         # resíduos padronizados de Pearson

    # Decomposição
    n_dims: int                         # número de dimensões não triviais
    singular_values: np.ndarray
    eigenvalues: np.ndarray             # inércias por dimensão (= s.v.²)
    total_inertia: float
    inertia_pct: np.ndarray             # % de inércia por dimensão
    inertia_cum: np.ndarray             # % acumulada

    # Coordenadas principais
    row_coords: pd.DataFrame            # F  (linhas x dimensões)
    col_coords: pd.DataFrame            # G  (colunas x dimensões)

    # Contribuições (somam 1.0 por coluna/dimensão) e cos² (qualidade)
    row_contrib: pd.DataFrame
    col_contrib: pd.DataFrame
    row_cos2: pd.DataFrame
    col_cos2: pd.DataFrame

    # Teste qui-quadrado de independência (informativo)
    chi2: float = field(default=np.nan)
    chi2_df: int = field(default=0)

    @property
    def dim_labels(self) -> List[str]:
        return [f"Dim {i + 1}" for i in range(self.n_dims)]


class CAError(ValueError):
    """Erro de validação ou de cálculo da ACS."""


def validate_table(df: pd.DataFrame) -> pd.DataFrame:
    """Valida e normaliza uma tabela de contingência.

    Regras:
    - Deve haver pelo menos 2 linhas e 2 colunas.
    - Todas as células devem ser numéricas e não negativas.
    - Não pode haver linhas ou colunas inteiramente nulas (soma zero).
    - Nomes de linhas (índice) e de colunas devem existir e ser únicos.

    Retorna uma cópia limpa (float) da tabela ou levanta CAError.
    """
    if df is None or df.empty:
        raise CAError("A tabela está vazia.")

    df = df.copy()

    # Garantir nomes de colunas como string e não nulos
    if df.columns.isnull().any():
        raise CAError("Há nomes de coluna ausentes. Defina um nome para cada coluna.")
    df.columns = [str(c).strip() for c in df.columns]

    # Garantir índice (nomes de linha)
    if df.index.isnull().any():
        raise CAError("Há nomes de linha ausentes. Defina um nome para cada linha.")
    df.index = [str(i).strip() for i in df.index]

    if df.shape[0] < 2 or df.shape[1] < 2:
        raise CAError(
            f"A tabela precisa de ao menos 2 linhas e 2 colunas "
            f"(recebido: {df.shape[0]} linhas, {df.shape[1]} colunas)."
        )

    if len(set(df.columns)) != len(df.columns):
        raise CAError("Há nomes de coluna duplicados. Use rótulos únicos.")
    if len(set(df.index)) != len(df.index):
        raise CAError("Há nomes de linha duplicados. Use rótulos únicos.")

    # Converter para numérico
    try:
        num = df.apply(pd.to_numeric, errors="raise")
    except (ValueError, TypeError):
        bad_cols = []
        for c in df.columns:
            coerced = pd.to_numeric(df[c], errors="coerce")
            if coerced.isnull().any():
                bad_cols.append(c)
        raise CAError(
            "Todas as células devem ser numéricas (frequências). "
            f"Valores não numéricos encontrados na(s) coluna(s): {', '.join(map(str, bad_cols))}."
        )

    if num.isnull().any().any():
        raise CAError("Há células vazias (NaN). Preencha todas as frequências com números.")

    arr = num.to_numpy(dtype=float)
    if np.any(arr < 0):
        raise CAError("Frequências negativas não são permitidas. Use apenas valores >= 0.")

    # Linhas/colunas totalmente nulas inviabilizam perfis
    row_sums = arr.sum(axis=1)
    col_sums = arr.sum(axis=0)
    if np.any(row_sums == 0):
        zero_rows = [num.index[i] for i in np.where(row_sums == 0)[0]]
        raise CAError(f"Estas linhas somam zero e devem ser removidas: {', '.join(map(str, zero_rows))}.")
    if np.any(col_sums == 0):
        zero_cols = [num.columns[j] for j in np.where(col_sums == 0)[0]]
        raise CAError(f"Estas colunas somam zero e devem ser removidas: {', '.join(map(str, zero_cols))}.")

    if arr.sum() == 0:
        raise CAError("A soma total da tabela é zero.")

    return num


def run_ca(df: pd.DataFrame) -> CAResult:
    """Executa a Análise de Correspondência Simples sobre uma tabela validada."""
    num = validate_table(df)

    row_names = list(num.index)
    col_names = list(num.columns)
    N = num.to_numpy(dtype=float)

    n = N.sum()
    P = N / n                                   # matriz de correspondência (proporções)
    r = P.sum(axis=1)                           # massas de linha
    c = P.sum(axis=0)                           # massas de coluna

    # Frequências esperadas e resíduos padronizados de Pearson
    expected = np.outer(r, c)                   # em proporção
    # Matriz de resíduos padronizados S = Dr^{-1/2} (P - r c^T) Dc^{-1/2}
    Dr_inv_sqrt = np.diag(1.0 / np.sqrt(r))
    Dc_inv_sqrt = np.diag(1.0 / np.sqrt(c))
    S = Dr_inv_sqrt @ (P - expected) @ Dc_inv_sqrt

    # SVD
    U, sv, Vt = np.linalg.svd(S, full_matrices=False)
    V = Vt.T

    # Número de dimensões não triviais
    rank = min(N.shape[0] - 1, N.shape[1] - 1)
    # filtrar valores singulares numericamente nulos
    tol = 1e-10
    keep = sv > tol
    n_dims = int(min(rank, keep.sum()))
    if n_dims < 1:
        raise CAError("A tabela não possui associação detectável (inércia total ~ 0).")

    sv = sv[:n_dims]
    U = U[:, :n_dims]
    V = V[:, :n_dims]

    eig = sv ** 2                               # autovalores = inércias por dimensão
    total_inertia = float(eig.sum())
    inertia_pct = eig / total_inertia * 100.0
    inertia_cum = np.cumsum(inertia_pct)

    # Coordenadas principais (mapa simétrico)
    F = Dr_inv_sqrt @ U @ np.diag(sv)           # linhas
    G = Dc_inv_sqrt @ V @ np.diag(sv)           # colunas

    dim_labels = [f"Dim {i + 1}" for i in range(n_dims)]

    # Contribuições: parcela de cada ponto na inércia de cada dimensão
    # contrib_linha[i,k] = r_i * F[i,k]^2 / eig_k
    row_contrib = (r[:, None] * F ** 2) / eig[None, :]
    col_contrib = (c[:, None] * G ** 2) / eig[None, :]

    # cos² (qualidade da representação): F[i,k]^2 / dist²(i ao centroide)
    row_dist2 = (F ** 2).sum(axis=1)
    col_dist2 = (G ** 2).sum(axis=1)
    row_dist2[row_dist2 == 0] = np.nan
    col_dist2[col_dist2 == 0] = np.nan
    row_cos2 = F ** 2 / row_dist2[:, None]
    col_cos2 = G ** 2 / col_dist2[:, None]

    # Qui-quadrado total (inércia total * n)
    chi2 = float(total_inertia * n)
    chi2_df = (N.shape[0] - 1) * (N.shape[1] - 1)

    def _df(data, idx):
        return pd.DataFrame(data, index=idx, columns=dim_labels)

    return CAResult(
        row_names=row_names,
        col_names=col_names,
        table=num,
        grand_total=float(n),
        row_mass=r,
        col_mass=c,
        row_profiles=pd.DataFrame(N / N.sum(axis=1, keepdims=True), index=row_names, columns=col_names),
        col_profiles=pd.DataFrame(N / N.sum(axis=0, keepdims=True), index=row_names, columns=col_names),
        expected=pd.DataFrame(expected * n, index=row_names, columns=col_names),
        std_residuals=pd.DataFrame(S, index=row_names, columns=col_names),
        n_dims=n_dims,
        singular_values=sv,
        eigenvalues=eig,
        total_inertia=total_inertia,
        inertia_pct=inertia_pct,
        inertia_cum=inertia_cum,
        row_coords=_df(F, row_names),
        col_coords=_df(G, col_names),
        row_contrib=_df(row_contrib, row_names),
        col_contrib=_df(col_contrib, col_names),
        row_cos2=_df(row_cos2, row_names),
        col_cos2=_df(col_cos2, col_names),
        chi2=chi2,
        chi2_df=chi2_df,
    )


def example_table() -> pd.DataFrame:
    """Tabela de exemplo: cargo do funcionário x hábito de fumo.

    Conjunto clássico de Greenacre ("smoking data"), amplamente usado em
    livros de Análise de Correspondência. Cruza categoria funcional de uma
    empresa com a intensidade do hábito de fumar.
    """
    data = {
        "Não fuma": [4, 4, 25, 18, 10],
        "Leve": [2, 3, 10, 24, 6],
        "Moderado": [3, 7, 12, 33, 7],
        "Intenso": [2, 4, 4, 13, 2],
    }
    idx = ["Direção Sênior", "Direção Júnior", "Gerentes Sênior",
           "Gerentes Júnior", "Secretárias"]
    return pd.DataFrame(data, index=idx)


if __name__ == "__main__":
    res = run_ca(example_table())
    print("Inércia total:", round(res.total_inertia, 5))
    print("Qui-quadrado:", round(res.chi2, 3), "gl =", res.chi2_df)
    print("Autovalores:", np.round(res.eigenvalues, 5))
    print("% inércia:", np.round(res.inertia_pct, 2))
    print("\nCoordenadas de linha:\n", res.row_coords.round(3))
    print("\nCoordenadas de coluna:\n", res.col_coords.round(3))
