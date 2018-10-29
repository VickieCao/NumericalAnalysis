from pandas import *
x1 = [0.0]*11
x2 = [0.0]*11
x3 = [0.0]*11

result = []
for i in range(1, 11):
    new = [i]
    x1[i] = round((-1 + 2*x2[i-1] - 3*x3[i-1]) / 5.0, 6)
    x2[i] = round((2 + 3*x1[i] - x3[i-1]) / 9.0, 6)
    x3[i] = round((3 - 2*x1[i] + 2*x2[i]) / (-7.0), 6)
    new.append(x1[i])
    new.append(x2[i])
    new.append(x3[i])
    result.append(new)
    print(i, x1[i], x2[i], x3[i])

table = DataFrame(result)
print(table)

writer = ExcelWriter('HW2_Gauss_Seidel.xlsx')
table.to_excel(writer, "sheet1")
writer.save()