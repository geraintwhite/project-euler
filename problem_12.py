def factors (n):
  return set(x for pair in ((i, n//i)
             for i in range(1, int(n**0.5) + 1) if n % i == 0) for x in pair)

i = 0
n = 0
while len(factors(n)) < 500:
  i += 1
  n += i

print(n)
