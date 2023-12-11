my_list = [[1, 5, 7, 8], [2, 3, 2, 1], [1, 1, 0, 2]]

# Take all
# for i in range(len(my_list)):
#     print(my_list[i])

# Not take from the end
# for i in range(len(my_list) - 1):
#     print(my_list[i])

# Not take from the start
# for i in range(2, len(my_list)):
#     print(my_list[i])

# Not take from the end and the start
# for i in range(1, len(my_list) - 1):
#     print(my_list[i])

for x in my_list:
    for i in range(len(x) - 1):
        print(my_list[i])
