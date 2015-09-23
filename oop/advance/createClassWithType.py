#!/usr/bin/env python
# -*- coding: utf-8 -*-

def createClass(name, *parentNames, **kw):
	return type(name, parentNames, kw)

def A(self):
	print 'A'

def B(self):
	print 'B'

t = (object,)
d = {"myA":A, "myB":B}
MyClass = createClass("MyClass", *t, **d)

print type(MyClass)
print dir(MyClass)

m = MyClass()
m.myA()
m.myB()


