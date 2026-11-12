from pathlib import Path

import numpy as np
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
OUTPUTS_DIR = ROOT_DIR / "outputs"


def garantir_pasta(caminho: Path) -> None:
    caminho.mkdir(parents=True, exist_ok=True)


def ler_csv_sinal(nome_arquivo: str):
    """
    Lê um CSV da pasta data/ com colunas:
    Time, Value

    Retorna:
    t -> tempo
    x -> potencial
    """
    caminho = DATA_DIR / nome_arquivo

    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    df = pd.read_csv(caminho, sep=None, engine="python")

    if "Time" not in df.columns or "Value" not in df.columns:
        raise ValueError(
            f"O arquivo {
                nome_arquivo} precisa ter as colunas 'Time' e 'Value'. "
            f"Colunas encontradas: {list(df.columns)}"
        )

    t = df["Time"].to_numpy(dtype=float)
    x = df["Value"].to_numpy(dtype=float)

    return t, x


def salvar_tabela(df: pd.DataFrame, nome_arquivo: str) -> None:
    garantir_pasta(OUTPUTS_DIR / "tables")
    caminho = OUTPUTS_DIR / "tables" / nome_arquivo
    df.to_csv(caminho, index=False)
    print(f"Tabela salva em: {caminho}")
