#Initial approximation
a = 1.0
b = 2.0

def f(x):
    result = x**4.0 - x - 10.0
    return result

i = 0
c = 0.0
while round((a+b)/2, 3) != round(c,3):
    c = (a+b)/2
    print(i, ' ', a, ' ', b, ' ', c, ' ', '{0:.3f}'.format(f(c)))

    if (f(a)*f(c)) < 0:
        a = a
        b = c
    else:
        a = c
        b = b
    i = i + 1

# Print the result of last step
print(i, ' ', a, ' ', b, ' ', round((a+b)/2,3), ' ', '{0:.3f}'.format(f((a+b)/2)))