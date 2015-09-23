#!/usr/bin/env python
#-*- coding:utf-8 -*-

def readfile(path):
	with open(path, 'r') as f:
		print f.read()

readfile("./testfile.txt")
