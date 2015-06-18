#!/usr/bin/python
'''
Exercise 8-7:
	perfect number: 
		number == sum(num'factors) (factor doesn't include num itself)
	require:
		define a function: isperfect()
		given an integer, judge if it's a perfert number 
		if it's perfect,return 1, otherwise return 0
	self-extend:
		find all the perfect numbers in a given range:[0,x]

result:
	in [1,1000],perfect numbers are:
		6, 28, 496, 8128		
'''

def isperfect(num):
	sum = 0
	#fact = []
	for count in range(num/2, 0, -1):
		if num % count == 0:
			sum += count
			#fact.append(count)
	#print fact
	if sum == num:
		return True
	else:
		return False

def perfectNums(scope = 1000):
	'find the perfect numbers in range[1,scope]'
	pers = []
	for n in range(1, scope+1): 	#!range default start is 0
		if isperfect(n):
			pers.append(n) 
	return pers

def test_isperfect():
	num = int(raw_input('enter a integer: '))
	print num, 'is perfect?',isperfect(num)


def test_perfectNums():
	print perfectNums.__name__
	print '\t',perfectNums.__doc__
	print 
	r = int(raw_input('enter the limit of integer range: '))
	print 'perfect number in [1,%d]:' % r
	print perfectNums(r)

if __name__ == '__main__':
	test_perfectNums()
