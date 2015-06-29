def f(x):
	if 0<x<10:
		return '(0,10)'
	else:
		if 10<=x<20:
			return '[10,20)'


>>> print f(5)
(0,10)
>>> print f(15)
[10,20)
>>> print f(30)
None

