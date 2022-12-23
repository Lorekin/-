import math as m
import numpy as np

x = int(input("Введите x:"))
k = 1
p = m.sin(x)
flag = True
while x > 2 * m.pi:
    count = x // (2 * m.pi)
    x -= count * 2 * m.pi
if x > 3 / 2 * m.pi:
    flag = False
    x -= 3 / 2 * m.pi
    k = -1
elif x > m.pi:
    x -= m.pi
    k = -1
elif x > m.pi / 2:
    flag = False
    x -= m.pi / 2
sum = 0
n = 0
delta = 0.0001
delta_1 = m.fabs(p - sum)
while delta_1 > delta:
    if flag:
        sum += k * np.power(-1, n) / m.factorial(2*n+1) * np.power(x, 2*n+1)
    else:
        sum += k * np.power(-1, n) / m.factorial(2*n) * np.power(x, 2*n)
    n += 1
    delta_1 = m.fabs(p - sum)
print(sum)
print(delta_1)
