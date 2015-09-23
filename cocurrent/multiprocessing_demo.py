#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process
import os

def runnable(name):
	print "this is a created process %s %s" % (name, os.getpid())

if __name__ == '__main__':
	print 'Parent process %s' % (os.getpid())
	p = Process(target = runnable, args = ('test',))
	print 'start'
	p.start()
	print os.getpid()
