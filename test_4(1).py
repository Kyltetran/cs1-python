def move(game_state, tetromino_type, position, movement_direction):
    # Copy the board to avoid modifying the original
    new_board = [row[:] for row in game_state]
    rows, cols = len(game_state), len(game_state[0])
    row, col = position

    # Remove the tetromino from its current position
    if tetromino_type == 'straight':
        for i in range(4):
            if 0 <= col + i < cols:
                new_board[row][col + i] = ''
    elif tetromino_type == 'skew':
        if 0 <= col < cols and 0 <= col + 1 < cols and 0 <= row - 1 < rows:
            new_board[row][col] = 'x'
            new_board[row][col + 1] = 'x'
            new_board[row + 1][col - 1] = 'x'
            new_board[row + 1][col] = ''

    # Move the tetromino
    if movement_direction == 'down' and row < rows - 1:
        new_row = row + 1
    elif movement_direction == 'left' and col > 0:
        col -= 1
        new_row = row
    elif movement_direction == 'right' and col < cols - 4:  # Adjusted for the 'straight' tetromino
        col += 1
        new_row = row
    else:
        new_row = row  # No movement in case of boundary

    # Place the tetromino in its new position
    if tetromino_type == 'straight':
        for i in range(4):
            if 0 <= col + i < cols:
                new_board[new_row][col + i] = 'x'
    elif tetromino_type == 'skew':
        if 0 <= col < cols and 0 <= col + 1 < cols and 0 <= new_row + 1 < rows:
            new_board[new_row][col] = 'x'
            new_board[new_row][col + 1] = 'x'
            new_board[new_row + 1][col - 1] = 'x'
            new_board[new_row + 1][col] = 'x'

    return new_board, [new_row, col]


print(move([
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', 'x', 'x', 'x', 'x', ''],
    ['', '', '', '', '', ''],
    ['x', '', 'x', '', '', '']],
    'straight', [6, 1], 'down'))

print(move([['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', 'x', 'x', 'x', 'x', ''],
            ['', '', '', '', '', ''],
            ['x', '', 'x', '', '', '']],
           'straight', [6, 1], 'left'))

print(move([['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', 'x', 'x', ''],
            ['', '', 'x', 'x', '', ''],
            ['', 'x', '', 'x', '', '']],
           'skew', [7, 2], 'down'))

print(move([['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', 'x', 'x', ''],
            ['', '', 'x', 'x', '', ''],
            ['', 'x', '', 'x', '', '']],
           'skew', [7, 2], 'right'))
