foo = [[1, 5, 7, 8], [2, 3, 2, 1], [1, 1, 0, 2]]

print(foo[1][2])

for i in foo:
    print(i)

for sublist in foo:
    for num in sublist:
        print(num)


countries = {'Vietnam': 'Hanoi', 'Singapore': 65, 91: 'India'}

for i in countries:
    print(i)
