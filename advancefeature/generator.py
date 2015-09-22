# -*- coding: utf-8 -*-

#simple generator
g = (x * x for x in range(11))

for n in g:
	print n

def fib(n):
	a = 0
	b = 1
	i = 1
	while i <= n :
		yield b
		a, b = b, a + b
		i += 1

g = fib(6)
for n in g: 
	print n
