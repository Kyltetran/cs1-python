def diagonal_sum(matrix):
    n = len(matrix)  # Assuming it's a square matrix
    total = 0

    for i in range(n):
        total += matrix[i][i]  # Summing primary diagonal
        total += matrix[i][n - 1 - i]  # Summing secondary diagonal

    # If the matrix has odd size, the central element will be counted twice
    if n % 2 == 1:
        total -= matrix[n // 2][n // 2]

    return total


# Test the function with the provided example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(diagonal_sum(matrix))
