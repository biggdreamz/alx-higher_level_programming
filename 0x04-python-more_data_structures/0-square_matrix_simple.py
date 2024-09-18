#!/usr/bin/python3

# Create a new matrix where each element is squared
def square_matrix_simple(matrix=[]):
    return [[element ** 2 for element in row] for row in matrix]
