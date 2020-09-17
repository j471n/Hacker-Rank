# Programmer : Jatin Sharma

n = int(input())
li = list(map(int, input().split()))
s = set(li)
a = int(((sum(s) * n) - sum(li)) / (n - 1))
print(a)
