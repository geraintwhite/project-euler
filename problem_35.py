from itertools import permutations as p

def prime(n):
    if n%2==0 or n%3==0: return False
    for i in range(6,int(n**.5),6):
        if n%(i+1)==0 or n%(i-1)==0:
            return False
    return True

n,c=101,[2,3,5,7,11,13,17,31,37,71,73,79,97]
while n<1000000:
    l=[int(''.join(i)) for i in p(str(n))]
    if all(prime(i) for i in l):
        c+=l
    n+=1
print(len(set(c)))
