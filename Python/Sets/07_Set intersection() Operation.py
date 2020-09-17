#Programmer : Jatin Sharma

n = int(input())
english_newspaper = set(map(int, input().split(" ")))

b = int(input())
french_newspaper = set(map(int, input().split(" ")))

result = english_newspaper.intersection(french_newspaper)
print(len(result))
