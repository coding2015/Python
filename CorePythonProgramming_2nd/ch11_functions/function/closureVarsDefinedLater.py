
def foo():
	y = 5	
	print '<foo>id(y):', id(y) 
	def bar(x=10):
		print '<bar>id(y):', id(y) 
		return x + y
	print bar()
	y = 8	
	print '<foo>id(y):', id(y) 
	print bar()



'''
>>> foo()
<foo>id(y): 16784392
<bar>id(y): 16784392
15
<foo>id(y): 16784320
<bar>id(y): 16784320
18
'''


def foo():
	bar = lambda: x+y
	x = 10
	y = 10
	return bar

>>> foo()()
20

	
