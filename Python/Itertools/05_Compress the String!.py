# Programmer : Jatin Sharma 

from itertools import groupby

s = input()

for i, j in groupby(s):
    print("({first}, {second})".format(first=len(list(j)), second=i), end = ' ')
    
    
