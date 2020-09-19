# Programmer : Jatin Sharma

from collections import deque

n = int(input())
d = deque()

for i in range(n):
    query = input().split()

    if query[0] == "append":
        d.append(query[1])
    elif query[0] == "appendleft":
        d.appendleft(query[1])

    elif query[0] == "pop":
        d.pop()

    elif query[0] == "popleft":
        d.popleft()


print(*d)

