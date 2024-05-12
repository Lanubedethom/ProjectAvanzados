import numpy as np
import time

def vandermonde_eval(P, x):
    """
    Evaluar el polinomio en la matriz de Vandermonde.
    :param P: Lista de coeficientes del polinomio.
    :param x: Puntos en los que se evaluará el polinomio.
    :return: Lista de ys evaluados en la matriz de Vandermonde usando reales.
    """
    y = []
    for xi in x:
        valor = sum(coef * xi**i for i, coef in enumerate(P))
        y.append(valor)
    return y

def interpolacion_lagrange(x, y):
    """
    Calcula los coeficientes del polinomio interpolante de Lagrange.
    :param x: Lista de valores de x.
    :param y: Lista de valores de y.
    :return: Lista de coeficientes del polinomio interpolante.
    """
    n = len(x)
    P = np.zeros(n)

    for k in range(n):
        L = np.array([y[k]])
        for j in range(n):
            if j != k:
                L = np.convolve(L, np.array([-x[j], 1]), mode='full')
                if (x[k] - x[j] > 1e-9):
                    L = L / (x[k] - x[j])
        P = np.add(P, L)
    return P

def multiplicar_polinomios(A, B):
    """
    Multiplica dos polinomios A y B utilizando la interpolación de Lagrange.
    :param A: Lista de coeficientes del primer polinomio.
    :param B: Lista de coeficientes del segundo polinomio.
    :param x: Puntos en los que se evaluarán los polinomios.
    :return: Lista de coeficientes del polinomio resultado de la multiplicación.
    """
    x = np.linspace(-1, 1, len(A) + len(B) - 1)
    # Evaluar los polinomios en los puntos x
    y_A = vandermonde_eval(A, x)
    y_B = vandermonde_eval(B, x)
    
    # Multiplicar los valores resultantes punto a punto
    y_producto = [a * b for a, b in zip(y_A, y_B)]
    C = [int(c) for c in interpolacion_lagrange(x, y_producto)]
    
    # Interpolar para obtener los coeficientes del polinomio resultante
    return C

def appFFT_Lagrange(A, B):
    inicio = time.perf_counter()
    C = multiplicar_polinomios(A, B)
    fin = time.perf_counter()
    tiempoMS = (float(fin) - float(inicio))*1000
    return tiempoMS, C

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
        print("Tiempo: ", tiempos)
        print("Respuesta: ", C)
    #return tiempos, tamagnos

if __name__ == '__main__':
    main()
