from decimal import Decimal, getcontext

getcontext().prec = 5

A = [[Decimal(-10), Decimal(1000000)], [Decimal(1), Decimal(2)]]
b = [Decimal(1000000), Decimal(1)]
n = len(A)


def findNextRow(matrix, column_index):
    max_value = 0
    max_index = column_index

    for row in range(column_index, n):
        current_value = abs(matrix[row][column_index])
        if current_value > max_value:
            max_value = current_value
            max_index = row

    return max_index


def swapRows(matrix, row_index_1, row_index_2):
    tmp = matrix[row_index_1]
    matrix[row_index_1] = matrix[row_index_2]
    matrix[row_index_2] = tmp


def gaussElimination(matrix, vector):
    matrix = matrix.copy()
    vector = vector.copy()

    for column in range(0, n-1):
        next_row_index = findNextRow(matrix, column)
        swapRows(matrix, column, next_row_index)
        swapRows(vector, column, next_row_index)

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