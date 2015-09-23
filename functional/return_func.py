# -*- coding: utf-8 -*-

#closure
def A():
	def b(j):
		def c():
			return j*j
		return c

	fs = []
	for i in range(1, 4):
		fs.append(b(i))
	return fs

f1, f2, f3 = A()

print f1()
print f2()
print f3()
