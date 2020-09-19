# Programmer : Jatin Sharma
import re

t = int(input())
for i in range(t):
    try:
        s = re.compile(input())
    except re.error:
        print("False")
    else:
        print("True")
        
        
