# Programmer : Jatin Sharma

from collections import Counter


x = int(input())
shoe_size = Counter(map(int, input().split()))
n = int(input())
total = 0

for i in range(n):

    size, price  = map(int,(input().split()))
    
    if shoe_size[size]:
        total +=price
        shoe_size[size] -= 1

print(total)
