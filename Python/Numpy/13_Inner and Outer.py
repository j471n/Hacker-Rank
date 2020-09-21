# Programmer : Jatin Sharma

import numpy as np

a = np.array(list(map(int, input().split())))
b = np.array(list(map(int, input().split())))
        
print(np.inner(a, b), np.outer(a, b), sep='\n')

