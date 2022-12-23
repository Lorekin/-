import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import math as m


x = [None] * 5
y = [None] * 5
for i in range(4):
    x[i] = m.pi*np.double(input(f"Введите x{i}:"))
    y[i] = np.sin(x[i])
x[4] = m.pi*np.double(input(f"Введите x*:"))
y[4] = np.sin(x[4])


def coef(x, y):
    a = [None]*4
    for i in range(4):
        a[i] = y[i]
    for j in range(1, 4):
        for i in range(3, j - 1, -1):
            a[i] = (a[i] - a[i - 1]) / (x[i] - x[i - j])
    return a


def polynom(a,b,c):
    arr = [None]*4
    vial0 = b*c
    vial1 = b+c
    arr[0] = 1
    arr[1] = -(vial1 + a)
    arr[2] = vial1*a+vial0
    arr[3] = -vial0*a
    return arr

def P4(a,x):
    temp = [None]*4
    for i in range(4):
            temp[i] = a[3]*polynom(x[0], x[1], x[2])[i]
    temp[1] += a[2]
    temp[2] += a[2]*(-x[0]-x[1]) + a[1]
    temp[3] += a[2]*x[0]*x[1] + a[1]*-x[0] + a[0]
    return temp


def k(y, x):
    coef = [None] * 4
    for j in range(4):
        coef[j] = y[j]/((x[j] - x[(j+1) % 4]) * (x[j] - x[(j+2) % 4]) * (x[j] - x[(j+3) % 4]))
    return coef


def L4(x):
    pol = [0]*4
    for i in range(4):
        pol[0] += k(y, x)[i] * polynom(x[(i+1) % 4], x[(i+2) % 4], x[(i+3) % 4])[0]
        pol[1] += k(y, x)[i] * polynom(x[(i+1) % 4], x[(i+2) % 4], x[(i+3) % 4])[1]
        pol[2] += k(y, x)[i] * polynom(x[(i+1) % 4], x[(i+2) % 4], x[(i+3) % 4])[2]
        pol[3] += k(y, x)[i] * polynom(x[(i+1) % 4], x[(i+2) % 4], x[(i+3) % 4])[3]
    return pol


def point(func,point):
    return np.polyval(func, point)


def plot(y1,y2,y):
    XNEW = np.linspace(np.min(x), np.max(x), 100)
    YNEW1 = point(y1,XNEW)
    YNEW2 = point(y2,XNEW)
    yi = np.sin(XNEW)
    plt.plot(XNEW,YNEW1,"-",XNEW,YNEW2,"-",XNEW,yi)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    test1 = L4(x)
    test2 = P4(coef(x,y) ,x)
    print("P4(x) =", test2[0], "*x^3 +", test2[1], "*x^2 +", test2[2], "*x +", test2[3])
    print("L4(x) =", test1[0], "*x^3 +", test1[1], "*x^2 +", test1[2], "*x +", test1[3])
    test3 = point(test2, x[4])
    test4 = point(test1, x[4])
    print("sin(", x[4], ") =", y[4])
    print("P4(",  x[4], ") =", test3)
    print("L4(",  x[4], ") =", test4)
    delta_arr = [None]*4
    for i in range(4):
        delta_arr[i] = abs(test1[i]-test2[i])
    print("delta_P4:", abs(y[4]-test4))
    print("delta_L4:", abs(y[4]-test3))
    print("delta_arr:", delta_arr)

    plot(test1,test2,y)


