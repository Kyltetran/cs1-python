def add_two(x, y):
    return x + y


test_case = [(1, 2, 3), (2, 4, 6), (3, 5, 8)]
test_num = 0
for x, y, expected_result in test_case:
    if add_two(x, y) == expected_result:
        test_num += 1
    else:
        test_num = test_num
