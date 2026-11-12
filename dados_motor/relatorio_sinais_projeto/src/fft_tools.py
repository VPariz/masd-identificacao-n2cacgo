import numpy as np
from scipy.signal import find_peaks

from .signal_tools import remover_media


def calcular_fft(t, x, remover_dc=True):
    """
    Calcula FFT de um sinal.

    Retorna:
    freq_pos -> frequências positivas
    X_pos    -> FFT nas frequências positivas
    fs       -> frequência de amostragem
    """
    dt = np.mean(np.diff(t))
    fs = 1 / dt
    n = len(t)

    if remover_dc:
        x = remover_media(x)

    X = np.fft.fft(x)
    freq = np.fft.fftfreq(n, d=dt)

    idx = freq > 0

    freq_pos = freq[idx]
    X_pos = X[idx] / n

    return freq_pos, X_pos, fs


def calcular_resposta_frequencia(t, entrada, saida):
    """
    Calcula G(jw) = Y(jw) / U(jw)
    """
    freq, U, fs = calcular_fft(t, entrada)
    _, Y, _ = calcular_fft(t, saida)

    eps = 1e-12
    G = Y / (U + eps)

    modulo = np.abs(G)
    modulo_db = 20 * np.log10(modulo)
    fase_graus = np.angle(G, deg=True)

    return freq, G, modulo, modulo_db, fase_graus, fs


def pegar_valor_em_frequencia(freq, G, f_alvo):
    """
    Pega ganho e fase na frequência mais próxima de f_alvo.
    """
    idx = np.argmin(np.abs(freq - f_alvo))

    f_real = freq[idx]
    ganho = np.abs(G[idx])
    ganho_db = 20 * np.log10(ganho)
    fase_graus = np.angle(G[idx], deg=True)

    return {
        "f_alvo_hz": f_alvo,
        "f_real_hz": f_real,
        "ganho": ganho,
        "ganho_db": ganho_db,
        "fase_graus": fase_graus,
    }


def encontrar_picos(freq, X, altura_relativa=0.05):
    """
    Encontra picos relevantes no espectro.
    """
    mag = np.abs(X)
    altura_minima = altura_relativa * np.max(mag)

    indices, propriedades = find_peaks(mag, height=altura_minima)

    return freq[indices], mag[indices], indices
