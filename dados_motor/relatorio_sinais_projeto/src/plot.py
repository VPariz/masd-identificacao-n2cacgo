from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# ================= CONFIGURAÇÕES =================

BASE_DIR = Path(__file__).resolve().parent.parent

PASTA_DADOS = BASE_DIR / "data/trig"
PASTA_SAIDA = BASE_DIR / "outputs"

ARQUIVO_ENTRADA = "e_2.csv"
ARQUIVO_SAIDA = "f2.csv"

TITULO = "Entrada e saída - 8,5 Hz"
EIXO_X = "Tempo (s)"
EIXO_Y = "Potencial (V)"

LEGENDA_ENTRADA = "Entrada"
LEGENDA_SAIDA = "Saída"

MOSTRAR_GRADE = True
MOSTRAR_LEGENDA = True

SALVAR_FIGURA = True
MOSTRAR_NA_TELA = True

NOME_FIGURA = "entrada_saida_8_5Hz.png"

# Use None para automático.
LIMITE_X = None
LIMITE_Y = None

# Exemplos:
# LIMITE_X = (0, 2)
# LIMITE_Y = (-5, 5)

REMOVER_MEDIA = False

# ==================================================


def ler_csv(caminho):
    """
    Lê um CSV com colunas Time e Value.
    """
    df = pd.read_csv(caminho, sep=None, engine="python")
    df.columns = [col.strip() for col in df.columns]

    if "Time" not in df.columns or "Value" not in df.columns:
        raise ValueError(f"O arquivo {caminho.name} não possui colunas Time e Value.")

    tempo = pd.to_numeric(
        df["Time"].astype(str).str.replace(",", ".", regex=False), errors="coerce"
    )

    valor = pd.to_numeric(
        df["Value"].astype(str).str.replace(",", ".", regex=False), errors="coerce"
    )

    dados = pd.DataFrame({"Time": tempo, "Value": valor}).dropna()

    return dados["Time"], dados["Value"]


def main():
    PASTA_SAIDA.mkdir(exist_ok=True)

    caminho_entrada = PASTA_DADOS / ARQUIVO_ENTRADA
    caminho_saida = PASTA_DADOS / ARQUIVO_SAIDA

    if not caminho_entrada.exists():
        print(f"Arquivo de entrada não encontrado: {caminho_entrada}")
        return

    if not caminho_saida.exists():
        print(f"Arquivo de saída não encontrado: {caminho_saida}")
        return

    tempo_entrada, valor_entrada = ler_csv(caminho_entrada)
    tempo_saida, valor_saida = ler_csv(caminho_saida)

    if REMOVER_MEDIA:
        valor_entrada = valor_entrada - valor_entrada.mean()
        valor_saida = valor_saida - valor_saida.mean()

    fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

    axs[0].plot(tempo_entrada, valor_entrada, label=LEGENDA_ENTRADA)

    axs[0].set_title("Sinal de entrada")
    axs[0].set_ylabel(EIXO_Y)

    if MOSTRAR_GRADE:
        axs[0].grid(True)

    if MOSTRAR_LEGENDA:
        axs[0].legend()

    axs[1].plot(tempo_saida, valor_saida, label=LEGENDA_SAIDA)

    axs[1].set_title("Sinal de saída")
    axs[1].set_xlabel(EIXO_X)
    axs[1].set_ylabel(EIXO_Y)

    if MOSTRAR_GRADE:
        axs[1].grid(True)

    if MOSTRAR_LEGENDA:
        axs[1].legend()

    fig.suptitle(TITULO)

    if LIMITE_X is not None:
        axs[0].set_xlim(LIMITE_X)
        axs[1].set_xlim(LIMITE_X)

    if LIMITE_Y is not None:
        axs[0].set_ylim(LIMITE_Y)
        axs[1].set_ylim(LIMITE_Y)

    plt.tight_layout()

    if SALVAR_FIGURA:
        caminho_figura = PASTA_SAIDA / NOME_FIGURA
        plt.savefig(caminho_figura, dpi=300)
        print(f"Figura salva em: {caminho_figura}")

    if MOSTRAR_NA_TELA:
        plt.show()
    else:
        plt.close()


if __name__ == "__main__":
    main()
