# Programmer : Jatin Sharma

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

[print(*i) for i in OrderedCounter(sorted(input())).most_common(3)]

