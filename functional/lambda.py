# -*- coding: utf-8 -*-

from functools import reduce

def advance(*l):
	return reduce(lambda x, y : x + y, l)

print advance(1, 2, 3, 4)
