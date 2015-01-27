n = 1000
prod = [a*b*c for a in range(1,n) for b in range(a+1,n) for c in range(b+1,n) if a*a+b*b==c*c and a+b+c==n]
print(prod)

#for a in range(1,n):
#    for b in range(a+1,n):
#        for c in range(b+1,n):
#            if a*a+b*b==c*c:
#                print(a+b+c)
