def get_winner(board):
    """Return the winner of the game Gomoku
       Check the entire board for any UNBLOCKED sequence of EXACTLY five consecutive 'b' (black) or 'w' (white) stones in a horizontal, vertical, or diagonal line

       Parameters
       ----------
       board: a two-dimensional list representing the Gomoku board

       Returns
       -------
       a string indicating the winner: black, white, or none

    """
    # Determine the size of the board
    board_height = len(board)
    board_width = len(board[0])

    # Check if a position is on the board
    def on_board(row, col):
        return 0 <= row < board_height and 0 <= col < board_width

    # Check if a position is blocked by an opponent's stone
    def is_blocked(row, col, color):
        # Only positions within the board can be blocked
        if on_board(row, col):
            # Determine the opponent's color
            opponent_color = 'w' if color == 'b' else 'b'
            return board[row][col] == opponent_color
        return False

    # Check if the sequence is an overline (longer than five of the same color)
    def is_overline(row, col, delta_row, delta_col, color):
        # Check the position immediately before the potential sequence
        start_row, start_col = row - delta_row, col - delta_col
        # Check the position immediately after the potential sequence
        end_row, end_col = row + 5 * delta_row, col + 5 * delta_col
        # If either the start or end position has the same color, it's an overline
        if on_board(start_row, start_col) and board[start_row][start_col] == color:
            return True
        if on_board(end_row, end_col) and board[end_row][end_col] == color:
            return True
        return False

    # Check for a sequence of five of the same color
    def check_sequence(row, col, delta_row, delta_col, color):
        # Check each position in the sequence of five for the correct color
        for i in range(5):
            if not on_board(row + i * delta_row, col + i * delta_col):
                return False
            if board[row + i * delta_row][col + i * delta_col] != color:
                return False
        # If the sequence is overlined, it's not a win
        if is_overline(row, col, delta_row, delta_col, color):
            return False
        # Check for blockage
        blocked_before = is_blocked(row - delta_row, col - delta_col, color)
        blocked_after = is_blocked(
            row + 5 * delta_row, col + 5 * delta_col, color)
        # The sequence is a win only if it's not blocked on both ends
        return not (blocked_before and blocked_after)

    # Check all stones on the board
    for row in range(board_height):
        for col in range(board_width):
            # Only check cells that have a stone
            if board[row][col] in ['b', 'w']:
                color = board[row][col]
                # Check all directions: horizontal, vertical, diagonal down-right, diagonal up-right
                for delta_row, delta_col in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                    # If a winning sequence is found, return the winner
                    if check_sequence(row, col, delta_row, delta_col, color):
                        return "black" if color == 'b' else "white"

    # If no winning sequence is found, return 'none'
    return 'none'
