import numpy as np
from scipy.signal import TransferFunction, lsim


def simular_funcao_transferencia(num, den, entrada, tempo):
    """
    Simula uma função de transferência contínua usando scipy.signal.lsim.

    Exemplo:
    num = [165.7, -2.425]
    den = [1, 9.902]
    """
    sistema = TransferFunction(num, den)

    tout, yout, _ = lsim(sistema, U=entrada, T=tempo)

    return tout, yout


def erro_medio_quadratico(y_real, y_modelo):
    return np.mean((y_real - y_modelo) ** 2)
