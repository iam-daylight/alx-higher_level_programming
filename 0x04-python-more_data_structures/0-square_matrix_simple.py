#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for v in range(len(matrix)):
        new_matrix[v] = list(map(lambda x: x**2, matrix[v]))
    return (new_matrix)
