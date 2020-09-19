# Programmer : Jatin Sharma

from collections import defaultdict


n, m = map(int, input().split())
dl = defaultdict(lambda: -1)
serial = 1

for i in range(1, n+1):
    temp = input()
    dl[temp] = dl[temp] + ' ' + str(i) if temp in dl else str(i)

for i in range(m):
    print(dl[input()])

