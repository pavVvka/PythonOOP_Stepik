"""
1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
"""

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
FIELDS = ('id', 'name', 'old', 'salary')

print(lst_in)
f = list(FIELDS)
print(f)
for x in lst_in:
    a = x.split()
    print(a)
    dc = dict(list(zip(f, a)))
    print(dc)






