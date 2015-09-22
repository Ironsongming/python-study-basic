# -*- coding: utf-8 -*-

def test(*l):
	for x in l:
		print x

test('a', '3', 1)

l = [1, 2, 3]
test(*l)
