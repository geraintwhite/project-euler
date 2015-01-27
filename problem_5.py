from functools import reduce


def lcm_brute():
    n = 2000
    while not all(n%i==0 for i in range(1,20)):
        n += 1
    return n

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(*args):
    return reduce(lcm, args)


print(lcmm(*range(1,20)))
