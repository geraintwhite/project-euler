i,x,y,z=0,0,0,0
for x in range(10):
    for y in range(10):
        for z in range(10):
            n=str(x)+str(y)+str(z)
            i+=1
            if i == 1000000: print(n)
print(i)
