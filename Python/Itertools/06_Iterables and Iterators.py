# Programmer : Jatin Sharma

from itertools import combinations

n = int(input())
s = list(input().split())
k = int(input())
com = list(combinations(s, k))
fil = filter(lambda x: 'a' in x, com)

print("%0.3f" % (len(list(fil)) / len(com)))
