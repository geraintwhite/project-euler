def d(n):
    return sum(set(x for p in ((i,n//i)
               for i in range(1,int(n**0.5)+1) if n%i==0) for x in p)
               -set([n]))

n=28123
a=[i for i in range(n) if d(i)>i]
s=[i+j for i in a for j in a if i+j<n and i!=j]
print(sum(i for i in range(n) if i not in s))
