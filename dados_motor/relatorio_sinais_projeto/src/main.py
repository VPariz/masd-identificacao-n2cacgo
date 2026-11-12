from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from signal_tools import (alinhar_sinais, analise_fft, analise_temporal,
                          espectro_simples, ler_sinal, obter_pares,
                          remover_media)

DATA_DIR = Path("data")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def plotar_tempo(t, u, y, freq_hz):
    plt.figure(figsize=(10, 4))
    plt.plot(t, u, label="Entrada")
    plt.plot(t, y, label="Saída")
    plt.grid(True)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Potencial (V)")
    plt.title(f"Entrada e saída - {freq_hz} Hz")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"tempo_{freq_hz}Hz.png", dpi=300)
    plt.close()


def plotar_espectros(t, u, y, freq_hz):
    f_u, mag_u = espectro_simples(t, u)
    f_y, mag_y = espectro_simples(t, y)

    plt.figure(figsize=(10, 4))
    plt.plot(f_u, mag_u, label="Entrada")
    plt.plot(f_y, mag_y, label="Saída")
    plt.grid(True)
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Magnitude")
    plt.title(f"Espectro por FFT - {freq_hz} Hz")
    plt.legend()
    plt.xlim(0, min(10 * freq_hz, max(f_u)))
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"fft_{freq_hz}Hz.png", dpi=300)
    plt.close()


def plotar_resposta_frequencia(df):
    plt.figure(figsize=(8, 4))
    plt.semilogx(df["freq_hz"], df["ganho_temporal"], "o-", label="Temporal")
    plt.semilogx(df["freq_hz"], df["ganho_fft"], "s-", label="FFT")
    plt.grid(True, which="both")
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Ganho")
    plt.title("Comparação do ganho")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "comparacao_ganho.png", dpi=300)
    plt.close()

    plt.figure(figsize=(8, 4))
    plt.semilogx(df["freq_hz"], df["fase_temporal_graus"], "o-", label="Temporal")
    plt.semilogx(df["freq_hz"], df["fase_fft_graus"], "s-", label="FFT")
    plt.grid(True, which="both")
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Fase (graus)")
    plt.title("Comparação da fase")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "comparacao_fase.png", dpi=300)
    plt.close()


def main():
    pares = obter_pares(DATA_DIR)

    if not pares:
        print("Nenhum par encontrado em data/.")
        return

    resultados = []

    for par in pares:
        freq_hz = par["freq_hz"]

        print(f"Analisando {freq_hz} Hz...")

        t_u, u = ler_sinal(par["entrada"])
        t_y, y = ler_sinal(par["saida"])

        t, u, y = alinhar_sinais(t_u, u, t_y, y)

        # Remove média para melhorar a análise de frequência
        u0 = remover_media(u)
        y0 = remover_media(y)

        plotar_tempo(t, u0, y0, freq_hz)
        plotar_espectros(t, u0, y0, freq_hz)

        ganho_temp, fase_temp, amp_u, amp_y = analise_temporal(t, u0, y0, freq_hz)

        freq_fft, ganho_fft, ganho_fft_db, fase_fft = analise_fft(t, u0, y0, freq_hz)

        erro_ganho = abs(ganho_fft - ganho_temp) / ganho_temp * 100
        erro_fase = abs(fase_fft - fase_temp)

        resultados.append(
            {
                "freq_hz": freq_hz,
                "freq_fft_usada_hz": freq_fft,
                "amp_entrada": amp_u,
                "amp_saida": amp_y,
                "ganho_temporal": ganho_temp,
                "fase_temporal_graus": fase_temp,
                "ganho_fft": ganho_fft,
                "ganho_fft_db": ganho_fft_db,
                "fase_fft_graus": fase_fft,
                "erro_ganho_percentual": erro_ganho,
                "erro_fase_graus": erro_fase,
            }
        )

    df = pd.DataFrame(resultados)
    df = df.sort_values("freq_hz")

    df.to_csv(OUTPUT_DIR / "resultados.csv", index=False)

    plotar_resposta_frequencia(df)

    print("\nAnálise concluída.")
    print(f"Tabela salva em: {OUTPUT_DIR / 'resultados.csv'}")
    print(f"Gráficos salvos em: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
