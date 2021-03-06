#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Pool
import os

def task(name):
	print "task %s (%s) is Running" % (name, os.getpid())
	start = time.time()
	time.sleep(random.random() * 200)
	end = time.time()
	print "task %s runs %0,2f seconds" % (name, end - start)

if __name__ == '__main__':
	print "Parent process %s " % os.getpid()
	p = Pool()
	for i in range(16):
		p.apply_async(task, args = (i,))
	print "waiting"
	p.close()
	p.join()
	print "end"
