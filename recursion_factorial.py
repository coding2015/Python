#!/usr/bin/python
'''
factorial: 
	N!= 1*2*3*...*N
	N >= 0, 0! = 1
	implement this in a recursion way
'''

def Factorial(n):
	if n > 1:
		return n * Factorial(n-1)
	elif n == 1 or n == 0:
		return 1


def main():
	n = int(raw_input('enter an integer> '))
	if n < 0:
		print n,'does not have a factorial'
	else:
		print '%d! = %d' % (n, Factorial(n))


if __name__ == '__main__':
	main()
