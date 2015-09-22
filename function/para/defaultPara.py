# -*- coding: utf-8 -*-

def test(name, age = 18, address = "China"):
	print name
	print age
	print address

test("songming")
test("songming", 22)
test("songming", 22, "USA")

#def immutable(l = []):
#	l.append('end')
#	print l

def immutable(l = None):
	if (l == None):
		l = []
		l.append('end')
	print l

immutable()
immutable()
