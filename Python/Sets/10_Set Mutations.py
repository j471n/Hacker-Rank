# Programmer : Jatin Sharma

def intersection_update(value):
    items = set(map(int, input().split(" ")))
    s.intersection_update(items)

def symmetric_difference_update(value):
    items = set(map(int, input().split(" ")))
    s.symmetric_difference_update(items)

def difference_update(value):
    items = set(map(int, input().split(" ")))
    s.difference_update(items)

def update(value):
    items = set(map(int, input().split(" ")))
    s.update(items)


a = int(input())
s = set(map(int, input().split(" ")))
q = int(input())

for i in range(q):

    query = input().split()
    
    if query[0] == "intersection_update":
        intersection_update(int(query[1]))

    elif query[0] == "symmetric_difference_update":
        symmetric_difference_update(int(query[1]))

    elif query[0] == "difference_update":
        difference_update(int(query[1]))

    elif query[0] == "update":
        update(int(query[1]))

print(sum(s))




"""
There is another Solution for that, you can use both, both works fine.. :) 

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split(" ")))
    
    q = int(input())
    
    for i in range (q):
        a, b = input().split(" ")
        c = set(map(int, input().split(" ")))
        eval('s.' + a + '(c)')
        
    print(sum(s))


"""

