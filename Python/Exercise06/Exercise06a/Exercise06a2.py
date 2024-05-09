from decimal import Decimal, getcontext

getcontext().prec = 5

A = [[Decimal(-1) / Decimal(100000), Decimal(1)], [Decimal(1), Decimal(2)]]
b = [Decimal(1), Decimal(1)]
n = len(A)


def gaussElimination(matrix, vector):
    matrix = matrix.copy()
    vector = vector.copy()

    for column in range(0, n-1):
        for row in range(column+1, n):
            l = matrix[row][column] / matrix[column][column]

            for k in range(column, n):
                t1 = matrix[row][k]
                t2 = l * matrix[column][k]
                matrix[row][k] = t1 - t2

            vector[row] = vector[row] - l * vector[column]

    return matrix, vector


def backSubstitution(matrix, vector):
    solution = [Decimal(0) for i in range(0, n)]

    for row in range(n-1, -1, -1):
        s = 0
        for column in range(row+1, n):
            s += matrix[row][column] * solution[column]

        t1 = (vector[row] - s)
        t2 = matrix[row][row]
        solution[row] = t1 / t2

    return solution


def solve(matrix, vector):
    transformed_matrix, transformed_vector = gaussElimination(matrix, vector)

    print(f"A^(n) = {transformed_matrix}")
    print(f"b^(n) = {transformed_vector}")

    solution = backSubstitution(transformed_matrix, transformed_vector)
    return solution


#print(f"A = {A}")
#print(f"b = {b}")
print(f"x = {solve(A, b)}")



