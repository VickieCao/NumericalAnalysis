import pandas as pd
import numpy as np
from math import *
import matplotlib.pyplot as plt

def f(x):
    y = 1.0 / (1.0 + x**2)
    return y

def Lagrange(X, Y, n, x):
    y = 0
    for i in range(n+1):
        l = 1
        for j in range(n+1):
            if j != i:
                l = l*((x-X[j])/(X[i]-X[j]))
        y = y + l*Y[i]
    return y


def equal_nodes(n):
    h1 = 10.0/n
    X = []
    Y = []
    for i in range(0, n+1):
        x = -5.0 + h1*i
        X.append(x)
    for i in range(0, n+1):
        y = f(X[i])
        Y.append(y)

    h2 = 10.0/(2*n)
    X_2n = []
    Y_2n = []
    for i in range(0, 2*n+1):
        x2 = -5.0 + h2*i
        X_2n.append(x2)
    for i in range(0, 2*n+1):
        y2 = f(X_2n[i])
        Y_2n.append(y2)

    return X, Y, X_2n, Y_2n


def Chebyshev_nodes(n):
    X = []
    for i in range(0, n+1):
        x = 5*cos(pi*(2*i+1)/(2*n+2))
        X.append(x)
    Y = []
    for i in range(0, n+1):
        y = f(X[i])
        Y.append(y)
    return X, Y


def P_equal(n):
    P_2n = []

    interpolating_interval = equal_nodes(n)
    X = interpolating_interval[0]
    Y = interpolating_interval[1]
    X_2n = interpolating_interval[2]
    Y_2n = interpolating_interval[3]

    for i in range(0, 2*n+1):
        p2 = Lagrange(X, Y, n, X_2n[i])
        P_2n.append(p2)

    result_list = [["n = " + str(n), " ", " ", " "]]
    for i in range(len(X_2n)):
        new_row = []
        new_row.append(X_2n[i])
        new_row.append(Y_2n[i])
        new_row.append(P_2n[i])
        new_row.append(abs(P_2n[i] - Y_2n[i]))
        result_list.append(new_row)

    result = pd.DataFrame(result_list)
    result.columns = ['x', 'f(x)', 'p(x)', '|P(x) - f(x)|']

    x_test = 1 + sqrt(10)
    error = abs(Lagrange(X, Y, n, x_test) - f(x_test))

    return result, error


x = np.arange(-5, 5, 0.1)
F = f(x)
P1= Lagrange(equal_nodes(8)[0], equal_nodes(8)[1], 8, x)
P2= Lagrange(Chebyshev_nodes(8)[0], Chebyshev_nodes(8)[1], 8, x)
plt.plot(x, F, linestyle = '-', label = 'f(x)')
plt.plot(x, P1, linestyle = ':', label = 'P(x)_equally spaced notes')
plt.plot(x,P2, linestyle = '--', label = 'P(x)_Chebyshev nodes')
plt.legend()
plt.show()
