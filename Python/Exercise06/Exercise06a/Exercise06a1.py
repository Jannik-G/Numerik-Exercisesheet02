from fractions import Fraction

A = [[Fraction(-1, 100000), Fraction(1, 1)], [Fraction(1, 1), Fraction(2, 1)]]
b = [Fraction(1, 1), Fraction(1, 1)]
n = len(A)


def gaussElimination(matrix, vector):
    matrix = matrix.copy()
    vector = vector.copy()

    for column in range(0, n-1):
        for row in range(column+1, n):
            l = matrix[row][column] / matrix[column][column]

            for k in range(column, n):
                matrix[row][k] = matrix[row][k] - l * matrix[column][k]

            vector[row] = vector[row] - l * vector[column]

    return matrix, vector


def backSubstitution(matrix, vector):
    solution = [Fraction(0, 1) for i in range(0, n)]

    for row in range(n-1, -1, -1):
        s = 0
        for column in range(row+1, n):
            s += matrix[row][column] * solution[column]

        solution[row] = (vector[row] - s) / matrix[row][row]

    return solution


def solve(matrix, vector):
    transformed_matrix, transformed_vector = gaussElimination(matrix, vector)

    print(f"A^(n) = {transformed_matrix}")
    print(f"b^(n) = {transformed_vector}")

    solution = backSubstitution(transformed_matrix, transformed_vector)
    return solution


def task1():




#print(f"A = {A}")
#print(f"b = {b}")
print(f"x = {solve(A, b)}")



