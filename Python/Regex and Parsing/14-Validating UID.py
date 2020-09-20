# Programmer : Jatin Sharma

import re


n = int(input())

for i in range(n):
    s = input()
    pattern = ''
    temp = all([re.search(r, s) for r in [r'[A-Za-z0-9]{10}',r'([A-Z].*){2}',r'([0-9].*){3}']]) and not re.search(r'.*(.).*\1', s)
            
    print('Valid' if temp else 'Invalid')
            
           
