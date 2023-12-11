def is_arithmetic_seq(lst):
    # Base cases for lists with less than two elements
    if len(lst) < 2:
        return "Yes"

    # Start the recursive check from the second element
    return _is_arithmetic_seq(lst, 1, lst[1] - lst[0])


def _is_arithmetic_seq(lst, index, common_diff):
    # If we've reached the end of the list, it's an arithmetic sequence
    if index == len(lst) - 1:
        return "Yes"

    # Check if the current pair of elements have the correct difference
    if lst[index + 1] - lst[index] != common_diff:
        return "No"

    # Recursively check the next pair
    return _is_arithmetic_seq(lst, index + 1, common_diff)


# Test cases
print(is_arithmetic_seq([]))          # "Yes"
print(is_arithmetic_seq([1]))         # "Yes"
print(is_arithmetic_seq([1, 2, 3]))   # "Yes"
print(is_arithmetic_seq([-1, 2, 5, 8]))  # "Yes"
print(is_arithmetic_seq([1, 3, 6]))   # "No"
print(is_arithmetic_seq([1, 4, 7, 4]))  # "No"


def deep_reverse(lst):
    if len(lst) == 0:
        return lst
    else:
        if type(lst[0] == 2):
            return deep_reverse(lst[1:]) + deep_reverse(lst[0])
        else:
            return deep_reverse(lst[1:]) + [lst[0]]


print(deep_reverse([1, 2, 3]))
print(deep_reverse([1, [2, 3], 4]))
print(deep_reverse([1, [2, [3, 4], [5, [6, 7], 8]]]))
