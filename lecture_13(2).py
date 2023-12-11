my_dict = {'abc': 1, 'abc': 2, 'ef': 3}

my_dict = {True: 1, 1: [1, 2, 3], 'ef': {'a': 1, 'b': 2}}

my_dict = {True: 1, 1: [1, 2, 3], 'ef': 'abc'}

my_dict = {'abc': 1, 'cd': 2, 'ef': 3}

my_dict = {'abc': 1, 'cd': True, 'ef': 'abc'}

# my_dict = {[1, 2]: 1, [3, 4]: "abc"}
# List CANNOT include as key in dictionary

my_dict = {True: 1, 1: True, 'ef': "abc"}

my_dict = {'abc': "123", 'cd': "456", 'ef': "789"}

my_dict = {1: 10, 2: 20, 3: 30}

# my_dict = {{"a": 1, "b": 2}: 1, "abc": 2}
# Dictionary CANNOT include as key in dictionary

my_dict = {1: 'abc', 2: 'def', 3: 'ghi'}

x = {"a": 2, "b": 3, "a": 4}
print(x["a"])

x = {}

x["a"] = 1

x["b"] = 2

x["a"] = 3

print(x["a"])

var = {"a": 10, "b": 20}

var["c"] = 30

results = []

for x in var:
    results.append(x)

print(results)

x = [[1, 2], [3, 4], [5, 6]]

print(x[:2])

x = [[1, 2, 3], [4, 5, 6]]

x[0][1] = 10

print(x)


def foo(table):
    n_rows = len(table)
    n_cols = len(table[0])
    new_table = []
    for c in range(n_cols):
        row = []
        for r in range(n_rows):
            row.append(table[r][c])
        new_table.append(row)
    return new_table


print(foo([[1, 2], [3, 4], [5, 6]]))


b = [[9, 6], [4, 5], [7, 7]]
x = b[:2]
x[1].append(10)

print(x)
