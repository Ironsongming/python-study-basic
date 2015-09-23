# -*- coding: utf-8 -*-

from functools import reduce

def advance(*l):
	def baseC(x, y):
		print l
		return x + y

	def baseD():
		return reduce(baseC, l)

	print baseD()

advance(1, 2, 3, 4)
