import pandas as pd
import numpy as np
from math import *


def f(x):
    y = exp(x) * cos(x)
    return y


def comp_trapezoidal(a, b, n):
    h = (b - a) / n
    S = 0
    for i in range(1, n):
        xi = a + i*h
        S = S + 2 * f(xi)

    S = S + f(a) + f(b)
    integration = (h/2) * S

    return integration


def simpson(a, b):
    y = (b - a)/6
    y = y * (f(a) + 4*f((a+b)/2) + f(b))
    return y

def comp_simpson(a, b, n):
    h = (a + b) / n
    integration = 0
    for i in range(n):
        ai = a + i*h
        bi = ai + h
        sub_int = simpson(ai, bi)
        integration = integration + sub_int

    return integration

int_result = []
exact = -0.5 * (exp(pi) + 1.0)
for n in [2, 4, 8, 16, 32, 64, 128]:
    I_trap = comp_trapezoidal(0, pi, n)
    error_trap = exact - I_trap
    I_simp = comp_simpson(0, pi, n)
    error_simp = exact - I_simp
    I_trap = "{0:.10f}".format(I_trap)
    error_trap = "{0:.10f}".format(error_trap)
    I_simp = "{0:.10f}".format(I_simp)
    error_simp = "{0:.10f}".format(error_simp)
    new = [n, I_trap, error_trap, I_simp, error_simp]
    int_result.append(new)

result = pd.DataFrame(int_result)
result.columns = ['n', 'I(f): Trapezoidal', 'En: Trapezoidal', 'I(f): Simpson', 'En: Simpson']
result.to_excel('Assignment4_Q5.xlsx')
print(result)
