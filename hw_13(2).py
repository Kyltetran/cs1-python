def is_winner_at(i, j, direction, stone_color, game_state_list, n_rows, n_cols):
    i4 = i + 4*direction[0]
    j4 = j + 4*direction[1]
    if 0 <= i4 < n_rows and 0 <= j4 < n_cols:
        # check if there is an unbroken line of five stones
        for k in range(5):
            if game_state_list[i + k*direction[0]][j + k*direction[1]] != stone_color:
                return False

        i_1 = i - direction[0]
        j_1 = j - direction[1]
        i5 = i + 5*direction[0]
        j5 = j + 5*direction[1]
        if stone_color == "w":
            other_stone_color = "b"
        else:
            other_stone_color = "w"

        # check to ensure there are exactly five stones only (i.e.not six or more)
        if (0 <= i_1 < n_rows and 0 <= j_1 < n_cols and game_state_list[i_1][j_1] == stone_color) or \
           (0 <= i5 < n_rows and 0 <= j5 < n_cols and game_state_list[i5][j5] == stone_color):
            return False

        # check to ensure neither end is blocked
        if (0 <= i_1 < n_rows and 0 <= j_1 < n_cols and game_state_list[i_1][j_1] == other_stone_color) and \
           (0 <= i5 < n_rows and 0 <= j5 < n_cols and game_state_list[i5][j5] == other_stone_color):
            return False

        # if there is no violation then return True
        return True
    return False


def get_winner(game_state_list):
    stone_color_to_player = {"b": "black", "w": "white"}
    n_rows = len(game_state_list)
    n_cols = len(game_state_list[0])
    for i in range(n_rows):
        for j in range(n_cols):
            # [Horizontal, vertical, diagonal, antidiagonal]
            for direction in [[0, 1], [1, 0], [1, 1], [1, -1]]:
                for stone_color in ["b", "w"]:
                    if is_winner_at(i, j, direction, stone_color, game_state_list, n_rows, n_cols):
                        return stone_color_to_player[stone_color]
    return "none"


print(get_winner([["", "", "w", "", "", ""],
                  ["", "b", "w", "", "", ""],
                  ["", "", "w", "b", "", ""],
                  ["", "", "w", "", "", ""],
                  ["", "b", "w", "", "", ""],
                  ["", "", "b", "", "", ""],
                  ["", "", "", "b", "", ""]]))


print(get_winner([["", "", "w", "", "", ""],
                  ["", "", "w", "", "", ""],
                  ["w", "b", "b", "b", "b", "b"],
                  ["", "", "w", "", "", ""],
                  ["", "", "w", "", "", ""],
                  ["", "", "", "", "", ""]]))


print(get_winner([["", "", "", "", "", ""],
                  ["", "", "", "", "", "w"],
                  ["", "", "b", "", "w", ""],
                  ["", "", "", "w", "", ""],
                  ["", "b", "w", "", "", ""],
                  ["", "w", "b", "", "", ""],
                  ["b", "", "", "b", "", ""]]))


print(get_winner([["w", "", "", "", "", ""],
                  ["", "b", "", "", "", ""],
                  ["", "", "b", "", "w", ""],
                  ["", "", "w", "b", "", ""],
                  ["", "", "w", "", "b", ""],
                  ["", "w", "", "", "", "b"],
                  ["", "", "", "", "", ""]]))


print(get_winner([["", "", "", "", "", "", ""],
                  ["w", "b", "b", "b", "b", "b", "w"],
                  ["", "w", "", "", "", "", ""],
                  ["", "", "w", "", "", "", ""],
                  ["", "", "", "w", "", "", ""],
                  ["", "", "", "", "w", "", ""],
                  ["", "", "", "", "", "b", ""],
                  ["", "", "", "", "", "", ""]]))


print(get_winner([["", "", "", "", "", "", "", "", ""],
                  ["", "b", "w", "w", "w", "w", "w", "", "b"],
                  ["", "", "b", "w", "b", "b", "", "w", ""],
                  ["", "", "", "b", "", "", "b", "", ""],
                  ["", "", "", "", "", "", "", "", ""]]))


print(get_winner([["w", "", "", "", "", "", ""],
                  ["", "b", "", "", "", "", ""],
                  ["", "", "b", "", "", "", ""],
                  ["", "", "w", "b", "", "", ""],
                  ["", "", "w", "", "b", "", ""],
                  ["", "w", "", "", "", "b", ""],
                  ["", "", "", "", "", "", "w"],
                  ["", "", "", "", "", "", ""]]))


print(get_winner([["w", "", "", "", "", "", ""],
                  ["", "b", "", "", "", "", ""],
                  ["", "", "b", "", "", "", ""],
                  ["", "", "w", "b", "", "", ""],
                  ["", "", "w", "", "b", "", ""],
                  ["", "w", "w", "", "", "b", ""],
                  ["", "", "w", "", "", "", "b"],
                  ["", "", "", "", "", "", ""]]))


print(get_winner([["", "", "", "", "", "", "", "", ""],
                  ["", "b", "", "", "", "w", "", "", ""],
                  ["", "", "b", "w", "b", "", "", "", ""],
                  ["", "", "w", "b", "b", "", "b", "b", ""],
                  ["", "", "w", "", "b", "", "", "", ""],
                  ["", "w", "w", "", "", "w", "", "", ""],
                  ["", "", "w", "", "", "", "", "", ""]]))
