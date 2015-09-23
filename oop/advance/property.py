#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Demo(object):

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, val):
		self.__name = val
	
d = Demo()
d.name = "songming"
print d.name
