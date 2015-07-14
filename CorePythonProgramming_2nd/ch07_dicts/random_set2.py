#!/usr/bin/python
#coding:utf-8

'''
Exercise 7-14
'''

from random import randint

def genSet():
	'produce a set contains 1~10 numbers in [0,9]'
	return set(randint(0,9) for i in range(randint(1,10)))

def main():
	A = genSet()
	B = genSet()
	print 'A:', A
	print 'B:', B
	
	AorB = A | B
	AandB = A & B 

	DONE = False	# 记录答对与否
	MAX = 3		# 给MAX次机会

	while MAX:
		MAX -= 1
		try:
			r1 = set(input('A|B = '))
			r2 = set(input('A&B = '))
		except TypeError:
			print 'invalid data, please input a sequence'
			MAX += 1
			continue
		if r1 == AorB and r2 == AandB:
			print 'Good job!'
			DONE = True
			break
		print 'Oop! not the right answer!' 

	if not DONE:
		print 'The right answers are:'
		print 'A|B=', AorB
		print 'A&B=', AandB

if __name__ == '__main__':
	main()


'''
$ python random_set2.py 
A: set([0, 9, 4, 7])
B: set([8, 3, 4, 5, 7])
A|B = 1
invalid data, please input a sequence
A|B = 1,3
A&B = 3,5
Oop! not the right answer!
A|B = 4,5
A&B = 2,6
Oop! not the right answer!
A|B = 2,5
A&B = 2,6
Oop! not the right answer!
The right answers are:
A|B= set([0, 3, 4, 5, 7, 8, 9])
A&B= set([4, 7])
'''	

'''
$ python random_set2.py 
A: set([1, 3, 5, 6, 7, 9])
B: set([0, 1, 3, 5, 6, 8, 9])
A|B = 0,1,3,5,7,6,9,9
A&B = 0
invalid data, please input a sequence
A|B = 0,1,3,5,6,7,8,9
A&B = 1,3,5,6,9
Good job!

'''
