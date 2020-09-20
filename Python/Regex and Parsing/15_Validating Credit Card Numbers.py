# Programmer : Jatin Sharma

import re

test = re.compile(r'^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$')
for _ in range(int(input())):
    s = input()
    print("Valid" if test.search(s) else "Invalid")
    
    
