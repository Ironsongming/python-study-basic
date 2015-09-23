#!/usr/bin/env python
# -*- coding:utf-8 -*-

from types import MethodType

def test(self):
	print "test"

class Demo(object):
	pass


d = Demo()
d.test = MethodType(test, d)
d.test()

Demo.test = MethodType(test, Demo)
print dir(Demo)
