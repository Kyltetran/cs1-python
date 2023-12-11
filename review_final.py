# def binary_to_int(s):
#     if s == '':
#         return 0
#     else:
#         return int(s[0])*2**(len(s) - 1) + binary_to_int(s[1:])


# def int_to_binary(int):
#     if int == 0:
#         return ''
#     else:
#         return int_to_binary(int // 2) + str(int % 2)


# def max(x, y):
#     if x > y:
#         return x
#     else:
#         return y


# def foo(lst1, lst2):
#     if lst1 == []:
#         return lst2
#     elif lst2 == []:
#         return lst1
#     else:
#         return [max(lst1[0], lst2[0])] + foo(lst1[1:], lst2[1:])


# def foo(lst):
#     if lst == []:
#         return []
#     elif lst[0] <= 0:
#         return foo(lst[1:])
#     else:
#         return [lst[0]] + foo(lst[1:])


# x = 'Fulbright University Vietnam'
# y = [1, 2, 3, 4, 5]
# print(x[-1])
# print(x[3:])
# print(y[2])
# print(y[1:])


# def find_rhyme(word):
#     for i in range(len(word)):
#         if word[i] in 'aeiouy':
#             return word[i:]


# print(find_rhyme('foundation'))
# print(find_rhyme('introduction'))
# print(find_rhyme('minh'))

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# b = a[1:]
# b[0] = [10, 11]
# b[1][0] = 99
# print(a)
# print(b)

# list1 = [[1, 2], [3, 4], [5, 6]]
# list2 = list1[1:]
# list2[0][0] = 10
# list2[1] = [7, 8]
# print(list1)
# print(list2)

# x = [[0, 1], [2, 3]]
# y = x[:]
# y[0] = [4, 5]
# y[1][1] = 6
# print(x)
# print(y)

# dict_1 = {"a": 10, "b": 20, "c": 30, "d": 30}
# dict_2 = {"b": 5, "c": 4, "a": 10}
# for x in dict_2:
#     if dict_1[x]:
#         dict_1[x] = dict_1[x] + dict_2[x]
#     else:
#         dict_1[x] = dict_2[x]

# print(dict_1)

# def fib(n):    # write Fibonacci series up to n
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()


# def fib2(n):   # return Fibonacci series up to n
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result


# class fuv_course:
#     def __init__(self, code, title, description=''):
#         self.code = code
#         self.title = title
#         self.description = description
#         assert type(code) == 'str' and type(title) == 'str'
#         assert len(code) > 0 and len(title) > 0

#     def get_info(self):
#         return self.code + ' - ' \
#             + self.title + ': ' \
#             + self.description

list_a = [[1, 2, 'b'], [3, 'c'], 'def']
empty_str = ''
for sublist in list_a:
    for i in sublist:
        if isinstance(i, str):
            empty_str += i

print(empty_str)
