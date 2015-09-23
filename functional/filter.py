# -*- coding: utf-8 -*-

def test(x):
	return x % 2 == 1

print filter(test, range(11))

