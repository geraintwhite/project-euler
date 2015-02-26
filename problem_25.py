def fibo (f):
    a, b, n = 0, 1, 0
    while f(a):
        a, b = b, a + b
        n += 1
    return n

print(fibo(lambda a: len(str(a)) < 1000))
