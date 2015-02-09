with open('problem_22.txt') as f:
    l = [s.strip('"') for s in f.read().split(',')];l.sort()
print(sum([(l.index(n)+1)*sum([ord(c)-64 for c in n]) for n in l]))
