#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):
	
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
	
	def get_name(self):
		return self.__name

