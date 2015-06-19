#!/usr/bin/python
#coding:utf-8
'''
Exercise 8-9:
	Fibonacci:
		f(x): x is an integer and x > 0
			f(n) = f(n-1) + f(n-2)
			f(2) = f(1) = 1 
			[f(x)]: 1,1,2,3,...
	define a function:
		which return the N fibonacci when given the N number

Exercise 11-14:
	implement Fibonacci in recursion way
	
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


def FibonacciRec(n):
	'''
	implement fibonacci in recursion way:
		F(n) = F(n-1) + F(n-2)
		double recursion
	'''
	if n > 2:
		ret = FibonacciRec(n-1) + FibonacciRec(n-2)
	elif n in (1,2):
		ret = 1
	else:
		ret = None
	return ret


def test_fibonacci():
	n = int(raw_input('enter an integer:'))
	print 'F(%d) = %s' % (n, Fibonacci(n))
	print 'F[%d]:' % n ,
	print [Fibonacci(x) for x in range(1,n+1)]

def test_fibonacci_rec():
	n = int(raw_input('enter an integer:'))
	print 'F(%d) = %s' % (n, FibonacciRec(n))
	print 'F[%d]:' % n ,
	print [FibonacciRec(x) for x in range(1,n+1)]
		#or map(FibonacciRec, range(11))

if __name__ == '__main__':
	test_fibonacci_rec()

	
