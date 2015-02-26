coins = [1,2,5,10,20,50,100,200]
n = 200

def combos_rec(n, coins):
    if n < 0: return 0
    if n == 0: return 1

    t=0
    for coin in coins:
        t += combos(n - coin, coins)
    return t

def combos(n, coins):
    combos = [1] + [0] * n
    for coin in coins:
        for i in range(coin, n + 1):
            combos[i] += combos[i - coin]
    return combos[n]

print(combos(n, coins))
