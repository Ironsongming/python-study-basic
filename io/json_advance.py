#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json

class Demo(object):
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
	
	def demo2dict(self):
		return dict(name = self.__name, 
					age = self.__age)


d = Demo("chensongming", 22)
print json.dumps(d, default = Demo.demo2dict)

