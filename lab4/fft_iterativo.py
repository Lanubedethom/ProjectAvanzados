import numpy as np
import matplotlib.pyplot as plt
import time


def bit_reverso(n):
    """
        Realiza el bit reverso de un numero n
        :param n: Numero entero al que se le va a realizar el bit reverso
        :return: Lista de indices con los bits invertidos
        ...
    """
    num_bits = int(np.log2(n))
    indices_reversos = [0] * n
    for i in range(n):
        indices_reversos[i] = int(
            format(i, '0' + str(num_bits) + 'b')[::-1], 2)
    return indices_reversos


def FFT(P):
    """
        Calcula la transformada rapida de Fourier usando iteracion
        y el concepto de operacion butterfly o mariposa para un polinomio P
        :param P: Lista de coeficientes del polinomio
        :return: Lista de coeficientes de la transformada de Fourier del polinomio
        ...
    """

    n = len(P)
    indices = bit_reverso(n)
    P = [P[i] for i in indices]

    for s in range(1, int(np.log2(n)) + 1):
        m = 2 ** s
        w_m = np.exp(-2 * np.pi * 1j / m)
        for k in range(0, n, m):
            w = 1
            for j in range(m // 2):
                t = w * P[k + j + m // 2]
                u = P[k + j]
                P[k + j] = u + t
                P[k + j + m // 2] = u - t
                w = w * w_m

    return P


def IFFT(P):
    """
        Calcula la transformada rapida de Fourier inversa de un polinomio P
        usando iteracion y el concepto de operacion butterfly o mariposa
        :param P: Lista de coeficientes de la transformada de Fourier del polinomio
        :return: Lista de coeficientes del polinomio original
        ...
    """
    n = len(P)
    indices = bit_reverso(n)
    P = [P[i] for i in indices]

    for s in range(1, int(np.log2(n)) + 1):
        m = 2 ** s
        w_m = np.exp(2 * np.pi * 1j / m)
        for k in range(0, n, m):
            w = 1
            for j in range(m // 2):
                t = w * P[k + j + m // 2]
                u = P[k + j]
                P[k + j] = u + t
                P[k + j + m // 2] = u - t
                w = w * w_m

    P = [val / n for val in P]

    return P


def multiplicar_polinomios(A, B):
    """
        Multiplica dos polinomios A y B utilizando la Transformada Rapida de Fourier (FFT).
        :param A: Lista de coeficientes del primer polinomio
        :param B: Lista de coeficientes del segundo polinomio
        :return: Lista de coeficientes del polinomio resultado de la multiplicacion
        ...
    """
    m = len(A)
    n = len(B)
    k = 2 ** (int(np.log2(m + n - 1)) + 1)

    A.extend([0] * (k - m))
    B.extend([0] * (k - n))

    ya = FFT(A)
    yb = FFT(B)

    yc = [ya[i] * yb[i] for i in range(k)]

    C = [int(val.real + 0.5) for val in IFFT(yc)]

    return C

# Módulo que es llamado por otros programas
def appFFT_Iterativo(A, B):
    # ------ INICIO de medicion de tiempo
    inicio = time.perf_counter()
    C = multiplicar_polinomios(A, B)
    fin = time.perf_counter()
    # ------ FIN
    TiempoMS = (float(fin) - float(inicio))*1000
    return TiempoMS, C

def main():
    # para registrar los tiempos de ejecucion para diferentes tamaños de polinomios
    tiempos = []
    tamagnos = [2**i for i in range(1, 11)]

    for tamn in tamagnos:
        A = [np.random.rand() for _ in range(tamn)]
        B = [np.random.rand() for _ in range(tamn)]

        # ------ INICIO de medicion de tiempo
        inicio = time.perf_counter()
        C = multiplicar_polinomios(A, B)
        fin = time.perf_counter()
        # ------ FIN

        tiempos.append(fin - inicio)

    plt.plot(tamagnos, tiempos, marker='o')
    plt.xlabel('Tamaño del polinomio')
    plt.ylabel('Tiempo de ejecucion (s)')
    plt.title('Tiempo de ejecucion para FFT iterativo con bit reverso')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()


if __name__ == '__main__':
    main()

