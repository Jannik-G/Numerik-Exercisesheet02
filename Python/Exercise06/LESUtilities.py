def solve(matrix, vector, n, use_permutations):
    transformed_matrix, transformed_vector = gaussElimination(matrix, vector, n, use_permutations)
    solution = backwardsSubstitution(transformed_matrix, transformed_vector, n)
    return solution, transformed_matrix, transformed_vector


def gaussElimination(orig_matrix, orig_vector, n, use_permutations):
    matrix, vector = copyLES(orig_matrix, orig_vector)

    for column in range(0, n-1):

        if use_permutations:
            permutate(matrix, vector, column, n)

        for row in range(column+1, n):
            l = matrix[row][column] / matrix[column][column]

            for k in range(column, n):
                matrix[row][k] = matrix[row][k] - l * matrix[column][k]

            vector[row] = vector[row] - l * vector[column]

    return matrix, vector


def backwardsSubstitution(matrix, vector, n):
    solution = [0 for i in range(0, n)]

    for row in range(n-1, -1, -1):
        s = 0
        for column in range(row+1, n):
            s += matrix[row][column] * solution[column]

        solution[row] = (vector[row] - s) / matrix[row][row]

    return solution


def copyLES(matrix, vector):
    return matrix.copy(), vector.copy()


def permutate(matrix, vector, column_index, n):
    next_row_index = findNextRow(matrix, column_index, n)
    swapRows(matrix, column_index, next_row_index)
    swapRows(vector, column_index, next_row_index)


def findNextRow(matrix, column_index, n):
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