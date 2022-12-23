import numpy as np

if __name__ == '__main__':
    y = [None] * 3
    y[0] = 0.0
    y[1] = 0.50
    y[2] = 0.86603
    h = 1
    arr = [None]*4
    arr[0] = (y[1] - y[0]) / h
    arr[1] = (y[2] - y[1]) / h
    arr[2] = (y[2] - y[0]) / (2*h)
    arr[3] = (y[2] - 2*y[1] + y[0]) / np.power(h, 2)
    print("Левая разность:", arr[0],"\nПравая разность:", arr[1],"\nЦентральная разность:", arr[2],"\nВыражение для производной 2го порядка:", arr[3],)
    n = (arr[0] + arr[1]) / 2
    if n == arr[2]:
        print("Проверка:", True)
    else:
        print("Проверка:", False)

