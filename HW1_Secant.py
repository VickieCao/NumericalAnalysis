
def f(x):
    result = x**4.0 - x - 10.0
    return result

# The reciprocal of the slope of secant line
def slope_re(x,y):
    result = (y-x)/(f(y)-f(x))
    return result

# Initial approximation
a = ['nan']*100
a[0] = 1.0
a[1] = 2.0
a[2] = a[1] - slope_re(a[0], a[1])*f(a[1])

i = 2
while(round(a[i],3) != round(a[i-1],3)):
    a[i+1] = a[i] - slope_re(a[i-1], a[i])*f(a[i])
    print(i-1, a[i-2], ' ', a[i-1], ' ', a[i], '{0:.3f}'.format(f(a[i])))
    i = i + 1

# Print the result of the last step
print(i-1, a[i-2], ' ', a[i-1], ' ', a[i], '{0:.3f}'.format(f(a[i])))