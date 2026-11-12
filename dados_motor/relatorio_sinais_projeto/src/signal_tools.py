from pathlib import Path

import numpy as np
import pandas as pd


def ler_sinal(caminho):
    """
    Lê CSV com colunas Time e Value.
    Retorna:
        t: vetor de tempo
        x: vetor de potencial
    """
    df = pd.read_csv(caminho, sep=None, engine="python")

    df.columns = [c.strip() for c in df.columns]

    if "Time" not in df.columns or "Value" not in df.columns:
        raise ValueError(f"{caminho} precisa ter colunas Time e Value.")

    t = pd.to_numeric(
        df["Time"].astype(str).str.replace(",", ".", regex=False), errors="coerce"
    )

    x = pd.to_numeric(
        df["Value"].astype(str).str.replace(",", ".", regex=False), errors="coerce"
    )

    dados = pd.DataFrame({"t": t, "x": x}).dropna()

    return dados["t"].to_numpy(), dados["x"].to_numpy()


def obter_pares(data_dir):
    """
    Procura pares do tipo:
        entrada: e_8_5.csv
        saída:   f8_5.csv
    """
    data_dir = Path(data_dir)
    pares = []

    for entrada in sorted(data_dir.glob("e_*.csv")):
        codigo_freq = entrada.stem.replace("e_", "")
        saida = data_dir / f"f{codigo_freq}.csv"

        if not saida.exists():
            print(f"Aviso: saída não encontrada para {entrada.name}")
            continue

        freq_hz = float(codigo_freq.replace("_", "."))

        pares.append({"freq_hz": freq_hz, "entrada": entrada, "saida": saida})

    return pares


def alinhar_sinais(t_u, u, t_y, y):
    """
    Garante que entrada e saída usem o mesmo vetor de tempo.
    Se necessário, interpola a saída no tempo da entrada.
    """
    if len(t_u) == len(t_y) and np.allclose(t_u, t_y):
        return t_u, u, y

    y_interp = np.interp(t_u, t_y, y)
    return t_u, u, y_interp


def remover_media(x):
    return x - np.mean(x)


def ajuste_senoidal(t, x, freq_hz):
    """
    Ajusta x(t) aproximadamente como:

        x(t) = A sen(wt + phi) + offset

    Retorna amplitude e fase.
    """
    w = 2 * np.pi * freq_hz

    matriz = np.column_stack([np.sin(w * t), np.cos(w * t), np.ones_like(t)])

    coef, _, _, _ = np.linalg.lstsq(matriz, x, rcond=None)

    a = coef[0]
    b = coef[1]
    offset = coef[2]

    amplitude = np.sqrt(a**2 + b**2)
    fase_rad = np.arctan2(b, a)
    fase_graus = np.degrees(fase_rad)

    return amplitude, fase_graus, offset


def analise_temporal(t, u, y, freq_hz):
    """
    Calcula ganho e fase pela forma temporal.
    Funciona melhor para sinais senoidais.
    """
    amp_u, fase_u, _ = ajuste_senoidal(t, u, freq_hz)
    amp_y, fase_y, _ = ajuste_senoidal(t, y, freq_hz)

    ganho = amp_y / amp_u
    fase = fase_y - fase_u

    # Ajusta fase para ficar entre -180 e 180 graus
    fase = (fase + 180) % 360 - 180

    return ganho, fase, amp_u, amp_y


def calcular_fft(t, x):
    """
    Calcula FFT de um sinal real.
    Retorna frequências positivas e magnitude complexa.
    """
    x = remover_media(x)

    dt = np.mean(np.diff(t))
    n = len(t)

    freq = np.fft.rfftfreq(n, d=dt)
    X = np.fft.rfft(x)

    return freq, X


def analise_fft(t, u, y, freq_hz):
    """
    Calcula G(jw) = Y(jw) / U(jw) na frequência desejada.
    """
    freq, U = calcular_fft(t, u)
    _, Y = calcular_fft(t, y)

    idx = np.argmin(np.abs(freq - freq_hz))

    G = Y[idx] / U[idx]

    ganho = np.abs(G)
    ganho_db = 20 * np.log10(ganho)
    fase = np.angle(G, deg=True)

    return freq[idx], ganho, ganho_db, fase


def espectro_simples(t, x):
    """
    Retorna frequência e magnitude normalizada para plot.
    """
    freq, X = calcular_fft(t, x)

    n = len(t)
    mag = np.abs(X) / n

    if len(mag) > 1:
        mag[1:] = 2 * mag[1:]

    return freq, mag
