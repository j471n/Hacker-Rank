# Programmer : Jatin Sharma

from itertools import combinations

s, k = input().split()


for i in range(1, int(k) + 1):
    for j in combinations(sorted(s.upper()), i):
        print(''.join(j))
        
