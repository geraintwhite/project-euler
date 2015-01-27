i = sum(range(101))**2
j = sum(i**2 for i in range(101))
print(abs(i-j))
