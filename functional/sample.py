# -*- coding: utf-8 -*-

def A(x):
	print x

def B(x, y, f):
	f(x)
	f(y)

B("China", "guangzhou", A)
