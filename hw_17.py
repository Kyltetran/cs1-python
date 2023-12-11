def max_black_line_length(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_length = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "b":
                # Check horizontal line
                length = 1
                while j + length < cols and matrix[i][j + length] == "b":
                    length += 1
                max_length = max(max_length, length)

                # Check vertical line
                length = 1
                while i + length < rows and matrix[i + length][j] == "b":
                    length += 1
                max_length = max(max_length, length)

    return max_length


def check_queens(board):
    rows = len(board)
    cols = len(board[0])

    # Helper function to check if a queen attacks another in diagonals
    def attacks_diagonally(row, col):
        for i in range(1, max(rows, cols)):
            if (row + i < rows and col + i < cols and board[row + i][col + i] == "q") or \
               (row - i >= 0 and col - i >= 0 and board[row - i][col - i] == "q") or \
               (row + i < rows and col - i >= 0 and board[row + i][col - i] == "q") or \
               (row - i >= 0 and col + i < cols and board[row - i][col + i] == "q"):
                return True
        return False

    # Check each queen's position
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "q":
                # Check for another queen in the same row or column
                if board[i].count("q") > 1 or [board[x][j] for x in range(rows)].count("q") > 1:
                    return "Yes"

                # Check for another queen in diagonals
                if attacks_diagonally(i, j):
                    return "Yes"

    return "No"
