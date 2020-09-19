# Programmer : Jatin Sharma

from collections import OrderedDict
words = OrderedDict()

for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1
   
print(len(words))
print(*words.values())




# There is one more Solution for that:
"""
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
    
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())

"""


