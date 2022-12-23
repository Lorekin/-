import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

x = [0, 1, 2, 3, 4]
y = [0, 0.5, 0.86603, 1, 0.86603]
x_0 = 1.5


def find_coef_splain(x, y):
    l = len(x)
    c = l - 1
    d = 2*l - 3
    Mlength = (l - 1) * 3 - 1
    M = np.zeros((Mlength, Mlength))
    for i in range(l - 1):
        M[i, i] = x[i + 1] - x[i]
        M[i, d + i] = (x[i + 1] - x[i])**3
        if i != 0:
            M[i, c - 1 + i] = (x[i + 1] - x[i])**2
        if l - 2 > i:
            M[l + i - 1, i], M[l + i - 1, i + 1] = 1, -1
            M[l + i - 1, i + d] = 3*(x[i + 1] - x[i])**2
            if i != 0:
                M[l + i - 1, c - 1 + i] = 2*(x[i + 1] - x[i])
                M[2*l - 3 + i, c + i - 1], M[2*l - 3 + i, c + i] = 1, -1
                M[2*l - 3 + i, d + i] = 3*(x[i + 1] - x[i])
            else:
                M[2*l - 3, c], M[2*l - 3, d] = -1, 3*(x[1] - x[0])
    M[-1, d - 1], M[-1, -1] = 1, 3*(x[-1] - x[2])
    A = np.zeros(Mlength)
    for i in range(l - 1):
        A[i] = y[i + 1] - y[i]
    solve_M = np.linalg.solve(M, A)
    b = solve_M[:c]
    c = np.insert(solve_M[c:d], 0, 0)
    d = solve_M[d:]
    return y[:-1], b, c, d


def find_dot_splain(x, a, b, c, d, x_0):
    for k in range(len(x)):
        if x[k] <= x_0 <= x[k + 1]:
            return a[k] + b[k]*(x_0 - x[k]) + c[k]*((x_0 - x[k])**2) + d[k]*((x_0 - x[k])**3)


def draw_graphic_splain(x, y, a, b, c, d):
    begin, end = x[0], x[-1]
    x_splain = np.arange(begin, end, 0.01)
    y_splain = np.zeros(len(x_splain))
    for i in range(len(x_splain)):
        y_splain[i] = find_dot_splain(x, a, b, c, d, x_splain[i])
    plt.plot(x_splain, y_splain)
    plt.scatter(x, y, color="red")
    plt.grid()
    plt.show()


if __name__ =='__main__':
    a, b, c, d = find_coef_splain(x, y)
    print(f"Значение в т. x = {x_0}:  ", find_dot_splain(x, a, b, c, d, x_0))
    draw_graphic_splain(x, y, a, b, c, d)
