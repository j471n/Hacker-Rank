# Programmer : Jatin Sharma

import re

s = input()
c = 'qwrtypsdfghjklzxcvbnm'

ss = re.findall(r'(?<=[' + c + '])([aeiou]{2,})(?=[' + c +'])', s, flags = re.I)
print('\n'.join(ss or ['-1']))

