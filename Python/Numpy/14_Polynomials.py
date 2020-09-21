# Programmer : Jatin Sharma

import numpy as np

arr = np.array(input().split(), float)
n = int(input())
        
print(np.polyval(arr, n))

