# -*- coding: utf-8 -*-

i = 1
f = 1.0
s = "chensongming"
l = [1, 2, 3, 4, 5]
t = (1, 2, 3, 4, 5)
d = {"int" : i, "float" : f, "string" : s, "list" : l}
print d

d['tuple'] = t
print d

print d['string']

print d.get('string')
print d.get('aaa', 'error')

print 'float' in d

d.pop('int')
print d

#对dict的遍历
for k,v in d.items():
	print k
	print v

for k,v in d.iteritems():
	print k
	print v

#更新dict
d2 = {"list2":l}
d.update(d2)
print d
