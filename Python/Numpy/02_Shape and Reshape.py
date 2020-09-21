# Programmer : Jatin Sharma

import numpy as np

li = list(map(int, input().split()))
np_li = np.array(li)

print(np.reshape(np_li, (3,3)))

