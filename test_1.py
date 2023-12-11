def get_age(birth_day, birth_month, birth_year, current_day, current_month, current_year):
    if birth_month > current_month:
        return current_year - birth_year - 1
    elif birth_month == current_month:
        if birth_month > current_month:
            return current_year - birth_year - 1
        else:
            return current_year - birth_year
    else:
        return current_year - birth_year


print(get_age(1, 10, 2023, 4, 10, 2023))
print(get_age(4, 10, 2022, 4, 10, 2023))
print(get_age(4, 12, 2022, 4, 10, 2023))
print(get_age(1, 6, 2022, 4, 10, 2023))
print(get_age(1, 6, 2000, 4, 10, 2023))
print(get_age(6, 10, 2000, 4, 10, 2023))


def is_time_slot_overlapped(start_1, end_1, start_2, end_2):
    if (end_1 > start_2 and end_1 < end_2) or \
       (end_2 > start_1 and end_2 < end_1):
        return 'Yes'
    else:
        return 'No'


print(is_time_slot_overlapped(9, 10, 13, 15))
print(is_time_slot_overlapped(20, 21, 10, 12))
print(is_time_slot_overlapped(9, 12, 10, 11))
print(is_time_slot_overlapped(13, 16, 12, 14))
print(is_time_slot_overlapped(9, 12, 11, 13))
print(is_time_slot_overlapped(11, 12, 9, 14))
