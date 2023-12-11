def is_at_least_two_even(list):
    count = 0
    for x in list:
        if x % 2 == 0:
            count = count + 1
    # for i in range(len(list)):
    #   if (list[i] % 2 == 0):
    #       count = count + 1
    print(count)
    if count >= 2:
        return 'Yes'
    else:
        return 'No'


print(is_at_least_two_even([True, False, 4.0]))
print(is_at_least_two_even(['abc', 2, 1]))
print(is_at_least_two_even([1.5, 2, 1]))
