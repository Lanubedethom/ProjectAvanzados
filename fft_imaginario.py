import numpy as np
import matplotlib.pyplot as plt
import time


def FFT(P):
    """
        Calcula la transformada rapida de Fourier de manera
        recursiva y usando el concepto de matriz de Vandermont en
        imaginarios para un polinomio P
        :param P: Lista de coeficientes del polinomio
        :return: Lista de coeficientes de la transformada de Fourier del polinomio
    """
    n = len(P)
    if n == 1:
        return P

    w = np.exp(-2 * np.pi * 1j / n)

    Pe, Po = P[::2], P[1::2]
    ye, yo = FFT(Pe), FFT(Po)

    y = [0] * n

    for j in range(n // 2):
        y[j] = ye[j] + (w**j) * yo[j]
        y[j + n // 2] = ye[j] - (w**j) * yo[j]

    return y


def IFFT(P):
    """
        Calcula la transformada rapida de Fourier inversa de un polinomio P
        usando el concepto de matriz de Vandermont en imaginarios
        :param P: Lista de coeficientes de la transformada de Fourier del polinomio
        :return: Lista de coeficientes del polinomio resultado original
    """
    n = len(P)
    if n == 1:
        return P

    w = np.exp(2 * np.pi * 1j / n)

    Pe, Po = P[::2], P[1::2]
    ye, yo = IFFT(Pe), IFFT(Po)

    y = [0] * n

    for j in range(n // 2):
        y[j] = ye[j] + (w**j) * yo[j]
        y[j + n // 2] = ye[j] - (w**j) * yo[j]

    return y


def multiplicar_polinomios(A, B):
    """
        Multiplica dos polinomios A y B utilizando la Transformada Rapida de Fourier (FFT).
        :param A: Lista de coeficientes del primer polinomio
        :param B: Lista de coeficientes del segundo polinomio
        :return: Lista de coeficientes del polinomio resultado de la multiplicacion
    """
    m = len(A)
    n = len(B)
    k = 2 ** (int(np.log2(m + n - 1)) + 1)

    A.extend([0] * (k - m))
    B.extend([0] * (k - n))

    ya = FFT(A)
    yb = FFT(B)

    yc = [ya[i] * yb[i] for i in range(k)]

    C = [int((val / k).real + 0.5) for val in IFFT(yc)]

    return C


def main():

    tiempos = []
    tamagnos = [2**i for i in range(1, 11)]

    for tamn in tamagnos:
        A = [np.random.rand() for _ in range(tamn)]
        B = [np.random.rand() for _ in range(tamn)]

        inicio = time.perf_counter()
        C = multiplicar_polinomios(A, B)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    plt.plot(tamagnos, tiempos, marker='o')
    plt.xlabel('Tamaño del polinomio')
    plt.ylabel('Tiempo de ejecucion (s)')
    plt.title('Tiempo de ejecucion para FFT con imaginarios')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()


if __name__ == '__main__':
    main()
