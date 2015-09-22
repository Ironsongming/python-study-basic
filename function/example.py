# -*- coding: utf-8 -*-

def empty():
	pass

def simple(x):
	print x
	return

def checkPara(x):
	if not isinstance(x, (int, float)):
		raise TypeError("error!!!")

	print x
	return 

def multiReturn(x):
	return x, x + 1, x + 2, x + 3

empty()
simple(1)
print multiReturn(1)
checkPara("songming")
