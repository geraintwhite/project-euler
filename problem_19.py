d,c=2,0
for i in range(1901,2001):
    for j in range(12):
        if d%7==0:
            c+=1
        if j in [3,5,8,10]:
            d+=30
        elif j==1:
            if d%400==0 or (d%4==0 and d%100!=0):
                d+=29
            else:
                d+=28
        else:
            d+=31
print(c)
