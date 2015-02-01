def collatz (n):
  return n / 2 if n % 2 == 0 else 3 * n + 1

def collatz_chain (n):
  i = 1
  while n > 1:
    n = collatz(n)
    i += 1
  return i

max_chain = (0, 0)
n = 1
while n < 1000000:
  i = collatz_chain(n)
  if i > max_chain[1]:
    max_chain = (n, i)
  n += 1
print(max_chain)
