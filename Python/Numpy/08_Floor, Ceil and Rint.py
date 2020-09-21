# Programmer : Jatin Sharma

import numpy as np

arr = np.array(list(map(float, input().split())))
np.set_printoptions(sign=' ')
print(np.floor(arr), np.ceil(arr), np.rint(arr), sep='\n')

