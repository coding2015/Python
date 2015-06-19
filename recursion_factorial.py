#!/usr/bin/python
#coding:utf-8
'''
factorial: 
	N!= 1*2*3*...*N
	N >= 0, 0! = 1
	implement this in a recursion way

Note:
	10! = 3628800
	1000!: RuntimeError:maximum recursion depth exceeded
	原因：递归展开(深度)存在限制
	试验结果：当n>=999时报错
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
