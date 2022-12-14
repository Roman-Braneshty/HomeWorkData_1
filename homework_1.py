import numpy as np

"""Задача 1)"""

coefficient = np.array([[1, 1, 1], [0.05, 0.07, 0], [0.05, 0, 0.06]], dtype=float)
coefficient

money = np.array([50000, 2250, 1400], dtype=float)
money

deposits = np.linalg.solve(coefficient, money)
deposits

print(f'Deposit in bank #1: {deposits[0]}')
print(f'Deposit in bank #2: {deposits[1]}')
print(f'Deposit in bank #3: {deposits[2]}')

"""Задача 2)"""

models = np.array([[1, 1, 1], [1, -1, 1], [1, 1, -1]], dtype=int)
models

count = np.array([1328, 100, 120], dtype=int)
count

quantity = np.linalg.inv(models).dot(count)
quantity

print('Iphone 6  -', int(quantity[0]))
print('Iphone 11 -', int(quantity[1]))
print('Iphone 12 -', int(quantity[2]))

"""Задача 3)"""

points = np.array([[3, 0, 3], [6, 1 / 4, 0], [1, 1 / 3, 1]], dtype=float)
points

diveder = np.array([1, 1, 1])
diveder

decart_points = np.linalg.solve(points, diveder)
decart_points

param = [(1 / i) ** 0.5 for i in decart_points]
param

print(f'Параметри: {param}')

"""Задача 4)"""

first = np.matrix("1, 1, 1; 9, 3, 1; 1, -1, 1")
first

second = np.matrix("12;54;2")
second

result = np.linalg.solve(first, second)
result

print(f'Коефіціент a: {int(result[0])}')
print(f'Коефіціент b: {int(result[1])}')
print(f'Коефіціент c: {int(result[2])}')

"""Задача 5)"""


def get_polynom(coords):
    a = []
    b = []
    for x, y in coords:
        row = []
        b.append(y)
        for i in range(len(coords)):
            row.append(x ** i)
        a.append(row)
    return np.linalg.solve(a, b)


result = get_polynom([(1, 2), (30, 50), (-1, 9)])

print(f'Коэффициенты многочлена: {[i for i in result]}')
