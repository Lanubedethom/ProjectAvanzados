import numpy as np


def bit_reverso(n):
    num_bits = int(np.log2(n))
    indices_reversos = [0] * n
    for i in range(n):
        indices_reversos[i] = int(
            format(i, '0' + str(num_bits) + 'b')[::-1], 2)
    return indices_reversos


def FFT(P):
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


def main():
    A = [1, 2, 3]  # A(x) = 1 + 2x + 3x^2
    B = [4, 5, 6]  # B(x) = 4 + 5x + 6x^2

    C = multiplicar_polinomios(A, B)  # C(x) = A(x) * B(x)

    print(C)


main()
