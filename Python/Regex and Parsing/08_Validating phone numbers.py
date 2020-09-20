# Programmer : Jatin Sharma

import re

n = int(input())
        
for i in range(n):
    s = input()
    print('YES' if re.match(r'[789]\d{9}$', s) else 'NO')
    
    
