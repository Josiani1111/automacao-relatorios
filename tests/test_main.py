
import pandas as pd
from src.main import calcular_total


def test_calcular_total():
    dados = {
        "Vendedor": ["Ana", "Carlos"],
        "Produto": ["Notebook", "Mouse"],
        "Quantidade": [3, 15],
        "Valor": [4500, 80]
    }

    df = pd.DataFrame(dados)

    resultado = calcular_total(df)

    assert resultado["Total"].tolist() == [13500, 1200]

    
def test_identificar_maior_venda():
    from src.main import identificar_maior_venda

    dados = {
        "Vendedor": ["Ana", "Carlos"],
        "Produto": ["Notebook", "Mouse"],
        "Quantidade": [3, 15],
        "Valor": [4500, 80],
        "Total": [13500, 1200]
    }

    df = pd.DataFrame(dados)

    maior_venda = identificar_maior_venda(df)

    assert maior_venda["Vendedor"] == "Ana"
    assert maior_venda["Total"] == 13500

    
def test_classificar_vendas():
    from src.main import classificar_vendas

    dados = {
        "Vendedor": ["Ana", "Carlos"],
        "Total": [13500, 1200]
    }

    df = pd.DataFrame(dados)

    resultado, alertas = classificar_vendas(df)

    assert resultado["Status"].tolist() == ["Normal", "Atenção"]
    assert len(alertas) == 1
    assert alertas.iloc[0]["Vendedor"] == "Carlos"