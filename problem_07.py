import math


def isprime(n):
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n)+1),2):
        if n%i==0:
            return False
    return True

i = 2
primes = [2]
while len(primes) < 10001:
    if isprime(i):
        primes.append(i)
    i+=1
#print(primes)
print(len(primes))
print(i-1)
