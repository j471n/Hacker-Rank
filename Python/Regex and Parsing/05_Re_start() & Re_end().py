# Programmer : Jatin Sharma

import re

s = input()
k = input()
index = 0

if re.search(k, s):
    while index + len(k) < len(s):
        temp = re.search(k, s[index:])
        print('({0}, {1})'.format(index + temp.start(), index + temp.end() - 1))
        index += temp.start() + 1
else:
    print('(-1, -1)')
    
    
