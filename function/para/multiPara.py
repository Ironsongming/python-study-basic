# -*- coding: utf-8 -*-

def test(name, age = 22, *friends, **extra):
	print name
	print age
	print "friends"
	for x in friends:
		print x
	
	print "extra"
	for k, v in extra.iteritems():
		print "%s is %s" % (k, v)

friends = ('a', 'b', 'c', 'd')
extra = {'a' : 1, 'b' : 2}
test("songming", *friends, **extra)
test(*friends, **extra)
