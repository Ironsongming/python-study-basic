# -*- coding: utf-8 -*-

from functools import reduce

def A(x):
	return x * 2

it = map(A, range(11))
print it

def B(x, y):
	return x * y

print reduce(B, (1, 2, 3, 4, 5))
