#!/usr/bin/python

'''
Fibonacci:
	f(x): x is an integer and x > 0
		f(n) = f(n-1) + f(n-2)
		f(2) = f(1) = 1 
		[f(x)]: 1,1,2,3,...
define a function:
	which return the N fibonacci when given the N number
'''

def Fibonacci(n):
	if n < 0:
		return None
	elif n <= 2:
		return 1
	else:
		x = x1 = x2 = 1
		for i in range(3,n+1):
			x = x1 + x2
			x2 = x1
			x1 = x
		return x 


def main():
	n = int(raw_input('enter a number> '))
	print 'F(%d) = %d' % (n, Fibonacci(n))
	print 'F[%d]:' % n ,
	print [Fibonacci(x) for x in range(1,n+1)]

if __name__ == '__main__':
	main()
