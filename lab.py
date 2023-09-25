import math
a = 4.26
b = 1.71
c = 3.86
x = float(input())
y = math.sin(x**2+a**2)*math.e**(b+x)/math.sqrt(a*(x**3)+c)
print(y)