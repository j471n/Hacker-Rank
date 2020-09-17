#Programmer : Jatin Sharma

s = set(input().split(" "))
b = set()
for i in range (int(input())):
    a = set(input().split(" "))
    b.update(a)
    
print(b.issubset(s))

