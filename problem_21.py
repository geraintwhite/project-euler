def d(n):
    return sum(set(x for pair in ((i, n//i)
               for i in range(1, int(n**0.5)+1) if n % i == 0) for x in pair)
               -set([n]))

t=0
for i in range(10000):
    j=d(i)
    if d(j) == i and i != j:
        t+=i
print(t)
