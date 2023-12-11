def foo(x, y, n):
    if x < n - 1:
        foo(x + 1, y, n)
    elif x == n - 1:
        if y < n - 1:
            foo(0, y + 1)


print(foo(1, 2, 3))
