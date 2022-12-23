def f(x):
    return x / (2 * x + 5)


def S(m, n):
    sum = 0
    for i in range(m, n):
        sum += y[i]
    return sum


if __name__ == '__main__':
    a = -1
    b = 1
    h = 0.5
    n = int((b - a) / h + 1)
    x = [None] * n
    y = [0] * n
    x[0] = a
    y[0] = f(x[0])
    for i in range(1, n):
        x[i] = x[i - 1] + h
        y[i] = f(x[i])
    f = h * ((y[0] + y[n - 1]) / 2 + S(1, n - 1))
    f1 = h / 3 * ((y[0] + y[n - 1]) + 4 * (y[1] + y[3]) + 2 * y[2])
    f_left = h * S(0, n - 1)
    f_right = h * S(1, n)
    sum = 0
    h1 = (b - a) / n
    for i in range(n):
        j = -1 + h1 * (h + i)
        sum += j / (2 * j + 5)
    f_middle = h1 * sum
    print("Метод Трапеции:", f)
    print("Метод Симпсона:", f1)
    print("Левые прямоугольники:", f_left, "\nПравые прямоугольники:", f_right, "\nСредние прямоугольники:", f_middle)
