# Programmer : Jatin Sharma

n = int(input())
li = list(map(int, input().split()))

print(all(i > 0 for i in li) and any(str(i) == str(i)[::-1] for i in li))

