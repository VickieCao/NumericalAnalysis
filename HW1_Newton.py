# Initial approximation
a = 2.0

def f(x):
    result = x**4.0 - x - 10.0
    return result

# f'(x)
def f_1(x):
    result = 4*(x**3) - 1
    return result

i = 0
b = a - f(a)/f_1(a)
while(round(a, 3) != round(b, 3)):
    print(i, ' ', '{0:.3f}'.format(a), '{0:.3f}'.format(f(a)))
    a = b
    b = a - f(a)/f_1(a)
    i = i + 1

# Print the results of last two steps
print(i, ' ', '{0:.3f}'.format(a), '{0:.3f}'.format(f(a)))
print(i+1, ' ', '{0:.3f}'.format(b), '{0:.3f}'.format(f(b)))