# -*- coding: utf-8 -*-

l = ['a', 'b', 'c', 'd']
print [ x.upper() for x in l]

l = range(11)
print [ x * x for x in l if x % 3 == 0]

print [ x * y for x in l if x % 3 == 0 for y in l if y % 2 == 0]

