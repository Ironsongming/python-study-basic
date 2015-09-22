t = (1, 2, 3, 4, 5)
s = set(t)
print s

s.add(6)
s.remove(1)
print s

for x in s:
	print x

t = (2, 3 ,4, 7)
s2 = set(t)
print s2

print s & s2
print s | s2

