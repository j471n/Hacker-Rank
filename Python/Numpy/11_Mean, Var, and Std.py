# Programmer : Jatin Sharma

import numpy as np

np.set_printoptions(legacy='1.13')
n, m = map(int,input().split())
a = np.array([input().split() for _ in range(m)],int)

print(np.mean(a,axis=1),np.var(a,axis=0),np.std(a), sep='\n')
