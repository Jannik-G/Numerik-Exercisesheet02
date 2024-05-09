from fractions import Fraction
from LESUtilities import solve
from decimal import Decimal, getcontext

def task1():
    matrix = [[Fraction(-1, 100000), Fraction(1, 1)], [Fraction(1, 1), Fraction(2, 1)]]
    vector = [Fraction(1, 1), Fraction(1, 1)]
    n = len(matrix)

    executeTask(1, matrix, vector, n, False)


def task2():
    getcontext().prec = 5

    matrix = [[Decimal(-1) / Decimal(100000), Decimal(1)], [Decimal(1), Decimal(2)]]
    vector = [Decimal(1), Decimal(1)]
    n = len(matrix)

    executeTask(2, matrix, vector, n, False)


def task3():
    getcontext().prec = 5

    matrix = [[Decimal(-1) / Decimal(100000), Decimal(1)], [Decimal(1), Decimal(2)]]
    vector = [Decimal(1), Decimal(1)]
    n = len(matrix)

    executeTask(3, matrix, vector, n, True)


def task4():
    getcontext().prec = 5

    matrix = [[Decimal(-10), Decimal(1000000)], [Decimal(1), Decimal(2)]]
    vector = [Decimal(1000000), Decimal(1)]
    n = len(matrix)

    executeTask(4, matrix, vector, n, True)


def executeTask(task_number, matrix, vector, n, use_permutations):
    solution, transformed_matrix, transformed_vector = solve(matrix, vector, n, use_permutations)
    print(f"===Task ({task_number})===")
    print(f"A^(n) = {transformed_matrix}")
    print(f"b^(n) = {transformed_vector}")
    print(f"x = {solution}\n")


task1()
task2()
task3()
task4()

