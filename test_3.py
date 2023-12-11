def check_queens(game_state_list):
    n_rows = len(game_state_list)
    n_cols = len(game_state_list[0])

    # def on_board(row, col):
    #     return 0 <= row < n_rows and 0 <= col < n_cols

    # def _check_queens(i, j, direction, game_state_list, n_rows, n_cols):
    #     for  in range(len(n_rows)):
    #         if not on_board(row + i * delta_row, col + i * delta_col):
    #             return False

    # for row in range(n_rows):
    #     for col in range(n_cols):
    #         for direction in [[0, 1], [1, 0], [1, 1], [1, -1]]:
    #             if _check_queens(row, col, direction, game_state_list, n_rows, n_cols):
    #                 return 'Yes'
    # return 'No'

    for row in range(n_rows):
        for col in range(n_cols):
            if row[col] != "" and \
               (row[col] == row[i] for i in range(n_cols)):
                return "Yes"

            if game_state_list[row][col] != "":
                if all(game_state_list[row][col] == game_state_list[row+i][col] for i in range(1, 5)):
                    if (row == 0 or game_state_list[row-1][col] != game_state_list[row][col]) and \
                       (row + 5 >= game_state_list or game_state_list[row+5][col] != game_state_list[row][col]):
                        return "Yes"

    return 'No'


def multiply_poly(lst1, lst2):
    if lst1 == [] or lst2 == []:
        return []
    else:
        return [lst1[0] * lst2[-1]] + multiply_poly(lst1[1:], lst2[1:])
