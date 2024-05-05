import numpy as np

def FFT(P):
    n = len(P)
    if n == 1:
        return P

    vandermonde_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            value = np.cos(2 * np.pi * i * j / n)
            row.append(value)
        vandermonde_matrix.append(row)

    W = np.array(vandermonde_matrix)

    y = np.dot(W, P)

    return y

def IFFT(P):
    n = len(P)
    if n == 1:
        return P

    vandermonde_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            value = np.cos(2 * np.pi * i * j / n)
            row.append(value)
        vandermonde_matrix.append(row)

    transposed_vandermonde_matrix = np.transpose(np.array(vandermonde_matrix))

    W_inv = transposed_vandermonde_matrix / n

    y = np.dot(W_inv, P)

    return y

def multiplicar_polinomios(A, B):
    m = len(A)
    n = len(B)
    k = 2 ** (int(np.log2(m + n - 1)) + 1)

    A.extend([0] * (k - m))
    B.extend([0] * (k - n))

    ya = FFT(A)
    yb = FFT(B)

    yc = np.fft.ifft(np.multiply(ya, yb)).real

    C = [int(round(val)) for val in yc[:m+n-1]]

    return C

def main():
    A = [5, 10, 15] 
    B = [20, 25, 30]

    C = multiplicar_polinomios(A, B) 

    print(C)

if __name__ == "__main__":
    main()
