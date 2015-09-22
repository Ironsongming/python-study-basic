# -*- coding: utf-8 -*-

def test(name, **kw):
	print "name is %s" % (name)
	for k, v in kw.iteritems():
		print "%s is %s" % (k, v)

test("songming", age = 10 , address = "China")
