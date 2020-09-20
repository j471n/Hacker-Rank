# Programmer : Jatin Sharma

import re

n = int(input())
        
for _ in range(n):
    s = input()
    matchs = re.findall(':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', s)
    if matchs:
        print(*matchs, sep='\n')
        
        
