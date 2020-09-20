# Programmer : Jatin Sharma

import re

s = input()
li = re.search(r'([a-zA-Z0-9])\1+', s)

print(li.group(1) if li else -1)

