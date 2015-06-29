#!/urs/bin/python
'''
math.sqrt(x), x>=0
	it does not support negative
	now enhance it: make it support negative, ie return a complex when x<0

Knowledge: 
	j = (-1)*(-1)
	ValueError: type is right but value is invalid
'''

import math
def sqrt(x):
	"plus support negative number's square-root base on math.squrt()"
	try:
		return math.sqrt(x)
	except ValueError:
		return complex(0,math.sqrt(-x))


def main():
	n = float(raw_input('enter a number> '))
	print "sqrt(%s) =" % n, sqrt(n)


if __name__ == '__main__':	
	main()
