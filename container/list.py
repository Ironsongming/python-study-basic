# -*- coding: utf-8 -*-

l = ['杜兰特', '加索尔', '米洛蒂奇']

print l[0]
print l[-1]

l.append('蒂格')
print l[-1]

l.pop()
print l[-1]

l.pop(1)
print l[1]

l.insert(1, '加索尔')
print l[1]

l = ['加索尔', 14, 700]
print l

l = [['加索尔', '加索尔'], '西班牙']
print l

l = []
print len(l)
