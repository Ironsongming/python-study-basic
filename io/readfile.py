#!/usr/bin/env python
# -*- coding:utf-8 -*-

def readfile(path):
	f = None
	try:
		f = open(path, 'r')
		print "opening"
		print f.read()
	except IOError as e:
		print "error"
	else:
		print "opened"
	finally:
		if f:
			f.close()
		print "close"

readfile("./testfile.txt")
