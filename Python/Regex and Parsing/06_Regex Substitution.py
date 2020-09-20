# Programmer : Jatin Sharma

import re

n = int(input())
        
for _ in range(n):
    s = input()
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', s))
    
    
