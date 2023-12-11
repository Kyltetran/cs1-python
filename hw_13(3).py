def _get_winner(i, j, direction, stone, game_state, n_rows, n_cols):
    i5 = i + direction[0]*4
    j5 = j + direction[1]*4
    if 0 <= i5 < n_rows and 0 <= j5 < n_cols:
        for k in range(5):
            if game_state[i + direction[0]*k][j + direction[1]*k] != stone:
                return False

        i0 = i - direction[0]
        j0 = j - direction[1]
        i6 = i + direction[0]*5
        j6 = j + direction[1]*5

        if stone == 'b':
            other_stone = 'w'
        else:
            other_stone = 'b'

        if (0 <= i0 < n_rows and 0 <= j0 < n_cols and game_state[i0][j0] == stone) or \
           (0 <= i6 < n_rows and 0 <= j6 < n_cols and game_state[i6][j6] == stone):
            return False
        if (0 <= i0 < n_rows and 0 <= j0 < n_cols and game_state[i0][j0] == other_stone) and \
           (0 <= i6 < n_rows and 0 <= j6 < n_cols and game_state[i6][j6] == other_stone):
            return False

        return True
    return False


def get_winner(game_state):
    stone_color = {'b': 'black', 'w': 'white'}
    n_rows = len(game_state)
    n_cols = len(game_state[0])
    for i in range(n_rows):
        for j in range(n_cols):
            for direction in [[0, 1], [1, 0], [1, 1], [1, -1]]:
                for stone in ['b', 'w']:
                    if _get_winner(i, j, direction, stone, game_state, n_rows, n_cols):
                        return stone_color[stone]
    return 'none'
