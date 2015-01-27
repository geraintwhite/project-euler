sum = 0
i = 1
j = 1

while sum < 4000000:
 a = i
 i = j
 j += a
 if j % 2 == 0:
  sum += j

print(sum)
