def cube_sum(n):
    if n == 1:
        return 1
    else:
        return n**3 + cube_sum(n-1)


print(['cube_sum(2)', cube_sum(2)])
print(['cube_sum(4)', cube_sum(4)])


def sum(lst):
    if lst == []:
        return 0
    else:
        return lst[0] + sum(lst[1:])


print(['sum([1, 2, 4])', sum([1, 2, 4])])


def get_even_sum(lst):
    if lst == []:
        return 0
    else:
        if lst[0] % 2 == 0:
            return lst[0] + get_even_sum(lst[1:])
        else:
            return get_even_sum(lst[1:])


print(['get_even_sum([1, 2, 4])', get_even_sum([1, 2, 4])])


def is_palindrome(input_str):
    if input_str == '':
        return True
    else:
        # if input_str[0] == input_str[-1]:
        if input_str == input_str[::-1]:
            return is_palindrome(input_str[1:-1])
        else:
            return False


print(is_palindrome('tet'))
print(is_palindrome('abccba'))
print(is_palindrome('abcbaa'))
