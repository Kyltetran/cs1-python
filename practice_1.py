def deep_reverse(lst):
    if lst == []:
        return lst
    else:
        if isinstance(lst[-1], list):
            return [deep_reverse(lst[-1])] + deep_reverse(lst[:-1])
        else:
            return [lst[-1]] + deep_reverse(lst[:-1])


def one_term_with_a_list(x, lst):
    long_list = []
    for i in lst:
        long_list.append([x[0] * i[0], x[1] + i[1]])
    return long_list


def add_coeff_if_same_expo(long_list):
    short_list = {}
    for element in long_list:
        expo, coeff = list(element)
        if expo in short_list:
            short_list[expo] += coeff
        else:
            short_list[expo] = coeff
    return [[coeff, expo] for expo, coeff in short_list.items() if coeff != 0]


def multiply_poly(lst1, lst2):
    if lst1 == [] or lst2 == []:
        return []
    else:
        return add_coeff_if_same_expo(one_term_with_a_list(lst1[0], lst2), multiply_poly(lst1[1:], lst2))


print(multiply_poly([[1, 1], [1, 0]], [[1, 1], [-1, 0]]))
