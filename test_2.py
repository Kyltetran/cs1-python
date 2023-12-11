def count_empty_string(list):
    count = 0
    for x in list:
        for i in x:
            if ' ' in i:
                count += 1
    return count


print(count_empty_string([]))
print(count_empty_string([' ']))
print(count_empty_string(['abc 123', 'ced', 'fly', 'over hype']))
print(count_empty_string([' kylte', 'tran', 'nhu quynh', ' Fulbright26 ']))


def is_symmetric(list):
    if list == list[::-1]:
        return 'Yes'
    else:
        return 'No'


print(is_symmetric([]))
print(is_symmetric([1]))
print(is_symmetric([1, 2, 1]))
print(is_symmetric([1, 2, 2, 1]))
print(is_symmetric([1, 2]))
print(is_symmetric([1, 2, 3]))
print(is_symmetric([1, 2, 2, 4]))
