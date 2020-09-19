# Programmer : Jatin Sharma

from dateutil import parser

for _ in range(int(input())):
    t1 = parser.parse(input().strip())
    t2 = parser.parse(input().strip())
    print(abs(int((t2-t1).total_seconds())))
    
    
