# -*- coding:utf-8 -*-

def G(s4):
	def H(func):
		def I(*args, **kw):
			print s4
			return func(*args, **kw)
		return I
	return H

@G(1)
def A():
	print "A"

A()
