import numpy as np


def FFT(P):
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
    A = [1, 2, 3]  # A(x) = 1 + 2x + 3x^2
    B = [4, 5, 6]  # B(x) = 4 + 5x + 6x^2

    C = multiplicar_polinomios(A, B)  # C(x) = A(x) * B(x)

    print(C)


main()
