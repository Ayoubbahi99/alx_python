



#Write a function that computes the square value of all integers of a matrix.
def square_matrix_simple(matrix=[]):
    for arr in matrix:
        for num in arr:
            num = num ** 2
    return matrix