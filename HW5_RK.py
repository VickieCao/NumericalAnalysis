import pandas as pd
from math import *

def f(t, x):
    y = cos(t) - sin(x) + t**2
    return y


h = 0.2
t = -1.0
x = 3

result_list = [[0, t, x]]
for i in range(1, 11):
    k1 = f(t, x)
    k2 = f(t + h/2, x + (h/2)*k1)
    k3 = f(t + h/2, x + (h/2)*k2)
    k4 = f(t + h, x + h*k3)
    x = x + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    t = t + h
    result_list.append([i, "{0:.1f}".format(t), x])

result = pd.DataFrame(result_list)
result.to_excel("HW5_Q5.xlsx")
print(result)
