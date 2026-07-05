"""Testes rápidos do núcleo de cálculo e da validação da ACS."""
import numpy as np
import pandas as pd

from ca_core import run_ca, validate_table, example_table, CAError


def test_greenacre_reference():
    res = run_ca(example_table())
    assert abs(res.total_inertia - 0.08519) < 1e-3, res.total_inertia
    assert abs(res.inertia_pct[0] - 87.76) < 0.5
    assert abs(res.inertia_pct[1] - 11.76) < 0.5
    # contribuições somam ~100% por dimensão
    assert np.allclose(res.row_contrib.sum(axis=0).to_numpy(), 1.0, atol=1e-6)
    assert np.allclose(res.col_contrib.sum(axis=0).to_numpy(), 1.0, atol=1e-6)
    print("OK: referência Greenacre, inércia =", round(res.total_inertia, 5))


def test_validation_errors():
    # negativos
    bad = pd.DataFrame({"A": [1, -2], "B": [3, 4]}, index=["x", "y"])
    try:
        validate_table(bad)
        assert False, "deveria falhar com negativo"
    except CAError as e:
        assert "negativ" in str(e).lower()

    # coluna soma zero
    bad2 = pd.DataFrame({"A": [0, 0], "B": [3, 4]}, index=["x", "y"])
    try:
        validate_table(bad2)
        assert False
    except CAError:
        pass

    # texto não numérico
    bad3 = pd.DataFrame({"A": ["foo", "2"], "B": ["3", "4"]}, index=["x", "y"])
    try:
        validate_table(bad3)
        assert False
    except CAError as e:
        assert "numéric" in str(e).lower()

    # dimensão mínima
    bad4 = pd.DataFrame({"A": [1]}, index=["x"])
    try:
        validate_table(bad4)
        assert False
    except CAError:
        pass

    print("OK: validações de erro funcionando")


def test_app_imports():
    import importlib.util
    spec = importlib.util.find_spec("streamlit")
    assert spec is not None, "streamlit não instalado"
    # garante que app.py é importável sintaticamente (compilação)
    import py_compile
    py_compile.compile("app.py", doraise=True)
    print("OK: app.py compila e streamlit disponível")


if __name__ == "__main__":
    test_greenacre_reference()
    test_validation_errors()
    test_app_imports()
    print("\nTodos os testes passaram.")
