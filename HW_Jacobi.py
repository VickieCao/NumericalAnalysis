from pandas import *
x1 = [None]*11
x2 = [None]*11
x3 = [None]*11
x1[0] = 0.0
x2[0] = 0.0
x3[0] = 0.0

result = []
for i in range(1, 11):
    new = [i]
    x1[i] = (-1.0 + 2.0*x2[i-1] - 3.0*x3[i-1]) / 5.0
    x2[i] = (2.0 + 3.0*x1[i-1] - x3[i-1]) / 9.0
    x3[i] = (3.0 - 2.0*x1[i-1] + 2.0*x2[i-1]) / (-7.0)
    new.append(x1[i])
    new.append(x2[i])
    new.append(x3[i])
    result.append(new)
    print(i, x1[i], x2[i], x3[i])

table = DataFrame(result)
print(table)

writer = ExcelWriter('HW2_Jacobi.xlsx')
table.to_excel(writer, "sheet1")
writer.save()
