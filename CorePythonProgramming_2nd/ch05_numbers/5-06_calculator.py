#!/usr/bin/python

def Calculator(x,y,op):
	'''calulator'''
	if op == '+':
		return x + y
	elif op == '-':
		return x - y
	elif op == '*':
		return x * y
	elif op == '/':
		return x / y
	elif op == '%':
		return x % y
	elif op == '**':
		return x ** y
	else:
		return "Error:oprator '%s' doesn't exit" % op


def main():
	print Calculator.__doc__
	expr = raw_input('enter an expression with whitespace to slip> ')
	(x,op,y) = expr.split()
	result = Calculator(int(x),int(y),op)
	print '%s = %r' % (expr,result)


if __name__ == '__main__':
	main()
